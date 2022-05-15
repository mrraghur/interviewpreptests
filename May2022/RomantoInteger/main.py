n = 10  # number of testcases

for j in range(n):

    with open("testcases/rmn" + str(j + 1) + ".txt") as f:
        rmn = f.read()

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def solutionGold(S):
        summ = 0
        for i in range(len(S) - 1, -1, -1):
            num = roman[S[i]]
            if 3 * num < summ:
                summ = summ - num
            else:
                summ = summ + num
        return summ

    ans = solutionGold(rmn)

    def solUser(S):  # wrong solution
        x = []
        k = 2
        return k

    u = solUser(rmn)

    if ans == u:
        print("Correct answer!, Testcase-" + str(j + 1))
    else:
        print("Wrong answer!, Testcase-" + str(j + 1))
