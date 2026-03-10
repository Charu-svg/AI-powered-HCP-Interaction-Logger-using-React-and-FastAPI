from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from app.tools import *

llm = ChatOpenAI(model="gpt-4o-mini")

tools = [
    log_interaction,
    edit_interaction,
    suggest_followup,
    generate_summary,
    save_interaction
]

agent = create_react_agent(llm, tools)