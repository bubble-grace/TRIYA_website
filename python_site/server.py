from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/sailors')
def sailors():
    return render_template("sailors.html")


@app.route('/programs', methods=["GET", "POST"])
def programs():
    if request.method == "GET":
        return render_template("programs.html")
    elif request.method == "POST":
        f = request.form
        print(f)
        return render_template("completion.html", results=f)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
