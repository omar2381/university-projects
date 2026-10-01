var form = document.getElementById('search_form');
form.addEventListener('submit',async function(event) {
    event.preventDefault();
    let keyword = document.getElementById('search_keyword').value;
    let response = await fetch('http://127.0.0.1:8090/poke/name=' + keyword);
    let body = await response.text();
    let results = JSON.parse(body);
    let resultsDiv = document.getElementById('search_results');
    resultsDiv.innerHTML = body

    alert(body);
})
