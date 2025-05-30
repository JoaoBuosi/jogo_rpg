// lang.js
const textos = {
  pt: {
    titulo: "Menu do Jogo",
    novoJogo: "Novo Jogo",
    continuar: "Continuar",
    opcoes: "Opções",
    perfil: "Perfil",
    creditos: "Créditos",
    voltar: "Voltar",
    volume: "Volume",
    dificuldade: "Dificuldade",
    idioma: "Idioma",
    salvar: "Salvar",
    facil: "Fácil",
    medio: "Médio",
    dificil: "Difícil",
    portugues: "Português",
    ingles: "Inglês",
    espanhol: "Espanhol",
    opcoesSalvas: "Opções salvas!"
  },
  en: {
    titulo: "Game Menu",
    novoJogo: "New Game",
    continuar: "Continue",
    opcoes: "Options",
    perfil: "Profile",
    creditos: "Credits",
    voltar: "Back",
    volume: "Volume",
    dificuldade: "Difficulty",
    idioma: "Language",
    salvar: "Save",
    facil: "Easy",
    medio: "Medium",
    dificil: "Hard",
    portugues: "Portuguese",
    ingles: "English",
    espanhol: "Spanish",
    opcoesSalvas: "Options saved!"
  },
  es: {
    titulo: "Menú del Juego",
    novoJogo: "Nuevo Juego",
    continuar: "Continuar",
    opcoes: "Opciones",
    perfil: "Perfil",
    creditos: "Créditos",
    voltar: "Volver",
    volume: "Volumen",
    dificuldade: "Dificultad",
    idioma: "Idioma",
    salvar: "Guardar",
    facil: "Fácil",
    medio: "Medio",
    dificil: "Difícil",
    portugues: "Portugués",
    ingles: "Inglés",
    espanhol: "Español",
    opcoesSalvas: "¡Opciones guardadas!"
  },
};

function aplicarIdioma() {
  const idioma = localStorage.getItem('idioma') || 'pt';
  const elementos = document.querySelectorAll('[data-texto]');
  elementos.forEach(elemento => {
    const chave = elemento.getAttribute('data-texto');
    const texto = textos[idioma][chave] || chave;
    elemento.textContent = texto;
  });
}

window.onload = aplicarIdioma;
