#question basically needs a queue, to maintain sliding window sum, and pop elements as soon as queue size is reached.

class MovingAverage:

    def __init__(self, size: int):
        self.size= size
        self.queue=[]
        
    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue)>=1:
            avg= sum(self.queue)/len(self.queue)
            if len(self.queue)>=self.size:
                self.queue.pop(0)
            return avg
        else:
            return 0

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
