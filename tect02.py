#character in string has index number
    #01234567890123
infoA = 'Hello sau 2023'
    #43240987654321

print( infoA[6])
print( infoA[-8])

#เข้าถึงตังอักษรหลายๆ ตัวใน string เราจะใช้ string ด้วย index number
#sau
print( infoA[6:9])
print( infoA[-8:-5])

#o sau 20
print( infoA[4:20])

# String Method 
print( infoA.upper() )
print(infoA.lower())
print(infoA.capitalize())
print(infoA.count() )
print(infoA.isdigit() )
print(infoA.islower() )
infoB = infoA.replace('SAU' , 'IoT')
print(infoA)
print(infoB)
print(infoB.replace('Hello', "Hi..."))

#string string
print( len(infoA))

print('SAU' ,35) #SAU 35
print('SAU'+str(35)) #SAU35
print('SAU',35,sep='') #SAU35
print('20','02','2023',sep='/')
print(20,'มกราคม',2023,sep='-')