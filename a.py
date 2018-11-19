from flask import Flask,jsonify,request,render_template
from validate_email import validate_email
import datetime 

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def login():
	return render_template('login.html',msg = "")


@app.route('/login',methods=['POST','GET'])
def login1():
	a = request.form
	if(a['uname']=='vipin' and a['pass']=='password'):
		return render_template('a.html',msg="")
	else:
		print('qwerty')
		return render_template('login.html',msg = 'enter agin')




@app.route('/listbook',methods = ['POST','GET'])
def listbook():
	transaction = True
	if request.method == 'POST':
		user = request.form
		if(len(user['name'])<=2):
			transaction = False
			print('name')
		if(len(user['author'])<=2):
			transaction = False
			print('author')

		if(len(str(user['bookid'])) != 5):
			transaction = False
			print('bookid')

		if(len(str(user['section']))<=1):
			transaction = False
			print('section')

		if(valid_date(user['date'])):
			transaction = False
			print('date')

		if (transaction == False):
			return render_template('a.html',msg="Please enter correct details")
		return "success"


def valid_date(s):
	try :
		formats = '%Y-%m-%d'
		print(s)
		s = datetime.datetime.strptime(s,formats)
		return False
	except ValueError:
		print("Ooooooo")
		return True



if __name__ == '__main__':
	app.run(port = 10,debug = True)
