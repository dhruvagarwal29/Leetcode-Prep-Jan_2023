def merge_interval(interval):

    # sort the intervals on basis of their start time 
    interval.sort(key=lambda x:x[0])
    # print(interval)
    merge_intervals= []
    first_interval = interval[0]
    
    for start, end in interval[1:]:
        end_index = first_interval[1]
        if start < end_index:
            end = max(end, end_index)
            merge_intervals.append([first_interval[0], end])
        else:
            merge_intervals.append([start,end])
    
    return merge_intervals
    

if __name__=="__main__":
    intervls = [[1,4], [2,5], [7,9]]

    print(merge_interval(intervls))
