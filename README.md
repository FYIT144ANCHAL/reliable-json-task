# Reliable JSON Task - Task 02 Structured Output

Make a model return JSON your code can rely on.

## What it must include - Completed
- **Schema**: Pydantic BaseModel defines required JSON structure
- **Validation**: Rejects bad output with Pydantic validation
- **Retry/Repair**: Fixes common LLM errors (markdown fences, trailing commas, single quotes) and retries up to 3 times
- **Outcome**: Small script that always returns valid, typed data

## How to run
pip install -r requirements.txt
python main.py

## Files
- main.py - main logic with schema, validation, repair
- requirements.txt - dependencies
- README.md - this file
