class QueueList:
    def __init__(self, list=None):
        self.queList = []
        self.size = 0
        if list:
            for _ in list:
                self.en_queue(_)
        
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