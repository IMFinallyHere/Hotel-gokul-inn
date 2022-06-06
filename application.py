from flask import Flask, render_template



application = Flask(__name__)


@application.route('/')
def home():
    return render_template('index.html')

@application.route('/nearby')
def nearby():
    return render_template('nearby.html')


if __name__=='__main__':
    application.run(host='0.0.0.0', port=5000)