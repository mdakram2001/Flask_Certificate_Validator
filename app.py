from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')


@app.route('/validator',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        lst=[i for i in range(1000,10000)]        
        num1 = request.form['num1']
        num1 = int(num1)     
        if num1 in lst:
            r = num1
            result = "Your Certificate is Valid!"
        else:
            result = "Invalid or Expired Certificate!"
        return render_template('results.html' , result = result)


@app.route('/postman_data',methods=['POST'])
def math_ops_by_post():
    if(request.method == 'POST'):
        lst=[i for i in range(1000,10000)]        
        num1 = request.json['num1']
        num2 = int(num1)     
        if num2 in lst:
            r = num2
            result = "Your Certificate is Valid!"
        else:
            result = "Invalid or Expired Certificate!"
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")