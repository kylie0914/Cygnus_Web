from flask import Flask, render_template, request, redirect, url_for
import os

ip = "0.0.0.0"
port = 5000

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/analysis")
def analysis():
    image = request.args.get('image', 'img/Cygnus_free_copyright.jpg')
    return render_template("analysis.html", image=image)

@app.route("/data_load", methods=["GET", "POST"])
def data_load():
    uploaded_file_url = None
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            uploaded_file_url = url_for('static', filename='uploads/' + file.filename)
    return render_template("data_load.html", uploaded_file_url= uploaded_file_url)

if __name__ == '__main__':
    app.run(host=ip, port=port)
