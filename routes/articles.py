from flask import Blueprint, request

import articles_app.services.articles as articles_service

articles_router = Blueprint("articles", __name__)


@articles_router.route("/articles", methods=["POST"])
def add_articles():
    return articles_service.add_articles(request.json["name"], request.json["price"])


@articles_router.route("/articles", methods=["GET"])
def get_articles():
    return {"articles": articles_service.get_articles()}


@articles_router.route("/articles/<articles_id>", methods=["GET"])
def get_articles_by_id(articles_id):
    return articles_service.get_articles_by_id(articles_id)


@articles_router.route("/articles/<articles_id>", methods=["PATCH"])
def modify_articles(articles_id):
    return articles_service.modify_articles(articles_id, request.json["name"])


@articles_router.route("/articles/<articles_id>", methods=["PUT"])
def put_articles(articles_id):
    return articles_service.put_articles(articles_id, request.json["quantity"])


@articles_router.route("/articles/buy/<articles_id>", methods=["POST"])
def buy_articles(articles_id):
    return articles_service.buy_articles(articles_id, request.json["your_money"], request.json["quantity"])


@articles_router.route("/articles/<articles_id>", methods=["DELETE"])
def delete_articles(articles_id):
    articles_service.delete_articles(articles_id)
    return "", 204


@articles_router.route("/articles/clear", methods=["DELETE"])
def clear_articles():
    articles_service.clear_articles()
    return "all the articles have been deleted"
