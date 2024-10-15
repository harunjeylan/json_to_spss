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


def main():
    if len(sys.argv) != 4:
        print("Usage: python json_to_spss <json_data> <output_file>")
        sys.exit(1)
    try:
        meta = sys.argv[1]
        data = sys.argv[2]
        output_file = sys.argv[3]

        parsed_data = parse_json(data)
        parsed_meta = parse_json(meta)

        df = pd.DataFrame(parsed_data)
        pyreadstat.write_sav(df, output_file, **parsed_meta)
        print(f"Data and metadata successfully written to {output_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
