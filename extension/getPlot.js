
document.addEventListener('DOMContentLoaded', function() {
    var historyButton = document.getElementById('historyButton');
    historyButton.addEventListener('click', fetchHistory);
});

function demoSpinner() {
    showSpinner();
    setTimeout(hideSpinner, 10000);
}

let urlList = [];

function fetchHistory() {
    showSpinner();
    setTimeout(30000);
    chrome.history.search({text: '', maxResults: 10}, function(data) {
        // urlList = []; // Clear the list before adding new items
        data.forEach(function(page) {
            if (!page.url.startsWith("https://www.google.com/search?q=")) {
                urlList.push(page.url);
            }
        });
        sendURLsToServer(urlList);
        pollDendrogram();
        hideSpinner();
    });

    console.log(urlList);
}

function sendURLsToServer(urlList) {
    fetch('http://127.0.0.1:8050/receive_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ urls: urlList }),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log('Success:', data.message); 
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function pollDendrogram() {
    fetch('http://127.0.0.1:8050/check_dendrogram')
        .then(response => response.json())
        .then(data => {
            if (data.available) {
                var graphHeader = document.getElementById('graphHeader');
                graphHeader.innerHTML = "";
                var iframe = document.getElementById('graph');
                iframe.style.visibility = 'visible';
                iframe.src = iframe.src;
                // Update the iframe src or reload it
            } else {
                // Poll again after a delay
                setTimeout(pollDendrogram, 5000);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function showSpinner() {
    document.getElementById('spinner-wrapper').style.display = 'flex';
}

function hideSpinner() {
    document.getElementById('spinner-wrapper').style.display = 'none';
}