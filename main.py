import math
import sys

logsame = 0
logsmall = 0
logbig = 0

range_input = int(input("Enter a number. : "))
for i in range(1, range_input + 1):
    num_input = sys.getsizeof(str(i))
    num_log = sys.getsizeof(str(math.log(i, 2)))

    if num_input == num_log:
        logsame += 1
    elif num_input > num_log:
        logsmall += 1
    elif num_input < num_log:
        logbig += 1

txt = open("output.txt", "w")
txt.write("검사 실시한 수 범위: 1 ~ " + str(range_input) + "\n")
txt.write("\n" + "입력 받은 수와 로그를 이용해 나타낸 수의 바이트 수가 같은 수의 개수: " + str(logsame) + "\n")
txt.write("\n" + "입력 받은 수보다 로그를 이용해 나타낸 수의 바이트 수가 작은 수의 개수: " + str(logsmall) + "\n")
txt.write("\n" + "입력 받은 수보다 로그를 이용해 나타낸 수의 바이트 수가 큰 수의 개수: " + str(logbig) + "\n")
txt.close()
