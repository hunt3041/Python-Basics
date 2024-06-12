class SuperList(list):
    def __len__(self):
        return 1000
    
my_list = SuperList([1,2,3,5,6])
my_list.append(12)
print(my_list)

print(my_list[5])
print(len(my_list))