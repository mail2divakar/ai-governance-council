from langchain_core.prompts import PromptTemplate
from services.openai_client import llm

triage_prompt = PromptTemplate(
    input_variables=["symptom", "urgency"],
    template="""
You are a clinical triage assistant for Baptist Health.

Symptom: {symptom}
Urgency: {urgency}

Rules:
- If chest pain, difficulty breathing, stroke symptoms, or severe bleeding:
  return EMERGENCY
- Otherwise return ROUTINE

Return only one word:
EMERGENCY or ROUTINE
"""
)
triage_chain = triage_prompt | llm