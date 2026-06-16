skills_db = [

    "Python",
    "C++",
    "Java",
    "SQL",

    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Artificial Intelligence",

    "TensorFlow",
    "PyTorch",
    "Scikit-learn",

    "Pandas",
    "NumPy",

    "FastAPI",
    "Flask",

    "Git",
    "GitHub",

    "Docker",
    "AWS",

    "NLP"
]

def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in skills_db:

        if skill.lower() in text:

            detected_skills.append(skill)

    return detected_skills