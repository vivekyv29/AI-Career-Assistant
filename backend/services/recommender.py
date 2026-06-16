def recommend_jobs(skills):

    jobs = []

    if "Python" in skills:
        jobs.append("Python Developer")

    if "Machine Learning" in skills:
        jobs.append("Machine Learning Engineer")

    if "Deep Learning" in skills:
        jobs.append("AI Engineer")

    if "NLP" in skills:
        jobs.append("NLP Engineer")

    if "TensorFlow" in skills:
        jobs.append("Deep Learning Engineer")

    return jobs