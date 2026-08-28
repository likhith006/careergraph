from database.connection import get_database


def create_constraints():
    queries = [
        """
        CREATE CONSTRAINT career_name_unique IF NOT EXISTS
        FOR (c:Career)
        REQUIRE c.name IS UNIQUE
        """,
        """
        CREATE CONSTRAINT skill_name_unique IF NOT EXISTS
        FOR (s:Skill)
        REQUIRE s.name IS UNIQUE
        """,
        """
        CREATE CONSTRAINT course_name_unique IF NOT EXISTS
        FOR (c:Course)
        REQUIRE c.name IS UNIQUE
        """,
        """
        CREATE CONSTRAINT project_name_unique IF NOT EXISTS
        FOR (p:Project)
        REQUIRE p.name IS UNIQUE
        """
    ]

    with get_database().driver.session() as session:
        for query in queries:
            session.run(query)


if __name__ == "__main__":
    create_constraints()
    print("Database constraints created successfully.")
    get_database().close()