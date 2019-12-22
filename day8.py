from pprint import pprint

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
 
      if value == "0":
        self.zeros += 1
      elif value == "1":
        self.ones += 1
      elif value == "2":
        self.twos += 1
            
      self.values[-1].append(value)

def make_layers():
  input_file = open(INPUT_FILE)
  data = input_file.readline().strip()
  layer_count, rem = divmod(len(data), AREA)
  assert rem == 0
  layers = []
  for i in range(layer_count):
    layers.append(layer(data[i*AREA : (i+1)*AREA]))
    
  return layers
  
def problem1():
	layers = make_layers()
	min_zeros = layers[0]
	for layer in layers[1:]:
		if layer.zeros < min_zeros.zeros:
			min_zeros = layer
			
	return min_zeros.ones * min_zeros.twos
	
def problem2():
	layers = make_layers()
	image = [[0]*WIDTH for _ in range(HEIGHT)]
	for i in range(HEIGHT):
		for j in range(WIDTH):
			k = 0
			while layers[k].values[i][j] == "2":
				k += 1
			image[i][j] = "." if layers[k].values[i][j] == "0" else "#"

		image[i] = "".join(image[i])
	
	return image
  
def main():
  print(f"one: {problem1()}")
  print("two:")
  pprint(problem2())

if __name__ == "__main__":
  main()
  