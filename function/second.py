import numpy as np
def main():

  arr = []
  with open('./result1.txt') as f:
    lines = f.readlines()
    for line in lines:
      col = line.split('\t')
      # print(max(eval(col[2])))
      arr.append([int(col[0]), max(eval(col[1])), max(eval(col[2]))])
  with open('./result2.txt', 'w') as f:
    for a in arr:
      print(a)
      f.write(str(a) + "\n") 
      # f.write('\n')