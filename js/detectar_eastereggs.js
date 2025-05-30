// Módulo para detectar ações do jogador e desbloquear Easter Eggs
document.addEventListener("DOMContentLoaded", () => {
  detectarCodigoSecreto();
  detectarCliqueFrase();
  detectarParado();
  detectarBotaoInvisivel();
  detectarComandoZaWarudo();
  detectarPrimos();
  detectarArthur();
});

// 1. CÓDIGO SECRETO: abbaxlp
function detectarCodigoSecreto() {
  let buffer = "";

  document.addEventListener("keydown", (e) => {
    buffer += e.key.toLowerCase();
    if (buffer.length > 10) buffer = buffer.slice(-10);
  });
}

// 2. CLIQUE 10x NA FRASE DO MENU
function detectarCliqueFrase() {
  const frase = document.querySelector("#frase-menu");
  if (!frase) return;

  let contador = 0;

  frase.addEventListener("click", () => {
    contador++;
    if (contador === 5) {
      desbloquear("anjoDesbloqueado", "Anjo");
    }
  });
}

// 3. PARADO POR 20 SEGUNDOS
function detectarParado() {
  let tempoParado = 0;
  let ultimoMovimento = Date.now();

  const resetar = () => ultimoMovimento = Date.now();

  ["mousemove", "keydown", "click"].forEach(evt =>
    document.addEventListener(evt, resetar)
  );

  setInterval(() => {
    if (Date.now() - ultimoMovimento >= 20000) {
      desbloquear("patoDesbloqueado", "Pato Dançando");
    }
  }, 1000);
}

// 4. BOTÃO INVISÍVEL NO CANTO INFERIOR DIREITO
function detectarBotaoInvisivel() {
  const botao = document.createElement("div");
  Object.assign(botao.style, {
    position: "fixed", bottom: "10px", right: "10px",
    width: "40px", height: "40px", zIndex: "9999",
    backgroundColor: "transparent", cursor: "pointer"
  });

  document.body.appendChild(botao);

  botao.addEventListener("click", () => {
    desbloquear("terrorDesbloqueado", "Terror");
  });
}

// 5. COMANDO "ZA WARUDO"
function detectarComandoZaWarudo() {
  let buffer = "";

  document.addEventListener("keydown", (e) => {
    buffer += e.key.toLowerCase();
    if (buffer.length > 15) buffer = buffer.slice(-15);

    if (buffer.includes("zawarudo")) {
      desbloquear("eastereggdioDesbloqueado", "Dio");
    }
  });
}

// 6. DIGITAR "primos" NA TELA INICIAL
function detectarPrimos() {
  let buffer = "";

  document.addEventListener("keydown", (e) => {
    buffer += e.key.toLowerCase();
    if (buffer.length > 10) buffer = buffer.slice(-10);

    if (buffer.includes("primos")) {
      desbloquear("primosDesbloqueado", "Primos");
    }
  });
}

// ✅ Função genérica para desbloquear qualquer Egg
function desbloquear(chave, nome) {
  if (localStorage.getItem(chave) === "true") return;

  localStorage.setItem(chave, "true");

  const aviso = document.createElement("div");
  aviso.textContent = `🎉 Easter Egg "${nome}" descoberto!`;
  Object.assign(aviso.style, {
    position: "fixed", top: "20px", left: "50%", transform: "translateX(-50%)",
    background: "#0f0", color: "#000", padding: "10px 20px", borderRadius: "10px",
    fontWeight: "bold", fontSize: "18px", zIndex: "10000"
  });

  document.body.appendChild(aviso);

  setTimeout(() => aviso.remove(), 5000);
}
