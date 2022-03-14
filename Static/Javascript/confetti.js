/*
 * Copyright (c) 2022/3/14.
 */

function confettiFalling() {

    let i;
    const box = document.getElementById("grid");
    const colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink'];

    for (i = 0; i < 1000; i++) {

		// Create 1000 DIV elements for confetti
        const div = document.createElement("div");
        div.classList.add("confetti");
        div.classList.add("active");
		box.appendChild(div);
	}

    const confetti = document.querySelectorAll('.confetti');

    for (i = 0; i < confetti.length; i++) {

        const size = Math.random() * 0.01 * [i];

        confetti[i].style.width = 3 + size + 'px';
		confetti[i].style.height = 10 + size + 'px';
		confetti[i].style.left = Math.random() * innerWidth + 'px';

        confetti[i].style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];

		box.children[i].style.transform = "rotate("+ size*[i] +"deg)";
	}
}