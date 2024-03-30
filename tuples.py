#tuples 
# country=("us","et","ng","mon")

# if "us" in country:
#     print("i am usian")
# else:
#     print("i''m not usian")
    
    
    #=============ranging of index of tuple=======
    
values=(10,20,30,40,50,60,70,80,90,100)

# values[start,end,jumpIndex] by default the jump index is 1
print(values[0:8])                #(10, 20, 30, 40, 50, 60, 70, 80)
print(values[0:8:2])              #(10, 30, 50, 70)
print(values[0:])                     #from index 0 to the end the blank default end
