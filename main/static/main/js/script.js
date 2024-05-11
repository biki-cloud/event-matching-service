console.log("xxxx");

document.addEventListener('DOMContentLoaded', function() {
  const sidebar = document.querySelector('#sidebar');
  const storedSidebarState = localStorage.getItem('sidebarExpanded');
  
  if (storedSidebarState === 'true') {
    sidebar.classList.add('expand');
  }

  const hamBurger = document.querySelector(".toggle-btn");
  hamBurger.addEventListener("click", function() {
    sidebar.classList.toggle("expand");
    localStorage.setItem('sidebarExpanded', sidebar.classList.contains('expand'));
  });
});
