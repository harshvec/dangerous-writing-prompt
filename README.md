# Dangerous Writing App

A minimalist writing tool with a twist — if you stop typing for too long, your progress gets wiped.  
Inspired by "The Most Dangerous Writing App," built with Flask.

## How it works

1. On the home page, set an **idle limit** in seconds.
2. Click **Start Writing** and begin typing in the text box.
3. If you stop typing for longer than the idle limit, your text is instantly cleared.
4. Keep typing to avoid losing your work!

## Tech stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, vanilla JavaScript
- Idle detection runs client-side; a request is sent to the Flask server (`/idle`) when the threshold is hit.

## Running locally

1. Clone the repo:
```bash
   git clone https://github.com/harshsh81234-web/dangerous-writing-prompt.git
   cd dangerous-writing-prompt
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run the app:
```bash
   python app.py
```

5. Open your browser at `http://127.0.0.1:5000`

## Project structure