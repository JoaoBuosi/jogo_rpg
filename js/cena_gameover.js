class CenaGameOver extends Phaser.Scene {
  constructor() {
    super('CenaGameOver');
  }

  create() {
    this.add.text(400, 250, 'Game Over', { fontSize: '48px', color: '#f00' }).setOrigin(0.5);
    const botao = this.add.text(400, 350, 'Reiniciar', { fontSize: '32px', color: '#0f0' }).setOrigin(0.5).setInteractive();

    botao.on('pointerdown', () => {
      this.scene.start('CenaIntro');
    });
  }
}
