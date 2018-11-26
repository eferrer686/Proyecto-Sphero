
let totalPopulation = 20;
let allSpheros = [];
let activeSpheros = [];
let counter = 0;

let numBestSpheros=1;
let winnerSphero = null;
let bestScore = 0;
let actualScore = 0;
let generation = 1;
let x = 50;
let y = 50;
var exit = null;

var walls = [];

var genWinner = null;

let timer = 30;

function setup() {
  createCanvas(800,400);

  rectMode(CENTER);
  ellipseMode(CENTER);

  //Select maze
  maze5();

  for (let i = 0; i < totalPopulation; i++) {
    var sphero = new Sphero(x,y,exit);
    activeSpheros.push(sphero);
    allSpheros.push(sphero);
  }



}

function draw() {
  background(0);
  graphics();

  sliderval = document.getElementById("vel").value;

  for(var i = 0;i<sliderval;i++){
    counter += 1;
    if((counter % (60*timer)) == 0){
      //create new generation and reset simulation
      reset();
    }else{

      //Run or keep running simulation
        play();
    }
  }

}
function play(){


  //Update spheros movement
  for(var i = 0;i < activeSpheros.length ;i++){

    if (activeSpheros[i].update()) {
      if (genWinner == null) {
        genWinner = generation;
      }
      winnerSphero = activeSpheros[i]
      reset();
      break;
    }


    if(activeSpheros[i].score > bestScore){
      bestScore=activeSpheros[i].score;
    }
  }





  //Make spheros "think"
  for(var i = 0;i < activeSpheros.length ;i++){

    activeSpheros[i].think();
  }

  /*
  //Delete spheros that collide
  for(var i = 0;i < activeSpheros.length ;i++){
    if(activeSpheros.length<=1){
      winnerSphero = activeSpheros[i];
      reset();
      break;
    }
    if(activeSpheros[i].collide==1){
      activeSpheros.splice(i);
      i--;
    }
  }*/

}


function reset(){
    counter = 0;
    generation++;
    getBestSpheros(numBestSpheros);

}
function getBestSpheros(num){
  let bestSpheros = [];

  for(var i  = 0 ;i<num ;i++){
    bestSpheros[i]=new Sphero(x,y,exit);
  }

  for(var i = 0; i< allSpheros.length ; i++){
    for(var j = 0 ; j<num ; j++){

      if (i<allSpheros.length && allSpheros[i].score > bestSpheros[j].score){

        newSphero = allSpheros.splice(i,1)[0];
        bestSpheros[j]=newSphero;
      }
    }

  }

  if(winnerSphero != null){
    bestSpheros[bestSpheros.length-1] = winnerSphero;
  }

  replacePopulation(bestSpheros,num,x,y,exit);
}
function replacePopulation(bestSpheros,num,x,y,exit){
  allSpheros=[];
  activeSpheros=[];



  for(var i = 0; i<totalPopulation+numBestSpheros-2; i++){
    var newSphero = new Sphero(x,y,exit);

    newSphero.setBrain(bestSpheros[i%num].brain.copy());
    newSphero.mutate();

    activeSpheros.push(newSphero);
    allSpheros.push(newSphero);

  }
  randomSphero = new Sphero(x,y,exit);
  activeSpheros.push(randomSphero);
  activeSpheros.push(randomSphero);

  newSphero = new Sphero(x,y,exit);
  newSphero.setBrain(bestSpheros[0].brain.copy());

  activeSpheros.push(newSphero);

}

function graphics(){
    document.getElementById("generation").innerHTML = "Generation number:   " + generation;
    document.getElementById("alive").innerHTML = "Number of spheros alive:  " + activeSpheros.length;
    document.getElementById("score").innerHTML = "Timer:  " + (Math.floor((timer-(counter/60))));
    document.getElementById("bestscore").innerHTML = "Best Score:   " + (Math.floor(bestScore));
    document.getElementById("winner").innerHTML = "Winner at generation: " + genWinner;
    //Update spheros movement
    noStroke();
    fill(255,100);
    for(var i = 0;i < activeSpheros.length ;i++){
      activeSpheros[i].show();
    }

    for (let i = 0; i < walls.length; i++) {
      fill(255,200);
      walls[i].show();

    }

    //update exit graphics
    fill(0,255,0);
    exit.show();

}


function maze1() {

  walls[0] = new Wall(350,50,50,200);
  walls[1] = new Wall(550,350,50,200);
  walls[2] = new Wall(50,250,200,50);
  exit = new Exit(700,300);
}


function maze2() {

  walls[0] = new Wall(150,150,50,310);
  walls[1] = new Wall(350,350,50,200);
  walls[2] = new Wall(550,150,50,310);
  exit = new Exit(750,50);
}

function maze3() {
  walls[0] = new Wall(600,50,50,600);
  walls[1] = new Wall(300,350,50,600);
  walls[2] = new Wall(100,50,50,200);
  walls[3] = new Wall(685,150,120,50);
  exit = new Exit(700, 50);
}

function maze4() {
  walls[0] = new Wall(200,50,100,50);
  walls[1] = new Wall(200,150,100,50);
  walls[2] = new Wall(200,250,100,50);
  walls[3] = new Wall(200,350,100,50);
  walls[4] = new Wall(600,150,50,300);
  walls[5] = new Wall(400,10,50,300);
  exit = new Exit(700, 50);
}

function maze5() {
  walls[0] = new Wall(350,200,500,50);
  walls[1] = new Wall(370,350,550,50);
  walls[2] = new Wall(625,50,50,350);

  exit = new Exit(750, 50);
}
