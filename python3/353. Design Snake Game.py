class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):

        self.x, self.y = 0, 0
        self.width, self.height = width, height
        self.foods = food
        self.food_idx = 0
        self.current_food = self.foods[self.food_idx]
        self.length = 1
        self.history_positions = [(0, 0)]
        self.offset = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }

    def move(self, direction: str) -> int:

        offset_x, offset_y = self.offset[direction]
        x, y = self.x + offset_x, self.y + offset_y
        if not (0 <= x < self.height and 0 <= y < self.width) or (x, y) in self.history_positions[1:]:
            return -1

        if self.current_food is not None and x == self.current_food[0] and y == self.current_food[1]:
            self.length += 1
            self.food_idx += 1
            self.current_food = None if self.food_idx >= len(self.foods) else self.foods[self.food_idx]

        self.history_positions.append((x, y))
        self.history_positions = self.history_positions[-self.length:]
        self.x, self.y = x, y

        return self.length - 1
