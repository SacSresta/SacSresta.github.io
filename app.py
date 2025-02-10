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
    
    # Load about_me
    try:
        with open('about_me.txt') as f:
            about_me = f.read()
    except Exception as e:
        print(f"Error loading about_me: {e}")
        about_me = ""
    
    # Load skills
    try:
        with open('skills.json') as f:
            skills = json.load(f)
            # Assuming skills are stored under a top-level "skills" key.
            skills = skills.get("skills", [])
    except Exception as e:
        print(f"Error loading skills: {e}")
        skills = []
    
    return projects, experience, education, about_me, skills

@app.route('/')
def index():
    projects, experience, education, about_me, skills = load_data()
    return render_template('index.html', 
                           projects=projects,
                           experience=experience,
                           education=education,
                           about_me=about_me,
                           skills=skills)

if __name__ == '__main__':
    app.run(debug=True, port=8000)