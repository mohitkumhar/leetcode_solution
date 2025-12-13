class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        map = {
            '0': ['9', '1'],
            '1': ['0', '2'],
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['4', '6'],
            '6': ['5', '7'],
            '7': ['6', '8'],
            '8': ['7', '9'],
            '9': ['8', '0'],
        }

        seen = set()

        for deadend in deadends:
            seen.add(deadend)
        if '0000' in seen:
            return -1

        queue = ['0000']
        seen.add('0000')
        turns = 0


        while queue:
            size = len(queue)

            for i in range(size):

                curr_lock = queue.pop(0)

                if curr_lock == target:
                    return turns

                curr_lock_arr = list(curr_lock)

                for j in range(4):
                    curr_turn = curr_lock_arr[j]

                    for possible_turns in map.get(curr_lock_arr[j]):

                        curr_lock_arr[j] = possible_turns
                        new_lock_str = ''.join(curr_lock_arr)

                        if new_lock_str not in seen:
                            queue.append(new_lock_str)
                            seen.add(new_lock_str)
                    
                        curr_lock_arr[j] = curr_turn

            turns += 1

        return -1
