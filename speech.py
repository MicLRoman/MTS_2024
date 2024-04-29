from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

import replicate

def get_lama_answer(
    prompt,
    system_prompt,
    temperature=0.9,
    top_p=0.5,
    max_tokens=1024,
):
    output = replicate.run(
    "meta/llama-2-70b-chat",
    input={
        "prompt": prompt,
        "system_prompt": system_prompt,
        "temperature": temperature,
        "top_p": top_p,
        "max_new_tokens": max_tokens,
    }
    )
    return "".join(output)


print(get_lama_answer('привет', 'be good'))