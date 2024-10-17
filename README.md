Here’s a detailed `README.md` file for your application:

---

# JSON to SPSS Converter Application

This application allows users to convert JSON data into SPSS (.sav) files using a Flask-based web service. The application leverages Python libraries such as `pandas` and `pyreadstat` to parse the JSON and create SPSS-compatible files. It also provides an easy-to-use API for interacting with the service and supports dynamic file generation.

## Features

- Converts JSON data and metadata into SPSS `.sav` format.
- Generates unique SPSS files for each request.
- Simple and easy-to-use API to upload JSON data and retrieve SPSS files.
- Built using Python, Flask, `pandas`, and `pyreadstat`.

## Prerequisites

- Python 3.6 or later.
- Flask for web service.
- `pandas` and `pyreadstat` for data manipulation and SPSS file creation.

### Required Python Packages

```bash
Flask==3.0.3
gunicorn==23.0.0
pandas==2.2.3
pyreadstat==1.2.7
```

## Project Structure

```
your_project_directory/
│
├── venv/                     # Virtual environment directory
│   ├── ...
│
├── output/                   # Output directory for SPSS files
│   ├── ...
│
├── main.py      # Your main Flask application file
├── wsgi.py                   # WSGI callable for deployment
├── dev.py                   # DEV WSGI callable for Development
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation (this file)
```

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/harunjeylan/json_to_spss.git
cd json_to_spss
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate   # On Linux/MacOS
venv\Scripts\activate      # On Windows
```

### 3. Install the Dependencies

Install the necessary packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python dev.py
```

The application will start at `http://localhost:2020`.

## Usage

### POST `/convert`

This endpoint accepts a JSON payload containing the `metadata` and `data` to be converted into an SPSS file.

#### Request Example

```json
{
  "data": [
    {
        "LevelManagement": "1",
        "Gender": "1",
        "Age": "2",
        "EducationLevel": "2",
        "MaritalStatus": "2",
        "Date": "2023-01-15"
    },
    {
        "LevelManagement": "2",
        "Gender": "2",
        "Age": "3",
        "EducationLevel": "3",
        "MaritalStatus": "1",
        "Date": "2023-02-20"
    },
    {
        "LevelManagement": "1",
        "Gender": "1",
        "Age": "4",
        "EducationLevel": "4",
        "MaritalStatus": "3",
        "Date": "2023-03-18"
    },
],
"metadata" : {
    "variable_value_labels": {
        "LevelManagement": { "1": "Headquarter", "2": "Branches" },
        "Gender": { "1": "Male", "2": "Female" },
        "Age": {
            "1": "Under 20",
            "2": "21-29",
            "3": "30-39",
            "4": "40-65",
            "5": "Above 65"
        },
        "EducationLevel": { "1": "Diploma", "2": "Bachelor", "3": "Masters", "4": "PhD" },
        "MaritalStatus": {
            "1": "Single",
            "2": "Married",
            "3": "Divorced",
            "4": "Separated"
        }
    },
    "variable_measure": {
        "LevelManagement": "nominal",
        "Gender": "nominal",
        "Age": "nominal",
        "EducationLevel": "nominal",
        "MaritalStatus": "nominal",
        "Date": "scale"
    },
    "column_labels": {
        "LevelManagement": "Level of Management",
        "Gender": "Gender",
        "Age": "Age",
        "EducationLevel": "Education Level",
        "MaritalStatus": "Marital Status",
        "Date": "Date of Response"
    }
}
}
```

#### Response Example

```json
{
  "message": "SPSS file created successfully: /output/abcdef123456.sav",
  "outputUrl": "/output/abcdef123456.sav"
}
```

### GET `/output/<filename>`

Use the dynamically generated URL from the `/convert` response to download the SPSS file.

#### Example

```bash
GET http://localhost:2020/output/abcdef123456.sav
```

## WSGI Deployment

To deploy the application in a production environment, you can configure a WSGI server.

### 1. Create a `wsgi.py` file:

```python
from your_flask_script import app

if __name__ == "__main__":
    app.run()
```

### 2. Example Deployment (Using Gunicorn)

Install Gunicorn:

```bash
pip install gunicorn
```

Run the application:

```bash
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

Run the application with Docker Compose:
```bash
docker compose up
```

## Troubleshooting

### PyCapsule_Import Could Not Import Module "datetime"

This error can be resolved by ensuring that your Python environment is correctly set up. Please make sure the following steps are followed:

- Ensure you're using the right Python version (`python --version`).
- Check for conflicts between different package versions.
- Use a virtual environment and ensure all dependencies are properly installed.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` file provides a clear and structured guide for setting up, running, and using the application. Let me know if you want to add or modify anything!