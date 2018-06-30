class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
   
    def __init__(self):
        self.S1 = []
        self.S2 = []
     
    def enqueue(self, data):
        print("inserting data... %d" % (data))
        self.S1.append(data)
    
    def dequeue(self):
        if not self.S2:
            while self.S1:
                self.S2.append(self.S1.pop())
        return self.S2.pop()


