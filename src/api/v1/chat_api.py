from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from ...services.chat_recommend import ChatRecommendService
from ...schemas.chat import ChatResponse, ChatRequest
import json

router = APIRouter(prefix="/chat", tags=["chat"])
chat_service = ChatRecommendService()

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat with AI agent that has database access."""
    try:
        result = chat_service.chat(request.prompt)
        return ChatResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stream")
async def stream_chat(request: ChatRequest):
    """Stream chat response with database access."""
    async def event_generator():
        try:
            async for event in chat_service.stream_chat(request.prompt):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        except Exception as e:
            yield f"data: {{\"error\": \"{str(e)}\"}}\n\n"
    
    return StreamingResponse(event_generator(), media_type="text/event-stream")