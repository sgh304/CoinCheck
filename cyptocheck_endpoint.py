#HANDLER

def lambda_handler(event, context):
    print('event.session.application.applicationId=' +
          event['session']['application']['applicationId'])

    # if (event['session']['application']['applicationId'] !=
    #         'amzn1.echo-sdk-ams.app.[unique-value-here]'):
    #     raise ValueError('Invalid Application ID')

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == 'LaunchRequest':
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == 'IntentRequest':
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == 'SessionEndedRequest':
        return on_session_ended(event['request'], event['session'])

#EVENTS

#Called when a session starts
def on_session_started(request, session):
    print('on_session_started requestId=' + request['requestId']
          + ', sessionId=' + session['sessionId'])

#Called when launched without intent
def on_launch(request, session):
    print('on_launch requestId=' + request['requestId'] +
          ', sessionId=' + session['sessionId'])

#Called when user clarifies an intent
def on_intent(request, session):
    print('on_intent requestId=' + request['requestId'] +
          ', sessionId=' + session['sessionId'])

    intent = request['intent']
    intent_name = request['intent']['name']

    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_message()
    elif intent_name == "CheckPrice":
        return check_price(intent)

#Called when a session ends
def on_session_ended(request, session):
    print('on_session_ended requestId=' + request['requestId'] +
          ', sessionId=' + session['sessionId'])

#BEHAVIOR

#Welcome/help
def get_welcome_message():
    pass

#RESPONSE BUILDER

def build_response(session_attributes, title, output, reprompt_text, should_end_session):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': 'Simple',
                'title': "SessionSpeechlet - " + title,
                'content': "SessionSpeechlet - " + output
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': reprompt_text
                }
            },
            'shouldEndSession': should_end_session
        }
    }
