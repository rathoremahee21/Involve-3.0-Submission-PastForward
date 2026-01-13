from data import options, historical_decision

def process_decision(user_choice):
    selected = options[user_choice]

    return {
        "short_term": selected["short_term"],
        "long_term": selected["long_term"],
        "lesson": selected["lesson"],
        "historical_match": user_choice == historical_decision,
        "result_type": user_choice   # used to style outcome panel
    }
