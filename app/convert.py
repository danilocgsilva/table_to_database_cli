from table_to_database.MySqlConfiguration import MySqlConfiguration
import os
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.ToDatabaseCore import ToDatabaseCore

mysqlConfiguration = MySqlConfiguration()

database_host_address = os.environ.get("DATABASE_HOST")
database_user = os.environ.get("DATABASE_USER")
database_password = os.environ.get("DATABASE_PASSWORD")
database_name = os.environ.get("DATABASE_NAME")

mysqlConfiguration.host = database_host_address
mysqlConfiguration.user = database_user
mysqlConfiguration.password = database_password
mysqlConfiguration.database = database_name

toDatabase = ToDatabase(ToDatabaseCore())
toDatabase.set_database_configuration(mysqlConfiguration)

table_path = input("Write the table path: ")
try:
    toDatabase.to_database(table_path)
except Exception as e:
    print(f"It was not possible to convert the table data from {table_path} into a database format.")
    print(e)
