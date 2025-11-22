from src.connectors.postgres.postgres_connector import PostgresConnectorContextManager

db_params = {
    "db_host": "localhost",
    "db_port": 5434,
    "db_name": "mydatabase",
    "db_user": "myuser",
    "db_password": "mypassword"
}

# with PostgresConnectorContextManager(**db_params) as connector:
#     df = connector.get_data_sql("SELECT * FROM facilities;")
#     print(df)

import requests
from src.connectors.file_system.parquet_reader import ParquetReader

jenkins_url = "http://localhost:8080/job/dqea-pipeline-om/lastSuccessfulBuild/artifact/parquet_data/facility_name_min_time_spent_per_visit_date.parquet"
response = requests.get(jenkins_url)
with open("facility_name_min_time_spent_per_visit_date.parquet", "wb") as f:
    f.write(response.content)

df = ParquetReader.read_parquet("facility_name_min_time_spent_per_visit_date.parquet")
print(df)