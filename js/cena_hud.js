export default class CenaHUD extends Phaser.Scene {
  constructor() {
    super('CenaHUD');
  }

  create() {
    this.textoVida = this.add.text(10, 10, 'Vida: 3', {
      fontSize: '20px',
      fill: '#fff'
    }).setScrollFactor(0);
  }
}
