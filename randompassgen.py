"""
Random 16 character password generator.

Just getting started with Python + Github.
"""

import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16

password = "".join(random.sample(total, length))

print(password)
