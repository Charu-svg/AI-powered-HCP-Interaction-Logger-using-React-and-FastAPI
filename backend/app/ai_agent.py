# app/ai_agent.py

# Stub version of AI functions (no LangGraph required)
def summarize_notes(notes: str) -> str:
    # Simple placeholder summary
    return notes[:50] + ("..." if len(notes) > 50 else "")
# app/ai_agent.py

# Temporary stub so backend runs
# If you had other LangGraph tools like `log_interaction` or `edit_interaction`, stub them too:
"""def log_interaction_tool(hcp_id: int, notes: str) -> dict:
    return {"hcp_id": hcp_id, "notes": notes, "summary": summarize_notes(notes)}

def edit_interaction_tool(interaction_id: int, new_notes: str) -> dict:
    return {"interaction_id": interaction_id, "new_notes": new_notes, "summary": summarize_notes(new_notes)}"""