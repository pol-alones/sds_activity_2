import time
import matplotlib.pyplot as plt

outputs = []
for i in range(50000):
    outputs.append((i, time.time_ns()))

x = []
y = []
# Change file name to match each scenario
# 1. No credit on EC2
# 2. Credit on EC2
# 3. VM
# 4. Physical Machine
# file = open("cpu_test_scenario_4.txt", "w")
# for i in range(len(outputs)):
#     file.write(str(outputs[i][0]) + ", " +
#                str((outputs[i][1]-outputs[0][1])/1e9) + "\n")
#     x.append(outputs[i][0])
#     y.append((outputs[i][1]-outputs[0][1])/1e9)
# file.close()

# print("CPU Test time to run 50,000 iterations: ", y[-1], "s")


def extract_data(filename):
    a = []
    b = []
    file = open(filename, "r")
    for line in file:
        line = line.split(", ")
        a.append(int(line[0]))
        b.append(float(line[1]))
    file.close()
    return a, b


x = []
y = []
x, y = extract_data("cpu_test_scenario_1.txt")
plt.plot(x, y, label="No Credit on EC2")
x, y = extract_data("cpu_test_scenario_2.txt")
plt.plot(x, y, label="Credit on EC2")
x, y = extract_data("cpu_test_scenario_3.txt")
plt.plot(x, y, label="VM")
x, y = extract_data("cpu_test_scenario_4.txt")
plt.plot(x, y, label="Physical Machine")
plt.legend()
plt.xlabel("Loop number")
plt.ylabel("Time Stamp (s)")
plt.title("CPU Test")
plt.savefig("cpu_test.png")
plt.show()
