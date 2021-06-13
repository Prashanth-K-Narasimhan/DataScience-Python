import numpy as np
import random
import sys

# print(10 * np.random.randn(2,2))

# print(100 * np.random.random_sample((2, 2)))
# mu, sigma = 0, 0.1,0.21

# print(np.random.normal(mu, sigma, 1000))

def main():

    file_name = "test_" + "3" + ".txt"
    fd = open(file_name, "w")

    for i in range(0, int("3")):
        # Generate a random list of argv[1] numbers
        rand_list = random.sample(range(-100, 100), int("3"))

        # Create diagonal dominance by adding other elemens to the diagonal
        for j in range(0, len(rand_list)):
            if (j == i):
                continue
            rand_list[i] += abs(rand_list[j])

        for j in range(0, len(rand_list)):
            if (j == len(rand_list) - 1):
                fd.write("%d" % rand_list[j])
            else:
                fd.write("%d " % rand_list[j])
        fd.write("\n")

    fd.close()

    file_name = "test_vector_" + "3" + ".txt"
    fd = open(file_name, "w")
    rand_list = random.sample(range(-100, 100), int("3"))

    for j in range(0, len(rand_list)):
        if (j == len(rand_list) - 1):
            fd.write("%d" % rand_list[j])
        else:
            fd.write("%d " % rand_list[j])
    fd.close()

def randMat():

    for i in range(0, 3):
        rand_list = random.sample(range(-100, 100), 3)

        print(rand_list)
        print("````")

        for j in range(0, len(rand_list)):
            if (j == i):
                continue
            rand_list[i] += abs(rand_list[j])
            print(f"{i, j} : {rand_list[i]}")
            print("````")

        for j in range(0, len(rand_list)):
            if (j == len(rand_list) - 1):
                print(rand_list[j] , end='\t')
            else:
                print(rand_list[j], end='\t')
        print("\n")

    print("\n")

    rand_list = random.sample(range(-100, 100), int("3"))

    for j in range(0, len(rand_list)):
        if (j == len(rand_list) - 1):
            print(rand_list[j] , end='\t')
        else:
            print(rand_list[j] , end='\t')

# randMat()
f = np.float64(305.459)
print(len(str(f).replace(".","")))