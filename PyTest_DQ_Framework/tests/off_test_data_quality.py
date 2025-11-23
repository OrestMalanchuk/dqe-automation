import pytest
from data_quality_library import DataQualityLibrary

@pytest.mark.parquet_data
def test_source_data_not_empty(source_data):
    DataQualityLibrary.check_dataset_is_not_empty(source_data)

@pytest.mark.parquet_data
def test_no_duplicates_in_source(source_data):
    DataQualityLibrary.check_duplicates(source_data)

@pytest.mark.db
def test_facilities_table_not_empty(db_connection):
    df = db_connection.get_data_sql("SELECT * FROM facilities;")
    DataQualityLibrary.check_dataset_is_not_empty(df)