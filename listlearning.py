users = ['mckinsey', 'kpmg', 'goldman']
data =  ['mckinsey', 2, True]
emptylist = [ ]

print("mckinsey" in emptylist)

print(users[0])
print(users[-2])

print(users.index('goldman'))
print(users[0:])
print(len(data))

users.append('bcg')
print(users)

users+= ['bainco']
print(users)

users.extend(['sequioa', 'blackrock'])
print(users)

users.insert(0, 'EY')
print(users)

users[1:3] = ['jpmorgan', 'lvmh'] #replacing values in the list
print(users)

users.remove('lvmh')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

data.clear()
print(data)

users.sort(key=str.upper)
users[1:2] = ['BLACK']
print(users)

users.sort(key=str.lower)
print(users)

str.upper()
print(users)


#users(key = str.upper)
#print(users)

nums=[1,4,5,4,7]
nums.reverse()
print(nums)

print(sorted(nums, reverse=True))
print(nums)

str.upper()
print(users)