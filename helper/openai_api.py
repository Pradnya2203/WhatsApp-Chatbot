import os

import openai
# from dotenv import load_dotenv
# load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')



def chat_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
    try:
        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": f'{prompt}'}
          ]
        )

        answer=completion.choices[0].message['content']
        # response = openai.Completion.create(
        #     model='gpt-3.5-turbo',
        #     engine='text-davinci-003',
        #     prompt=f'Human: {prompt}\nAI: ',
        #     temperature=0.9,
        #     max_tokens=150,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0.6,
        #     stop=['Human:', 'AI:']
        # )

        # response = openai.ChatCompletion.create(
        #     model='gpt-3.5-turbo',
        #     messages=[
        #         {'role': 'system', 'content': 'You are a helpful assistant.'},
        #         {'role': 'user', 'content': prompt},
        #     ]
        # )
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
