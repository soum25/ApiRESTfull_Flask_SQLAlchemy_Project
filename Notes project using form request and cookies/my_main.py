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


@app.route("/")
def home_page():
    content = """
    <h1> Bienvenue dans votre bloc note.</h1> 
    <h2> Veuillez suivre les instructions suivantes </h2> 
    <ul>
      <li> To save your list content, write in the url: <b> "localhost/5000/sauver/ your notes (for instance:sport voyager danser)"</b>  </li>
      <li> To display all your list elements , write in the url: <b> "localhost/5000/afficher" </b> </li>
      <li> To delete all the content of your list, write in the url:<b> "localhost/5000/supprimer" </b></li>
    </ul>
    <img src=static/image0.gif>
    """
    return content


@app.route("/sauver/<notes>")
def bloc_notes(notes):
    content = """
    <h1> Sauvegarde des données</h1>
    <h2> If you want to see them , follow this link 👉🏼 <b> "localhost/5000/afficher" </b> <h2> 
    <a href="localhost/5000/afficher"></a>
    """
    resp = make_response(content)
    resp.set_cookie("stock_data", notes.strip())
    return resp


@app.route("/ajouter/<notes>")
def ajouter_notes(notes):
    content = """
    <h1> Notes rajouteées </h1>
    <h2> If you want to see them , follow this link 👉🏼 <b> "localhost/5000/afficher" </b> <h2> 
    <a href="localhost/5000/afficher"></a>
    """
    my_notes = request.cookies.get("stock_data")
    my_notes = my_notes.split(",")
    notes = notes.split(",")
    my_notes += notes
    my_notes = ",".join(my_notes)
    resp = make_response(content)
    resp.set_cookie("stock_data", my_notes.strip())
    return resp


@app.route("/afficher")
def get_notes():
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
