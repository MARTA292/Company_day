var empresas = [];

empresas.push({
    key: "nombre",
    key: "persona_contacto",
    key: "mail",
    key: "tlf"
});

function enviar(){
    empresas[0].value = document.getElementsById("nombre_empresa");
    empresas[1].value = document.getElementsById("persona_contacto");
    empresas[2].value = document.getElementsById("mail_contacto");
    empresas[3].value = document.getElementsById("tlf_contacto");
    //console.log(nombre, persona_contacto, mail, tlf);
    console.log(empresas);
    rellenarDatosTabla();
}

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