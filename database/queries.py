from database.connection import get_database


def get_all_careers():
    query = """
    MATCH (c:Career)
    RETURN c.name AS name, c.description AS description
    ORDER BY c.name
    """

    with get_database().driver.session() as session:
        result = session.run(query)
        return [record.data() for record in result]


def get_career(career_name):
    query = """
    MATCH (c:Career {name: $career_name})
    RETURN c.name AS name, c.description AS description
    """

    with get_database().driver.session() as session:
        result = session.run(query, career_name=career_name)
        record = result.single()

        if record:
            return record.data()

        return None


def get_required_skills(career_name):
    query = """
    MATCH (c:Career {name: $career_name})-[:REQUIRES]->(s:Skill)
    RETURN s.name AS name,
           s.category AS category,
           s.level AS level
    ORDER BY s.name
    """

    with get_database().driver.session() as session:
        result = session.run(query, career_name=career_name)
        return [record.data() for record in result]


def get_courses_for_career(career_name):
    """
    Multi-hop graph traversal:

    Career -> Skill <- Course
    """

    query = """
    MATCH (c:Career {name: $career_name})
          -[:REQUIRES]->(s:Skill)
          <-[:COVERS]-(course:Course)

    RETURN DISTINCT
           course.name AS name,
           course.provider AS provider,
           course.level AS level
    ORDER BY course.name
    """

    with get_database().driver.session() as session:
        result = session.run(query, career_name=career_name)
        return [record.data() for record in result]


def get_projects_for_career(career_name):
    query = """
    MATCH (c:Career {name: $career_name})
          -[:HAS_PROJECT]->(p:Project)

    RETURN p.name AS name,
           p.difficulty AS difficulty,
           p.description AS description
    ORDER BY p.name
    """

    with get_database().driver.session() as session:
        result = session.run(query, career_name=career_name)
        return [record.data() for record in result]


def get_related_careers(career_name):
    query = """
    MATCH (c:Career {name: $career_name})
          -[:RELATED_TO]->(related:Career)

    RETURN related.name AS name,
           related.description AS description
    ORDER BY related.name
    """

    with get_database().driver.session() as session:
        result = session.run(query, career_name=career_name)
        return [record.data() for record in result]


def get_career_path(career_name):
    """
    Find connected careers through shared skills.

    Career -> Skill <- Career
    """

    query = """
    MATCH (c1:Career {name: $career_name})
          -[:REQUIRES]->(s:Skill)
          <-[:REQUIRES]-(c2:Career)

    WHERE c1 <> c2

    RETURN DISTINCT
           c2.name AS name,
           collect(DISTINCT s.name) AS shared_skills

    ORDER BY c2.name
    """

    with get_database().driver.session() as session:
        result = session.run(query, career_name=career_name)
        return [record.data() for record in result]


def get_career_graph(career_name):
    query = """
    MATCH (c:Career {name: $career_name})

    OPTIONAL MATCH (c)-[r]->(n)

    RETURN
        elementId(c) AS source_id,
        c.name AS source_name,
        labels(c)[0] AS source_type,
        type(r) AS relationship,
        elementId(n) AS target_id,
        n.name AS target_name,
        labels(n)[0] AS target_type
    """

    with get_database().driver.session() as session:
        result = session.run(query, career_name=career_name)

        return [record.data() for record in result]