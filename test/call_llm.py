import boto3
from strands.models import BedrockModel
from strands import Agent

print("Connecting to AWS Bedrock...")

session = boto3.Session(
    aws_access_key_id="AKIAZI2LD5URJHK7U2PN",
    aws_secret_access_key="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",
    region_name="us-east-1"
)

bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    boto_session=session
)

agent = Agent(model=bedrock_model)

print("Sending request...")

try:
    response = agent("Hello, how are you?")
    print("\nResponse:")
    print(response.message)
except Exception as e:
    print(f"\nError: {e}")