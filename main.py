from flask import Flask, url_for, redirect, request
from flask import render_template
from flaskwebgui import FlaskUI
from flask_bootstrap import Bootstrap

app = Flask(__name__)
#Bootstrap(app)
#app.config['UPLOAD_EXTENSIONS'] = ['.csv']
ui = FlaskUI(app, width=800, height=600)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def upload_files():
    print("in upload_files")
    print(request)
    upload_file = request.files['file']
    print(upload_file)
    if upload_file.filename != '':
        print(upload_file.filename)
        upload_file.save('uploaded_files/' + upload_file.filename)
    return redirect(url_for('index'))


if __name__ == "__main__":
    #app.run()
    app.run(debug=True)
    #ui.run()
    #delete a file after calulation 
    