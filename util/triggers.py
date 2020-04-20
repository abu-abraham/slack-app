from util.slack import *

SLACK_BOT_TOKEN = 'XXXX'

def matchDetailsFlow():
    return ""

def cricketFlow(payload):
    selected_matches = {}
    for x in payload['actions'][0]['selected_options']:
        selected_matches[x['value']] = x['value']
    callback_id = {'action': 'match_selection'}
    dialog = generateDialogWithSelect(json.dumps(callback_id), json.dumps(callback_id), "Select the match you wannt", "Matches", selected_matches )
    api_data = {
        'token': SLACK_BOT_TOKEN,
        'trigger_id': payload['trigger_id'],
        'dialog': json.dumps(dialog)
    }
    api_url = 'https://slack.com/api/dialog.open'
    requests.post(api_url, data=api_data)

def footballFlow():
    return ""