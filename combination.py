class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combination( n , k , path , idx):
            if len(path) == k:
                res.append(path[:])
                return 
            for i in range(idx , n+1):
                path.append(i)
                combination(n , k , path , i + 1)
                path.pop()
        idx = 1
        combination(n , k , [] , idx)
        return res
