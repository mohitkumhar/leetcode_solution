class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        idle_time = 1
        total_waiting_time = 0

        for customer in customers:
            if idle_time <= customer[0]:
                idle_time = customer[0] + customer[1]
            else:
                idle_time = idle_time + customer[1]
            total_waiting_time = total_waiting_time + idle_time - customer[0]
        return total_waiting_time / len(customers)
