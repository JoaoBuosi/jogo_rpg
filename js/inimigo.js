class Inimigo {
  constructor(scene, x, y) {
    const inimigo = scene.inimigos.create(x, y, null).setSize(30, 30).setVelocityY(100);
    inimigo.setTint(0xff0000);
  }
}
