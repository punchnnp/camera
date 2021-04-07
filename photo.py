import matplotlib.pyplot as plt
image = []
# open file from directory
with open("image_hi1.0.txt", "r")as f:
    # separate value into list
    file = f.read().split(",")
    # make image to 2d array
    for h in range(24):
        data = []
        for w in range(32):
            data.append(float(file[h*32 + w]))
        image.append(data)
# use imshow matplotlib to show figure
print(image)
plt.imshow(image)
plt.show()

