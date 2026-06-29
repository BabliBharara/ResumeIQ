// Selecting Elements

const analyzeBtn = document.getElementById("analyzeBtn");
const resumeInput = document.getElementById("resume");
const jobDescription = document.getElementById("jobDescription");

const loading = document.getElementById("loading");
const resultSection = document.getElementById("resultSection");

// Analyze Button Click

analyzeBtn.addEventListener("click", async function () {

    // Validation

    if (resumeInput.files.length === 0) {
        alert("Please upload your resume.");
        return;
    }

    if (jobDescription.value.trim() === "") {
        alert("Please paste the job description.");
        return;
    }

    // Show Loading

    loading.classList.remove("hidden");

    // Hide Previous Result

    resultSection.classList.add("hidden");

    // Disable Button

    analyzeBtn.innerText = "Analyzing...";
    analyzeBtn.disabled = true;

    try {

        // Create Form Data

        const formData = new FormData();

        formData.append("resume", resumeInput.files[0]);
        formData.append("job_description", jobDescription.value);

        // Send Data to FastAPI

        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log(data);

        // Show Result

        resultSection.innerHTML = `
            <h2>ATS Result</h2>
            <div class="result-box">
                <pre>${data.result}</pre>
            </div>
        `;

        resultSection.classList.remove("hidden");

    } catch (error) {

        console.error(error);

        alert("Something went wrong.");

    } finally {

        loading.classList.add("hidden");

        analyzeBtn.innerText = "Analyze Resume";

        analyzeBtn.disabled = false;

        resultSection.scrollIntoView({
            behavior: "smooth"
        });

    }

});