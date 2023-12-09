document.addEventListener('DOMContentLoaded', function() {
    var historyButton = document.getElementById("historyButton");
    historyButton.addEventListener('click', main);
})

async function main() {
    let urlList = await fetchHistory();
    console.log(urlList);
    let message = await sendURLsToServer(urlList);
    console.log(message);
    let available = await getGraph();
    console.log(available);
}

async function fetchHistory() {
    showSpinner();
    let response = await chrome.history.search({text: '', maxResults: 10});
    // console.log(response);
    return response;
}

async function sendURLsToServer(urlList) {

    let local_urlList = [];

    urlList.forEach(function(page) {
        local_urlList.push(page.url)
    });

    let response = await fetch('http://127.0.0.1:8050/receive_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ urls : local_urlList }),
    })

    let data = await response.json();
    // console.log(data);
    return data.message
}

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
        iframe.src = iframe.src;
    }

    hideSpinner();

    return available

}

function showSpinner() {
    document.getElementById('spinner-wrapper').style.display = 'flex';
}

function hideSpinner() {
    document.getElementById('spinner-wrapper').style.display = 'none';
}


