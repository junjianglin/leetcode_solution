class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses or not prerequisites:
            return True
            
        #build adjacency list
        graph_list = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            graph_list[pre[1]].append(pre[0])
        #print graph_list
        visited = [False] * numCourses
        for i in range(numCourses):
            stack = [False] * numCourses
            if self.haveCycle(graph_list,i,visited,stack):
                return False
        return True
    
    def haveCycle(self,graph_list,node,visited,stack):
        if visited[node]:
            return False
        if not graph_list[node]:
            return False
        elif stack[node]:
            return True
        else:
            stack[node] = True
            adjNodes = graph_list[node]
            #print adjNodes
            for adj in adjNodes:
                if self.haveCycle(graph_list,adj,visited,stack):
                    return True
            return False
        visited[node] = True
sol = Solution()
print sol.canFinish(3,[[0,2],[1,2],[2,0]])
