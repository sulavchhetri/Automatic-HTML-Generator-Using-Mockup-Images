import logging
import base64
from PIL import Image
import io
from flask import Flask,render_template,request


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filemode='w', filename='logger.log')

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        img_file = request.files['image']
        img = Image.open(io.BytesIO(img_file.read()))
        logger.info(img, img_file)
        result = True
    return render_template('index.html', result=result)



if __name__ == "__main__":
    app.run(debug=True)
