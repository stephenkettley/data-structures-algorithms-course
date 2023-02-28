# basic arrays

new_list = [1, "hello", 3]
result = new_list[1]

if 1 in new_list:
    print(True)

for i in new_list:
    if i == 1:
        print(True)
        break

new_list.append(4)
new_list.insert(2, 12)
new_list.remove(3)
