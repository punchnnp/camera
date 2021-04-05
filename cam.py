# import time,board,busio
import numpy as np
# import adafruit_mlx90640
#
# i2c = busio.I2C(board.SCL, board.SDA, frequency=40000)    # set i2c
# mlx = adafruit_mlx90640.MLX90640(i2c)   # begin MLX90640 with I2C com
# mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ   # set refresh rate
#
frame = np.zeros((24*32,))  # set up array for storing all 768 temp
#
# while True:
#     try:
#         mlx.getFrame(frame)
#         break
#     except ValueError:
#         continue
#
# print('temp: {0:2.1f}C {1:2.1f}F'.format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))

import seeed_mlx90640
mlx = seeed_mlx90640.grove_mxl90640()
mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_8_HZ

while True:
    try:
        mlx.getFrame(frame)
    except ValueError:
        continue

