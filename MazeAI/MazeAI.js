
let totalPopulation = 50;
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

var genWinner = null;

let timer = 20;

function setup() {
  createCanvas(800,400);
  
  rectMode(CENTER);
  ellipseMode(CENTER);

  exit = new Exit(700,300);
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
  for(var i = 0; i<totalPopulation-2; i++){
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

    //update exit graphics
    fill(0,255,0);
    exit.show();

}