import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]) :
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo', 'hai', 'haai'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('It sounds like you have had a long day!', ['i', 'i am', 'feel', 'bad'], required_words=['i', 'feel', 'bad'])
    response('It sounds like you have had a tired day!', ['i', 'i am', 'very', 'tired'], required_words=['i', 'tired'])
    response('Thank You!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank You!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('That sounds wonderful!', ['today', 'is', 'a', 'nice', 'day'], required_words=['day', 'nice'])

    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_DRINKING, ['what', 'you', 'drink'], required_words=['you', 'drink'])
    response(long.R_SICK, ['i', 'am', 'sick'], required_words=['i', 'sick'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

    return best_match


def get_response(user_input):
    spilt_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(spilt_message)
    return response


while True:
    print('Bot: ' + get_response(input('You: ')))
