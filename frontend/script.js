console.log("Kya re bhondu");
const csvFile = document.getElementById("csvFile");
const uploadBtn = document.getElementById("uploadBtn");
const result = document.getElementById("result");
const predictionForm = document.getElementById("predictionForm")
uploadBtn.addEventListener("click", async(event)=>{
    event.preventDefault();
    event.stopPropagation();
    if (!csvFile.files.length) {
        result.textContent = "Please select a CSV file.";
        return;
    }
    const formData = new FormData();
    formData.append("file", csvFile.files[0]);
    try {
        const response = await fetch("http://127.0.0.1:8000/upload/csv", {
            method: "POST",
            body: formData
        })
            .then(response =>{
                console.log("FETCH RESPONSE:", response.status);
                return response;
            })
            .catch(error=> {
                console.error("FETCH ERROR:", error);
                throw error;
            });
        const data = await response.json();
        console.log("Response:", data.ml.final_evaluation);
        if (!response.ok){
            throw new Error(data.detail || "Upload failed.");
        }
        result.innerHTML = `
            <h2>ML Result</h2>
            <p><strong>Target:</strong>${data.ml.target_column}</p>
            <p><strong>Problem Type:</strong>${data.ml.problem_type}</p>
            <p><strong>Best Model:</strong>${data.ml.best_model}</p>`;
        const evaluation = data.ml.final_evaluation;
        const evaluationContainer = document.createElement("div");
        Object.entries(evaluation).forEach(([key, value]) => {
            const item = document.createElement("p");
            const label = document.createElement("strong");
            label.textContent = `${key}: `;
            item.appendChild(label);
            item.appendChild(document.createTextNode(value));
            evaluationContainer.appendChild(item);
        });
        result.appendChild(evaluationContainer);
        const artifacts = data.ml.preprocessing.artifacts;
        predictionForm.innerHTML = "";
        const inputColumns = [
            ...Object.keys(artifacts.frequency_maps),
            "bath",
            "balcony",
            ...artifacts.encoded_columns
        ];
        for (const column of inputColumns) {
            const input = document.createElement("input");
            input.type = "text";
            input.id = column;
            input.name = column;
            predictionForm.appendChild(input);
        }
        const predictBtn = document.createElement("button");
        predictBtn.type = "button";
        predictBtn.textContent = "Predict";
        predictionForm.appendChild(predictBtn);
        predictBtn.addEventListener("click", async() => {
            const inputData = {};
            for (const input of predictionForm.querySelectorAll("input")) {
                inputData[input.name] = input.value;
            }
            console.log("PREDICTION DATA:", inputData);
            try {
                const response = await fetch("http://127.0.0.1:8000/predict/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(inputData)
                });
                const data = await response.json();
                console.log("PREDICTION RESPONSE:", data);
                if (!response.ok) {
                    throw new Error(data.detail || "Prediction failed.");
                }
                result.innerHTML += 
                    `<h2>Prediction</h2>
                    <p><strong>Predicted Price:</strong>${data.prediction}</p>`;
            } catch (error) {
                console.error("PREDICTION ERROR:", error);
            }
        });
    } catch (error) {
        result.textContent = "Upload failed.";
        console.error(error);
    }
})