// Yevgeniy Gorbachev
// SoftDev1 pd1
// K12 -- Connect the Dots
// 2020-03-27

const w3svg = "http://www.w3.org/2000/svg";
const image = document.getElementById("vimage");
const clearbutton = document.getElementById("clear");

let x_last = y_last = -1;

function dot(x, y) {
	let circle = document.createElementNS(w3svg, "circle");
	circle.setAttribute("cx", x);
	circle.setAttribute("cy", y);
	circle.setAttribute("r", 2);
	circle.setAttribute("fill", "black");
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
	image.appendChild(dot(e.offsetX, e.offsetY));
	if (x_last != -1) {
		image.appendChild(line(x_last, y_last, e.offsetX, e.offsetY));
	};

	x_last = e.offsetX;
	y_last = e.offsetY;
};


function clear() {
	image.innerHTML = "";
	x_last = y_last = -1;

};

image.addEventListener('click', draw);
clearbutton.addEventListener('click', clear);
