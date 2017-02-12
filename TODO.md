# TODO

- [x] **Tests!**
- [ ] Actual database instead of an in-memory one that gets rebuilt every
  launch.
  - [ ] Favorite images. (maybe)
  - [ ] Tag images. (maybe)
  - [ ] Ability to mark images as hidden (present on the filesystem, but not
    shown)
- [ ] Fully featured API.
  - [x] `/api/database/redothumbs` Regenerates thumbnails.
  - [x] `/api/database/refresh` Rebuilds file paths/`Image` objects.
  - [ ] `/api/database/snapshot` Complete snapshot of the `Database` object in
    JSON format.
  - [ ] `/api/images` List of images in JSON format.
  - [ ] `/api/image/<string:filename>` Information/metadata about image in JSON
    format.
- [ ] Properly handle MIME types in the image "proxy".
- [x] Admin interface.
  - [x] Regenerates thumbnails through the interface.
  - [x] Refresh database through the interface.
- [ ] Authentication. Admin interface is completely open.
- [ ] Use SCSS instead of using vanilla CSS for neater stylesheets.
- [ ] Clientside settings modal.
  - [ ] Hover preview settings.
    - [ ] Ability to toggle the hover preview.
    - [ ] Ability to adjust the hover preview offset.
  - [ ] Colorschemes? Useless but fun.
    - [ ] Dark colorscheme. (inverted)
    - [ ] Blue colorscheme.
    - [ ] White colorscheme. (gray/near white navigation bar instead of it
      being black)
- [x] Thumbnails.
  - [ ] Use proper math for calculating the ratio of thumbnails.
- [x] Hover preview.
  - [x] Flip the preview depending on cursor position.
  - [ ] Do not swap the orientation when the cursor reaches the last third of
    the screen. Instead, take into account the size of the image and flip it
    when it overflows off of the screen.
