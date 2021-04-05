import time, board, busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL, board.SDA, frequency=40000)    # set i2c
mlx = adafruit_mlx90640.MLX90640(i2c)   # begin MLX90640 with I2C com
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ   # set refresh rate
mlx_shape = (24, 32)

plt.ion()
fig, ax = plt.subplots(figsize=(12, 7))
therm1 = ax.imshow(np.zeros(mlx_shape), vmin=0, vmax=60)
cbar = fig.colorbar(therm1)
cbar.set_label('Temperature [$^{\circ}$C]', fontsize=14)

frame = np.zeros((24*32,))  # set up array for storing all 768 temp
t_array = []
while True:
    t1 = time.monotonic()
    try:
        mlx.getFrame(frame)
        data_array = (np.reshape(frame,mlx_shape))
        therm1.set_data(np.fliplr(data_array))
        therm1.set_clim(vmin=np.min(data_array), vmax=np.max(data_array))
        cbar.on_mappable_change(therm1)
        plt.pause(0.001)
        fig.savefig('mlx90640_test_fliplr.png', dpi=300, facecolor='#FCFCFC', bbox_inches='tight')
        t_array.append(time.monotonic()-t1)
        print('Sample Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
        # break
    except ValueError:
        continue

# print('temp: {0:2.1f}C {1:2.1f}F'.format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))

# import seeed_mlx90640
# mlx = seeed_mlx90640.grove_mxl90640()
# mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_8_HZ
#
# while True:
#     try:
#         mlx.getFrame(frame)
#     except ValueError:
#         continue

