class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        import collections
        adj = collections.defaultdict(list) # Outgoing connections (rom prereq), representation of the graph
        in_degree = [0] * numCourses # no of incoming connections for each node.

        #creaet the graph
        for preq, course in prerequisites:
            adj[preq].append(course) # create the graph
            in_degree[course]+=1 # create the in-degree DS

        q = collections.deque([])
        for course, ind in enumerate(in_degree): # add the nodes which have no incoming (no prereq), we want to run them first 
            if ind == 0:
                q.append(course)
        
        count_course = 0 # count the times you add to the queue, this should be either equl to the graph nodes, or if not there is a cycle ie there are more processing
        while q:
            curr = q.popleft()
            count_course +=1

            for edge in adj[curr]: # go through all the neighbors or outgoing conenctions to this node
                in_degree[edge]-=1 # decrease the incopming edge by one for this neighbor
                if in_degree[edge]==0: # remove it and add it to the q, we want to essentially remove it from the graph and create topogival sorted list ( in theaor)
                    q.append(edge)
        
        return count_course==numCourses

