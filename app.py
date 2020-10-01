from flask import Flask

app = Flask(__name__)
app.config(['SQL_ALCHEMY'])

@app.route('/')
def hello():
    return 'hello'

app.run(host='127.0.0.1', port=8080, debug=True)