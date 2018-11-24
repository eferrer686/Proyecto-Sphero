class Wall{
    constructor(x,y,width,height){
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }
    show(){
        rect(this.x,this.y,this.width,this.height);
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