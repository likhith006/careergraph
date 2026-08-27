from database.connection import db

message = db.verify_connection()

print(message)

db.close()