import re

TECH_SKILLS = {
    "python",
    "java",
    "c++",
    "sql",
    "tensorflow",
    "pytorch",
    "machine learning",
    "deep learning",
    "docker",
    "aws",
    "azure",
    "gcp",
    "fastapi",
    "flask",
    "react",
    "node",
    "mongodb",
    "mysql",
    "git",
    "github",
    "kubernetes"
}


def extract_keywords(text):
    words = re.findall(
        r"[a-zA-Z+#.]+",
        text.lower()
    )

    return set(words)


def calculate_ats_score(
    resume_text,
    job_description
):

    resume_keywords = extract_keywords(
        resume_text
    )

    jd_keywords = extract_keywords(
        job_description
    )

    matched = list(
        resume_keywords &
        jd_keywords
    )

    missing = list(
        jd_keywords -
        resume_keywords
    )

    keyword_score = (
        len(matched)
        /
        max(len(jd_keywords), 1)
    ) * 100

    skills_found = [
        skill
        for skill in TECH_SKILLS
        if skill.lower()
        in resume_text.lower()
    ]

    skills_score = min(
        len(skills_found) * 5,
        100
    )

    experience_score = (
        80
        if "experience"
        in resume_text.lower()
        else 50
    )

    education_score = (
        100
        if (
            "b.tech"
            in resume_text.lower()
            or "bachelor"
            in resume_text.lower()
        )
        else 50
    )

    final_score = round(
        (
            keyword_score * 0.50
            +
            skills_score * 0.20
            +
            experience_score * 0.15
            +
            education_score * 0.15
        ),
        2
    )

    return {
        "ats_score": final_score,
        "keyword_score": round(
            keyword_score,
            2
        ),
        "skills_score": skills_score,
        "experience_score":
            experience_score,
        "education_score":
            education_score,
        "matched": matched,
        "missing": missing
    }