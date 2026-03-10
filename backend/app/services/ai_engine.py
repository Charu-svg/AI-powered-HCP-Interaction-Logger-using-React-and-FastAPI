def summarize_interaction(notes):

    return f"""
Summary:
Doctor interaction recorded.

Notes: {notes}

Suggested Action:
Follow up with the doctor in next visit.
"""


def calculate_engagement(notes):

    notes = notes.lower()

    if "interested" in notes:
        return 80
    elif "follow up" in notes:
        return 60
    elif "not interested" in notes:
        return 20
    else:
        return 40