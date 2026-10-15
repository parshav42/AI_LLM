from openai import OpenAI

client = OpenAI(
    base_url='http://127.0.0.1:11434/v1',
    api_key='dummy_key'

)
while True:
    n = input('user:')
    responce = client.chat.completions.create(
    model='gemma3:1b',
    messages=[
        {
            'role':'user',
            'content':n
        }
    ]
    )
    print(f'assistent:',responce.choices[0].message.content)
    if n == 'exit':
        break



