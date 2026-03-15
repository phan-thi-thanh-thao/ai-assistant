import boto3
from strands.models import BedrockModel
from ...core.config import config

class ClaudeClient:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
            region_name=config.AWS_REGION
        )
        self.model = BedrockModel(
            model_id=config.CLAUDE_MODEL_ID,
            boto_session=self.session,
            temperature=config.CLAUDE_TEMPERATURE,
            max_tokens=config.CLAUDE_MAX_TOKENS
        )
    
    def get_model(self):
        return self.model

claude_client = ClaudeClient()