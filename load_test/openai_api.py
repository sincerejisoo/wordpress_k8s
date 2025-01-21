import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "I am going to make a dummy post for my wordpress blog to test the API."
        },
        {
            "role": "user",
            "content": "Please make a post with the title 'Sample Post #i' and the content is on your own. Make ten copies"
        }
    ]
)

print(completion.choices[0].message.content)