from flask import Flask
app = Flask(__name__)
print(123)
@app.route('/')
def hello_world():
    return 'Hello, Docker!'