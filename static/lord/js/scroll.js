const link = document.querySelector('.contacts');

link.addEventListener('click', function (event) {
  event.preventDefault();
  window.scrollTo({
    top: document.documentElement.scrollHeight,
    behavior: 'smooth'
  });
});