from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(0, 10)
    curr_date = datetime.datetime.now().year
    return render_template('index.html', num=random_num, year=curr_date)


@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age_data = age_response.json()['age']
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    gender_data = gender_response.json()['gender']
    return render_template('guess.html',name=name, age=age_data, gender=gender_data)


@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/c82ac18eba0a99fa145f')
    blog_data = response.json()
    return render_template('blog.html', items= blog_data)

if __name__ == "__main__":
    app.run(debug=True)


