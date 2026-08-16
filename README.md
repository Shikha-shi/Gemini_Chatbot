# Gemini Chatbot

This is a simple chatbot built with **Python and the Google Gemini API**. You can ask questions directly from the terminal and get responses from Gemini.

## How to Run the Project

First, clone the repository and move into the project folder:

```bash
git clone <your-repository-url>
cd Gemini_Chatbot
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install all the required packages:

```bash
pip install -r requirements.txt
```

### Add your Gemini API key

Create a file named `.env` in the project folder and add:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

**Don't share your API key or upload the `.env` file to GitHub.**

Finally, start the chatbot:

```bash
python main.py
```

You can now chat with Gemini directly in your terminal:

```text
You: hello
Gemini: Hello! How can I help you?

You: What is Python?
Gemini: Python is a programming language...
```

When you're finished, type:

```text
exit
```

to close the chatbot.
