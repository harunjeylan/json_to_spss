const { exec } = require('child_process');
const fs = require('fs');

function convertJsonToSpss(jsonData, outputFile) {
    // Escape the input to prevent command injection
    const escapedJsonData = JSON.stringify(jsonData);

    const command = `./dist/json_to_spss '${escapedJsonData}' ${outputFile}`;

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
            ID: { type: 0, width: 8, decimal: 0 },
            Name: { type: 1, width: 50, decimal: 0 },
            Age: { type: 0, width: 8, decimal: 0 },
            Gender: { type: 0, width: 8, decimal: 0 },
            Score: { type: 0, width: 8, decimal: 2 }
        }
    }
};

convertJsonToSpss(jsonData, './output-file.sav');
