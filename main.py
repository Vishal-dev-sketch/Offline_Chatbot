from openai import OpenAI

client = OpenAI(
    api_key="ollama", #API_Key
    base_url="http://localhost:11434/v1"
)

msg_history=[]

while True:
    user_input=input("You :\n")

    if user_input.lower()=="e":
        break

    print("---------------------------------------------------------------------------------------\n") 

    msg_history.append({"role":"user", "content":user_input})

    response = client.chat.completions.create(  # sending prompt to the ai
     model="qwen2.5:14b",
     messages=msg_history
    )

    reply=response.choices[0].message.content   #receiving reply of Ai
    print(f"Ai:\n{reply}")

    print("---------------------------------------------------------------------------------------\n")

    msg_history.append({"role":"assistant", "content":reply})