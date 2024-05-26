def cube(x):
    return x**3
print(cube(2))

l=[5,4,7,8,9,2]
newl=[]

# for item in l:
#     newl.append(cube(item)) #Here for i in item we can use anything 
newl=list(map(cube,l))  #On upper hand we use for loop and for same thing we map function
print(newl)

