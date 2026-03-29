from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from ...services.chat_recommend import ChatRecommendService
from ...schemas.chat import ChatRequest, ChatResponse
import json

router = APIRouter(prefix="/chat", tags=["chat"])
chat_service = ChatRecommendService()

def _build_prompt(request: ChatRequest) -> str:
    conditions = ", ".join(request.medical_conditions) if request.medical_conditions else "Không có"
    return (
        f"Thông tin người dùng:\n"
        f"- Cân nặng: {request.weight}kg, Chiều cao: {request.height}cm\n"
        f"- Mục tiêu: {request.goal}\n"
        f"- Yêu cầu: {request.requirement}\n"
        f"- Chế độ ăn: {request.diet_type}\n"
        f"- Bệnh lý: {conditions}\n"
        f"Hãy gợi ý bài tập phù hợp."
    )

@router.post("/workout", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        prompt = _build_prompt(request)
        result = chat_service.chat(prompt)
        return ChatResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/workout/stream")
async def stream_chat(request: ChatRequest):
    async def event_generator():
        try:
            prompt = _build_prompt(request)
            async for event in chat_service.stream_chat(prompt):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        except Exception as e:
            yield f"data: {{\"error\": \"{str(e)}\"}}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")