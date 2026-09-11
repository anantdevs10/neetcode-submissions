import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # cpu is idle no available tasks
        # cpu choose shortest processing time
        # cpu chooses task with smallest index if multiple have short processing time
        #order in which the CPU will process the tasks

        res = []
        
        for i, task in enumerate(tasks):
            tasks[i] = (task[0], task[1], i)
        checking = tasks[:]
        heapq.heapify(tasks)
        print(tasks)

        j = 0

        while len(res) < len(checking):
            lst = []
            if tasks and j < tasks[0][0]:
                j = tasks[0][0]
            while tasks and j >= tasks[0][0]:
                val = heapq.heappop(tasks)
                lst.append((val[1], val[0], val[2])) # time, enqueue, index
            heapq.heapify(lst)
            if lst:
                val = heapq.heappop(lst)
                true_val = (val[1], val[0] , val[2])
                res.append(true_val[2])
                j+=val[0]
            
            while lst:
                ans = heapq.heappop(lst)
                ans = (ans[1], ans[0] , ans[2])
                heapq.heappush(tasks, ans)


        return res
