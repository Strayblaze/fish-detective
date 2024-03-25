import os
import pandas as pd
import time
import torch
import torch.nn as nn
import torch.optim as optim
from torchtext.data import Field, TabularDataset, BucketIterator

TEXT = Field(tokenize='spacy', lower=True, include_lengths=True)
LABEL = Field(sequential=False, use_vocab=False)

fields = [('title', None), ('body', TEXT), ('label', LABEL)]

train_data, test_data = TabularDataset.splits(
    path='ParsFile/', train='train.csv', test='test.csv',
    format='csv', fields=fields, skip_header=True
)

TEXT.build_vocab(train_data, max_size=5000)

class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.LSTM(embedding_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, text, text_lengths):
        embedded = self.embedding(text)
        packed_embedded = nn.utils.rnn.pack_padded_sequence(embedded, text_lengths)
        packed_output, (hidden, cell) = self.rnn(packed_embedded)
        output, output_lengths = nn.utils.rnn.pad_packed_sequence(packed_output)
        return self.fc(output[-1])

INPUT_DIM = len(TEXT.vocab)
EMBEDDING_DIM = 100
HIDDEN_DIM = 256
OUTPUT_DIM = 1

model = TextClassifier(INPUT_DIM, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM)

optimizer = optim.Adam(model.parameters())
criterion = nn.BCEWithLogitsLoss()

def train(model, iterator, optimizer, criterion):
    model.train()
    for batch in iterator:
        text, text_lengths = batch.body
        optimizer.zero_grad()
        predictions = model(text, text_lengths).squeeze(1)
        loss = criterion(predictions, batch.label.float())
        loss.backward()
        optimizer.step()

# Аналогично для тестовой выборки

# Предсказание
def predict(model, iterator):
    model.eval()
    predictions = []
    with torch.no_grad():
        for batch in iterator:
            text, text_lengths = batch.body
            preds = model(text, text_lengths).squeeze(1)
            predictions.extend(preds.tolist())
    return predictions


