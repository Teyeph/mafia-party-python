from flask import Flask, render_template
from forms import HomeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9kah283hdjialksuen8366d38maop'


@app.route("/")
def homepage():
    form = HomeForm()
    return render_template("home.html", form=form)


if __name__ == "__main__":
    app.run()
