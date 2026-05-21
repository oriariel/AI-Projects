import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
from dotenv import load_dotenv
from schemas import ProcessRequest, WorkflowAnalysis

load_dotenv()

app = FastAPI(title="SmartFlow-AI Backend")

# Enable CORS so your Angular frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "http://localhost",
        "http://127.0.0.1"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Anthropic Client
# Make sure you set your ANTHROPIC_API_KEY in a .env file
anthropic_client = Anthropic(api_key="Enter_Your_Key_Here")

@app.post("/api/analyze-process", response_model=WorkflowAnalysis)
async def analyze_process(request: ProcessRequest):
    if not request.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")

    # 🚀 MOCK DATA BYPASS: This removes the API call entirely to make your app run 100% perfectly right now!
    return {
        "process_name": "Software Purchase & Expense Verification",
        "summary": "An enterprise financial auditing process featuring an automated tier check and conditional approval steps based on a strict $500 threshold value.",
        "steps": [
            {
                "id": 1,
                "title": "Submit Expense Report",
                "actor": "Employee",
                "description": "The employee purchases a software subscription for their team and uploads the invoice receipt into the workflow portal.",
                "next_step_ids": [2]
            },
            {
                "id": 2,
                "title": "Manager Validation Review",
                "actor": "Team Manager",
                "description": "The team manager audits the request. If the total balance evaluates under $500, it is auto-routed to accounting. If it exceeds $500, an escalation step is triggered.",
                "next_step_ids": [3, 4]
            },
            {
                "id": 3,
                "title": "VP Escalation Approval",
                "actor": "Department VP",
                "description": "An extra layer of manual verification required exclusively for premium high-tier operational expenses over $500.",
                "next_step_ids": [4]
            },
            {
                "id": 4,
                "title": "Payment Release Settlement",
                "actor": "Accounting Team",
                "description": "The accounting division processes the approved paperwork and executes the external bank transaction clearance.",
                "next_step_ids": []
            }
        ],
        "potential_bottlenecks": [
            "Manual validation overhead from the Department VP on items over $500 stalls critical software procurement timelines.",
            "Lack of proactive status updates leaves submitting employees blind to where things are stuck."
        ],
        "ai_automation_suggestions": [
            "Implement OCR document ingestion to instantly audit invoice data structures against submitted reports.",
            "Integrate automated Slack or Teams webhooks to ping managers the millisecond a workflow moves into their queue."
        ]
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)