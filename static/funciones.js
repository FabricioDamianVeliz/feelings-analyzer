function mostrarResultado() {
    var resultado = document.getElementById('sentimiento');
    resultado.style.display = 'block';
}

function eliminarCodigosEscape(texto) {
    return texto.replace(/\x1b\[[0-9;]*[a-zA-Z]/g, '');
}

function analizarSentimientos() {
    var userPrompt = document.getElementById('userPrompt').value;

    fetch('/analizar_sentimientos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',  // Update content type to JSON
        },
        body: JSON.stringify({
            'user_prompt': userPrompt,
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('La solicitud falló');
        }
        return response.json();
    })
    .then(data => {
        var sentimientoTexto = eliminarCodigosEscape(data.sentimiento);
        document.getElementById('sentimiento').innerText = sentimientoTexto;
        document.getElementById('errorMensaje').innerText = '';
    })
    .catch(error => {
        document.getElementById('errorMensaje').innerText = 'Error: ' + error.message;
    });
}
