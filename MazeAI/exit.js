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

  

  collide(sphero){
    if (sphero.x > this.x-(this.width/2) &
        sphero.x < this.x+(this.width/2) &
        sphero.y > this.y-(this.height/2) &
        sphero.y < this.y+(this.height/2)) {
          
          return true;
   
        }
        else{
          return false;
        }
  }
}
