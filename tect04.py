#-------------------List คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ อีกทั้งแก้ไขได้ด้วย------------------------------
        #   0   1   2   3   4   5   
my_list1 = [10,20,True,10,'SAU', [20, 'IOT']]
        #   6   5   4   3   2           1   คิด-

#การเข้าถึงข้อมูลในlist เพื่อเอาข้อมูลมาใช้ หรือแก้ไขคำข้อมูลให้มันใหม่
#เข้าถึงแต่ละข้อมูล
print(my_list1[4]) # SAU
print(my_list1[-2])# SAU
print(my_list1[5])# [20, 'IOt]
print(my_list1[-1])#[20, 'Iot]
print(my_list1[5][1]  ) # IOt
print(my_list1[-1][-1] ) # IOt


#เข้าถึงทีละข้อมูล
print(my_list1[1:4]) #20, True, 10
print(my_list1[3:]) #10 ,'SAU', [20,'IOt']
print(my_list1[:3]) #10, 20, True

# เข้าถึงทุกข้อมูล
for info in my_list1 :
    print(info, end=',')

print()

print(my_list1)