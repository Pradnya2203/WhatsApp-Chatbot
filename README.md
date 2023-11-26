# Team Jury
## Connect chatGPT to WhatsApp
 
### Steps to setup this repository

Step 1: Create a .env file in the main directory and copy the following code 

```
OPENAI_API_KEY=
TWILIO_SID=
TWILIO_TOKEN=
```
Step 2: Create account on twilio and add the Twilio SID and Twilio token in the .env file 
                twilio: https://www.twilio.com/en-us

Step 3: Create an account on openai, generate and add the open_api_key in the .env file 
                openai: https://openai.com/

### How to use this repository

Step 1: Run ``` pip install -r requirements.txt ``` in your first terminal

Step 2: Run ``` python main.py ``` in your first terminal

Step 3: Run ``` ngrok http 5000 ``` in your second terminal

Step 4: Add the ngrok link to your twilio account in the settings section and now you are all ready to use this chatbot

