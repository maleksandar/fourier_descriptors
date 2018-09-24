# Image searching using Fourier descriptors

## Project
This repo contains a faculty project on Mathematical faculty at the University of Belgrade for "Scientific Calculations" course. The subject of the project is "Image searching using Fourier descriptors".

Main literature used: [Generic Fourier Descriptor for Shape-based Image Retrieval](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.69.3839&rep=rep1&type=pdf)

The solution in this repo consists of two main parts:
- Module for calculating the GFD (generic Fourirer descriptor)
- Web server that enebles the simple demonstration of the search

## Live demo
You can see live demo of the app deployed on heroku on: [fgd-image-search demo](https://fgd-image-search.herokuapp.com/) 

## Solution
### Simplification:
The solution in the main module takes some assumptions:
- We are operating on black and white images that can be trivialy converted to logical byte arrays (ones and zeros)

Note: *The solution can be expanded to search over colored images by first transforming the images to black and white and then rounding the values of each pixel to 0 or 1. (val < 128 -> 0; val >=128 -> 1)*

## Build and run
For any editor:
1. In the root folder run `pip install -r requirements.txt`
    - *It's highly recomended to use virtual environment: [python virtual envs](https://docs.python-guide.org/dev/virtualenvs/)*
2. Set environment variable `FLASK_APP` on your system to `web_server.py`
    - On windows open cmd and run:
     ```set FLASK_APP=web_server.py```
    - On unix based systems (linux / mac) open terminal and run: 
    `export FLASK_APP="web_server.py"`
3. At the root folder run command: `flask run`
4. Visit `0.0.0.0:5000` for local development

If you are using vs code:
1. The first step is the same as for any editor (*see instructions above*)
2. Copy & paste this configuration into configuration array in `.vscode/launch.json`
```
{
    "name": "Python: Flask",
    "type": "python",
    "request": "launch",
    "module": "flask",
    "env": {
        "FLASK_APP": "web_server.py"
    },
    "args": [
        "run",
        "--no-debugger",
        "--no-reload"
    ],
    "jinja": true
}
```
3. Open debug session tab and click on play button
4. Visit `0.0.0.0:5000` for local development

You can also run the app from the terminal with `python web_server.py`

## Presentation
[Google Docs Presentation](https://docs.google.com/presentation/d/1GRu_zzV7ugnXUYwxSmmy9c18RrzdXvhnh_uSPBY0UJ4/edit?usp=sharing)
