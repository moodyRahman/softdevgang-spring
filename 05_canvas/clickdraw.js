var curr_state = "circle"


const canvas = document.getElementById("mood");
const button = document.getElementById("toggle");
const status = document.getElementById("status");
const clear = document.getElementById("clear");
const ctx = canvas.getContext("2d");


var toggle = function(e){
	if (curr_state === "circle"){
		curr_state = "rect";
		status.innerHTML = "rectangle";
	}
	
	else{
		curr_state = "circle";
		status.innerHTML = "circle";

	}

	console.log("current state is");
	console.log(curr_state);

};

var clearcanvas = function(canvas, contex){
	context.clearRect(0, 0, canvas.width, canvas.height);
};

var draw = function (e, state){
	var rect = canvas.getBoundingClientRect();
	const x = e.clientX - rect.left;
	const y = e.clientY - rect.top;
	console.log(e);
	if (e.buttons > 0){
		if (state === "circle"){
	                ctx.beginPath();
	                ctx.arc(x, y, 5, 0, 2 * Math.PI);
	                ctx.stroke();
	        }
	        else {
	                ctx.beginPath();
	                ctx.rect(x, y, 8, 8);
			ctx.stroke();
		}
	}
};



button.addEventListener("click", toggle);
clear.addEventListener("click", function(){ctx.clearRect(0, 0, canvas.width, canvas.height);});
canvas.addEventListener("mousemove", function(e, state){draw(e, curr_state)});
