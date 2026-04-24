from langchain_core.prompts import PromptTemplate
from services.openai_client import llm

intent_prompt = PromptTemplate.from_template("""
Extract:
- symptom
- urgency
- department

Return ONLY JSON:
{{
  "symptom": "",
  "urgency": "",
  "department": ""
}}

Message:
{message}
""")

intent_chain = intent_prompt | llm