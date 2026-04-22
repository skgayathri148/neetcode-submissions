class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_map = {}
        for i in range(len(position)):
            car_map[position[i]] = speed[i]
        
        position.sort(reverse=True)

        stack = []
        for car in position:
            time = (target - car) / car_map[car]
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)