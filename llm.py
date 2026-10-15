from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

client = OpenAI(
    base_url= os.getenv('API'),
    api_key='dummy_key'

)

message = []
while True:
    n = input('user:')
    message.append(
                {
            'role':'user',
            'content':n + 'after anser llm perticular topic ask qutionshort anser in 10 word '
        }
    
    )
    responce = client.chat.completions.create(
    model='gemma3:1b',
    messages=message
    )
    message.append(
                {
            'role':'assistent:',
            'content':'responce.choices[0].message.content'
        }
    
    )
    
    print(f'assistent:',responce.choices[0].message.content)
    if n.lower() in  ['exit','bye','parshav']:
        break



