import time 

class Algorithm:
    def__ init __ (self,data):
    self.data = data 

    def linear_search(self,target):
        for value in self.data:
            if value == target:
                return True
                return False

   def binary_search(self, Target):
    left, right = 0, len(self.data) -1

    while left <= right:
        mid = (left + right) // 2

        if self.data[mid] == target:
            return True
            elif self.data[mid] < target:     
                left = mid + 1
                else:
                    right = mid - 1
                    return False

    def main():
        data = list(range(1,1_000_001))                
        algo = Algorithm(data)
        target = 999_999

        linear_time = algo.measure_runtime(algo.linear_search, target)
        binary_time = algo.measure_runtime(algo.binary_search, target)

        print("Algorithm Performance Analyzer")
        print("-------------------------------")
        print(f"Linear Search Time:{linear_time:.6f} seconds")
         print(f"Binary Search Time:{binarY_time:.6f} seconds")

         if __ name __ "__ main__"
         main()