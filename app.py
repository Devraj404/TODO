from flask import *
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return redirect(url_for('new_list'))
    return render_template("index.html")


@app.route("/createList", methods=["GET","POST"])
def new_list():
    return render_template("createList.html" )


if __name__ == "__main__":
    app.run(debug=True, port=8000)