from nltk.corpus import wordnet

synonym_set = set()

while True:
    synonym = input("Enter the word for which you want to get a synonym (or type 'exit' to quit): ")

    if synonym.lower() == 'exit':
        break

    synonyms = wordnet.synsets(synonym)
    if synonyms:
        for syn in synonyms:
            lemma_name = syn.lemmas()[0].name()
            if lemma_name not in synonym_set:
                print(lemma_name)
                synonym_set.add(lemma_name)
    else:
        print("No synonyms found for the word.")
