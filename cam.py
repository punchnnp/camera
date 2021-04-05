import seeed_mlx90640
mlx = seeed_mlx90640.groove._mlx90640()
mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_8_HZ

try:
    mlx.getFrame(frame)
except ValueError:
        continue
