import json
import logging
from fastapi import FastAPI
from models.request_models import PatientRequest
from chains.intent_chain import intent_chain
from chains.triage_chain import triage_chain
from chains.scheduling_chain import scheduling_chain
from chains.response_chain import response_chain

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def root():
    return {"message": " Baptist Health AI Assistant is running!"}

@app.post("/patient-assistant")
async def patient_assistant(request: PatientRequest):
    # Step 1: Extract intent
    logger.info(f"--- STEP 1: Intent Extraction ---")
    logger.info(f"User Message: {request.message}")
    
    result = intent_chain.invoke({
        "message": request.message
    })
    intent_raw = result.content
    
    try:
        intent = json.loads(intent_raw)
        logger.info(f"Extracted Intent: {json.dumps(intent, indent=2)}")
    except Exception:
        logger.error(f"Failed to parse intent JSON: {intent_raw}")
        return {"error": "Unable to parse intent"}

    symptom = intent["symptom"]
    urgency = intent["urgency"]
    department = intent["department"]

    # Step 2: Triage
    logger.info(f"--- STEP 2: Clinical Triage ---")
    logger.info(f"Triage Input -> Symptom: {symptom}, Urgency: {urgency}")
    
    triage_result = triage_chain.invoke({
        "symptom": symptom,
        "urgency": urgency
    }).content
    
    logger.info(f"Triage Result: {triage_result}")

    appointment = ""

    # Step 3: Schedule only if not emergency
    logger.info(f"--- STEP 3: Scheduling ---")
    if triage_result == "ROUTINE":
        logger.info(f"Scheduling appointment for Department: {department}")
        appointment = scheduling_chain.invoke({
            "department": department
        }).content
        logger.info(f"Appointment Info: {appointment}")
    else:
        logger.info("Emergency detected. Skipping routine scheduling.")

    # Step 4: Final response
    logger.info(f"--- STEP 4: Response Generation ---")
    logger.info(f"Generating final response for Triage: {triage_result}")
    
    final_response = response_chain.invoke(
        {
            "triage_result": triage_result,
            "appointment": appointment
        }
    ).content
    
    logger.info("Chain complete. Returning response to user.")

    return {
        "symptom": symptom,
        "urgency": urgency,
        "department": department,
        "triage": triage_result,
        "message": final_response
    }