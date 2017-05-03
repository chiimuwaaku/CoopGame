var game = new Phaser.Game(800, 600, Phaser.CANVAS,'phaser-example', {
  preload: preload,
  create: create,
  update: update,
  render: render
}, false, false);

var tentatrice1;
var tentatrice2;
var cursors;

function Tentatrice (game, sprite_code, init_pos) {
  this.sprite = game.add.sprite(init_pos.x, init_pos.y, sprite_code);
  game.physics.enable(this.sprite);
  this.speed = 300
  this.move = function(direction) {
    if (direction == 'up') {
      this.sprite.body.velocity.x = 0;
      this.sprite.body.velocity.y = -1 * this.speed;
    } else if (direction == 'down') {
      this.sprite.body.velocity.x = 0;
      this.sprite.body.velocity.y = this.speed;
    } else if (direction == 'left') {
      this.sprite.body.velocity.x = -1 * this.speed;
      this.sprite.body.velocity.y = 0;
    } else if (direction == 'right') {
      this.sprite.body.velocity.x = this.speed;
      this.sprite.body.velocity.y = 0;
    }
  }
}


function preload() {

  //  You can fill the preloader with as many assets as your game requires

  //  Here we are loading an image. The first parameter is the unique
  //  string by which we'll identify the image later in our code.

  //  The second parameter is the URL of the image (relative)
  game.load.image('tentatrice1', 'assets/perso_test6.png');
  game.load.image('tentatrice2', 'assets/perso_test7.png');

}

function create() {
  //  To make the sprite move we need to enable Arcade Physicss
  game.physics.startSystem(Phaser.Physics.ARCADE);

  tentatrice1 = game.add.sprite(80, 0, 'tentatrice1');
  tentatrice1.anchor.set(0.5);

  // tentatrice2 = game.add.sprite(200, 300, 'tentatrice2');
  tentatrice2 = new Tentatrice(game, 'tentatrice2', {'x': 100, 'y': 300});

  //  And enable the Sprite to have a physics body:
  game.physics.enable(tentatrice1);
  // game.physics.enable(tentatrice2);
  // tentatrice1.body.velocity.x=150;

  cursors = game.input.keyboard.createCursorKeys();

}

function update() {
  //  If the sprite is > 8px away from the pointer then let's move to it
  if (game.physics.arcade.distanceBetween(tentatrice1, tentatrice2.sprite) > 8) {
    game.physics.arcade.moveToObject(tentatrice1, tentatrice2.sprite, 200);
  } else {
    tentatrice1.body.velocity.set(0);
  }


  if (cursors.up.isDown) {
    tentatrice2.move('up');
  } else if (cursors.down.isDown) {
    tentatrice2.move('down');
  } else if (cursors.left.isDown) {
    tentatrice2.move('left');
  } else if (cursors.right.isDown) {
    tentatrice2.move('right');
  }
}

function render() {

    // Display
    game.debug.spriteInfo(tentatrice1, 32, 32);
    // game.debug.inputInfo(32, 32);
    // game.debug.spriteInputInfo(tentatrice1, 32, 130);
    // game.debug.pointer( game.input.activePointer );

}
