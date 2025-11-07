from fastapi import HTTPException 

from langchain.tools import tool , ToolRuntime
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver 

from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# result = llm.invoke("Hello how are you")

# print(result.content)

@tool
def get_services(username : str) -> str:
    """User service access check"""
    if username == "nimal" : 
        return "nimal you are blocked from the system"
    else :
        return f"Hello how are you {username} "

    

agent = create_agent(
    model=llm,
    tools=[get_services],
    system_prompt="You are chatbot get_services tool check user access to the system",
    checkpointer=InMemorySaver(),
)

def call_agent(message : str) : 
    try : 
        result = agent.invoke(
            {"messages" : [{"role" : "user" , "content" : message}]},
            {"configurable": {"thread_id": "1"}},  # Create thread id from frontend add pass to here with it can identify thread id
        ) 
        ai_message = result["messages"][-1]
        print(ai_message.content)

        return {
            "status" : "success",
            "response" : ai_message.content
        }
    except Exception as e:
        return HTTPException(status_code=400 , detail="Agent calling fail")

# print(result)



call_agent("Hello i am nimal")