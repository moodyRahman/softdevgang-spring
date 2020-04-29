// Yevgeniy Gorbachev and Moududur Rahman
// SoftDev1 pd1/ pd9
// K12 -- Connect the Dots
// 2020-03-27

const w3svg = "http://www.w3.org/2000/svg";
const image = document.getElementById("vimage");
const clearbutton = document.getElementById("clear");
const movebutton = document.getElementById("move");
const alld = [-5, 5];
var tomove = false;
let allcircles = image.childNodes;

const radius = 10;

function dot(x, y) {
	let circle = document.createElementNS(w3svg, "circle");
	circle.setAttribute("cx", x);
	circle.setAttribute("cy", y);
	circle.setAttribute("r", radius);
	circle.setAttribute("fill", "red");
	circle.setAttribute("dx", alld[Math.floor(Math.random() * alld.length)]);
	circle.setAttribute("dy", alld[Math.floor(Math.random() * alld.length)]);
	return circle;
};

function draw(e) {
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

function move() {
	// allcircles.forEach(circ => {
	// 	console.log(circ);
	// 	let cx = circ.getAttribute("cx");
	// 	let cy = circ.getAttribute("cy");
	// 	if (cx => 500 || cx <=0){
	// 		dx = -1 * dx;
	// 	}
	// 	if (cy => 500 || cy <= 0) {
	// 		dy = -1 * dy;
	// 	}
	// 	// setInterval(function(){
	// 	// 	circle.setAttribute("cx", cx + dx);
	// 	// 	circle.setAttribute("cy", cy + dy);
	// 	// }, 1);
	// 	circ.setAttribute("cx", cx + dx);
	// 	circ.setAttribute("cy", cy + dy);
	// });

	for (let i = 1; i < allcircles.length; i++) {
		let circ = allcircles[i];
		let cx = Number(circ.getAttribute("cx"));
		let cy = Number(circ.getAttribute("cy"));
		let dx = Number(circ.getAttribute("dx"));
		let dy = Number(circ.getAttribute("dy"));
		console.log(cx);
		console.log(cy);
		console.log(dx);
		console.log(dy);
		// console.log("-------------");
		// if (cx > 500 || cx < 0) {
			// dx = -1 * dx;
			// circ.setAttribute("dx", dx * -1);
		// }
		if (cx > 500){
			dx = -1 * dx;
			circ.setAttribute("dx", dx * -1);
			circ.setAttribute("cx", 499);
		}
		if (cx < 0){
			dx = -1 * dx;
			circ.setAttribute("dx", dx * -1);
			circ.setAttribute("cx", 499);
		}

		if (cy > 500) {
			dy = -1 * dy;
			circ.setAttribute("dy", dy * -1);
			circ.setAttribute("dy", 499);
		}
		if (cy < 0) {
			dy = -1 * dy;
			circ.setAttribute("dy", dy * -1);
			circ.setAttribute("cy", 499);
		}
		// if (cy > 500 || cy < 0) {
		// 	dy = -1 * dy;
		// 	circ.setAttribute("dy", dy * -1);
		// }
		// setInterval(function(){
		// 	circle.setAttribute("cx", cx + dx);
		// 	circle.setAttribute("cy", cy + dy);
		// }, 1);
		circ.setAttribute("cx", cx + dx);
		circ.setAttribute("cy", cy + dy);
	}
}

setInterval(move, 2);


image.addEventListener('click', draw);
clearbutton.addEventListener('click', clear);
movebutton.addEventListener('click', move);
