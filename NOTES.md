# Notes: How the Offline Chatbot Works

## 1. Main idea

This project is a small terminal chatbot. It sends messages to a language model running locally through Ollama. The Python `openai` package is used because Ollama provides an OpenAI-compatible API endpoint.

Once the model is downloaded, chat requests can run on your computer without sending the prompt to a hosted AI API. Ollama itself must be running.

## 2. Code flow

1. **Import `OpenAI`**  
   The program uses the OpenAI Python library to send chat-completion requests.

2. **Create the client**  
   `base_url="http://localhost:11434/v1"` points the client to Ollama running on the same computer. The string `"ollama"` is a placeholder API key for this local setup; it is not a real secret key.

3. **Set the model name**  
   `MODEL_NAME = "qwen2.5:14b"` must match a model installed in Ollama.

4. **Create `messages`**  
   This list stores the conversation history in the Python program.

5. **Read user input**  
   The `while` loop keeps asking for input. Enter `e` or `exit` to stop.

6. **Add the user message**  
   The user message is appended to `messages`.

7. **Send the conversation**  
   The program sends the current message list to Ollama using `client.chat.completions.create(...)`.

8. **Read the AI reply**  
   `response.choices[0].message.content` extracts the reply text from the returned response.

9. **Save the AI reply**  
   The assistant message is appended to `messages`, so it can be included in the next request.

10. **Repeat**  
    The next request includes the earlier messages, giving the model context from the current conversation.

## 3. How conversation memory works

The model does not automatically keep this chat history between separate API requests. The Python program keeps the history in `messages` and sends it again with each request.

Example:

- Turn 1: `[user1]`
- Turn 2: `[user1, assistant1, user2]`
- Turn 3: `[user1, assistant1, user2, assistant2, user3]`

Both append operations matter:
- Append the user's message before making the request.
- Append the assistant's reply after receiving it.

If the program is restarted, this in-memory list is lost. This example does not save history to a file or database.

## 4. Context window

A model's **context window** is the amount of input it can process in one request, measured in tokens. The conversation history grows with each turn, so eventually it may approach the model's context limit. Very long histories can use more memory and processing time, and a request may fail or need truncation.

This project resends the full history each turn. It does not create unlimited memory.

## 5. Roles and message format

This project uses messages shaped like:

```python
{"role": "user", "content": "Hello"}
{"role": "assistant", "content": "Hi!"}
```

Common roles include:
- `system`: instructions that guide the assistant's behavior
- `user`: input from the person using the chatbot
- `assistant`: the model's response

Do not assume every AI provider supports exactly the same roles, request fields, or response structure. This code works with Ollama's OpenAI-compatible chat-completions endpoint and the installed `openai` Python library.

## 6. Important code details

- `api_key="ollama"` is a placeholder for this local Ollama setup.
- `base_url` points to the local API; it is not a cloud API address.
- `MODEL_NAME` must match the model tag installed with Ollama.
- The `try/except` block displays a useful error if the request fails.
- If a request fails, the latest user message is removed from the history to avoid leaving an incomplete turn in the list.

## 7. Current limitations

- History exists only while the Python program is running.
- Full history is resent on every turn.
- There is no history trimming, summarization, system prompt, or persistent storage.
- A 14B model can require substantial RAM and may respond slowly depending on hardware and quantization.
