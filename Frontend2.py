import streamlit as st 
from Backend2 import chatbot 
from Backend2 import retreive_all_threads 
from langchain_core.messages import HumanMessage
import uuid

# ----------------------- UTILITIES -----------------------
def generate_thread_id():
    return str(uuid.uuid4())

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(thread_id)
    st.session_state["message_history"] = []
  
    st.session_state["thread_names"][thread_id] = "New Conversation"

def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(
        config={"configurable": {"thread_id": thread_id}}
    ).values

    return state.get("messages", [])

# ---------------------SETUP -----------------------
st.sidebar.title("Chatbot with LangGraph")


if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = retreive_all_threads()

if "thread_names" not in st.session_state:
    st.session_state["thread_names"] = {}

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()
    add_thread(st.session_state["thread_id"])
    st.session_state["thread_names"][st.session_state["thread_id"]] = "New Conversation"

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# ------------------ LLM FOR TITLE GENERATION ----------------
from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    api_key="05M3e310UpAluqszzJMayblJMIvViXqf",
    model="mistral-small-latest"
)

#PROPER conv. name generator (runs only once)
def get_conversation_name(thread_id):
    # 1. If name already generated → return cached
    if thread_id in st.session_state["thread_names"] and \
       st.session_state["thread_names"][thread_id] != "New Conversation":
        return st.session_state["thread_names"][thread_id]

    # 2. Load conv. messages
    messages = load_conversation(thread_id)
    if not messages:
        return "New Conversation"

    # 3. Use first few msgs to create title
    formatted_msgs = []
    for msg in messages[:3]:
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        formatted_msgs.append({"role": role, "content": msg.content})

    prompt = (
        "Generate a short 1–3 word title for this conversation. "
        "Return ONLY the title:\n"
        f"{formatted_msgs}"
    )

    title = llm.invoke(prompt).content.strip()

    # store permanently (never regenerate)
    st.session_state["thread_names"][thread_id] = title
    return title

# ----------------------- SIDEBAR ----------------------------
if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversations")

for thread_id in st.session_state["chat_threads"]:
    title = get_conversation_name(thread_id)

    if st.sidebar.button(title, key=f"thread-btn-{thread_id}"):
        st.session_state["thread_id"] = thread_id

        msgs = load_conversation(thread_id)
        history = []
        for m in msgs:
            role = "user" if isinstance(m, HumanMessage) else "assistant"
            history.append({"role": role, "content": m.content})

        st.session_state["message_history"] = history

# Ensure current thread is in list
add_thread(st.session_state["thread_id"])

# ----------------------- MAIN CHAT AREA -----------------------
config = {"configurable": {"thread_id": st.session_state["thread_id"]}}

# Display memory
for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

# ----------------------- USER INPUT -----------------------
user_input = st.chat_input("Type here...")

if user_input:
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.text(user_input)

    # Streaming
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            chunk.content for chunk, meta in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=config,
                stream_mode="messages"
            )
        )

    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})

    #After first message → generate permanent title(
    if st.session_state["thread_names"][st.session_state["thread_id"]] == "New Conversation":
        get_conversation_name(st.session_state["thread_id"])

