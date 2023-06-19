const darkModeBtn=document.querySelector("#dark-mode-btn");
const body=document.querySelector("body");

darkModeBtn.addEventListener("click", toggleDarkMode);

function toggleDarkMode() {
	body.classList.toggle("dark-mode");
}