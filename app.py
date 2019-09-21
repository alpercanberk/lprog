from flask import Flask, redirect, render_template, request, jsonify, url_for, Response, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['FLASK_DEBUG'] = 1
    app.run()
