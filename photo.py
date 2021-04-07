import matplotlib.pyplot as plt
image = []
with open("image_hi0.txt", "r")as f:
    file = f.read().split(",")
    for h in range(24):
        data = []
        for w in range(32):
            data.append(float(file[h*32 + w]))
        image.append(data)
print(image)
plt.imshow(image)
plt.show()


