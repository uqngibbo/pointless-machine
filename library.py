from re import sub

def print_message(message):
    print(message)

def replace_words_with_spam(message):
    newmessage = ' '.join(['SPAM' for i in message.split()])
    return newmessage

def add_zero_to_number(number):
    newnumber = number + 0
    return newnumber

def multiply_number_by_one(number):
    newnumber = number*1
    return newnumber

def censor_words(message):
    newmessage = ' '.join([sub("[a-zA-Z]+", "#", m) for m in message.split()])
    return newmessage
