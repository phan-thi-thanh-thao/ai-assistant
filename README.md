# AI Assistant API

API for AI Assistant with Claude AI and Database operations.

## Features

- 🤖 Chat with Claude AI via AWS Bedrock
- 🗄️ Database operations with Supabase
- 📊 Search functionality across tables
- 🔍 User management
- 📝 Comprehensive logging

## Quick Start

### Using Docker (Recommended)

1. Clone the repository
2. Create `.env` file with required variables
3. Run with Docker Compose:

```bash
docker-compose up -d
```

### Manual Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

## API Endpoints

- **Chat**: `POST /api/v1/chat/`
- **Database**: `GET /api/v1/database/tables`
- **Users**: `GET /api/v1/database/users`
- **Search**: `POST /api/v1/database/users/search`
- **Health**: `GET /api/v1/health`
- **Docs**: `GET /docs`

## Environment Variables

```env
# AWS Bedrock
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-west-2
CLAUDE_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0
MAX_TOKENS=2048
TEMPERATURE=0.7

# Supabase
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

## Project Structure

```
src/
├── api/v1/          # API endpoints
├── bedrock/         # Claude AI service
├── database/        # Database operations
├── schemas/         # Pydantic models
└── utils/           # Utilities (logging)
```