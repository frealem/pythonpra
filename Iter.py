#creating custom iteration 
class Pow_of_Two:
    '''class to implement an iteration of '''
    def __init__(self,max=0):
        self.max=max
        
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2 ** self.n  
            self.n += 1
            return result
        else:
            raise StopIteration  
        
print(Pow_of_Two.__doc__)
a=Pow_of_Two(5)
i=iter(a)
print(next(i))
print(next(i))
print(next(i)) 
print(next(i))        

for i in range(6,11):
    print (i)