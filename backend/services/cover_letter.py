from services.chatbot_service import ask_gemini

def generate_cover_letter(
    name,
    role,
    skills
):

    prompt = f"""
    Write a professional cover letter.

    Name: {name}

    Job Role: {role}

    Skills: {skills}
    """

    return ask_gemini(prompt)