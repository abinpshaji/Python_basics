my_dict={"name":"ebin","age":27,56:12,"hobbies":["cycling","coding",34,12]}

my_dict.update({"name":"aswin"})
print(my_dict)

print(my_dict.pop("age"))
print(my_dict)
print(my_dict.popitem())
print(my_dict)

my_dict[7]="laptop"
print(my_dict)
print(my_dict[7])
print(my_dict.get(89,False))