import json
from flask import jsonify
from util.triggers import *

def _identifyRequest(form_json):
    if message['type'] == "dialog_submission":
        if json.loads(message['callback_id'])['action'] == 'match_details':
            return "match_details"
    if message['actions'] and message['actions'][0]:
        if json.loads(message['actions'][0]['action_id'])['action'] == 'cricket_match_selection':
            return "cricket_match_selection"
        if json.loads(message['actions'][0]['action_id'])['action'] == 'football_match_selection':
            return "football_match_selection"
    return None


def routeRequest(form_json):
    requestType = _identifyRequest(form_json)
    if requestType == None:
        return jsonify(success=False)
    if requestType == 'match_details':
        matchDetailsFlow(form_json)
        return ('', 200)
    if requestType == 'football_match_selection':
        cricketFlow(form_json)
    if requestType == 'cricket_match_selection':
        footballFlow(form_json)
    return jsonify(success=True)