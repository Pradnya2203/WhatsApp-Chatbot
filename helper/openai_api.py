import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')



def chat_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
    if prompt=="hi":
        return {
            'status': 1,
            'response': 'Hello! How can I assist you today? Are you experiencing any specific symptoms or do you have health-related questions on your mind?'
        }
    
    s = "Just take your best guess and answer briefly the possible diagnosis and ask follow up questions and give a prescription in numbered points like you are a clinician and end it there without any extra message and don't put any extra messages about yourself, the prompt is : "
    st = s + prompt
    print(st)
    try:
        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": f'{st}'}
          ]
        )

        answer=completion.choices[0].message['content']

        print(answer)
        return {
            'status': 1,
            'response': (f'{answer}')
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
