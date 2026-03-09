import random
from datetime import datetime


random.seed(datetime.now().timestamp())

for i in range(5):
    print(random.randint(0, 10), end="\t")
