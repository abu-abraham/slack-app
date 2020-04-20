import flask
import requests
from flask import request, make_response, Response, jsonify
import json
from util.router import routeRequest

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/cricket', methods=['POST'])
def cricketFlow():
    action_id = "cricket_match_selection"
    payload = generateMultiSelectOption("Matches you need to track", 
        action_id, "Matches", ["IND vs AUS", "AUS vs ENG"] )
    return jsonify(payload)

@app.route('/football', methods=['POST'])
def footballFlow():
    action_id = "football_match_selection"
    payload = generateMultiSelectOption("Matches you need to track", 
        action_id, "Matches", ["ENG vs HOL", "SPN vs FRC"] )
    return jsonify(payload)

@app.route('/sports', methods=['POST'])
def sportFlow():
    form_json = json.loads(request.form["payload"])
    return routeRequest(form_json)
    

app.run()

