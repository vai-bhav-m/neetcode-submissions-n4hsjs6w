class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for pre in graph[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)  
            return True

        
        return not(False in [dfs(course) for course in range(numCourses)])
