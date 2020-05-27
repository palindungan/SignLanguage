import tensorflow as tf

import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist # gambar dengan ukuran 28x28 dari tulisan tangan angka 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train[0])
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()


