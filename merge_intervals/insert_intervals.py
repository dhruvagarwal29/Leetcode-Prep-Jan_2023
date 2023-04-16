from interval import *
class Interval:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def print_interval(self):
        print(f"start = {self.start} , end = {self.end}")


def insert_interval(existing_intervals, new_interval):
  # Write your code here   
  new_interval_start = new_interval.start
  new_interval_end = new_interval.end
  
  result = []

  for i in range(len(existing_intervals)):
    # if new interval end is less than existing interval start then append 
    # it and return the output
    if existing_intervals[i].start > new_interval_end:
      result.append(Interval(new_interval_start, new_interval_end))
      return result + existing_intervals[i:]
    elif existing_intervals[i].end < new_interval_start:
      result.append(Interval(existing_intervals[i]))
    else:
      new_interval_start = min(new_interval_start,existing_intervals[i].start )
      new_interval_end = max(new_interval_end,existing_intervals[i].end )

  result.append(Interval(new_interval_start, new_interval_end))

  
  return result