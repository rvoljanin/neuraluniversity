from tensorflow.keras.datasets import mnist #Библиотека с базой Mnist
from tensorflow.keras.models import Sequential, model_from_json # Подлючаем класс создания модели Sequential
from tensorflow.keras.layers import Dense # Подключаем класс Dense - полносвязный слой
from tensorflow.keras.optimizers import Adam # Подключаем оптимизатор Adam
from tensorflow.keras import utils #Утилиты для to_categorical
from tensorflow.keras.preprocessing import image #Для отрисовки изображения
import numpy as np # Подключаем библиотеку numpy
from PIL import Image, ImageChops

def load_img (img,invert=0):
    size = (28,28)
    raw = Image.open(img)
    gray = raw.convert('L')
    worb = gray.point(lambda x: 0 if x<128 else 255, '1')
    resize = worb.resize(size, resample=0)

    if invert:
        resize = ImageChops.invert(resize)

    data = np.array(resize).reshape(784)
    return np.expand_dims(data,axis=0)

def load_model():
    model_file = open('model.json', 'r') # Чтение файла с моделью
    loaded_model_json = model_file.read()
    model_file.close()
    l_model = model_from_json(loaded_model_json) # Создаём модель по данным из файла

    l_model.load_weights("model.h5") # Загружаем в модель веса из файла

    l_model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]) # Компилируем модель

    return l_model

def model_predict(model,data):
    prediction = model.predict(data)

    return np.argmax(prediction)


digit = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'} # Вспомогательный словарь
gimp = "gimp_data_set/" # Набор изображений созданных в редакторе
handwritten = "handwritten_data_set/" # Набор изображений с фотографий, обработвнных в редакторе

model = load_model() # создаём модель

print("Image    Predict")
for i in digit:
    img_path = gimp + digit[i] + '.bmp'
    print(digit[i] + "\t" + digit[model_predict(model,load_img(img_path))])

print("Image    Predict")
for i in digit:
    img_path = handwritten + digit[i] + '.bmp'
    print(digit[i] + "\t" + digit[model_predict(model,load_img(img_path,1))])
