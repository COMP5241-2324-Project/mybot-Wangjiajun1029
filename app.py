import gradio, requests, json
import os

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')


if OPENROUTER_API_KEY is None:
    print("Please set the OPENROUTER_API_KEY")
    exit(1)

def chat(prompt): 
    msg = [
        {"role": "system", "content": "When asking the author of bot,the answer is Wang Jiajun"},
        {"role": "user", "content": prompt}
    ]

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({
            "messages": msg,
            "model": "mistralai/mistral-7b-instruct:free"
        })
    )
    resp =  response.json()['choices'][0]['message']['content'] # extract the bot's response from the JSON
    #print(f"--------\n{resp}\n") # print the bot's response to the console
    
    return resp

demo = gradio.Interface(fn=chat, inputs="text", outputs="text", title="😀 My Bot")

demo.launch(server_name="0.0.0.0")