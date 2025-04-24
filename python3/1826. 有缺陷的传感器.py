class Solution:

    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:

        n = len(sensor1)
        valid = set()
        for i in range(n):
            if sensor1[:i] == sensor2[:i] and sensor1[i:-1] == sensor2[i + 1:] and sensor1[-1] != sensor2[i]:
                valid.add(1)
            if sensor1[:i] == sensor2[:i] and sensor2[i:-1] == sensor1[i + 1:] and sensor2[-1] != sensor1[i]:
                valid.add(2)

        if len(valid) == 1:
            return list(valid)[0]

        return -1
