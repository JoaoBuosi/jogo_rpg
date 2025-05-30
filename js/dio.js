// dio.js
// Salva o Shadow Dio como desbloqueado
localStorage.setItem("shadow_dio_desbloqueado", "true");

// Redireciona após alguns segundos
setTimeout(() => {
  window.location.href = "escolha_personagem.html";
}, 5000);
