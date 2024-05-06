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
    prompt = f"Improve the following resume keep the format:\n{resume_text}\n\nImproved Resume:"
    
    # Request the model to generate improved text
    response = model.generate_content(prompt)
    
    # Extract the improved text from the response
    print(response.text)
    return response.text

# Example usage
resume_text = """
John Doe
123 Main Street
Anytown, USA
johndoe@email.com
555-123-4567

Objective:
Seeking a software engineering position to utilize my skills in Python, Java, and web development.

Experience:
Software Engineer Intern
XYZ Company
May 2020 - August 2020
- Developed and maintained web applications using Django framework
- Collaborated with team members to deliver high-quality software products

Education:
Bachelor of Science in Computer Science
ABC University
Graduated May 2021
"""

# improved_resume = improve_resume(resume_text)