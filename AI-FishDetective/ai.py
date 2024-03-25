import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, Conv1D, GlobalMaxPooling1D
from sklearn.model_selection import train_test_split
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))


# Загрузка данных
data = pd.read_csv('spam.csv')
texts = data['body'].values
labels = data['Label'].values

# Преобразование текста в числовые векторы
tokenizer = Tokenizer(num_words=5000) #
tokenizer.fit_on_texts(texts) #
sequences = tokenizer.texts_to_sequences(texts)
x = pad_sequences(sequences, maxlen=200)
y = labels

# Разделение данных на обучающую и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Создание модели
model = Sequential()
model.add(Embedding(5000, 50, input_length=200))
model.add(Conv1D(128, 5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(1, activation='sigmoid'))

# Компиляция модели
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Оценка модели
loss, accuracy = model.evaluate(x_test, y_test)
print('Accuracy: %f' % (accuracy*100))