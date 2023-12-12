async function checkAvailability() {
    let response = await fetch('http://127.0.0.1:8050/check_dendrogram');

    let data = await response.json();
    // console.log(data);

    // console.log(data.available);
    return data.available
}

async function getGraph() {
    let available = false;
    let timeoutReached = false;

    setTimeout(() => {
        timeoutReached = true;
    }, 3000);

    while (!available && !timeoutReached) {
        available = await checkAvailability();
        console.log(available);

    }

    if (timeoutReached) {
        console.log("Request timed out after 3 seconds.");
    } else {
        console.log("Availability Confirmed.");

        var graphFrame = document.getElementById('graphFrame');
        graphFrame.style.display = 'block';
        var graphHeader = document.getElementById('graphHeader');
        graphHeader.innerHTML = "";
        graphHeader.style.position = 'relative';
        var iframe = document.getElementById('graph');
        iframe.style.visibility = 'visible';
        iframe.src = "http://127.0.0.1:8050/";
    }

    hideSpinner();

    return available

}