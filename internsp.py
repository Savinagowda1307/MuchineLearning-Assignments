
##List
myList=['a','b',1,2,'c','d',10]
print((myList))
print(len(myList))
print(type(myList))
print(myList[3])
myList[3]=5
print(myList[3])
print(myList[0:2])
myList.append('g')
print(myList)
myList.insert(1,10)
print(myList)
myList.remove('g')
print(myList)
myList.pop(0)
print(myList)

for i in myList:
    print(i)




##Tuple
    
myTuple=('a','b',1,2,'c','d',10)
print((myTuple))
print(len(myTuple))
print(type(myTuple))
print(myTuple[-1])
print(myTuple[2:5])
for p in myTuple:
    print(p)


##Set
    
mySet={'a','b',1,2,'c','d',10}
print((mySet))
print(len(mySet))
print(type(mySet))


mySet.add('name')
print(mySet)

mySet.remove('name')
print(mySet)
mySet.discard('d')
print(mySet)
mySet.pop()
print(mySet)

for s in mySet:
    print(s)




##Dictionary

myDict={'name':'Savina' ,'age':21, 'number':85}
print(myDict)
print(type(myDict))
print(len(myDict))
print(myDict['name'])
myDict['name']='Savi'
print(myDict)
x=myDict.keys()
print(x)
myDict['clg']='Pesitm'
print(myDict)
myDict.pop('clg')
print(myDict)


for m in myDict.values():
  print(m)

for n in myDict.keys():
  print(n)

for a, b in myDict.items():
  print(a, b)


