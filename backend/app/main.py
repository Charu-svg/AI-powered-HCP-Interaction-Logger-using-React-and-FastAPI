from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, crud

# create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="http://localhost:3000")

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Root API
@app.get("/")
def root():
    return {"message": "Backend running successfully"}


# Get all interactions
@app.get("/interactions/", response_model=list[schemas.Interaction])
def read_interactions(db: Session = Depends(get_db)):
    return crud.get_interactions(db)


# Create interaction
@app.post("/interactions/", response_model=schemas.Interaction)
def create_interaction(interaction: schemas.InteractionCreate, db: Session = Depends(get_db)):
    return crud.create_interaction(db, interaction)


# AI Autofill API
@app.post("/ai_autofill")
def ai_autofill(data: dict):

    instruction = data.get("instruction", "")

    text = instruction.lower()

    ai_fields = {}

    # Extract doctor name
    if "dr" in text:
        words = instruction.split()
        for i, word in enumerate(words):
            if word.lower() == "dr" and i + 1 < len(words):
                ai_fields["doctor_name"] = "Dr " + words[i + 1]


    # Detect interaction type
    if "call" in text:
        ai_fields["interaction_type"] = "Call"
    elif "email" in text:
        ai_fields["interaction_type"] = "Email"
    else:
        ai_fields["interaction_type"] = "Meeting"

    # Sentiment detection
    if "positive" in text:
        ai_fields["sentiment"] = "Positive"
    elif "negative" in text:
        ai_fields["sentiment"] = "Negative"
    else:
        ai_fields["sentiment"] = "Neutral"

    ai_fields["notes"] = instruction

    summary = f"Interaction logged with {ai_fields.get('doctor_name','doctor')}."

    return {
        "ai_fields": ai_fields,
        "ai_summary": summary
    }
@app.post("/ai_autofill")
def ai_autofill(data: dict):

    instruction = data.get("instruction", "")
    text = instruction.lower()

    ai_fields = {}
@app.post("/ai_followup")
def ai_followup(data: dict):

    notes = data.get("notes","")

    followups = []

    text = notes.lower()

    if "hypertension" in text:
        followups.append("Share hypertension clinical study")

    if "drug" in text:
        followups.append("Send product brochure")

    followups.append("Schedule follow-up meeting")

    return {
        "suggestions": followups
    }    

    # Extract doctor name
    if "dr" in text:
        words = instruction.split()
        for i, word in enumerate(words):
            if word.lower() == "dr" and i+1 < len(words):
                ai_fields["doctor_name"] = "Dr " + words[i+1]

    # Interaction type
    if "call" in text:
        ai_fields["interaction_type"] = "Call"
    elif "email" in text:
        ai_fields["interaction_type"] = "Email"
    else:
        ai_fields["interaction_type"] = "Meeting"

    # Sentiment
    if "positive" in text:
        ai_fields["sentiment"] = "Positive"
    elif "negative" in text:
        ai_fields["sentiment"] = "Negative"
    else:
        ai_fields["sentiment"] = "Neutral"

    ai_fields["notes"] = instruction

    # AI Follow-up suggestion
    if "drug" in text or "medicine" in text:
        ai_fields["follow_up"] = "Share product brochure and schedule follow-up meeting"
    else:
        ai_fields["follow_up"] = "Plan next meeting with doctor"

    summary = f"Interaction logged with {ai_fields.get('doctor_name','doctor')}."

    return {
        "ai_fields": ai_fields,
        "ai_summary": summary
    }
