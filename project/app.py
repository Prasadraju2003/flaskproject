from flask import Flask,render_template,request,send_file
import pyqrcode
import png
from pyqrcode import QRCode
  

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",methods =["POST"] )
def result():
    s  = request.form.get("text")
    url = pyqrcode.create(s)
    url.png('static/images/qr.png', scale = 6)
    return render_template("qr.html")
@app.route('/download')
def download_qr():
    path = 'static/images/qr.png'
    return send_file(path,mimetype='image/png',as_attachment=True)
if __name__ == "__main__":
        app.run(debug = True)