import pytest
from src.connectors.postgres.postgres_connector import PostgresConnectorContextManager
from src.data_quality.data_quality_validation_library import DataQualityLibrary
from src.connectors.file_system.parquet_reader import ParquetReader

def pytest_addoption(parser):
    parser.addoption("--db_host", action="store", default="localhost", help="Database host")

def pytest_configure(config):
    """
    Validates that all required command-line options are provided.
    """
    required_options = [
        "--db_user", "--db_password"
    ]
    for option in required_options:
        if not config.getoption(option):
            pytest.fail(f"Missing required option: {option}")

# @pytest.fixture(scope='session')
# def db_connection(request):
#     ...
#     try:
#         with PostgresConnectorContextManager(...) as db_connector:
#             yield db_connector
#     except Exception as e:
#         pytest.fail(f"Failed to initialize PostgresConnectorContextManager: {e}")
#
# ...
def db_connection(request):
    db_params = {
        "db_host": request.config.getoption("--db_host"),
        "db_port": int(request.config.getoption("--db_port")),
        "db_name": request.config.getoption("--db_name"),
        "db_user": request.config.getoption("--db_user"),
        "db_password": request.config.getoption("--db_password")
    }
    try:
        with PostgresConnectorContextManager(**db_params) as db_connector:
            yield db_connector
    except Exception as e:
        pytest.fail(f"Failed to initialize PostgresConnectorContextManager: {e}")