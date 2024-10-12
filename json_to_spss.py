import json
import pandas as pd
import pyreadstat
import sys


def parse_json(json_data):
    """Parse JSON data into a dictionary."""
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON data: {e}")


def prepare_dataframe(data, variable_types):
    """Convert the data to a DataFrame and ensure correct numeric types."""
    df = pd.DataFrame(data)

    # Automatically convert to numeric where required
    for column, var_type in variable_types.items():
        if var_type == 0:  # 0 indicates numeric type in the metadata
            df[column] = pd.to_numeric(df[column], errors="coerce")
            # Convert to integer if all values are whole numbers
            if (df[column] == df[column].astype(int)).all():
                df[column] = df[column].astype(int)

    return df


def process_value_labels(value_labels):
    """Convert value label keys to integers."""
    return {
        variable: {int(k): v for k, v in labels.items()}
        for variable, labels in value_labels.items()
    }


def convert_json_to_spss(json_data, output_file):
    """Main function to convert JSON data to SPSS format."""
    try:
        # Step 1: Parse the JSON data
        parsed_json = parse_json(json_data)

        # Step 2: Extract data and metadata
        data = parsed_json["data"]
        metadata = parsed_json["metadata"]

        # Step 3: Prepare the DataFrame
        variable_types = metadata.get("variable_types", {})
        df = prepare_dataframe(data, variable_types)

        # Step 4: Extract metadata details (variable labels, value labels, etc.)
        variable_labels = metadata.get("variable_labels", {})
        value_labels = process_value_labels(metadata.get("value_labels", {}))

        # Step 5: Write DataFrame to SPSS file with metadata
        pyreadstat.write_sav(
            df,
            output_file,
            variable_value_labels=value_labels,
            column_labels=variable_labels,
        )

        print(f"Data and metadata successfully written to {output_file}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python json_to_spss <json_data> <output_file>")
        sys.exit(1)

    json_data = sys.argv[1]  # JSON data as a string
    output_file = sys.argv[2]  # Output file path (SPSS .sav file)

    convert_json_to_spss(json_data, output_file)


if __name__ == "__main__":
    main()
