from langchain.tools import tool

@tool
def log_interaction(text: str):
    """Extract interaction fields from message"""
    return {"message": text}

@tool
def edit_interaction(text: str):
    """Edit existing form values"""
    return {"edit": text}

@tool
def suggest_followup(text: str):
    """Suggest follow up actions"""
    return "Send clinical study, schedule follow-up meeting"

@tool
def generate_summary(text: str):
    """Generate interaction summary"""
    return "Interaction summary generated"

@tool
def save_interaction(text: str):
    """Save interaction in database"""
    return "Interaction saved"