install: requirements.txt
	pip install -r requirements.txt

start: app.py
	uvicorn app:app --port 8009 --reload