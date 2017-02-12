let thePreview;
let mX = 0, mY = 0;
const previewOffset = 2;

function updateHoverPosition() {
  const sX = innerWidth, sY = innerHeight;

  if (mX > sX - (sX / 3)) {
    thePreview.style.left =
      `calc(${mX}px - ${previewOffset}rem - ${thePreview.offsetWidth}px)`;
  } else {
    thePreview.style.left = `calc(${mX}px + ${previewOffset}rem)`;
  }
  if (mY > sY - (sY / 3)) {
    thePreview.style.top =
      `calc(${mY}px - ${previewOffset}rem - ${thePreview.offsetHeight}px)`;
  } else {
    thePreview.style.top = `calc(${mY}px + ${previewOffset}rem)`;
  }
}

function activateHover(th) {
  thePreview = document.createElement('img');
  let imageFullSrc = th.src.replace(/\.thumb/, '');
  thePreview.src = imageFullSrc;

  thePreview.id = 'preview';
  thePreview.style.position = 'absolute';
  thePreview.style.maxWidth = '20vw';
  updateHoverPosition();
  document.body.appendChild(thePreview);
}

function deactivateHover(th) {
  thePreview.parentNode.removeChild(thePreview);
}

window.addEventListener('mousemove', function(event) {
  mX = event.pageX; mY = event.pageY;
  if (thePreview) {
    updateHoverPosition();
  }
});

window.addEventListener('load', function() {
  let image = document.querySelector('img.presentation');
  let thumbnails = document.querySelectorAll('img.thumb');

  for (let thumbnail of thumbnails) {
    thumbnail.addEventListener('mouseover', function() {
      activateHover(thumbnail);
    });

    thumbnail.addEventListener('mouseout', function() {
      deactivateHover(thumbnail);
    });
  }

  if (image) {
    image.style.maxWidth = '80vw';
    image.style.maxHeight = '80vh';

    image.addEventListener('click', function() {
      if (image.style.maxWidth === '80vw') {
        image.style.maxWidth = '100%';
        image.style.maxHeight = '100%';
      } else {
        image.style.maxWidth = '80vw';
        image.style.maxHeight = '80vh';
      }
    });
  }
});
