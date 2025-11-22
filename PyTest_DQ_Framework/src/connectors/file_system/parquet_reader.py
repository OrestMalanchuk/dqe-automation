import pandas as pd

class ParquetReader:
    """
    Provides functionality to read and process Parquet files.
    """

    @staticmethod
    def read_parquet(file_path, columns=None):
        """
        Reads a Parquet file into a pandas DataFrame.

        Args:
            file_path (str): Path to the Parquet file.
            columns (list, optional): List of columns to read. If None, reads all columns.

        Returns:
            pd.DataFrame: DataFrame containing the data from the Parquet file.
        """
        if columns:
            df = pd.read_parquet(file_path, columns=columns)
        else:
            df = pd.read_parquet(file_path)
        return df

    @staticmethod
    def get_row_count(df):
        """
        Returns the number of rows in the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame.

        Returns:
            int: Number of rows.
        """
        return len(df)

    @staticmethod
    def get_column_names(df):
        """
        Returns the column names of the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame.

        Returns:
            list: List of column names.
        """
        return df.columns.tolist()