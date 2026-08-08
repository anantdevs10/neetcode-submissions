class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        position = [p for p, s in cars]
        speed = [s for p, s in cars]
        position.sort(reverse=True)
        required_travel_distance = []
        for i in range(len(position)):
            required_travel_distance.append(target - position[i])

        division_array = []
        
        for j in range(len(speed)):
            time = required_travel_distance[j] / speed[j]
            if division_array and time <= division_array[-1]:
                continue
            else:
                division_array.append(time)


        return len(division_array)

        