from typing import Dict, Any
import json
from ..agent.base_agent import BaseAgent
from ..agent.tools.db_tool import get_all_tables, get_table_data, get_record_by_id, search_in_table
from ..agent.bedrock.system_prompt import DEFAULT
from ..core.log_utils import get_logger

class ChatRecommendService:
    def __init__(self, system_prompt: str = None):
        self.agent = BaseAgent(
            tools=[get_all_tables, get_table_data, get_record_by_id, search_in_table],
            system_prompt=system_prompt or DEFAULT
        )
        self.logger = get_logger(__name__)
    
    def chat(self, user_question: str) -> Dict[str, Any]:
        """Chat with agent that has access to database tools."""
        try:
            response = self.agent.chat(user_question)
            text = str(response)

            start = text.find('{')
            end = text.rfind('}') + 1
            if start != -1 and end > start:
                parsed = json.loads(text[start:end])
                if 'workout_suggestion' not in parsed:
                    parsed = {"content": text, "workout_suggestion": None}
                return parsed

            return {"content": text, "workout_suggestion": None}

        except Exception as e:
            self.logger.error(f"Error in chat: {e}")
            return {"content": "Sorry, an error occurred.", "workout_suggestion": None}
    
    async def stream_chat(self, user_question: str):
        """Stream chat response with database access."""
        try:
            async for event in self.agent.stream_async(user_question):
                yield event
        except Exception as e:
            self.logger.error(f"Error in stream chat: {e}")
            yield {"error": "An error occurred while processing your question."}