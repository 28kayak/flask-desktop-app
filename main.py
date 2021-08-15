from flask import Flask, url_for, redirect, request
from flask import render_template
from flaskwebgui import FlaskUI
from flask_bootstrap import Bootstrap
import file_handler as handler

app = Flask(__name__)
#Bootstrap(app)
app.config['UPLOAD_EXTENSIONS'] = ['.csv']
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
        file_loc = 'uploaded_files/' + upload_file.filename
        upload_file.save(file_loc)
        data = handler.calculate(file_loc)
    #return redirect(url_for('index',data))
    return render_template('index.html', data=[data, "hello kaya" ])

if __name__ == "__main__":
    #app.run()
    #app.run(debug=True)
    ui.run()
    #delete a file after calulation 
    