# seo-pixel-width-ui
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

UI of the pixel width tool https://github.com/AnthonySigogne/seo-pixel-width

## DEMO
A demo can be found here : http://pixelwidth.byprog.com/  

## INSTALL AND RUN

### REQUIREMENTS
This tool requires *Python3+* and the pixel width API (see link above).

### WITH PIP
```
git clone https://github.com/AnthonySigogne/seo-pixel-width-ui.git
cd seo-pixel-width-ui
pip install -r requirements.txt
```

Then, run the tool :
```
FLASK_APP=index.py HOST=<ip> PORT=<port> flask run --port 80
```
Where :
* `ip` + `port` : route to pixel width API

To run in debug mode, prepend `FLASK_DEBUG=1` to the command :
```
FLASK_DEBUG=1 ... flask run --port 80
```

### WITH DOCKER
To run the tool with Docker, you can use my DockerHub image :
https://hub.docker.com/r/anthonysigogne/seo-pixel-width-ui/
```
docker run -p 80:5000 \
-e "HOST=<ip>" \
-e "PORT=<port>" \
anthonysigogne/seo-pixel-width-ui
```
Where :
* `ip` + `port` : route to pixel width API

Or, build yourself a Docker image :
```
git clone https://github.com/AnthonySigogne/seo-pixel-width-ui.git
cd seo-pixel-width-ui
docker build -t seo-pixel-width-ui .
```

## USAGE AND EXAMPLES
To use the pixel width tool, just type this endpoint in your web browser : http://localhost/

![Pixel width tool](images/pixel-width.png?raw=true "Pixel width tool" )

## LICENCE
MIT
