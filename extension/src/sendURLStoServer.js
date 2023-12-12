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