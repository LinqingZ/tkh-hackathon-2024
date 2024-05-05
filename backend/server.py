
# Filename - server.py
 
# Import flask and datetime module for showing date and time
from flask import Flask, request
import datetime
from improver import improve_resume
 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
 
 
# Route for seeing a data
@app.route('/data')
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
 
@app.route('/display_string', methods=['POST'])
def display_string():
    data = request.json
    resume = data.get('string', '')
    improved_resume = improve_resume(resume)
    return {
        "improved_resume":i
    }

# Running app
if __name__ == '__main__':
    app.run(debug=True)