import os
import io
import numpy

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message

def dataFrameFromDir(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({
            'message': message,
            'class': classification
        })
        index.append(filename)
    return DataFrame(rows, index=index)

data = DataFrame({ 'message': [], 'class': [] })

data = data.append(dataFrameFromDir('../emails/spam', 'spam'))
data = data.append(dataFrameFromDir('../emails/ham', 'ham'))

print data.head()