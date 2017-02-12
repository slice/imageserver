# `imageserver`

imageserver is a lightweight server that hosts images. These images are
available through the built-in web interface.

## Prerequisites

- Python 3.6 is required. Python 2 and versions of Python 3 below 3.6 are
  not supported.
  - If you know how to program in Python, you can convert the codebase to
    be compatible with Python 3.5 &mdash; it'll just take a few tweaks.
- Pillow (PIL fork) and Flask. Install by:
  - Finding out if your Linux distribution has packages for Pillow and
    Flask. If your distro has them, install it.
  - Alternatively, run `[sudo] pip install -r requirements.txt`

## Setup

1. Ensure that all dependencies have been installed.
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
$ PYTHONPATH=. FLASK_APP=imageserver.app FLASK_DEBUG=1 flask run

# production
$ PYTHONPATH=. FLASK_APP=imageserver.app flask run --host 0.0.0.0

# Runs on :5000 by default. Use --port XXXX (e.g. --port 80) to use a
# custom port.
```
