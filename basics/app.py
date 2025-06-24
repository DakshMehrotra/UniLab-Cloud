from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lab_ready = False

@app.route("/", methods=["GET", "POST"])
def index():
    global lab_ready
    if request.method == "POST":
        if request.form.get("launch_lab"):
            lab_ready = True
        if request.form.get("logout"):
            lab_ready = False
        return redirect(url_for("index"))
    return render_template("index.html", lab_ready=lab_ready)

if __name__ == "__main__":
    app.run(debug=True)
