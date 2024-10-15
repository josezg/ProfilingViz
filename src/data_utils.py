import pandas as pd
import logging
import io

def load_excel(file):
    """Load an Excel file and returns the data."""
    try:
        data = pd.read_excel(file)
        return data
    except Exception as e:
        logging.error(f"Error loading Excel file: {e}")
        raise

def load_csv(file):
    """Load a CSV file using a dynamically determined separator and returns the data."""
    try:
        # Read the first few lines to determine the separator
        file.seek(0)  # Reset file pointer to the beginning
        first_line = file.readline().decode('utf-8')  # Decode bytes to string
        # Possible separators
        separators = [',', ';', '\t', '|']
        # Determine the separator based on the first line
        separator = max(separators, key=first_line.count)

        # Load the CSV file using the determined separator
        file.seek(0)  # Reset file pointer to the beginning again
        data = pd.read_csv(file, sep=separator)
        return data
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        raise
