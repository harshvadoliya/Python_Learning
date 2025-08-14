print("EX 1")
n1=int(input("Enter the First no.:"))
n2=int(input("Enter the Second no.:"))

if n1*n2<=1000:
    print(n1*n2)
else:
    print(n1+n2)

print("EX 2")
s=int(input("Enter start no.:"))
e=int(input("Enter End no.:"))
previous_no= s-1

for i in range (s,e+1):
    x_sum = previous_no+i
    print("Current Number",i,"Previous Number",previous_no,"Sum:",x_sum)
    previous_no = i

print("EX 3")
w=input("Enter the String:")
size=list(w)
for i in size[0::2]:
    print(i)

print("EX 4")
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

print("EX 5")
l1=[10,20,30,40,10]

first_no=l1[0]
last_no=l1[-1]

if first_no == last_no:
    print("True")
else:
    print("False")

print("EX 6")

li=[10,12,15,20,36,100]
for i in li:
    if i % 5 == 0:
        print(i)

print("EX 7")

str_x="Emma is good developer. Emma is a writer"
cnt = str_x.count("Emma")
print(cnt)

