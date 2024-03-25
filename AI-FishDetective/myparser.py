import os
import pandas as pd
import time
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from torchtext.data import Field, TabularDataset, BucketIterator

# Загрузка обученной модели PyTorch (предположим, что у нас есть файл 'ai_ready.pt')
model = torch.load('ai_ready.pt')

# Токенизатор
tokenizer = get_tokenizer('basic_english')

# Функция pad_sequences
def pad_sequences(sequences, maxlen):
    padded = torch.zeros(len(sequences), maxlen)
    for i, seq in enumerate(sequences):
        length = min(maxlen, len(seq))
        padded[i, :length] = torch.tensor(seq[:length])
    return padded

def check_directory_and_run_model(directory):
    directory = os.path.join(directory, "ParsFile")  # Поддиректория, которую мы будем проверять
    while True:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        if len(files) > 1:
            raise Exception("Больше одного файла в директории.")
        elif len(files) == 0:
            print("Нет файлов в директории.")
        else:
            file = files[0]
            if not file.endswith('.csv'):
                raise Exception("Файл не является .csv файлом.")
            else:
                data = pd.read_csv(os.path.join(directory, file))
                texts = data['body'].values
                sequences = [tokenizer(text) for text in texts]
                x = pad_sequences(sequences, maxlen=200)
                with torch.no_grad():
                    predictions = model(x)
                return predictions

        time.sleep(60)  # Проверка каждую минуту