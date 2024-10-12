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
/path/to/your/dist/json_to_spss '{"data":[{"ID":1,"Name":"Alice","Age":25,"Gender":"1","Score":85.5},{"ID":2,"Name":"Bob","Age":30,"Gender":"2","Score":78.0}],"metadata":{"variable_labels":{"ID":"Identification Number","Name":"Name of Respondent","Age":"Age of Respondent","Gender":"Gender of Respondent","Score":"Test Score"},"value_labels":{"Gender":{"1":"Male","2":"Female"}},"variable_types":{"ID":0,"Name":1,"Age":0,"Gender":0,"Score":0}}}' '/path/to/output/file.sav'
```

### From Laravel

To integrate this executable with a Laravel application, you can create a function to call the executable using the `shell_exec` function. Here's an example:

```php
public function convertJsonToSpss(Request $request)
{
    // Validate incoming request data
    $request->validate([
        'json_data' => 'required|string',
        'output_file' => 'required|string'
    ]);

    // Prepare the command to call the compiled Python script
    $jsonData = escapeshellarg($request->json_data);
    $outputFile = escapeshellarg($request->output_file);

    // Command to execute the compiled Python script
    $command = "/path/to/your/dist/json_to_spss $jsonData $outputFile";

    // Execute the command and capture the output
    $output = shell_exec($command);

    // Check if the output file was created successfully
    if (file_exists($outputFile)) {
        return response()->json(['message' => 'SPSS file created successfully.', 'output_file' => $outputFile], 200);
    } else {
        return response()->json(['message' => 'Failed to create SPSS file.', 'error' => $output], 500);
    }
}
```

### From Node.js

To run the application from a Node.js environment, you can use the `child_process` module to execute the Python executable. Here's an example:

```javascript
const { exec } = require('child_process');

function convertJsonToSpss(jsonData, outputFile) {
    // Escape the input to prevent command injection
    const escapedJsonData = JSON.stringify(jsonData).replace(/"/g, '\\"');
    const command = `/path/to/your/dist/json_to_spss ${escapedJsonData} ${outputFile}`;

    exec(command, (error, stdout, stderr) => {
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

// Example usage
const jsonData = {
    data: [
        { ID: 1, Name: "Alice", Age: 25, Gender: "1", Score: 85.5 },
        { ID: 2, Name: "Bob", Age: 30, Gender: "2", Score: 78.0 }
    ],
    metadata: {
        variable_labels: {
            ID: "Identification Number",
            Name: "Name of Respondent",
            Age: "Age of Respondent",
            Gender: "Gender of Respondent",
            Score: "Test Score"
        },
        value_labels: {
            Gender: {
                "1": "Male",
                "2": "Female"
            }
        },
        variable_types: {
            ID: 0,
            Name: 1,
            Age: 0,
            Gender: 0,
            Score: 0
        }
    }
};

convertJsonToSpss(jsonData, '/path/to/output/file.sav');
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
