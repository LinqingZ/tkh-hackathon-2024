# Resume Review Pro

Welcome to Resume Review Pro, a tool designed to help you evaluate resumes against job descriptions, providing valuable feedback and interview preparation tips. This application utilizes AI technology to analyze resumes and offer insights into how well they match specific job descriptions, highlight relevant keywords, and provide professional feedback for improvement.

## Getting Started

Follow these steps to set up and run the application:

1. **Create a Python Virtual Environment**: Set up a virtual environment using `virtualenv` to isolate project dependencies.
   ```bash
   python -m virtualenv .
   ```

2. **Activate Virtual Environment**: Activate the virtual environment in your terminal.
   ```bash
   .\scripts\activate
   ```

3. **Install Dependencies**: Install the required dependencies listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate Gemini Pro API Key**: Obtain an API key for the Gemini Pro model. This key will be used to configure the generative AI model.

5. **Create .env File**: Create a `.env` file in the project directory and define your API key.
   ```plaintext
   GOOGLE_API_KEY = "Your API Key"
   ```

6. **Run the Application**: Start the application using Streamlit.
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Job Description Input**: Paste the job description into the designated text area.

2. **Resume Upload**: Upload the resume you want to evaluate. Supported file formats include PDF and DOCX.

3. **Review Result**: Click the "Review Result" button to initiate the evaluation process.

4. **Evaluation Results**: The application will display the evaluation results, including job description match percentage, highlighted keywords, highlighted experience, resume feedback, and interview preparation tips.

## Dependencies

- Streamlit
- Google Generative AI
- PyPDF2
- docx2txt
- python-dotenv

