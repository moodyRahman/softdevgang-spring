

const animate = document.getElementById("animate");
const stop = document.getElementById("stop");
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d")
var radius = 6;
var mode = "grow";
var drawing = true;

var drawcircle = function(){
        if (drawing){
        if (radius > 250){
                mode = "shrink";
        }
        if (radius <= 0){
                mode = "grow";
        }
        if (mode === "grow"){
                context.clearRect(0, 0, canvas.width, canvas.height)
                context.beginPath();
                context.arc(250, 250, radius, 0, 2 * Math.PI);
                context.stroke();
                radius = radius + 2;
        }
        else {
                context.clearRect(0, 0, canvas.width, canvas.height)
                context.beginPath();
                context.arc(250, 250, radius, 0, 2 * Math.PI);
                context.stroke();
                radius = radius - 2;
        }
        var mood = window.requestAnimationFrame(drawcircle);
        console.log(radius);}
};


stop.addEventListener("click", function(){drawing = false;})
animate.addEventListener("click", function(){
                                        if (drawing === false){
                                                drawing = true;
                                                drawcircle();}
                                        }
                                );

drawcircle();

// window.requestAnimationFrame(drawcircle);
