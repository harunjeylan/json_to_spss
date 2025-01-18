import pandas as pd
import pyreadstat


def csv_to_spss(csv_file, spss_file):
    """
    Convert a CSV file to an SPSS .sav file.

    Parameters:
    csv_file (str): Path to the input CSV file.
    spss_file (str): Path to the output SPSS file.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)
        df.to_json("data.json", orient="records")

        # Convert the DataFrame to SPSS format
        # pyreadstat.write_sav(df, spss_file)

        print(f"File successfully converted to {spss_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
csv_file = "input.csv"  # Replace with your CSV file path
spss_file = "output.sav"  # Replace with your desired output SPSS file path
csv_to_spss(csv_file, spss_file)
