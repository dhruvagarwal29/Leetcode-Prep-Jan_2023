# Schedule Tasks on Minimum Machines

from heapq import *
def min_machines(tasks_lists):

    machine = 0
    min_heap = []

    # sort the task list based on the start time 
    tasks_lists = sorted(tasks_lists, key = lambda x: x[0])

    if not tasks_lists:
        return 0

    for task in tasks_lists:
        # if nothing is there in heap or task start time is less than the minheap 0 which means the end time of 
        # previous process than you have to increase the counter for the machines as now we need one more machien 
        # at the same time as the start time of the second process is lesser than the end time of previous 
        # process so push that in minheap too and increase the machine pointer 
        if not min_heap or task[0] < min_heap[0]:
            heappush(min_heap, task[1])
            machine +=1

        # if tast start time is greater than the minheap root end time(previous job end time) then remove the 
        # current min heap and push the new job in the heap as it is going to over
        elif task[0] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, task[1])

    return machine

if __name__=="__main__":

    input_list = [(1, 1), (5, 5), (4, 8), (4, 4), (6, 6), (10, 10), (7, 7)]

    print(min_machines(input_list))