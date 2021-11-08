## RHGA University schedule telegram bot

### Local deploy

1. Create virtual env and activate
    
    `python -m venv venv`
    
    `$ source venv/bin/activate`
   
2. Install requirements

    `pip install -r requirements.txt`
   
3. Add excel file to the root of the project

4. Create `local_settings.py` and fill it with necessary variables (TELEGRAM_BOT_TOKEN, etc)

5. Launch uvicorn server

   `python -m uvicorn main:app --reload`