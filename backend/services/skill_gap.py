def find_missing_skills(
    user_skills,
    required_skills
):

    return list(
        set(required_skills)
        - set(user_skills)
    )