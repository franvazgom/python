

function obtienePremios() {
    const url = 'https://api.nobelprize.org/2.1/laureates';
    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error("La solicitud no fue exitosa");
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => { 
        console.error(' Error en la solicitud..', error); 
    });
}

obtienePremios();