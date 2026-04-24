from langchain_core.prompts import PromptTemplate
from services.openai_client import llm

schedule_prompt = PromptTemplate(
    input_variables=["department"],
    template="""
You are connected to Baptist Health scheduling.

Department: {department}

Mock available appointments:
- Cardiology: Tomorrow 10:00 AM
- Orthopedics: Friday 2:00 PM
- General Medicine: Tomorrow 4:00 PM

Return the best available slot for the department.
"""
)

scheduling_chain = schedule_prompt | llm