import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
from main import search

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/images/<path:filename>')
def custom_static(filename):
    return send_from_directory('images', filename)

@app.route('/search/<image_name>')
def search_image(image_name):
    stats = search(image_name)
    return jsonify(stats[:4])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)