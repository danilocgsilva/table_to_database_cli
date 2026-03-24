from table_to_database.MySqlConfiguration import MySqlConfiguration
import os

mysqlConfiguration = MySqlConfiguration()

database_host_address = os.environ.get("DATABASE_HOST")
database_user = os.environ.get("DATABASE_USER")
database_password = os.environ.get("DATABASE_PASSWORD")
database_name = os.environ.get("DATABASE_NAME")

mysqlConfiguration.host = database_host_address
mysqlConfiguration.user = database_user
mysqlConfiguration.password = database_password
mysqlConfiguration.database = database_name


