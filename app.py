from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form['url']
    color = request.form['color']

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color="white")

    img_path = "temp_qr.png"
    img.save(img_path)

    return send_file(img_path, as_attachment=True, download_name='qr_code.png')

if __name__ == '__main__':
    app.run(debug=True)
