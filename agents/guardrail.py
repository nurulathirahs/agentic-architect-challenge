def check_response(reply):
    banned_words = [
        "password",
        "secret",
        "api key"
    ]

    for word in banned_words:
        if word in reply.lower():
            return "Response blocked: sensitive information detected"

    return reply