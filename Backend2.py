from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
# from langgraph.checkpoint.memory import InMemorySaver
#**************** change 1
from langgraph.checkpoint.sqlite import SqliteSaver 
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",  
#     api_key="...."             
# )

# load environment variables

llm = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API_KEY"),
    model="mistral-small-latest"
)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}
# ************************ change 2

# to create database
import sqlite3
conn=sqlite3.connect("chatbot.db", check_same_thread=False)
# we will use database for all threads 
# Checkpointer
checkpointer = SqliteSaver(conn)

# creates 3 threads for 1 thread:
# start chat and end 

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

# extract no, of threads in database to send to front end
def retreive_all_threads():
    all_threads=set() #to get unique thread 
    for checkpoint in checkpointer.list(None):  # None means all threads
        all_threads.add(checkpoint.config["configurable"]["thread_id"])

    return list(all_threads)
