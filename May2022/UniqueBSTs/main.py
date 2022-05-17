n = 2  # number of testcases
cp = 0
cf = 0
for j in range(n):
    with open("testcases/UnqBST" + str(j + 1) + ".txt") as f:
        n = int(f.read())

    from math import factorial

    class Solution:
        def solutionGold(self, n):
            catalan_number = factorial(2 * n) // factorial(n) // factorial(n) // (n + 1)
            return catalan_number

    obj = Solution()
    ans = obj.solutionGold(n)

    def soluser(n):
        # wrong solution
        x = []
        k = -2
        return k

    u = soluser(n)

    if ans == u:
        cp += 1
        print("YES")
    else:
        cf += 1
        print("NO")


print("The number of test cases passed: ", cp)
print("The number of test cases failed: ", cf)
