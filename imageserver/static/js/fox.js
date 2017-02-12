let thePreview;
let mX = 0, mY = 0, aX = 0, aY = 0;
const previewOffset = 2;

function updateHoverPosition() {
  const sX = innerWidth, sY = innerHeight;

  if (aX > sX - (sX / 2.5)) {
    thePreview.style.left =
      `calc(${mX}px - ${previewOffset}rem - ${thePreview.offsetWidth}px)`;
  } else {
    thePreview.style.left = `calc(${mX}px + ${previewOffset}rem)`;
  }
  if (aY > sY - (sY / 2.5)) {
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
  aX = event.screenX; aY = event.screenY;
  if (thePreview) {
    updateHoverPosition();
  }
});

const adminButtons = ['#refresh-database', '#regenerate-thumbs'];

function disableAdminButtons() {
  for (let adminButtonId of adminButtons) {
    document.querySelector(adminButtonId).disabled = true;
  }
}

function enableAdminButtons() {
  for (let adminButtonId of adminButtons) {
    document.querySelector(adminButtonId).disabled = false;
  }
}

window.addEventListener('load', function() {
  let image = document.querySelector('img.presentation');
  let thumbnails = document.querySelectorAll('img.thumb');
  let refresh = document.querySelector('#refresh-database');
  let reThumbs = document.querySelector('#regenerate-thumbs');

  for (let thumbnail of thumbnails) {
    thumbnail.addEventListener('mouseover', function() {
      activateHover(thumbnail);
    });

    thumbnail.addEventListener('mouseout', function() {
      deactivateHover(thumbnail);
    });
  }

  if (refresh) {
    refresh.addEventListener('click', function() {
      // XXX: this url is hardcoded
      disableAdminButtons();
      fetch('/api/database/refresh').then((resp) => resp.text()).then((text) => {
        alert(`Finished! Took ${text} ms.`);
        enableAdminButtons();
      });
    });
  }

  if (reThumbs) {
    reThumbs.addEventListener('click', function() {
      // XXX: this url is hardcoded
      disableAdminButtons();
      fetch('/api/database/redothumbs').then((resp) => resp.text()).then((text) => {
        let ms = parseInt(text);
        alert(`Finished! Took ${ms} ms (${ms / 1000} seconds).`);
        this.disabled = false;
        enableAdminButtons();
      });
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
