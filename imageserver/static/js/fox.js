window.addEventListener('load', function() {
  const fullButton = document.querySelector('#full-button');
  let image = document.querySelector('img.presentation');

  image.style.maxWidth = '80vw';
  image.style.maxHeight = '80vh';

  fullButton.addEventListener('click', function() {
    if (image.style.maxWidth === '80vw') {
      image.style.maxWidth = '100%';
      image.style.maxHeight = '100%';
    } else {
      image.style.maxWidth = '80vw';
      image.style.maxHeight = '80vh';
    }
  });
});
