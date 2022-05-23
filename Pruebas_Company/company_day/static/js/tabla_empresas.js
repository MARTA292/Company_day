var empresas = json.parse(empresas)

function rellenarDatosTabla(){
    //window.location.href = "tabla_empresas.html";
    for (let i = 0; i < empresas.length; i++) {
        //Creamos fila
        const filaNueva = document.createElement("tr");
        //Creamos celda del video, poenemos valor del path
        const cnombre = document.createElement('td');
        cnombre.innerText = empresas.nombre[i];
        const cpersona = document.createElement("td");
        cpersona.innerText = empresas.persona_contacto[i];
        const cmail = document.createElement("td");
        cmail.innerText = empresas.mail[i];
        const ctlf = document.createElement("td");
        ctlf.innerText = empresas.tlf[i];
        filaNueva.appendChild(cnombre);
        filaNueva.appendChild(cpersona);
        filaNueva.appendChild(cmail);
        filaNueva.appendChild(ctlf);
        document.getElementById("tabla_empresas").appendChild(filaNueva);
    }
}