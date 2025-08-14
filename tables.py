list1 = [2,3,5]
list2 = [7]
end_no=int(input('Enter the end no.:'))
result = []

if 0 in list1 or 1 in list1 or 0 in list2 or 1 in list2 or list1 == list2:
    print('Input Error:List in 0,1 and same input')
else:
    for i in range(1,end_no+1):
        if all(i % num == 0 for num in list1):
            if all(i % num != 0 for num in list2):
                result.append(i)
    print(result)