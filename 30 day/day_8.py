n = int(raw_input())
dict = {}
for i in range(0, n):
    input = str(raw_input()).split(' ')
    name = input[0]
    phone = int(input[1])
    dict[name] = phone
for j in range(0, n):
    name = str(raw_input())
    if name in dict:
        phone = dict[name]
        print name + "=" + str(phone)
    else:
        print "Not found"