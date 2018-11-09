class Exit{
  constructor(x,y){
    this.width = 50;
    this.height = 50;
    this.x = x;
    this.y = y;
  }

  show(){

   rect(this.x,this.y,this.width,this.height);
   
  }
  update(){


  }
  offscreen(){
    if(this.x<-this.width){return true;}
    else{return false;}
  }

  hits(bird){
    if(bird.y-(bird.r/2) < this.y|| bird.y+(bird.r/2) > this.bottom){
      if(bird.x > this.x && bird.x < this.x+this.width){return true;}
    }
  }

  collide(sphero){
    if (sphero.x > this.x-(this.width/2) &
        sphero.x < this.x+(this.width/2) &
        sphero.y > this.y-(this.height/2) &
        sphero.y < this.y+(this.height/2)) {
          
          return 1;
   
        }
        else{
          return 0;
        }
  }
}
