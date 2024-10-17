import json
import os
import pandas as pd
import pyreadstat
from flask import Flask, request, send_file, jsonify

app = Flask(__name__)

# Ensure the 'output' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)


def convert_json_to_spss(metadata, data, output_file):
    """Convert JSON data to SPSS format and save it."""

    # Convert parsed data to a DataFrame
    df = pd.DataFrame(data)

    # Check if metadata contains valid SPSS attributes
    if not isinstance(metadata, dict):
        raise ValueError("Metadata should be a valid JSON object.")

    # Write the DataFrame to SPSS .sav file
    pyreadstat.write_sav(df, output_file, **metadata)
    return output_file


@app.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.json
        print(data)
        if not data or "metadata" not in data or "data" not in data:
            return (
                jsonify(
                    {
                        "error": "Invalid request. Ensure 'metadata' and 'data' are provided."
                    }
                ),
                400,
            )

        metadata = data["metadata"]
        jsonData = data["data"]
        output_file_name = f"{output_dir}/{os.urandom(4).hex()}.sav"

        # Convert JSON to SPSS
        convert_json_to_spss(metadata, jsonData, output_file_name)

        return (
            jsonify(
                {
                    "message": f"SPSS file created successfully: /{output_file_name}",
                    "output_url": f"/{output_file_name}",
                }
            ),
            200,
        )
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/output/<path:filename>", methods=["GET"])
def get_file(filename):
    """Serve the generated SPSS file."""
    file_path = os.path.join(output_dir, filename)
    if not os.path.isfile(file_path):
        return jsonify({"error": "File not found."}), 404

    return send_file(file_path, as_attachment=True)
