"""
A pointless virtual machine

"""

from library import *
from variables import *

def do_nothing():
    pass

print_message(replace_words_with_spam(POWER))

number = 19920829
print(number, multiply_number_by_one(number))

for item in MENU:
    print_message(censor_words(item))
