class CenaIntro extends Phaser.Scene {
  constructor() {
    super('CenaIntro');
  }

  create() {
    this.add.text(400, 250, 'Felix Game', { fontSize: '48px', color: '#fff' }).setOrigin(0.5);
    const botao = this.add.text(400, 350, 'Jogar', { fontSize: '32px', color: '#0f0' }).setOrigin(0.5).setInteractive();

    botao.on('pointerdown', () => {
      this.scene.start('CenaJogo');
    });
  }
}
