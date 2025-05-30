class Player {
  constructor(scene, x, y) {
    this.scene = scene;
    this.sprite = scene.physics.add.sprite(x, y, null).setSize(40, 40).setCollideWorldBounds(true);
    this.sprite.setTint(0x00ff00);

    this.balas = scene.physics.add.group();

    this.cursor = scene.input.keyboard.createCursorKeys();
    this.space = scene.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);
  }

  update() {
    this.sprite.setVelocity(0);

    if (this.cursor.left.isDown) this.sprite.setVelocityX(-200);
    if (this.cursor.right.isDown) this.sprite.setVelocityX(200);
    if (this.cursor.up.isDown) this.sprite.setVelocityY(-200);
    if (this.cursor.down.isDown) this.sprite.setVelocityY(200);

    if (Phaser.Input.Keyboard.JustDown(this.space)) {
      const bala = this.balas.create(this.sprite.x, this.sprite.y - 20, null);
      bala.setSize(5, 10).setVelocityY(-300).setTint(0xffff00);
    }
  }
}
