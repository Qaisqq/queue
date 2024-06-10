class Queue:
    def __init__(self):
        self.que = []
        self.size = 0
        
    def en_queue(self, data):
        if self.que[0] == None:
            self.que[0] = data
            self.size +=1
        else:
            counter = self.size
            while counter != 0:
                self.que[counter+1] = self.que[counter]
                counter -=1
            self.que[0] = data
            self.size +=1
