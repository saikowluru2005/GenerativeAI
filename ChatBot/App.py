from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
message=[
    SystemMessage(content='You are a funny AI agent')
]
print("Welcome to Bot")
while True:
    text=input("You: ")
    if text==0:
        break
    message.append(HumanMessage(content=text))
    response=model.invoke(message)
    message.append(AIMessage(content=response.text))
    print("model: ",response.text)