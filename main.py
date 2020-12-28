import math
drawx = []
drawy = []
t = 0
width, height = 512, 512
center = 256
while t <= 2*math.pi:
	x = 2*math.cos(t) + math.cos(2*t)
	y = 2*math.sin(t) - math.sin(2*t)
	drawx.append(x)
	drawy.append(y)
	t += 0.01
for i in range(len(drawx)):
	drawx[i] = round(drawx[i] + center)
	drawy[i] = round(drawy[i] + center)
clean_space = [[0 for j in range(width)] for i in range(height)]
for i in range(len(drawx)):
	clean_space[drawx[i]][drawy[i]] = 1
with open('Image.bmp', 'wb') as f:
	f.write(b'BM')
	f.write((154).to_bytes(4, byteorder='little'))
	f.write((0).to_bytes(2, byteorder='little'))
	f.write((0).to_bytes(2, byteorder='little'))
	f.write((122).to_bytes(4, byteorder='little'))
	f.write((108).to_bytes(4, byteorder='little'))
	f.write((512).to_bytes(4, byteorder='little'))
	f.write((512).to_bytes(4, byteorder='little'))
	f.write((1).to_bytes(2, byteorder='little'))
	f.write((32).to_bytes(2, byteorder='little'))
	f.write((3).to_bytes(4, byteorder='little'))
	f.write((32).to_bytes(4, byteorder='little'))
	f.write((2835).to_bytes(4, byteorder='little'))
	f.write((2835).to_bytes(4, byteorder='little'))
	f.write((0).to_bytes(4, byteorder='little'))
	f.write((0).to_bytes(4, byteorder='little'))
	f.write(b'\x00\x00\xFF\x00')
	f.write(b'\x00\xFF\x00\x00')
	f.write(b'\xFF\x00\x00\x00')
	f.write(b'\x00\x00\x00\xFF')
	f.write(b' niW')
	f.write((0).to_bytes(36, byteorder='little'))
	f.write((0).to_bytes(4, byteorder='little'))
	f.write((0).to_bytes(4, byteorder='little'))
	f.write((0).to_bytes(4, byteorder='little'))

	for i in range(0, 512):
		for j in range(0, 512):
			if clean_space[i][j]:
				f.write(b'\x00\x00\x00\xFF')
			else:
				f.write(b'\xFF\xFF\xFF\xFF')
