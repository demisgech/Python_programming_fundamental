list1 = [1,2,3]
list2 = [10,20,30]

# (1,10),(2,20),(3,30)
zipped_list = zip(list1,list2)
for zip_item in zipped_list:
    print(zip_item)