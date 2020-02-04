"""
A pointless virtual machine

"""

from library import *
from variables import *

print_message(replace_words_with_spam(POWER))

for item in MENU:
    print_message(censor_words(item))
