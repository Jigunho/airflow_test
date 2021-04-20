import numpy as np
arr = []
def main():

  with open('./result2.txt') as f:
    lines = f.readlines()
    max_n = -1
    for line in lines:
      arr.append(eval(line))
      # col = line.split('\t')

  with open('./result3-1.txt', 'w') as f:
    f.write(str(arr[np.random.randint(100)]))