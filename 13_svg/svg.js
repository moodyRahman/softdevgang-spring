// Yevgeniy Gorbachev
// SoftDev1 pd1
// K12 -- Connect the Dots
// 2020-03-27

const w3svg = "http://www.w3.org/2000/svg";
const image = document.getElementById("vimage");
const clearbutton = document.getElementById("clear");

let x_last = y_last = -1;
let circles = [];
const radius = 8;

function dot(x, y) {
	let circle = document.createElementNS(w3svg, "circle");
	circle.setAttribute("cx", x);
	circle.setAttribute("cy", y);
	circle.setAttribute("r", 8);
	circle.setAttribute("ischange", 0);
	circle.addEventListener("click", function(){ changecolor(circle) });
	return circle;
};

function line(x_1, y_1, x_2, y_2) {
	let line = document.createElementNS(w3svg, "line");
	line.setAttribute("x1", x_1);
	line.setAttribute("y1", y_1);
	line.setAttribute("x2", x_2);
	line.setAttribute("y2", y_2);
	line.setAttribute("stroke", "black");
	return line;
};

function draw(e) {
	let c = dot(e.offsetX, e.offsetY)
	image.appendChild(c);

};


function clear() {
	image.innerHTML = "";
	x_last = y_last = -1;mouselocater

};

function changecolor(circle){
	if (circle.getAttribute("ischange") == 0){
		circle.setAttribute("ischange", 1);
		return;
	}

	if (circle.getAttribute("ischange") == 1){
		circle.setAttribute("fill", "red");
	}

	console.log(circle);

};

image.addEventListener('click', draw);
clearbutton.addEventListener('click', clear);
