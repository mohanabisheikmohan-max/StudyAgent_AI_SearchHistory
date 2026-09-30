# StudyAgent AI

StudyAgent AI is a Flask + Gemini AI study/technical agent.

## Features

- AI study and coding assistant
- Calculator tool
- Current-date tool
- Searchable chat history
- History stored in the browser using localStorage
- Search history by question or answer
- Open an old conversation
- Delete one history item
- Clear all history
- Quick action buttons
- Responsive dark glass UI
- Render-ready deployment

## Local setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` from `.env.example`:

```env
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-3.1-flash-lite
```

Run:

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## Render

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
gunicorn app:app
```

Add this Render environment variable:

```text
GEMINI_API_KEY = your Gemini API key
```

Do not set OAuth credentials for this project. The Python code explicitly uses:

```python
client = genai.Client(api_key=API_KEY)
```
