from strands import Agent
from .bedrock.claude import claude_client
from .bedrock.system_prompt import DEFAULT

class BaseAgent:
    def __init__(self, tools=None, system_prompt=None):
        self.agent = Agent(
            model=claude_client.get_model(),
            system_prompt=system_prompt or DEFAULT,
            tools=tools or [],
            callback_handler=None
        )
    
    def chat(self, message: str):
        result = self.agent(message)
        # Extract text content from AgentResult
        if hasattr(result, 'content'):
            return result.content
        elif hasattr(result, 'text'):
            return result.text
        else:
            return str(result)
    
    async def stream_async(self, message: str):
        async for event in self.agent.stream_async(message):
            yield event

