class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        asteroids = asteroids[::-1]
        while len(asteroids) != 0:
            check = True
            value = asteroids.pop()
            while check and len(stack) > 0:
                comparator = stack[-1]
                if (comparator > 0 and value > 0) or (comparator < 0):
                    stack.append(value)
                    check = False
                elif (int(float(value))**2) == (int(float(comparator)**2)):
                    stack.pop()
                    check = False
                elif (int(float(value))**2) > (int(float(comparator)**2)):
                    stack.pop()
                else:
                    check = False
            if check and len(stack) == 0:
                stack.append(value)
        return stack
        