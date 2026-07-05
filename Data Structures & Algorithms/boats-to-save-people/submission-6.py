class Solution:
    def numRescueBoats(self, people, limit):
        people = sorted(people)
        people = people[::-1]
        p0 = 0
        p1 = len(people)-1
        boats = []
        while p0 <= p1:
            if people[p0] + people[p1] <= limit:
                boats.append([people[p0], people[p1]])
                p1-=1
            elif people[p0] <= limit:
                boats.append([people[p0]])
            p0+=1


        return len(boats)

        
            




        