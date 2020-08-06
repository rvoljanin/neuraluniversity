from tensorflow.keras.datasets import mnist #Библиотека с базой Mnist
from tensorflow.keras.models import Sequential, model_from_json # Подлючаем класс создания модели Sequential
from tensorflow.keras.layers import Dense # Подключаем класс Dense - полносвязный слой
from tensorflow.keras.optimizers import Adam # Подключаем оптимизатор Adam
from tensorflow.keras import utils #Утилиты для to_categorical
from tensorflow.keras.preprocessing import image #Для отрисовки изображения
import numpy as np # Подключаем библиотеку numpy
from PIL import Image, ImageChops

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

def load_gpimg (img): # Предподготовка изображений созданных в графическом редакторе GIMP
    org = np.asarray(image.load_img(img))[:,:,0]
    data = org.reshape(784).astype('float32')
    data = data / 255

    return np.expand_dims(data,axis=0)

def load_hwimg (img): # Предподготовка изображений рукописных цифр
    org = np.asarray(image.load_img(img).resize((28,28), resample=0))[:,:,0].reshape(784).astype('float32')
    data = np.array([])

    for i in range(len(org)):
        if org[i] > 100:
            data = np.append(data, 0)
        else:
            data = np.append(data, 255-org[i])
    
    data = data / 255

    return np.expand_dims(data,axis=0)

digit = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'} # Вспомогательный словарь
gimp = "gimp_data_set/" # Набор изображений созданных в редакторе
handwritten = "handwritten_data_set/" # Набор изображений с фотографий, обработвнных в редакторе

model = load_model() # создаём модель

print("="*80)
print("GIMP dataset")
print("="*80)
print("Image\tPredict")
for i in digit:
    img_path = gimp + digit[i] + '.bmp'
    print(digit[i] + "\t" + digit[model_predict(model,load_gpimg(img_path))])

print("="*80)
print("handwritten dataset")
print("="*80)
print("Image\tPredict")
for i in digit:
    img_path = handwritten + digit[i] + '.bmp'
    print(digit[i] + "\t" + digit[model_predict(model,load_hwimg(img_path))])
