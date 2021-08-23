from datetime import datetime
from uuid import uuid4

from werkzeug.wrappers import request

from articles_app.db.connector import ENGINE
from articles_app.db.models import Article


def add_articles(article: str, price: int):
    with ENGINE.scoped_session() as session:
        new_article = Article(name=article, price=price)
        session.add(new_article)
        session.commit()
        return {"id": new_article.id, "item": new_article.name, "price": new_article.price}


def get_articles():
    with ENGINE.scoped_session() as session:
        db_article = session.query(Article).all()
        return [{"id": row.id, "item": row.name, "price": row.price, "quantity": row.quantity} for row in db_article]


def get_articles_by_id(article_id: str):
    with ENGINE.scoped_session() as session:
        db_article = session.query(Article).filter(
            Article.id == article_id).one_or_none()
        if db_article is None:
            return {"error": "articles not found", "article_id": article_id}
        return {"id": db_article.id, "item": db_article.name, "price": db_article.price, "quantity": db_article.quantity}


def modify_articles(article_id: str, article_content: str, article_price):
    with ENGINE.scoped_session() as session:
        db_article = session.query(Article).filter(
            Article.id == article_id).one_or_none()
        if db_article is None:
            return {"error": "articles not found", "article_id": article_id}
        db_article.name = article_content
        db_article.price = article_price
        session.commit()
        return {"id": db_article.id, "articles": db_article.name}


def put_articles(article_id, article_quantity: int):
    with ENGINE.scoped_session() as session:
        db_article = session.query(Article).filter(
            Article.id == article_id).one_or_none()
        if db_article is None:
            return {"error": "articles not found", "article_id": article_id}
        db_article.quantity += article_quantity
        session.commit()
        return {"quantity": db_article.quantity}


def buy_articles(article_id, client_money: int, article_quantity: int):
    with ENGINE.scoped_session() as session:
        db_article = session.query(Article).filter(
            Article.id == article_id).one_or_none()
        if db_article is None:
            return {"error": "articles not found", "article_id": article_id}
        if article_quantity < 0:
            return {"error": "your money is not acceptable"}
        if client_money < db_article.price * article_quantity:
            return {"error": "you don't have enough money to buy this article"}
        if db_article.quantity < article_quantity or db_article.quantity == 0 or db_article.quantity < 0:
            return {"error": " This article is no more in stock"}
        db_article.quantity -= article_quantity
        session.commit()
        remaining = client_money - (db_article.price * article_quantity)
        return {"your_money": client_money, "article_id": article_id, "remaining_money": remaining, "quantity": db_article.quantity}


def delete_articles(article_id):
    with ENGINE.scoped_session() as session:
        db_article = session.query(Article).filter(
            Article.id == article_id).one_or_none()
        if db_article is None:
            return {"error": "articles not found", "article_id": article_id}
        session.delete(db_article)
        session.commit()


def clear_articles():
    with ENGINE.scoped_session() as session:
        db_article = session.query(Article).delete()
        session.commit()
        return (f"Table deleted {db_article}")
