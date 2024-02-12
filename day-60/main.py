from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        return f'Name:{name} Password:{password}'
    
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
