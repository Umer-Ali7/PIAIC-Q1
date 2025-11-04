# Live Cricket Scores (Flask)

A tiny Flask app that fetches live cricket scores from ESPNcricinfo''s RSS feed and displays them nicely.

## Setup

1. Create and activate a virtual environment (recommended):

   python -m venv .venv
   .venv\\Scripts\\activate

2. Install dependencies:

   pip install -r requirements.txt

## Run

From the project root (this folder):

   set FLASK_APP=app
   set FLASK_ENV=development
   flask run --port 5000

Then open http://127.0.0.1:5000 in your browser.

## Notes

- The app caches the feed for 60 seconds to reduce network calls.
- If the feed fails to load, an error banner is shown and the page still renders.
