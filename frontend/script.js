console.log("Kya re bhondu");
const csvFile = document.getElementById("csvFile");
const uploadBtn = document.getElementById("uploadBtn");
const result = document.getElementById("result");
const predictionForm = document.getElementById("predictionForm")
uploadBtn.addEventListener("click", async()=>{
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
        });
        const data = await response.json();
        if (!response.ok){
            throw new Error(data.detail || "Upload failed.");
        }
        result.innerHTML = `
            <h2>Dataset Information</h2>
            <p><strong>Rows:</strong>${data.dataset.shape[0]}</p>
            <p><strong>Columns:</strong>${data.dataset.shape[1]}</p>
            <h2>ML Result</h2>
            <p><strong>Target:</strong>${data.ml.target_column}</p>
            <p><strong>Problem Type:</strong>${data.ml.problem_type}</p>
            <p><strong>Best Model:</strong>${data.ml.best_model}</p>`;
        const artifacts = data.ml.preprocessing.artifacts;
        predictionForm.innerHTML = "";
        for (const column of artifacts.encoded_columns) {
            const input = document.createElement("input");
            input.type = "text";
            input.id = column;
            input.name = column;
            predictionForm.appendChild(input);
        }
    } catch (error) {
        result.textContent = "Upload failed.";
        console.error(error);
    }
})