const coll=document.getElementsByClassName("collapsible");

for (let i=0; i < coll.length; i++) {
	const content=coll[i].nextElementSibling;
	const isContentVisible=window.getComputedStyle(content).getPropertyValue("display") !=="none";

	coll[i].addEventListener("click", function() {
			this.classList.toggle("active");

			if (isContentVisible) {
				content.classList.remove("show");
			}

			else {
				content.classList.add("show");
			}
		});
}