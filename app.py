import redis
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def Home(name=None):
    return render_template('base.html')


# debug mode running on 5050 port
if __name__=="__main__":
    app.run(host="localhost", debug=True, port=5050)