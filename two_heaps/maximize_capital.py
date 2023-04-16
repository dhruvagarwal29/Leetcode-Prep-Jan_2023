#maximize the capital 
# try to maximize the capital 
from heapq import *
def find_maximum_capital(capital, profits, num_of_projects, initial_capital):
    # 1) push all the project capitals to minheap so we can choose it with the available capital
    # 2) go through the top projects of min_heap and filter those can be completed within out available capital
    # 3) insert all these projects in max_heap, so that we can choose projet with maximum profit
    # 4) select the top project of max_heap for investment 
    # 5) repeat 2 and 3 steps for required no of projects 

    # make 2 heaps, one will save the profits and other capital...for capitals we are using min_heap 
    # and for profits max_heap 

    min_capital_heap = []
    max_profit_heap = []

    # insert all the projects capital to min heap 

    for i in range(0, len(profits)):
        heappush(min_capital_heap, (capital[i], i))

    available_capital = initial_capital

    for i in range(num_of_projects):
        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            capital, index =  heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[index], index))
    
        # terminate if we are not able find the project that can be implemented using the available capital
        if not max_profit_heap:
            break

        # if we can find the project then add the profit in the available capital
        profit_made = -heappop(max_profit_heap)[0] # pop the project with highest profit

        # add the capital to the previous capital
        available_capital += profit_made

    return available_capital
if __name__=="__main__":
    print(find_maximum_capital([0,1,2], [1,2,3], 2,1))