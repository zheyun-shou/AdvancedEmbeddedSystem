import numpy as np
#from keras.preprocessing import image
from tensorflow.keras.preprocessing import image
from keras.models import load_model
import matplotlib.pyplot as plt

model_dir = 'rps.h5'
model = load_model(model_dir)
model.summary()

for num in range(10, 11):
    path = "20220908-144708 image1.png"
    #path = "sc3.jpg"
    img = image.load_img(path, target_size=(150, 150))
    plt.imshow(img)
    #plt.show()
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    #paper-rock-scissors
    print(classes)

print(type(classes))

temp = np.array([[0.,0.,1.]])

print(temp[0][2])

print(type(temp))

if classes[0][0] == 1.0:
    print('You gave paper!')
elif classes[0][1] == 1.0:
    print('You gave rock!')
else:
    print('You gave scissors!')