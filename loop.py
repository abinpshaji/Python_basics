my_list=[45,23,4,10,5,66,2]

for k in my_list:
    #print(k)
    print(k,end=" ")

print("")

for n in {45,23,5,2}:
    print(n,end="")

print("Interating over Dictionary")
v={"name":"ebin","age":27,2:45}
print(v.items())
for k,val in v.items():
    print(k,val)

print("")

my_list=[45,23,4,10,5,66,2]
print(enumerate(my_list))
for c,k in enumerate(my_list):
    print(c,k)