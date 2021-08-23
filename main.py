from flask import Flask
from flask_cors import CORS
from articles_app.api.routes.articles import articles_router

app = Flask(__name__)
CORS(app)
app.register_blueprint(articles_router)

app.run()
