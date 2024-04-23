def mutiple (x,y):
    print (x*y)
a=mutiple(4,5)
print(a)

def check_numders(x,y):
    if x+y<100:
        return "100 kishi"
    else:
        return "100 den ulken "
print(check_numders(50,51))    

def find_max(list1):
    return max(list1)
a = find_max([1, 2, 3, 4, 5])
print(a)