import time
import board
import busio
import adafruit_mlx90640

i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

frame = [0] * 768
x = 0
while True:
    x += 1
    try:
        mlx.getFrame(frame)
        if (x % 10) == 0:
            with open(f"image_hi{x % 10}.txt", "w")as f:
                for h in range(24):
                    for w in range(32):
                        t = frame[h * 32 + w]
                        f.write(t)
                    f.write("\n")

    except ValueError:
        # these happen, no biggie - retry
        continue

    print(frame)