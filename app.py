from flask import Flask,render_template,request


app = Flask(__name__)


@app.route('/')

def registration_form():

    return render_template('register.html')



@app.route('/submit',methods=['POST'])


def submit():



   name = request.form['name']

   email = request.form['email']
    
     return f"Registration successful for {name} with email {email}"



if__name__=='__main__':
   
    app.run(host='0.0.0.0',port=5000)