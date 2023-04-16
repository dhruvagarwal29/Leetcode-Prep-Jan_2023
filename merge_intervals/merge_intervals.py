# given a list of intervals, merge all the overlapping intervals to produce a list that has only
# mutually exclusive intervals

class Interval:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def print_interval(self):
        print(f"start = {self.start} , end = {self.end}")

def merge(intervals):
    if len(intervals) < 2:
        return intervals
    
    # sort the intervals on the start time basis 

    intervals.sort(key = lambda x:x.start)

    merged_intervals= []

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval.start <= end:     # overlapping intervals, adjust the 'end'
            end = max(interval.end, end) # getting the max value from current end or 0th indexed end
        else: # non overlapping interval, add the previous interval and reset 
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end
    
    # add the last interval
    merged_intervals.append(Interval(start, end))
    return merged_intervals


if __name__=="__main__":
    intervals = [Interval(1,4), Interval(2,5), Interval(7,9)]

    for i in merge(intervals):
        i.print_interval()
    print()