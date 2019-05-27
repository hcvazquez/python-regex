'''
&& → and
|| → or
Both && and || should have a space " " on both sides.
'''

import re

#Squaring numbers
def square(match):
    if match.group() == '&&':
        return 'and'
    elif match.group() == '||':
        return 'or'

N = int(input())

for i in range(N): 
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", square, input()))
