from database.base_database import Base_Database_Postres

postreges_connection = Base_Database_Postres('users')

postreges_connection.connect()

postreges_connection.execute_query("SELECT * FROM users")
# postreges_connection.execute_query(
#     "INSERT INTO users (type, name, password)"
#     "VALUES('ADMIN', 'Alexandre', '1234');")
# postreges_connection.execute_query("SELECT * FROM users")
# postreges_connection.disconnect()
