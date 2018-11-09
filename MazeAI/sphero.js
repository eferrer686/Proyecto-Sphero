function mutate(x) {
  if (random(1) < 0.1) {
    let offset = randomGaussian() * 0.5;
    let newx = x + offset;
    return newx;
  } else {
    return x;
  }
}


class Sphero{
  constructor(x,y,exit){
    
    this.x = x;
    this.y = y;
    this.gravity = 2;
    this.velocity = 1;
    this.r = 20;

    this.exit = exit

    this.originalDist = this.getDist();
    this.brain = new NeuralNetwork(5,20,4);

    this.score = this.originalDist - this.getDist();
  }
  show(){
   ellipse(this.x,this.y,this.r);
  }
  
  moveRight(){
    if (this.x<width) {
      this.x += this.velocity;
    }
  }
  moveLeft(){
    if (this.x>0) {
      this.x -= this.velocity;
    }
  }
  moveUp(){
    if (this.y<height) {
      this.y += this.velocity;
    }
  }
  moveDown(){
    if (this.y>0) {
      this.y -= this.velocity;
    }
  }

  update(){
    
    this.score = this.originalDist - this.getDist();
    return this.exit.collide(this)==1;
  }

  think(){
    let input = [];

    input[0] = this.y;
    input[1] = this.x;
    input[2] = this.exit.x;
    input[3] = this.exit.y;
    input[4] = this.exit.collide(this);
  
    let output = this.brain.predict(input);
    if(output[0]>0.5){
      this.moveRight();
    }
    if(output[1]>0.5){
      this.moveLeft();
    }
    if(output[2]>0.5){
      this.moveUp();
    }
    if(output[3]>0.5){
      this.moveDown();
    }
  }

  mutate(){
    this.brain.mutate(mutate);
  }
  setBrain(newBrain){
    this.brain = newBrain ;
  }

  getDist(){
    return Math.sqrt(Math.pow(Math.abs(this.x-this.exit.x),2) + Math.pow(Math.abs(this.y-this.exit.y),2));
  }
}
