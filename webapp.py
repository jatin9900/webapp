from flask import Flask, render_template

helloworld = Flask(__name__)

@helloworld.route("/<code>")
def error(code):
    if code=='404':
        return '404'

    if code=='403':
        return '403'

    if code=='500':
        return '500'

    if code=='502':
        return '502'


if __name__=="__main__":
    helloworld.run(host="0.0.0.0",port=int("5000"),debug="True")
