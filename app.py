from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        return f'First Name: {first_name}<br>Last Name: {last_name}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
