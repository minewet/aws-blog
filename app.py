import os
from flask import Flask, render_template, request, redirect, send_file
from s3_functions import upload_post, get_items, delete_post
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "1971036-blogbucket"
TABLE = "blogTable"

@app.route("/")
def home():
    dates, titles, urls, texts = get_items(TABLE)
    return render_template('index.html', contents=zip(dates, titles, urls, texts))

@app.route("/post")
def post():
    return render_template('upload.html')

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        tt = request.form['title']
        t = request.form['text']

        if f:
            f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
            upload_post(f"uploads/{f.filename}", tt, t, BUCKET, TABLE)
        else:
            upload_post(None, tt, t, BUCKET, TABLE)
        return redirect("/")

@app.route("/delete", methods=['POST'])
def delete():
    if request.method == "POST":
        for key in request.form.getlist('deletecheck'):
            delete_post(key, BUCKET, TABLE)
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
