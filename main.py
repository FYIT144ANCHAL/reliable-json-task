from pydantic import BaseModel, ValidationError, Field
from typing import List
import json
import re

class UserData(BaseModel):
    name: str = Field(description="User's full name")
    age: int = Field(ge=0, le=120)
    email: str
    skills: List[str]

def get_reliable_json(llm_response: str) -> dict:
    json_match = re.search(r'\{.*\}', llm_response, re.DOTALL)
    if not json_match:
        raise ValueError("No JSON found")
    json_str = json_match.group()
    try:
        data = json.loads(json_str)
    except:
        data = json.loads(json_str.replace("'", '"'))
    validated = UserData(**data)
    return validated.model_dump()

if __name__ == "__main__":
    test_resp = 'Here is JSON: {"name": "Anchal", "age": 21, "email": "anchal@test.com", "skills": ["Python", "GitHub"]}'
    print(get_reliable_json(test_resp))
