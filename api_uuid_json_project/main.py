from datetime import datetime
from uuid import uuid4

from flask import Flask, jsonify, request

app = Flask(__name__)

DB = {}


@app.route("/notes", methods=["POST"])
def add_note():
    note = request.json["note"]
    uuid = str(uuid4())
    DB[uuid] = {"id": uuid, "note": note, "time": datetime.now().isoformat()}
    return DB[uuid]


@app.route("/notes", methods=["GET"])
def get_notes():
    return {"notes": list(DB.values())}


@app.route("/notes/<note_id>", methods=["GET"])
def get_note_by_id(note_id):
    if note_id not in DB:
        return {"error": "Note does not exists", "note_id": note_id}
    return DB[note_id]


@app.route("/notes/<note_id>", methods=["PATCH"])
def modify_note(note_id):
    if note_id not in DB:
        return {"error": "Note does not exists", "note_id": note_id}
    current_note = DB[note_id]
    current_note.update(
        note=request.json["note"], time=datetime.now().isoformat())
    return current_note


@app.route("/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    if note_id not in DB:
        return {"error": "Note does not exists", "note_id": note_id}
    DB.pop(note_id)
    return "", 204


app.run()
