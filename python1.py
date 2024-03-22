# for i in range(1,10):
#     if (i==4):
#         continue
#     print(i)

primes=[2,3,4,5.6,55,'r']

print(primes[3:])   #from index 3 to...
print(primes[:2])    #from 0 to index 2
print(primes[2:4])       #from 2 to 4
primes[5]="modification"
print(primes)    #to modify the index=5

primes.append("appended")
primes.extend(['ex1','ex2'])
primes.insert(3,"i'm inserted")
print(primes)