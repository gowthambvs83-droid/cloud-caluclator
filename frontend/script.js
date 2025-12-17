function calculate() {
    // Read values from HTML
    const n1 = document.getElementById("num1").value;
    const n2 = document.getElementById("num2").value;
    const op = document.getElementById("operation").value;

    // Send data to Python backend
    fetch("https://cloud-calculator.onrender.com", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            num1: n1,
            num2: n2,
            operation: op
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Result: " + data.result;
    });
}

