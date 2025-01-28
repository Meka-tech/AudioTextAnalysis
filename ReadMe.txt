For mac backend installation
**in a fresh terminal***
-brew install python@3.11 **optional**
-cd backend
-python3.11 -m venv .venv
-source .venv/bin/activate
-pip install -r requirements.txt

frontend installation 
**in a fresh terminal**
-cd frontend && npm install


////////////////////////////////////////

# Terminal 1 - Run backend
-cd backend
-source .venv/bin/activate  # On Windows: venv\Scripts\activate
-python app.py

# Terminal 2 - Run frontend
cd frontend && npm start