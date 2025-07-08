function toggleTheme() {
    document.body.classList.toggle('light-theme');
}

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });

  // Add event listener to content div for collapsing
  coll[i].nextElementSibling.addEventListener("click", function() {
    this.previousElementSibling.classList.toggle("active");
    if (this.style.display === "block") {
      this.style.display = "none";
    } else {
      this.style.display = "block";
    }
  });

  var links = coll[i].nextElementSibling.getElementsByTagName("a");
  for (var j = 0; j < links.length; j++) {
    links[j].addEventListener("click", function(event) {
      event.stopPropagation();
    });
  }
} 
