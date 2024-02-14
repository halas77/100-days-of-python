from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678qwertyu'


@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Length(min=6, message=(u'Little short for an email address?')), validators.Email(message=(u'That\'s not a valid email address.'))])
    password = PasswordField('Password', [validators.Length(min=6, message=(u' short password'))])
    submit = SubmitField('Submit')
    

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':    
            return render_template('index.html', email = login_form.email.data)
        
        return 'Wrong Email or Password'
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
    


    
    
    

    
    
