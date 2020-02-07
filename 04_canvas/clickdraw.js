

var curr_state = "circle"
const canvas = document.getElementById("mood");
const button = document.getElementById("toggle");
const status = document.getElementById("status");

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


button.addEventListener("click", toggle);

canvas.addEventListener("mousemove", function(e, state){draw(e, curr_state)});


const ctx = canvas.getContext("2d");


var getMousePos = function(e) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
    };
};


var draw = function (e, state){
	var rect = canvas.getBoundingClientRect();

	const x = e.clientX - rect.left;
	const y = e.clientY - rect.top;

	console.log(state, x, y, e);

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





};




