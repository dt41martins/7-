import gensim.downloader as api

model = api.load("word2vec-google-news-300")

words = ["māja", "dzīvoklis", "jūra"]

word_vectors = {word: model[word] for word in words}

similarity_matrix = {}
for word1 in words:
    for word2 in words:
        if word1 != word2:
            similarity = model.similarity(word1, word2)
            similarity_matrix[(word1, word2)] = similarity

for (word1, word2), similarity in similarity_matrix.items():
    print(f"Vārdi '{word1}' un '{word2}' līdzība: {similarity:.4f}")
