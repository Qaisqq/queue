class Queue:
    def __init__(self):
        self.queList = []
        self.size = 0
        
    def en_queue(self, data):
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
        self.queList.append(data)

    def de_queue(self):
        x =  self.queList.pop(0)
        return x

