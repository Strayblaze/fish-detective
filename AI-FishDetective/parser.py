import os
import pandas as pd
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Обученная модель
model = load_model('ai_ready.h5')

# Токенизатор и Функция pad_sequences
tokenizer = Tokenizer(num_words=5000)
pad_sequences = pad_sequences

def check_directory_and_run_model(directory):
    directory = os.path.join(directory, "ParsFile")  # Поддиректория, которую мы будем проверять
    while True:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        if len(files) > 1:
            raise Exception("More than one file in the directory.")
        elif len(files) == 0:
            print("No files in the directory.")
        else:
            file = files[0]
            if not file.endswith('.csv'):
                raise Exception("The file is not a .csv file.")
            else:
                data = pd.read_csv(os.path.join(directory, file))
                texts = data['body'].values
                sequences = tokenizer.texts_to_sequences(texts)
                x = pad_sequences(sequences, maxlen=200)
                predictions = model.predict(x)
                return predictions

        time.sleep(60)  # Проверка каждую минуту