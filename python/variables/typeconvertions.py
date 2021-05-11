# data types
# data types are---> intiger, string, float
# intiger=1,2,3
# string="mitya"
# float=2.0, 3.5 5.1

# there are 2 types of convertions
# 1. implicit
# 2, explicit

#1,implicit
a = 10
b = 34
print(a+b)
# output will be 44,
# --------------------------------------
# convirtions of
# convert intiger to string ---> str(int)
# convert float to string ----> str(float)
# convert string to intiger ---> int(str)

a = 10
print(type(a))
# a is intiger
print(type(str(a)))
# it will be str. because we are converting int into str :str(a)
b = "mitya"
print(str(a)+b)

a = 10
b = "20"
print(str(a)+b)
# output is 1020 because a in converting in to str.

print(a+int(b))
print(type(int)(b))
#output will be 30 because b string converting in to int

a = 44
print(a)
print(type(a))
print(float(a))
# int is converting in to float



