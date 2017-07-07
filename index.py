#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API - compute the pixels width and remaining width of a title and/or description of page for Google SERP.

The goal of this tool is to optimize the writing of titles and descriptions of web pages.
If the title or description of your page is too long, Google will automatically cut it to a certain length and add "..." at the end.
This decreases the chance that a visitor will visit your site.

The source device used in this tool is a laptop with Chrome web browser (user agent) :
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36

In this configuration, the maximum width of the title is 554 pixels, and 1204 pixels for the description.

See https://github.com/AnthonySigogne/seo-pixel-width for more information.
"""

__author__ = "Anthony Sigogne"
__copyright__ = "Copyright 2017, Byprog"
__email__ = "anthony@byprog.com"
__license__ = "MIT"
__version__ = "1.0"

import os
import requests
from flask import Flask, request, jsonify, render_template

# init flask app and env variables
app = Flask(__name__)
host = os.getenv("HOST")
port = os.getenv("PORT")

@app.route("/", methods=['GET'])
def pixels_width():
    """
    URL : /
    Compute pixels width and remaining width of a title or/and description.
    Method : POST or GET (no data)
    Form data :
        - select : url to analyze
    Return the list of relevant keywords.
    """
    # GET data
    title = request.args.get("title", None)
    description = request.args.get("description", None)
    url = request.args.get("url", None)

    if url :
        # analyze url
        try :
            r = requests.post('http://%s:%s/pixels_url'%(host, port), data = {'url':url})
        except :
            return "Error, check your installation"

        if r.status_code == requests.codes.ok :
            # show the result
            data = r.json()
            return render_template('layout.html',
                url=url[:90]+"..." if len(url) > 90 else url,
                data=data)
        else :
            # error for this url (invalid link, no content,...)
            return render_template('layout-empty.html', error="Invalid link or no content to analyze...")

    elif title or description :
        # analyze title and/or description
        try :
            r = requests.post('http://%s:%s/pixels'%(host, port), data = {'title':title, "description":description})
        except :
            return "Error, check your installation"

        if r.status_code == requests.codes.ok :
            # show the result
            data = r.json()
            return render_template('layout.html',
                data=data)

    # return homepage (no query)
    return render_template('layout-empty.html')
