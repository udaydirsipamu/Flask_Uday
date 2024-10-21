from flask import Flask, render_template, request
import re
app=Flask(__name__)

database=['u@gmail.com','t@gmail.com','s@gmail.com','v@gmail.com']
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/index-form')
def index_form():
    return render_template('index_form.html')


@app.route('/results',methods=['POST'])
def results():
    test_string=request.form['test_string']
    regex = request.form['regex']
    matches = re.findall(regex, test_string)
    return render_template('index_result.html',test_string=test_string, regex=regex, matches=matches)

@app.route('/email-validation')
def email_validation():
        return render_template('email_validation.html')

@app.route('/validate-email',methods=['POST'])
def validate_email():
    email=request.form['email']
    regex=r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex,email):
        if email in database:
            result=f"<strong>{email}</strong> is a valid email address."
        else:
            result=f" <strong>{email}</strong> is not registerd with us.Kindly register and come back."
    else:
        result=f"'{email}' is not a valid email address."
    return render_template('email_result.html',email=email,result=result)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)