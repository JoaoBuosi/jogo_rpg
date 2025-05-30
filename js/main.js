const config = {
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  backgroundColor: '#111',
  physics: {
    default: 'arcade',
    arcade: { debug: false }
  },
  scene: [CenaIntro, CenaJogo, CenaGameOver, CenaHUD]
};

const game = new Phaser.Game(config);
