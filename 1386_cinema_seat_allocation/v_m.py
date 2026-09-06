class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left = {2, 3, 4, 5}
        middle = {4, 5, 6, 7}
        right = {6, 7, 8, 9}

        reserved_seats_set = {}

        groups_that_fit = 2 * n
        for row, seat in reservedSeats:
            if seat == 1 or seat == 10:
                continue
            if row not in reserved_seats_set:
                reserved_seats_set[row] = set()
            reserved_seats_set[row].add(seat)
            
        for entry in reserved_seats_set:
            left_free = not (left & reserved_seats_set[entry])
            right_free = not (right & reserved_seats_set[entry])
            middle_free = not (middle & reserved_seats_set[entry])

            if left_free and right_free:
                continue
            elif left_free or right_free or middle_free:
                groups_that_fit -= 1
            else:
                groups_that_fit -= 2
        
        return groups_that_fit