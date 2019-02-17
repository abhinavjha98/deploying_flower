from flask import Flask,request,render_template
app = Flask(__name__)

from inference import get_flower_name
from commons import get_tensor

@app.route("/", methods=['GET','POST'])
def hello():
	if request.method =='GET':
		return render_template("index.html")
	if request.method =='POST':
		if 'file' not in request.files:
			print("file not uploaded")
			return
		file = request.files['file']
		image = file.read()
		get_flower_name(image_bytes=image)
		return render_template('result.html',flower = 'lily')
    
    	
if __name__ == '__main__':
	app.run(debug=True)    

