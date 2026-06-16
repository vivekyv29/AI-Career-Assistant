from fastapi import APIRouter
from pydantic import BaseModel

from services.chatbot_service import ask_gemini

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):

    response = ask_gemini(
        request.message
    )

    return {
        "response": response
    }