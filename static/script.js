document.addEventListener("DOMContentLoaded", function() {
    if (!annyang) {
        return alert("Lo siento, tu navegador no soporta el reconocimiento de voz :(");
    }
    const $comandosReconocidos = document.querySelector("#comandosReconocidos"),
        $vozDetectada = document.querySelector("#vozDetectada");

    const loguearComandoReconocido = contenido => {
        $comandosReconocidos.innerHTML += contenido + "<br>";
    };

    const loguearVozDetectada = contenido => {
        $vozDetectada.innerHTML += contenido + "<br>";
    };

    annyang.setLanguage("es-MX");
    let comandos = {
        "hola": () => {
            loguearComandoReconocido(`Hola mundo!`);

        },
        "hola *mes": mes => {
            if ("enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre".split(",").indexOf(mes.toLowerCase()) === -1) {
            	console.log("Hola")
            	loguearComandoReconocido(`Ok te muestro el reporte de ventas de ${mes}`);
                return;
            }
            else{
            	console.log("Chao")
            }
        },
        "enviar correo a *usuario": usuario => {
            let usuarioCorregido = usuario.replace(/\ /g, "").replace(/arroba/g, "@").toLowerCase();
            loguearComandoReconocido(`Originalmente es ${usuario} pero creo que el correcto es ${usuarioCorregido}`);
        },
        "mi nombre es *nombre y tengo *anios años": (nombre, anios) => {
            loguearComandoReconocido(`Hola ${nombre} es genial que tu edad sea ${anios} :)`);
        }
    };

    annyang.addCommands(comandos);

    annyang.addCallback("result", frases => {
        loguearVozDetectada(`<strong>Probablemente has dicho: </strong> <br> ${frases.join("<br>")}`);
    });

    annyang.start();
});