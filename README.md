# Image searching using Fourier descriptors

## Project
This repo contains a faculty project on Mathematical faculty at the University of Belgrade for "Scientific Calculations" course. The subject of the project is "Image searching using Fourier descriptors".

Main literature used: [Generic Fourier Descriptor for Shape-based Image Retrieval link](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.69.3839&rep=rep1&type=pdf)

The solution in this repo consists of two main parts:
- Module for calculating the GFD (generic Fourirer descriptor)
- Web server that enebles the simple demonstration of the search

## Solution
### Simplification:
The solution in the main module takes some assumptions:
- We are operating on black and white images that can be trivialy converted to logical byte arrays (ones and zeros)

Note: *The solution can be expanded to search over colored images by first transforming the images to black and white and then rounding the values of each pixel to 0 or 1. (val < 128 -> 0; val >=128 -> 1)*

## Build and run
For any editor:

1. Set environment variable `FLASK_APP` on your system to `web_server.py`
    - On windows open cmd and run:
     ```set FLASK_APP=web_server.py```
    - On unix based systems (linux / mac) open terminal and run: 
    `export FLASK_APP="web_server.py"`
2. At the root folder run command: `flask run`

If you are using vs code:
1. Copy & paste this config into `.vscode/launch.json`
2. Open debug session tab and click on play button
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