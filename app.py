from flask import Flask, render_template
import json

app = Flask(__name__)

def load_data():
    # Load projects
    try:
        with open('projects.json') as f:
            projects = json.load(f)
    except Exception as e:
        print(f"Error loading projects: {e}")
        projects = []
    
    # Load experience
    try:
        with open('experience.json') as f:
            experience = json.load(f)
    except Exception as e:
        print(f"Error loading experience: {e}")
        experience = []
    
    # Load education
    try:
        with open('education.json') as f:
            education = json.load(f)
    except Exception as e:
        print(f"Error loading education: {e}")
        education = []
    try:
        with open('about_me.txt') as f:
            about_me = f.read()
    except Exception as e:
        print(f"Error loading education: {e}")
        about_me = []
    
    return projects, experience, education,about_me

@app.route('/')
def index():
    projects, experience, education,about_me = load_data()
    return render_template('index.html', 
                         projects=projects,
                         experience=experience,
                         education=education,
                         about_me = about_me)



if __name__ == '__main__':
    app.run(debug=True, port = 8000)
