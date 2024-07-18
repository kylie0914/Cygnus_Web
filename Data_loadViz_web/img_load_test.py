# PATH: C:\Users\momoc\OneDrive\바탕 화면\MGH\PJT\VR_web\img_load_test.py
from flask import Flask, render_template

ip = "0.0.0.0" # "127.0.0.1"
port = 5000

app = Flask(__name__)
 
# @app.route("/")
# def main():
#     return render_template("img_with_title.html")  #  connect 'html' file using render template

@app.route("/")
def main():
    return render_template("img_with_button.html")  #  connect 'html' file using render template

if __name__ == '__main__':
    app.run(host=ip, port=port)