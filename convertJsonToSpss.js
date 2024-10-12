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
            ID: 0,
            Name: 1,
            Age: 0,
            Gender: 0,
            Score: 0
        }
    }
};

convertJsonToSpss(jsonData, './output-file.sav');
