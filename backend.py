#from flask import Flask, render_template
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import fingers
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('abc.html')

#@app.route('/upload', methods = ['GET', 'POST'])
#def upload_file():
#   if request.method == 'POST':
#      f = request.files['file']
#      text=fingers.fingermain()
#      print (text)
#      #f.save(secure_filename(f.filename))
#      return text#file uploaded
@app.route('/new')
def run():
    text=fingers.fingermain()
    print (text)
   
   #f.save(secure_filename(f.filename))
    return text#file uploaded
	
	
if __name__ == '__main__':
    app.run(debug=True)
