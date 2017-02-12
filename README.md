# `imageserver`

![](https://i.imgur.com/VMTONmw.gif)

imageserver is a lightweight server that hosts images. These images are
available through the built-in web interface.

**imageserver is NOT fully featured, finished, or ready for production yet.
[Check the TODO list for more
information.](https://github.com/sliceofcode/imageserver/blob/master/TODO.md)
It is recommended that you run imageserver on your local/home network
exclusively, and not on the public web.**

## Prerequisites

- Python 3.6 is required. Python 2 and versions of Python 3 below 3.6 are
  not supported.
  - If you know how to program in Python, you can convert the codebase to
    be compatible with Python 3.5 &mdash; it'll just take a few tweaks.
- Pillow (PIL fork) and Flask. Install by:
  - Finding out if your Linux distribution has packages for Pillow and
    Flask. If your distro has them, install it.
  - If your Linux distro has no packages for Pillow and Flask, they will be
    installed automatically by `setup.py` in a few steps.

## Setup

1. Run `[sudo] pip install --editable .`
2. Create an `images` directory at the root of the repository (the
   directory that has this file inside of it).
3. Fill that directory with images. Image filetypes that are supported by
   both Pillow (PIL fork) and your web browser are supported.
   - Make sure the directory is flat (no subdirectories, all images should
     just be in that directory). Imageserver will ignore subdirectories.
4. Run `imageserver/generate_thumbnails.py`. This will generate thumbnails
   for all of the images in the `images` folder. This will take a bit if
   you have high resolution images.
5. Start the server:

```sh
# hacking/development
$ ./run dev

# production
$ ./run prod
# to run on a custom port, do:
$ ./run prod $PORT
```
