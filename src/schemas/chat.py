from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class ChatRequest(BaseModel):
    prompt: str

class ExerciseItem(BaseModel):
    exercise_id: int
    reps: int
    duration_seconds: int
    rest_seconds: int
    order_index: int

class WorkoutSuggestion(BaseModel):
    title: str
    description: str
    level: str
    total_estimated_duration: int
    exercises: List[ExerciseItem]

class ChatResponse(BaseModel):
    content: str
    workout_suggestion: Optional[WorkoutSuggestion] = None
    