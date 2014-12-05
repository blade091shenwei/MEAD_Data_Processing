s = 'Martin....so now were down to regulating the shape of cakes? And I\'m an ignoramus?!'

import re

m = re.split('\! |\? |\. ', s)

print m
for sentence in m:
    if cmp(sentence,'') == 0:
        pass
    else:
        print sentence

