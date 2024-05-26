def cube(x):
    return x**3

l=[2,4,5,6,1]
newl=list((map(cube,l)))
print(newl)

def filter_function(self):
    return self>4

newnewl=list((filter(filter_function,l)))

print(newnewl)
