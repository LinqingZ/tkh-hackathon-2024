import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

genai.configure(api_key="AIzaSyAYp0biB5gY3V5z8OaN7buJzysvNpHNm5M")
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def improve_resume(resume_text):
    # Specify the prompt for the GPT-3 model
    prompt = f"Improve the following resume keep the format and same information:\n{resume_text}\n\nImproved Resume:"
    
    # Request the model to generate improved text
    response = model.generate_content(prompt)
    
    # Extract the improved text from the response
    print(response.text)
    return response.text

# Example usage

# improved_resume = improve_resume(resume_text)