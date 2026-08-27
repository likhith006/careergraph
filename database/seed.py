from database.connection import db


def seed_database():
    with db.driver.session() as session:

        # -------------------------
        # Careers
        # -------------------------
        careers = [
            {
                "name": "Data Scientist",
                "description": "Analyzes data and builds predictive models to solve business problems."
            },
            {
                "name": "Machine Learning Engineer",
                "description": "Builds and deploys machine learning models and intelligent applications."
            },
            {
                "name": "Data Analyst",
                "description": "Analyzes datasets and creates insights, reports, and dashboards."
            },
            {
                "name": "AI Engineer",
                "description": "Develops applications using artificial intelligence and machine learning."
            }
        ]

        for career in careers:
            session.run(
                """
                MERGE (c:Career {name: $name})
                SET c.description = $description
                """,
                career
            )

        # -------------------------
        # Skills
        # -------------------------
        skills = [
            {"name": "Python", "category": "Programming", "level": "Intermediate"},
            {"name": "SQL", "category": "Database", "level": "Intermediate"},
            {"name": "Machine Learning", "category": "AI", "level": "Advanced"},
            {"name": "Statistics", "category": "Mathematics", "level": "Intermediate"},
            {"name": "Data Visualization", "category": "Analytics", "level": "Intermediate"},
            {"name": "Deep Learning", "category": "AI", "level": "Advanced"},
            {"name": "TensorFlow", "category": "AI Framework", "level": "Advanced"},
            {"name": "Natural Language Processing", "category": "AI", "level": "Advanced"},
            {"name": "Git", "category": "Development", "level": "Beginner"}
        ]

        for skill in skills:
            session.run(
                """
                MERGE (s:Skill {name: $name})
                SET s.category = $category,
                    s.level = $level
                """,
                skill
            )

        # -------------------------
        # Courses
        # -------------------------
        courses = [
            {
                "name": "Python for Data Science",
                "provider": "Coursera",
                "level": "Beginner"
            },
            {
                "name": "SQL for Data Analysis",
                "provider": "DataCamp",
                "level": "Intermediate"
            },
            {
                "name": "Machine Learning Fundamentals",
                "provider": "Coursera",
                "level": "Intermediate"
            },
            {
                "name": "Deep Learning with TensorFlow",
                "provider": "Udemy",
                "level": "Advanced"
            },
            {
                "name": "Statistics for Data Science",
                "provider": "edX",
                "level": "Intermediate"
            },
            {
                "name": "Natural Language Processing",
                "provider": "Coursera",
                "level": "Advanced"
            }
        ]

        for course in courses:
            session.run(
                """
                MERGE (c:Course {name: $name})
                SET c.provider = $provider,
                    c.level = $level
                """,
                course
            )

        # -------------------------
        # Projects
        # -------------------------
        projects = [
            {
                "name": "Customer Churn Prediction",
                "difficulty": "Intermediate",
                "description": "Build a machine learning model to predict customer churn."
            },
            {
                "name": "Sales Dashboard",
                "difficulty": "Beginner",
                "description": "Create an interactive dashboard for analyzing sales data."
            },
            {
                "name": "Image Classification",
                "difficulty": "Advanced",
                "description": "Build a deep learning model for image classification."
            },
            {
                "name": "Sentiment Analysis",
                "difficulty": "Advanced",
                "description": "Analyze text and classify customer sentiment."
            }
        ]

        for project in projects:
            session.run(
                """
                MERGE (p:Project {name: $name})
                SET p.difficulty = $difficulty,
                    p.description = $description
                """,
                project
            )

        # -------------------------
        # Career -> Skill
        # -------------------------
        career_skills = {
            "Data Scientist": [
                "Python",
                "SQL",
                "Machine Learning",
                "Statistics",
                "Data Visualization"
            ],
            "Machine Learning Engineer": [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "Git"
            ],
            "Data Analyst": [
                "Python",
                "SQL",
                "Statistics",
                "Data Visualization"
            ],
            "AI Engineer": [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "Natural Language Processing"
            ]
        }

        for career, skill_list in career_skills.items():
            for skill in skill_list:
                session.run(
                    """
                    MATCH (c:Career {name: $career})
                    MATCH (s:Skill {name: $skill})
                    MERGE (c)-[:REQUIRES]->(s)
                    """,
                    {"career": career, "skill": skill}
                )

        # -------------------------
        # Course -> Skill
        # -------------------------
        course_skills = {
            "Python for Data Science": ["Python"],
            "SQL for Data Analysis": ["SQL"],
            "Machine Learning Fundamentals": ["Machine Learning"],
            "Deep Learning with TensorFlow": ["Deep Learning", "TensorFlow"],
            "Statistics for Data Science": ["Statistics"],
            "Natural Language Processing": ["Natural Language Processing"]
        }

        for course, skill_list in course_skills.items():
            for skill in skill_list:
                session.run(
                    """
                    MATCH (c:Course {name: $course})
                    MATCH (s:Skill {name: $skill})
                    MERGE (c)-[:COVERS]->(s)
                    """,
                    {"course": course, "skill": skill}
                )

        # -------------------------
        # Career -> Project
        # -------------------------
        career_projects = {
            "Data Scientist": [
                "Customer Churn Prediction",
                "Sales Dashboard"
            ],
            "Machine Learning Engineer": [
                "Customer Churn Prediction",
                "Image Classification"
            ],
            "Data Analyst": [
                "Sales Dashboard"
            ],
            "AI Engineer": [
                "Image Classification",
                "Sentiment Analysis"
            ]
        }

        for career, project_list in career_projects.items():
            for project in project_list:
                session.run(
                    """
                    MATCH (c:Career {name: $career})
                    MATCH (p:Project {name: $project})
                    MERGE (c)-[:HAS_PROJECT]->(p)
                    """,
                    {"career": career, "project": project}
                )

        # -------------------------
        # Career -> Career
        # -------------------------
        related_careers = [
            ("Data Scientist", "Machine Learning Engineer"),
            ("Data Scientist", "Data Analyst"),
            ("Machine Learning Engineer", "AI Engineer"),
            ("Data Analyst", "Data Scientist")
        ]

        for career1, career2 in related_careers:
            session.run(
                """
                MATCH (c1:Career {name: $career1})
                MATCH (c2:Career {name: $career2})
                MERGE (c1)-[:RELATED_TO]->(c2)
                """,
                {
                    "career1": career1,
                    "career2": career2
                }
            )

    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
    db.close()