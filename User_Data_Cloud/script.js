async function getUserData() {
    const id = document.getElementById('userId').value.trim(); // Add .trim()
    const msg = document.getElementById('msg');
    const resultCard = document.getElementById('resultCard');

    if (!id) {
        msg.innerText = "Please enter an ID.";
        return;
    }

    msg.innerText = "Fetching...";
    msg.style.color = "blue";
    resultCard.style.display = "none";

    try {
        // We use a GET request and pass the ID in the URL
        const response = await fetch(`https://gklkrqrcnk.execute-api.us-east-1.amazonaws.com/prod?id=${id}`);
        const data = await response.json();

        if (response.ok && data.name) {
            document.getElementById('userName').innerText = data.name;
            document.getElementById('userEmail').innerText = data.email;
            resultCard.style.display = "block";
            msg.innerText = "Data retrieved!";
            msg.style.color = "green";
        } else {
            msg.innerText = "User not found.";
            msg.style.color = "red";
        }
    } catch (err) {
        msg.innerText = "Error connecting to cloud.";
        msg.style.color = "red";
    }
}