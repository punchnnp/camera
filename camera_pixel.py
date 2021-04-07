# library for camera
import board
import busio
import adafruit_mlx90640

# make a connection to i2c
i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

# connect camera to i2c
mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

# set camera refresh rate
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

# set initial frame [initial value]*length
frame = [0] * 768
x = 0
while True:

    try:
        mlx.getFrame(frame)
        x += 1
        if (x % 10) == 0:
            print(frame)
            # open file and save to file
            with open(f"image_hi{x / 10}.txt", "w")as f:
                # range of horizontal line in array
                for h in range(24):
                    # range of vertical line in array
                    for w in range(32):
                        t = frame[h * 32 + w]
                        # write pixel to file.txt
                        f.write("%2f," % t)


    except ValueError:
        # these happen, no biggie - retry
        continue
