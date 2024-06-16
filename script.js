function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const responseArea = document.getElementById("response-area");

    // Placeholder for sending message to backend and getting a response
    responseArea.innerHTML += `<div>User: ${userInput}</div>`; // Display user message
    responseArea.innerHTML += `<div>Bot: Echoing - ${userInput}</div>`; // Display bot response (placeholder)

    document.getElementById("user-input").value = ''; // Clear input field
}
