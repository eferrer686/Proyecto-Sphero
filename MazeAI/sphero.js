function mutate(x) {
  if (random(1) < 0.5) {
    let offset = randomGaussian() * 0.8;
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

    this.collide = 0;

    this.exit = exit

    this.originalDist = this.getDist();
    this.brain = new NeuralNetwork(9,50,4);

    this.score = this.originalDist - this.getDist();
  }
  show(){
   ellipse(this.x,this.y,this.r);
  }
  
  moveRight(){
    if (this.x<width) {
      this.x += this.velocity;

      if(this.checkCollide()){
        this.x -= this.velocity;
      }
      

    }
  }
  moveLeft(){
    if (this.x>0) {
      this.x -= this.velocity;

      if(this.checkCollide()){
        this.x += this.velocity;
      }
    }
  }
  moveUp(){
    if (this.y<height) {
      this.y += this.velocity;

      if(this.checkCollide()){
        this.y -= this.velocity;
      }
    }
  }
  moveDown(){
    if (this.y>0) {
      this.y -= this.velocity;

      if(this.checkCollide()){
        this.y += this.velocity;
      }
    }
  }

  update(){
    this.score = this.originalDist - this.getDist();
    return this.exit.collide(this);
  }

  think(){
    let input = [];

    var dists = this.see();

    input[0] = this.y;
    input[1] = this.x;
    input[2] = this.exit.x;
    input[3] = this.exit.y;
    input[4] = this.collide;
    input[5] = dists[0];
    input[6] = dists[1];
    input[7] = dists[2];
    input[8] = dists[3];
    
  
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

  checkCollide(){
    this.collide = 0;
    //Check collision in new position
    for (let i = 0; i < walls.length; i++) {
      if (walls[i].collide(this)){
        this.collide = 1;
        return true;
      }
    }
  }

  see(){
    var dists = [width-this.x,this.x,height-this.y,this.y];

    for (let i = 0; i < walls.length; i++) {
      //Look Right
      if((walls[i].x - walls[i].width - this.x) >=0 & 
         (walls[i].x - walls[i].width - this.x) < dists[0] & 
         this.y > (walls[i].y-(walls[i].height/2)) &
         this.y < (walls[i].y+(walls[i].height/2))){

          dists[0] = walls[i].x - walls[i].width - this.x;

      }

      //Look Left
      if(this.x - walls[i].x + walls[i].width >=0 & 
        this.x - walls[i].x + walls[i].width < dists[1] & 
        this.y > (walls[i].y-(walls[i].height/2)) &
        this.y < (walls[i].y+(walls[i].height/2))){

          dists[1] = this.x - walls[i].x + walls[i].width;

      }

      //Look Up
      if((walls[i].y - walls[i].height - this.y) >= 0 & 
        (walls[i].y - walls[i].height - this.y) < dists[2] & 
        this.x > (walls[i].x-(walls[i].width/2)) &
        this.x < (walls[i].x+(walls[i].width/2))){

         dists[2] = walls[i].y - walls[i].height - this.y;

     }

     //Look Down
     if((this.y - walls[i].y + walls[i].height) >= 0 & 
       (this.y - walls[i].y + walls[i].height) < dists[3] & 
       this.x > (walls[i].x-(walls[i].width/2)) &
       this.x < (walls[i].x+(walls[i].width/2))){

         dists[3] = this.y - walls[i].y + walls[i].height;

     }
    }
    
    //console.log(dists);
    
    return dists;
  }
}
