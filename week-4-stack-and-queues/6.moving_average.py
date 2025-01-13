'''
This question is asked by Microsoft. Design a class, MovingAverage, which contains a method, 
next that is responsible for returning the moving average from a stream of integers.
Note: a moving average is the average of a subset of data at a given point in time.

Ex: Given the following series of events...

// i.e. the moving average has a capacity of 3.
MovingAverage movingAverage = new MovingAverage(3);
m.next(3) returns 3 because (3 / 1) = 3
m.next(5) returns 4 because (3 + 5) / 2 = 4 
m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6


MovingAverage class definition:

public class MovingAverage {
    // TODO: declare any instance variables you require.

    /**
    * Initializes a MovingAverage with a
    * capacity of `size`.
    */
    public MovingAverage(int size) {
    // TODO: initialize your MovingAverage.
    }

    /**
    * Adds `val` to the stream of numbers
    * and returns the current average of the numbers.
    */
    public double next(int val) {
    // TODO: implement this method.
    }
}
'''

from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.queue = deque()
        self.sum = 0
        self.size = size
    
    def next(self, val):
        self.queue.append(val)
        self.sum += val
        
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()

        return self.sum / len(self.queue)
    
moving_average = MovingAverage(3)
assert moving_average.next(3) == 3
assert moving_average.next(5) == 4
assert moving_average.next(7) == 5
assert moving_average.next(6) == 6
