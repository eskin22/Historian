
document.addEventListener('DOMContentLoaded', function() {
    var historyButton = document.getElementById('historyButton');
    historyButton.addEventListener('click', fetchHistory);
});

// function fetchHistory() {
//     chrome.history.search({text: '', maxResults: 10}, function(data) {
//         var historyDiv = document.getElementById('historyResults');
//         historyDiv.innerHTML = '';
//         data.forEach(function(page) {
//             var pageElement = document.createElement('p');
//             pageElement.textContent = page.url;
//             historyDiv.appendChild(pageElement);
//         });
//     });
// }

let urlList = [];

function fetchHistory() {
    chrome.history.search({text: '', maxResults: 10}, function(data) {
        // urlList = []; // Clear the list before adding new items
        data.forEach(function(page) {
            urlList.push(page.url); // Add URLs to the list
        });
        sendURLsToServer(urlList); // Process or return the list as needed
        pollDendrogram();
    });

    console.log(urlList);
}

// function sendURLsToServer(urlList) {
//     fetch('http://127.0.0.1:8050/receive_data', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ urls: urlList }),
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Success:', data);
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }

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
            return response.json(); // This parses the JSON response.
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log('Success:', data.message); // 'data' is a parsed JavaScript object.
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
                var iframe = document.getElementById('graph');
                iframe.src = iframe.src;
                // Update the iframe src or reload it
                // document.getElementById('your-iframe-id').src = 'new dendrogram URL or reload';
            } else {
                // Poll again after a delay
                setTimeout(pollDendrogram, 5000); // 5 seconds delay
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

// Call this function after sending URLs to the server
pollDendrogram();