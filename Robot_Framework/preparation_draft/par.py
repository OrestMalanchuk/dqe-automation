import pandas as pd
from IPython.display import display
from pandas import to_datetime


def read_parquet_to_dataframe(folder_path: str, filter_date) -> pd.DataFrame:
    """
    Reads a partitioned Parquet dataset into a Pandas DataFrame.
    It can optionally filter the data by a date partition.

    Note: This function assumes the dataset is partitioned by a column named 'date'
    with string values in 'YYYY-MM-DD' format.
    """
    filters = [('visit_date', '==', to_datetime(filter_date).normalize())] if filter_date else None
    try:
        df = pd.read_parquet(folder_path, filters=filters)
        # After filtering, the partition column ('date') might be categorical.
        # Convert it to string to ensure consistency for comparison.
        if 'visit_date' in df.columns:
            df['visit_date'] = df['visit_date'].astype(str)
        return df.reset_index(drop=True)
    except Exception as e:
        raise RuntimeError(f"Failed to read Parquet dataset from {folder_path}: {e}")

df = read_parquet_to_dataframe('../parquet_data/facility_type_avg_time_spent_per_visit_date', "2025-10-29")