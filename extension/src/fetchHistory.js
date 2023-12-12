async function fetchHistory() {
    showSpinner();
    let response = await chrome.history.search({text: '', maxResults: 10});
    // console.log(response);
    return response;
}