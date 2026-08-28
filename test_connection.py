from database.connection import get_database

message = get_database().verify_connection()

print(message)

get_database().close()