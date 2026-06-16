roadmaps = {

    "Machine Learning Engineer": {

        "Month 1": [
            "Python",
            "SQL",
            "Git"
        ],

        "Month 2": [
            "Statistics",
            "Machine Learning"
        ],

        "Month 3": [
            "Deep Learning",
            "Projects"
        ]
    },

    "Data Scientist": {

        "Month 1": [
            "Python",
            "SQL"
        ],

        "Month 2": [
            "Statistics",
            "Machine Learning"
        ],

        "Month 3": [
            "Data Visualization",
            "Projects"
        ]
    }
}


def generate_roadmap(goal):

    return roadmaps.get(
        goal,
        {
            "message":
            "Roadmap not found"
        }
    )