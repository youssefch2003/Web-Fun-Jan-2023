class Ninja {
    constructor(name,health,speed = 3,strength = 3){
        this.name =name
        this.health =health
        this.speed =speed
        this.strength =strength
    }
    // methods
    sayName(){
        console.log(this.name);
    }
    showStats(){
        console.log(this);
    }
    drinkSake(){
        return this.health +=10
    }
   
}
 
class Sensei extends Ninja {
    constructor(name){
        super(name,200,10,10)
        this.wisdom = 10
    }
    speakWisdom(){
        this.drinkSake();
        console.log("What one programmer can do in one month, two programmers can do in two months.");
    }
    
}
const superSensei = new Sensei("Jackie Chan");
superSensei.speakWisdom();
superSensei.showStats();