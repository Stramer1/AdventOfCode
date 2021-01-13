from aocd import get_data
from textwrap import wrap

width, height = 25, 6
layers = wrap(get_data(day=8, year=2019), width * height)

minimum = min((layer.count("0"), layer.count("1") * layer.count("2")) for layer in layers)
print(minimum[1])

picture = list(layers[0])
for layer in layers:
	for pixel in range(width * height):
		if picture[pixel] == "2":
			picture[pixel] = layer[pixel]

for layer in range(0, height*width, width):
	print("".join(picture[layer:layer+width]).replace("0", " "))