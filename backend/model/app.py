import streamlit as st
import google.generativeai as genai
import os
import json
import requests
import docx2txt
import PyPDF2 as pdf
from dotenv import load_dotenv
import time
import json


# Load environment variables from a .env file
load_dotenv()

# Configure the generative AI model with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model configuration for text generation
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# Define safety settings for content generation
safety_settings = [
    {"category": f"HARM_CATEGORY_{category}", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
    for category in ["HARASSMENT", "HATE_SPEECH", "SEXUALLY_EXPLICIT", "DANGEROUS_CONTENT"]
]


def generate_response_from_gemini(input_text):
    # Create a GenerativeModel instance with 'gemini-pro' as the model type
    llm = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    # Generate content based on the input text
    output = llm.generate_content(input_text)
    # Return the generated text
    return output.text


def extract_text_from_pdf_file(uploaded_file):
    # Use PdfReader to read the text content from a PDF file
    pdf_reader = pdf.PdfReader(uploaded_file)
    text_content = ""
    for page in pdf_reader.pages:
        text_content += str(page.extract_text())
    return text_content


def extract_text_from_docx_file(uploaded_file):
    # Use docx2txt to extract text from a DOCX file
    return docx2txt.process(uploaded_file)


# Prompt Template
input_prompt_template = """
As an expert in resume and interview reviews, specializing in technology, 
software engineering, data science, full stack web development, cloud engineering, 
DevOps, and big data, your role is to evaluate resumes against job descriptions. 
Provide top-notch assistance in improving resumes to stand out in the competitive job market. 
Your goal is to analyze the resume for relevant skills, experience, and qualifications matching 
the job description provided, highlighting keywords from job description, 
and giving professional feedback for improvements on the resume. 
Lastly, give some industry tips to how to prepare on the interview.
resume:{text}
description:{job_description}
I want the response in one single string having the structure
{{"Job Description Match":"%","Job Description Keywords":"","Highight Experience":", "Resume Feedback":"", "Interview Prep Tips":""}}
"""

# Streamlit app
# Initialize Streamlit app

st.set_page_config(page_title="Resume Review Pro")

st.title("Resume Review")
st.markdown('<style>h1{color: black; text-align: center; font-family:POPPINS}</style>', unsafe_allow_html=True)

job_description = st.text_area("Paste the Job Description", height=300)
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx"], help="Please upload a PDF or DOCX file")

if uploaded_file is not None:
    st.markdown('<h8 style="color: #1A4D2E;text-align: center;">File uploaded successfully!</h8>', unsafe_allow_html=True)
else:
    st.markdown('<h8 style="color: black;text-align: center;">Please upload your Resume!</h8>', unsafe_allow_html=True)

submit_button = st.button("Review Result")


if submit_button:
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf_file(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx_file(uploaded_file)
        response_text = generate_response_from_gemini(input_prompt_template.format(text=resume_text, job_description=job_description))
        # print(type(response_text))
        # print(response_text)

        st.subheader('Resume Evaluation Result', divider='rainbow')
        # check if the app can get response from the gemini, show on the website if there is response
        if response_text:
            if json.loads(response_text):
                response_text = json.loads(response_text)

                if 'Job Description Match' in response_text:
                    match_percentage = response_text['Job Description Match'].replace("\n", "<br>")
                    st.markdown('<h3 style="color: black;text-align: left;">Job Description Match:</h3>', unsafe_allow_html=True)
                    st.write(f"<div style='text-align:left; font-family: sans-serif; font-size: 15px;'>{match_percentage}</div>", unsafe_allow_html=True)

                if 'Job Description Keywords' in response_text:
                    job_keyword = response_text['Job Description Keywords'].replace("\n", "<br>")
                    st.markdown('<h3 style="color: black;text-align: left;">Job Description Keywords:</h3>', unsafe_allow_html=True)
                    st.write(f"<div style='text-align:left; font-family: sans-serif; font-size: 15px;'>{job_keyword}</div>", unsafe_allow_html=True)


                if "Highight Experience" in response_text:
                    job_exp = response_text["Highight Experience"].replace("\n", "<br>")
                    st.markdown('<h3 style="color: black;text-align: left;">Highight Experience:</h3>', unsafe_allow_html=True)
                    st.write(f"<div style='text-align:left; font-family: sans-serif; font-size: 15px;'>{job_exp}</div>", unsafe_allow_html=True)


                if "Resume Feedback" in response_text:
                    res_feeback = response_text["Resume Feedback"].replace("\n", "<br>")
                    st.markdown('<h3 style="color: black;text-align: left;">Resume Feedback:</h3>', unsafe_allow_html=True)
                    st.write(f"<div style='text-align:left; font-family: sans-serif; font-size: 15px;'>{res_feeback}</div>", unsafe_allow_html=True)

                if "Interview Prep Tips" in response_text:
                    interview_tips = response_text["Interview Prep Tips"].replace("\n", "<br>")
                    st.markdown('<h3 style="color: black;text-align: left;">Interview Prep Tips:</h3>', unsafe_allow_html=True)
                    st.write(f"<div style='text-align:left; font-family: sans-serif; font-size: 15px;'>{interview_tips}</div>", unsafe_allow_html=True)

            else:
                st.markdown('<h3 style="color: yellow; text-align: left;">Unable to get expected output.</h3>', unsafe_allow_html=True)
        else:
            st.markdown('<h3 style="color: yellow; text-align: left;">Unable to get expected output.</h3>', unsafe_allow_html=True)
    else:
        st.markdown('<h6 style="color: black;text-align: center;">Please upload your Resume!</h6>', unsafe_allow_html=True)



