"""
A pointless virtual machine

"""

from library import print_message, replace_words_with_spam, multiply_number_by_one
from variables import HELLO, POWER

print_message(replace_words_with_spam(POWER))

number = 19920829
print(number, multiply_number_by_one(number))
