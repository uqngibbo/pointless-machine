"""
A pointless virtual machine

"""

from library import print_message, replace_words_with_spam
from variables import HELLO

print_message(replace_words_with_spam(HELLO))
