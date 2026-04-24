from langchain_core.prompts import PromptTemplate
from services.openai_client import llm

response_prompt = PromptTemplate(
    input_variables=["triage_result", "appointment"],
    template="""
You are a Baptist Health patient assistant.

If triage_result is EMERGENCY:
Return:
"Your symptoms may require immediate attention. Please visit the nearest emergency room or call 911."

Otherwise:
Return a friendly appointment confirmation using:
{appointment}
"""
)

response_chain = response_prompt | llm