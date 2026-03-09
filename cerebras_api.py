
import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras

load_dotenv()

client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY")
)

def email_summarize(content):
    completion = client.chat.completions.create(
        messages=[{"role":"user","content": content}],
        model="llama3.1-8b",
        max_completion_tokens=1024,
        temperature=0.2,
        top_p=1,
        stream=False
    )

    return completion.choices[0].message.content