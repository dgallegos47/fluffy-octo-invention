import numpy as np
from PIL import Image

K = # Hope you know what K to use...

x, y = np.meshgrid(range(106), range(K, K + 17))
result = 0.5 < ((y // 17) // (2 ** (17 * x + y % 17))) % 2
result = np.flipud(result)
Image.fromarray(result).save("code.png")
