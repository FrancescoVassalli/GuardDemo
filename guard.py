from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def check_statement(statement:str):
    completion= client.chat.completions.create(
        model="llama-guard-3-8b",
        messages=[
            {
                "role": "system",
                "content": "Task: Check if there is unsafe content in children's video game contents according our safety policy with the below categories.\n\n<BEGIN UNSAFE CONTENT CATEGORIES>\nS1: Violent Crimes. \nS2: Non-Violent Crimes. \nS3: Sex Crimes. \nS4: Child Exploitation. \nS5: Defamation. \nS6: Specialized Advice. \nS7: Privacy. \nS8: Intellectual Property. \nS9: Indiscriminate Weapons. \nS10: Hate. \nS11: Self-Harm. \nS12: Sexual Content. \nS13: Elections. \n<END UNSAFE CONTENT CATEGORIES>"
            },
            {
                "role": "user",
                "content": f"{statement}"
            }
        ],
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content
