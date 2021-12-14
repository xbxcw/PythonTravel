import os
import sys

# print(sys.path)
pa = os.walk('.')
print([i for i in pa])
