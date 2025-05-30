class CenaJogo extends Phaser.Scene {
  constructor() {
    super('CenaJogo');
  }

  create() {
    this.player = new Player(this, 400, 500);
    this.inimigos = this.physics.add.group();

    this.time.addEvent({
      delay: 1000,
      loop: true,
      callback: () => {
        new Inimigo(this, Phaser.Math.Between(0, 800), 0);
      }
    });

    this.physics.add.overlap(this.player.balas, this.inimigos, (bala, inimigo) => {
      bala.destroy();
      inimigo.destroy();
      this.events.emit('addKill');
    });

    this.physics.add.overlap(this.player.sprite, this.inimigos, () => {
      this.events.emit('perdeVida');
    });

    this.scene.launch('CenaHUD');
  }

  update() {
    this.player.update();
  }
}
