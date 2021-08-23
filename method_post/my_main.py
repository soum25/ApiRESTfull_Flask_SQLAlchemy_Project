from flask import (
    Flask,
    render_template,
    request,
    make_response,
    render_template_string,
    url_for,
    redirect,
)

app = Flask(__name__, static_url_path="/static")


@app.route("/formulaire")
def get_form():
    return render_template("formulaire.html")


@app.route("/submit_list", methods=["POST"])
def handle_form():
    if not request.cookies.get("stock_data"):
        new_content = request.form["notes"]
        resp = make_response(redirect(url_for("get_form")))
        resp.set_cookie("stock_data", new_content)
        return resp
    else:
        new_content = request.form["notes"]
        resp = make_response(redirect(url_for("get_form")))
        old_cookies = request.cookies.get("stock_data")
        old_cookies = old_cookies.split(",")
        new_cookies = request.form["notes"]
        new_cookies = new_cookies.split(",")
        old_cookies = old_cookies + new_cookies
        old_cookies = ",".join(old_cookies)
        resp.set_cookie("stock_data", old_cookies)
        return resp


@app.route("/afficher")
def re_notes():
    my_notes = request.cookies.get("stock_data")
    my_notes = my_notes.split(",")
    return render_template("data.html", data=my_notes)


@app.route("/supprimer")
def suppresiondesnotes():
    content = " <h1> All the Notes have been delected </h1>"
    resp = make_response(content)
    resp.set_cookie("stock_data", expires=0)
    return resp


if __name__ == "__main__":
    app.run()
