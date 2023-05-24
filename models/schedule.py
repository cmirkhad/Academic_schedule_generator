class Schedule:
    def __init__(self, groups):
        self.slots = {}
        for group in groups:
            self.slots[group.course] = [["" for _ in range(11)] for _ in range(6)]  # 6 days, 11 slots per day
