// Yevgeniy Gorbachev
// SoftDev1 pd1
// K12 -- Connect the Dots
// 2020-03-27

const w3svg = "http://www.w3.org/2000/svg";
const image = document.getElementById("vimage");
const clearbutton = document.getElementById("clear");

const radius = 10;

function dot(x, y) {
	let circle = document.createElementNS(w3svg, "circle");
	circle.setAttribute("cx", x);
	circle.setAttribute("cy", y);
	circle.setAttribute("r", radius);
	circle.setAttribute("fill", "red");
	return circle;
};

function draw(e) {
	console.log(e);
	let c = dot(e.offsetX, e.offsetY)
	e.preventDefault()

	if (e.target == image) {
		image.appendChild(c);
	}
	c.addEventListener("click", changecolor);
};


function clear() {
	image.innerHTML = "";
};

function changecolor(e) {
	let c = e.target;
	if (c.getAttribute("fill") == "red") {
		c.setAttribute("fill", "blue");
	}
	else {
		image.removeChild(c);
		let newc = dot(
			Math.floor(Math.random() * 501),
			Math.floor(Math.random() * 501)
		);

		image.appendChild(newc);
		e.preventDefault();
		newc.addEventListener("click", changecolor);
	}
};


image.addEventListener('click', draw);
clearbutton.addEventListener('click', clear);
