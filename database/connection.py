import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

COGNODB_URI = os.getenv("COGNODB_URI")
COGNODB_USERNAME = os.getenv("COGNODB_USERNAME")
COGNODB_PASSWORD = os.getenv("COGNODB_PASSWORD")


class Database:
    def __init__(self):
        if not all((COGNODB_URI, COGNODB_USERNAME, COGNODB_PASSWORD)):
            raise RuntimeError(
                "COGNODB_URI, COGNODB_USERNAME, and COGNODB_PASSWORD must be configured."
            )

        self.driver = GraphDatabase.driver(
            COGNODB_URI,
            auth=(COGNODB_USERNAME, COGNODB_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def verify_connection(self):
        try:
            with self.driver.session() as session:
                result = session.run("RETURN 'CognoDB connection successful!' AS message")
                record = result.single()
                return record["message"]
        except Exception as e:
            return f"Connection failed: {e}"


db = None


def get_database():
    global db

    if db is None:
        db = Database()

    return db