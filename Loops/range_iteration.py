import time


bacteria = "a"
generations = 10

for generation in range(0, generations):
  bacteria = bacteria * 2
  time.sleep(0.5)
  print(bacteria)