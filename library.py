
def print_message(message):
    print(message)

def replace_words_with_spam(message):
    newmessage = ' '.join(['SPAM' for i in message.split()])
    return newmessage
