import json
import random
import random
from datetime import datetime

# Data as a big dict
# dggs = {}
# sample_size = 1000

# random.seed(datetime.now())
# for n in range(1, sample_size):
#      dggs["N" + str(n)] =  random.randint(1, 255)

# j = json.dumps(dggs, indent = 2)
# f = open('dggs_sample_1.json', 'w')

# print >> f, j

# f.close()


# Data as set of dicts 
# dggs = {}
# sample_size = 1000
# f = open('dggs_sample_2.json', 'w')

# random.seed(datetime.now())
# for n in range(1, sample_size):
#      dggs["N" + str(n)] =  random.randint(1, 255)
#      j = json.dumps(dggs, indent = 2)
#      print >> f, j 
#      dggs = {}


# f.close()


# Data as a csv
sample_size = 255
f = open('dggs_sample_4.csv', 'w')
random.seed(datetime.now())

for n in range(1, sample_size):
     key = str(n)
     val =  random.randint(1, 1000)
     print >> f, "%s %s" % (key, val)

f.close()