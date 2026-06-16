question_bank = {

    "Python": [
        "What is a list in Python?",
        "What is OOP?",
        "What is a decorator?"
    ],

    "Machine Learning": [
        "What is supervised learning?",
        "What is Random Forest?",
        "Explain bias-variance tradeoff."
    ],

    "SQL": [
        "What is a JOIN?",
        "Difference between WHERE and HAVING?",
        "What is normalization?"
    ]
}
def generate_questions(skills):

    questions = []

    for skill in skills:

        if skill in question_bank:

            questions.extend(
                question_bank[skill]
            )

    return questions