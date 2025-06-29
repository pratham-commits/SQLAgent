import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent,AgentType
from langchain.sql_database import SQLDatabase
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()
LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"
groq_api_key=os.getenv("GROQ_API_KEY")
st.set_page_config(page_title="Langchain: Chat with SQL DB")
st.title("Langchain: chat with SQL DB")


radio_options=["Sqlite3 - student.db","Connect to your SQL database"]

selected_option=st.sidebar.radio(label="Choose the db",options=radio_options)

if radio_options.index(selected_option)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Provide My SQL host:")
    mysql_user=st.sidebar.text_input("My SQL user:")
    mysql_pass=st.sidebar.text_input("Password:")
    mysql_db=st.sidebar.text_input("My SQL database:")
    
else:
    db_uri=LOCALDB
    
if not db_uri:
    st.info("Please enter the database info")
    
##llm model

llm=ChatGroq(api_key=groq_api_key,
             model_name="Llama-3.3-70B-Versatile",
             streaming=False)



#configuration of databases
@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_pass=None,mysql_db=None):
    if db_uri==LOCALDB:
        db_file_path=(Path(__file__).parent/"student.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{db_file_path}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///",creator=creator))
    
    elif db_uri==MYSQL:
        if not (mysql_db and mysql_host and mysql_pass and mysql_user):
            st.error("Please provide all MySQL details")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_pass}@{mysql_host}/{mysql_db}"))
    
if db_uri==MYSQL:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_pass,mysql_db)
else:
    db=configure_db(db_uri)
    
## toolkit : basically interaction with the databases

toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"]=[
        {"role":"assistant","content":"How can I help you?"}
    ]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
user_query=st.chat_input(placeholder="What do you want to know from the database?")

if user_query:
    st.session_state.messages.append({"role":"user","content":user_query})
    st.chat_message("user").write(user_query)
    
    
    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response = agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.messages.append({
            "role":"assistant","content":response
        })
        st.write(response)