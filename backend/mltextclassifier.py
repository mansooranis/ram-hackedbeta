import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

list_of_training_set = ["trainingset/janger.txt", "trainingset/jfear.txt", "trainingset/joy.txt",
                        "trainingset/jsadness.txt"]

df_list = []
for i in list_of_training_set:
    df = pd.read_csv(i, names=["Sentences", "Label"], sep="\t")
    df_list.append(df)

df = pd.concat(df_list)
sentences = df["Sentences"].values
y = df["Label"].values
# print(sentences,labels)
vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(sentences)
vectorizer.transform(sentences).toarray()
sentences_train, sentences_test, y_train, y_test = train_test_split(
    sentences, y, test_size=0.25, random_state=1000)
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)
X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print("Accuracy:", score)