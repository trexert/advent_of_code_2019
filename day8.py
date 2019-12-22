WIDTH = 25
HEIGHT = 6
AREA = HEIGHT * WIDTH
INPUT_FILE = "day8.input"

class layer(object):
  def __init__(self, data):
    self.zeros = 0
    self.ones = 0
    self.twos = 0
    self.values = []
    for i, value in enumerate(data):
      if i % WIDTH == 0:
          self.values.append([])
 
      if value == 0:
        self.zeros += 1
      elif value == 1:
        self.ones += 1
      elif value == 2:
        self.twos += 1
            
      self.values[-1].append(value)

def solve():
  input_file = open(INPUT_FILE)
  data = input_file.readline().strip()
  layer_count, rem = divmod(len(data), AREA)
  assert rem == 0
  layers = []
  min_zeros = None
  for i in range(layer_count):
    current_layer = layer(data[i*AREA : (i+1)*AREA])
    if min_zeros is None or current_layer.zeros < min_zeros.zeros:
      min_zeros = current_layer
    layers.append(current_layer)
  return min_zeros.ones * min_zeros.twos
  
def main():
  print(solve())

if __name__ == "__main__":
  main()
  