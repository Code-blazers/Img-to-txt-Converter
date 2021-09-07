from flask import*

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

# to run the application
# export FLASK_APP=web.py
# flask run


if __name__ == "__main__":
    app.run(debug=True)
