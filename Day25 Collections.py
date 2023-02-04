####collections #########

from collections import Counter
a = "aaaabbbccccdddddeeeeeeeeefff"
my_counter = Counter(a)
print(my_counter)
print("Values in counter: ",my_counter.values())
print("Keys in counter: ",my_counter.keys())

from collections import Counter
a = ["a","a","b","b","c","c","f","f"]
my_counter = Counter(a)
print(my_counter)
print("Values in counter: ",my_counter.values())
print("Keys in counter: ",my_counter.keys())

####namedtuple############

from collections import namedtuple
Point=namedtuple('Point','x,y')
point_one = Point(18,4)
print("Point is: ",point_one)
print("Values of x and y are: ",point_one.x,point_one.y)


##########OrderedDict###########
from collections import OrderedDict
ordered_dict=OrderedDict()
ordered_dict['a']=100
ordered_dict['b']=200
ordered_dict['c']=300
ordered_dict['d']=400
ordered_dict['e']=500
ordered_dict['f']=600
ordered_dict['g']=700
print(ordered_dict)

###########defaultdict################
from collections import defaultdict

d= defaultdict(int)
d['a']=1
d['b']=2
print(d)
print(d['d'])

def default_value():
    return 100

d= defaultdict(default_value)
d['a']=1
d['b']=2
print(d)
print(d['d'])

########deque#####################

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.popleft()
print(d)




























