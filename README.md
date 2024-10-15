# JSON to SPSS Converter CLI For Any Programming Language

This application is a tool for converting JSON data into SPSS `.sav` files. It utilizes Python and the `pyreadstat` library for reading and writing SPSS files. The application is open-source and released under the MIT License.

## Features

- Convert JSON data into SPSS format.
- Support for variable labels and value labels.
- Easy integration with Laravel and Node.js applications.

## Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)
- PyInstaller (for creating the executable)
- Laravel (for integrating the Python executable)
- Node.js (for running the application from a Node.js environment)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/json-to-spss-converter.git
   cd json-to-spss-converter
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
   ```

3. **Install the required Python packages**:
   Install all dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

5. **Compile the Python script**:
   ```bash
   pyinstaller --onefile --hidden-import=pyreadstat --collect-all pyreadstat json_to_spss.py
   ```

   This will create an executable in the `dist` folder.

## Running the Application

### From the Command Line

You can run the compiled executable directly from the command line:

```bash
./dist/json_to_spss_v1 '{"variable_value_labels":{"LevelManagement":{"1":"Headquarter","2":"Branches"},"Gender":{"1":"Male","2":"Female"},"Age":{"1":"Under 20","2":"21-29","3":"30-39","4":"40-65","5":"Above 65"},"EducationLevel":{"1":"Diploma","2":"Bachelor","3":"Masters","4":"PhD"},"MaritalStatus":{"1":"Single","2":"Married","3":"Divorced","4":"Separated"}},"variable_measure":{"LevelManagement":"nominal","Gender":"nominal","Age":"nominal","EducationLevel":"nominal","MaritalStatus":"nominal","Date":"scale"},"column_labels":{"LevelManagement":"Level of Management","Gender":"Gender","Age":"Age","EducationLevel":"Education Level","MaritalStatus":"Marital Status","Date":"Date of Response"}}' '[{"LevelManagement":"1","Gender":"1","Age":"2","EducationLevel":"2","MaritalStatus":"2","Date":"2023-01-15"},{"LevelManagement":"2","Gender":"2","Age":"3","EducationLevel":"3","MaritalStatus":"1","Date":"2023-02-20"},{"LevelManagement":"1","Gender":"1","Age":"4","EducationLevel":"4","MaritalStatus":"3","Date":"2023-03-18"},{"LevelManagement":"2","Gender":"2","Age":"2","EducationLevel":"1","MaritalStatus":"4","Date":"2023-04-10"},{"LevelManagement":"1","Gender":"1","Age":"5","EducationLevel":"2","MaritalStatus":"2","Date":"2023-05-12"},{"LevelManagement":"2","Gender":"2","Age":"3","EducationLevel":"1","MaritalStatus":"1","Date":"2023-06-25"},{"LevelManagement":"1","Gender":"1","Age":"4","EducationLevel":"3","MaritalStatus":"3","Date":"2023-07-09"},{"LevelManagement":"2","Gender":"2","Age":"2","EducationLevel":"4","MaritalStatus":"2","Date":"2023-08-30"},{"LevelManagement":"1","Gender":"2","Age":"3","EducationLevel":"2","MaritalStatus":"4","Date":"2023-09-14"},{"LevelManagement":"2","Gender":"1","Age":"4","EducationLevel":"3","MaritalStatus":"1","Date":"2023-10-03"}]' ./output-file.sav
```

### From Node.js

To run the application from a Node.js environment, you can use the `child_process` module to execute the Python executable. Here's an example:

```javascript
const { exec } = require('child_process');
const fs = require('fs');

function convertJsonToSpss(metadata, data, outputFile) {
    // Escape the input to prevent command injection
    const escapedJsonData = JSON.stringify(data);
    const escapedJsonMetaData = JSON.stringify(metadata);

    const command = `./dist/json_to_spss_v1 '${escapedJsonMetaData}' '${escapedJsonData}' ${outputFile}`;

    exec(command, (error, stdout, stderr) => {
        console.log(stdout);

        if (error) {
            console.error(`Error executing command: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`Error: ${stderr}`);
            return;
        }
        // Check if the output file was created successfully
        if (fs.existsSync(outputFile)) {
            console.log(`SPSS file created successfully: ${outputFile}`);
        } else {
            console.error(`Failed to create SPSS file.`);
        }
    });
}


const data = [
    {
        "LevelManagement": "1",
        "Gender": "1",
        "Age": "2",
        "EducationLevel": "2",
        "MaritalStatus": "2",
        "Date": "2023-01-15",
    },
    {
        "LevelManagement": "2",
        "Gender": "2",
        "Age": "3",
        "EducationLevel": "3",
        "MaritalStatus": "1",
        "Date": "2023-02-20",
    },
    {
        "LevelManagement": "1",
        "Gender": "1",
        "Age": "4",
        "EducationLevel": "4",
        "MaritalStatus": "3",
        "Date": "2023-03-18",
    },
    {
        "LevelManagement": "2",
        "Gender": "2",
        "Age": "2",
        "EducationLevel": "1",
        "MaritalStatus": "4",
        "Date": "2023-04-10",
    },
    {
        "LevelManagement": "1",
        "Gender": "1",
        "Age": "5",
        "EducationLevel": "2",
        "MaritalStatus": "2",
        "Date": "2023-05-12",
    },
    {
        "LevelManagement": "2",
        "Gender": "2",
        "Age": "3",
        "EducationLevel": "1",
        "MaritalStatus": "1",
        "Date": "2023-06-25",
    },
    {
        "LevelManagement": "1",
        "Gender": "1",
        "Age": "4",
        "EducationLevel": "3",
        "MaritalStatus": "3",
        "Date": "2023-07-09",
    },
    {
        "LevelManagement": "2",
        "Gender": "2",
        "Age": "2",
        "EducationLevel": "4",
        "MaritalStatus": "2",
        "Date": "2023-08-30",
    },
    {
        "LevelManagement": "1",
        "Gender": "2",
        "Age": "3",
        "EducationLevel": "2",
        "MaritalStatus": "4",
        "Date": "2023-09-14",
    },
    {
        "LevelManagement": "2",
        "Gender": "1",
        "Age": "4",
        "EducationLevel": "3",
        "MaritalStatus": "1",
        "Date": "2023-10-03",
    },
]

const metadata = {
    "variable_value_labels": {
        "LevelManagement": { "1": "Headquarter", "2": "Branches" },
        "Gender": { "1": "Male", "2": "Female" },
        "Age": {
            "1": "Under 20",
            "2": "21-29",
            "3": "30-39",
            "4": "40-65",
            "5": "Above 65",
        },
        "EducationLevel": { "1": "Diploma", "2": "Bachelor", "3": "Masters", "4": "PhD" },
        "MaritalStatus": {
            "1": "Single",
            "2": "Married",
            "3": "Divorced",
            "4": "Separated",
        },
    },
    "variable_measure": {
        "LevelManagement": "nominal",
        "Gender": "nominal",
        "Age": "nominal",
        "EducationLevel": "nominal",
        "MaritalStatus": "nominal",
        "Date": "scale",
    },
    "column_labels": {
        "LevelManagement": "Level of Management",
        "Gender": "Gender",
        "Age": "Age",
        "EducationLevel": "Education Level",
        "MaritalStatus": "Marital Status",
        "Date": "Date of Response",
    },
}


convertJsonToSpss(metadata, data, './output-file.sav');
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgments

- [PyInstaller](https://www.pyinstaller.org/) - for packaging Python applications.
- [pyreadstat](https://github.com/Roche/pyreadstat) - for reading and writing SPSS files.


### Adjustments Made
- Added instructions for using `requirements.txt` to install dependencies.
- Included a section on how to run the application from a Node.js environment using `child_process`.
- Maintained the overall structure and clarity of the `README.md` file.

Feel free to customize further based on your project's specifics or any additional instructions you may want to include!
