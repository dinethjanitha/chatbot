# Chatbot with LangChain and Google Gemini

This project is a chatbot built using LangChain and Google's Gemini AI model.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google API Key for Gemini

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dinethjanitha/chatbot
cd chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv .
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source bin/activate
```

### 4. Install Dependencies

Install from requirements file (if available):
```bash
pip install -r requirements.txt
```

### 5. Set Up Google Gemini API Key

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_api_key_here
```

## Project Structure

```
chatbot/
├── main.py              # Main application file
├── agents/              # Agent-related modules
│   └── tools.py         # Custom tools for agents
├── README.md            # This file
├── .env                 # Environment variables (create this)
└── requirements.txt     # Python dependencies
```

## Running the Application

```bash
fastapi dev main.py
```

## Documentation References

### LangChain Documentation
- **Official Documentation**: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)
- **LangChain Google Gemini Integration**: [https://python.langchain.com/docs/integrations/chat/google_generative_ai](https://python.langchain.com/docs/integrations/chat/google_generative_ai)
- **LangGraph Documentation**: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
- **LangChain Core Concepts**: [https://python.langchain.com/docs/concepts/](https://python.langchain.com/docs/concepts/)

### Google Gemini Documentation
- **Gemini API Documentation**: [https://ai.google.dev/docs](https://ai.google.dev/docs)
- **Get Started with Gemini**: [https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python)


## Common Issues and Troubleshooting

### API Key Issues
- Ensure your `.env` file is in the project root
- Verify the API key is valid and active
- Check that `python-dotenv` is installed: `pip install python-dotenv`

### Import Errors
- Make sure virtual environment is activated
- Reinstall packages if needed: `pip install --upgrade langchain langchain-google-genai`

### Rate Limiting
- Gemini API has rate limits. Implement retry logic or use exponential backoff
- Consider upgrading your API quota if needed

## Changelog

See [ChangeLog.md](ChangeLog.md) for version history and updates.
