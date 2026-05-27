AI Assistant
A modular AI assistant built in Python with support for local commands, offline-first behavior, LLM fallback, reminders, and voice interaction.

Features
Modular command system
NLP-based intent detection
Offline/local handling for common tasks
LLM fallback for general questions
Conversation memory for contextual replies
Notes storage
Calculator
System information
Sample weather handling
Reminder system with background worker
Voice input and voice output support
Cache for repeated answers
Tech Stack
Python
asyncio
threading
SQLite
JSON storage
OpenAI-compatible SDK
Speech/audio libraries


Project Structure
bash
ai_assistant/
│
├── main.py
├── .env
├── assistant/
├── commands/
├── nlp/
├── services/
└── data/

How it works

User gives input by text or voice
Intent classifier detects what the user wants
Matching local command is executed if available
If local system cannot answer, offline knowledge/cache is checked
If still unanswered, the query is sent to the LLM
Response is returned as text and optionally audio
Supported Commands
calculate (Maths)
save note buy milk
show notes
system info
what is the weather in delhi
remind me to drink water in 5 minutes



Setup
Install dependencies:

bash
pip install -r requirements.txt
Create .env file:

env
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=your_base_url_here
OPENAI_MODEL=openai/gpt-4o-mini
Run:

bash
python main.py
Purpose
This project demonstrates:

clean software architecture
modular design
offline-first assistant behavior
multithreading
async handling
NLP intent routing
hybrid AI assistant design
If you want, I can also make it into a more professional GitHub-style README with:

installation
screenshots section
features section
future improvements
project highlights for resume/projects.
