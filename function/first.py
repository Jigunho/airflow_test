import numpy as np
def main():
  with open('./result1.txt', 'w') as f:
    for i in range(0,100):
      f.write('{}\t{}\t{}\n'.format(i, list(np.random.rand(3)), list(np.random.rand(3))))
