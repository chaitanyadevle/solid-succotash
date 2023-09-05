class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalties = []
        for closing_index in range(len(customers)):
            prev_y = customers.count('Y', 0, closing_index)
            prev_n = customers.count('N', 0, closing_index)
            forward_y = customers.count('Y', closing_index, len(customers))
            forward_n = customers.count('N', closing_index, len(customers))
            penaly = ((prev_y * 0) + (prev_n * 1)) + ((forward_y * 1) + (forward_n * 0))
            penalties.append(penaly)
        print('penalties:', penalties)
        return customers

if __name__ == "__main__":
    '''
    "NNNN"
    "YYYY"
    '''
    a = Solution().bestClosingTime("YYYY")
    print(a)
