const easterEggs = {
  konami: {
    sequence: [
      "ArrowUp", "ArrowUp",
      "ArrowDown", "ArrowDown",
      "ArrowLeft", "ArrowRight",
      "ArrowLeft", "ArrowRight",
      "b", "a"
    ],
    action: () => {
      if (!localStorage.getItem("konami_achieved")) {
        
      }
        localStorage.setItem('joaoDesbloqueado', 'true')
        localStorage.setItem('fernandoDesbloqueado', 'true')
        localStorage.setItem("arthurdesbloqueado", "true");
        localStorage.setItem('eastereggdioDesbloqueado', 'true')
        localStorage.setItem('patoDesbloqueado', 'true')
        localStorage.setItem('terrorDesbloqueado', 'true')
        localStorage.setItem('primosDesbloqueado', 'true')
        localStorage.setItem('anjoDesbloqueado', 'true')

      }
    }
  }

let inputBuffer = [];
let textoBuffer = "";

document.addEventListener("keydown", (e) => {
  const tecla = e.key.toLowerCase();

  // Konami
  inputBuffer.push(tecla);
  if (inputBuffer.length > 10) inputBuffer.shift();

  for (let key in easterEggs) {
    const egg = easterEggs[key];
    if (inputBuffer.slice(-egg.sequence.length).join(",") === egg.sequence.map(k => k.toLowerCase()).join(",")) {
      egg.action();
    }
  }

  // Texto "paz"
  if (/^[a-zA-Z]$/.test(tecla)) {
    textoBuffer += tecla;
    if (textoBuffer.length > 10) textoBuffer = textoBuffer.slice(-10);
  }

  if (textoBuffer.includes("paz")) {
    ativarAnjo();
    textoBuffer = "";
  }
});

function ativarAnjo() {
  const anjo = document.getElementById("anjoEaster");
  const explosao = document.getElementById("explosaoEaster");
  const somExplosao = document.getElementById("somExplosao");
  const somTiro = document.getElementById("somTiro");

  if (!anjo || !explosao || !somExplosao || !somTiro) return;

  anjo.style.display = "block";
  anjo.style.left = "-150px";

  let pos = -150;
  const entrada = setInterval(() => {
    pos += 5;
    anjo.style.left = pos + "px";
    if (pos >= 150) {
      clearInterval(entrada);

      // Anjo para, atira
      somTiro.currentTime = 0;
      somTiro.play();

      // Delay e explosão
      setTimeout(() => {
        explosao.style.display = "block";
        somExplosao.currentTime = 0;
        somExplosao.play();

        setTimeout(() => {
          anjo.style.display = "none";
          explosao.style.display = "none";
        }, 2000);
      }, 500);
    }
  }, 16); // ~60fps
}

