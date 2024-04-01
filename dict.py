# # this about dictionary
# dict={"x":30,"y":40,"z":50}
# print(dict)
# dict["z"]=60
# print(dict)

# # to access the value using key get()
# print(dict.get("x"))
# # another form of dict
dict2=dict([(1,"jave"),(2,"javawa"),(3,"javeye")])

print(dict2)

# if i want access javawa
print(dict2[2])
#  insertion
dict2[6]="pythonian"
print(dict2)
#deletion
dict2.pop(3)
print(dict2)