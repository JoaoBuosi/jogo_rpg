function verificarHorario() {
  const agora = new Date();
  const horas = agora.getHours();
  const minutos = agora.getMinutes();

  const container = document.getElementById("mensagemContainer");

  if (horas === 3 && minutos === 33) {
    container.classList.add("bloody");
    document.getElementById("mensagemTexto").textContent = "Eles estão observando você...";
  } else {
    container.classList.remove("bloody");
    document.getElementById("mensagemTexto").textContent = "Você descobriu uma verdade escondida...";
  }
}

setInterval(verificarHorario, 10000); // Verifica a cada 10s
verificarHorario(); // Verifica na hora que abrir a página
