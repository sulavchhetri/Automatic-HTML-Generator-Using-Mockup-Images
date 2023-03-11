import logging
import base64
from PIL import Image
import io
from flask import Flask, render_template, request, redirect, url_for
from converter import Converter


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filemode='w', filename='logger.log')

app = Flask(__name__)


def get_html_from_converter():
    converter = Converter()
    return converter.get_html()


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if img_file := request.files['image']:
            img = Image.open(io.BytesIO(img_file.read()))
            result = get_html_from_converter()
            return redirect(url_for('generate_html', result=result))
    return render_template('index.html')


@app.route('/output')
def generate_html():
    result = get_html_from_converter()
    return render_template('showhtml.html', result=result)


@app.route('/preview')
def preview_html():
    result = get_html_from_converter()
    return render_template('preview.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
