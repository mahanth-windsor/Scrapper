import numpy as np
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.JobDetails import JobDetails

corpus = []
recommendation = []
corpus.append("sales associate")

def getAllRows():
    with open('pageLinks.csv', 'r') as file:
        reader = csv.DictReader(file)
        csv_reader = csv.reader(file)
        global rows
        rows = list(reader)
    pass

def getRowsWithHeading():
    getAllRows()
    with open('pageLinks.csv', 'r') as file:
        reader = csv.DictReader(file)
        # csv_reader = csv.reader(file)
        # global rows
        # rows = list(reader)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]

        for row in data['Job Description']:
            # print(row)
            corpus.append(str(row))
    #
    # print(corpus[0])
    vect = TfidfVectorizer(min_df=1, stop_words="english")

    tfidf = vect.fit_transform(corpus)
    pairwise_similarity = tfidf * tfidf.T
    pairwise_similarity

    arr = pairwise_similarity.toarray()
    print(arr)
    np.fill_diagonal(arr, np.nan)
    threshold = 0.1
    for x in range(0,tfidf.shape[0]):
      for y in range(x,tfidf.shape[0]):
        if(x!=y):
          if(cosine_similarity(tfidf[x],tfidf[y])>threshold and (corpus[x] == str(corpus[0]) or corpus[y] == str(corpus[0]))):
            print("text1 "+corpus[x])
            print("text2 "+corpus[y])
            print("Cosine similarity:",cosine_similarity(tfidf[x],tfidf[y]))
            print()
            job = JobDetails(rows[y]['Job Title'], rows[y]['Company'],rows[y]['Job Page link'],rows[y]['Job Description'])
            recommendation.append(job)
    return recommendation
def main():
    getRowsWithHeading()


if __name__ == "__main__":
    main()

# input_doc = "sales associate"
# input_idx = corpus.index(input_doc)
#
# print(np)
#
# result_idx = np.nanargmax(arr[input_idx])
# print(corpus[result_idx])
