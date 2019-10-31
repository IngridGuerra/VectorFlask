const fetchTest = () => {

    fetch("/getQueries", {method: 'GET'})
    .then(response => {
        return response.json()
    })
    .then(result => {
        console.log(result)
        let queries = document.createElement('p')
        queries.innerHTML = result["queries"]["1"] + " " + result["queries"]["2"] + " " + result["queries"]["3"]
        document.body.appendChild(queries)
    });
}

//Unused xD
function fetchQueries() {
    var q = document.getElementById("queries");
    var strUser = q.options[q.selectedIndex].text;
    alert(strUser);
    return(strUser);
}