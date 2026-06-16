def evaluate(question, answer):

    score = min(
        len(answer.split()) // 10,
        10
    )

    return f"""
Score: {score}/10

Strengths:
- Answer provided

Improvements:
- Add more details
- Add examples
"""