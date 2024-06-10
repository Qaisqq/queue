class Queue:
    def __init__(self):
        self.queList = []
        self.size = 0
        
    def en_queue(self, data):
        self.queList.append(data)
        self.size +=1

    def de_queue(self):
        x =  self.queList.pop(0)
        self.size -=1
        return x

    def is_empty(self):
        return self.size == 0

    def calc_size(self):
        count = 0
        for _ in self.queList:
            count += 1
        return count

    def peek(self):
        if self.size == 0:
            raise IndexError
        return self.queList[0]



## I tried making the append method from scatch, but i couldnt figure it out
# if self.queList[0] == None:
#     self.queList[0] = data
#     self.size +=1
# else:
#     counter = self.size
#     while counter != 0:
#         self.queList[counter+1] = self.queList[counter]
#         counter -=1
#     self.queList[0] = data
#     self.size +=1