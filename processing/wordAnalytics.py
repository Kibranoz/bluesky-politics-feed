import numpy as np
import math
def makeAnalyticMatrix(wordList1, wordList2, nlp):
    matrix = None
    for word1 in wordList1:
        vec1 = []
        for word2 in wordList2:
            doc1 = nlp(word1)
            doc2 = nlp(word2)
            vec1.append(doc1.similarity(doc2))
        if isinstance(matrix, np.ndarray):
            matrix = np.vstack((matrix, np.array(vec1)))
        else:
            matrix = np.array(vec1)
    return matrix
# Compare a one word list to a list of actuality subject.
def wordIsIncluded(wordList1, wordList2, nlp):
    analyticMatrix = makeAnalyticMatrix(wordList1, wordList2, nlp)
    if isinstance(analyticMatrix, np.ndarray):
        max = analyticMatrix.max()
        if max >= 0.4:
            return True
    else:
        return False


def skeetIsIncluded(wordList1, wordList2, nlp):
    excludedWords = ["lundi", "mardi",
     "année", "jour", "noël", "matin", "bitcoin", "trade", "ETFs"]

    absolutelyInclude = ["pspp", "legault", "plamondon", "gnd", "trudeau", "poilièvre", 'nadeau-dubois', "rodriguez", "libéral", "conservateur", "provincial"]

    count = 0
    usedWords = []
    for element in wordList1:
        if element not in excludedWords:
            if element in list(wordList2) and element not in usedWords:
                if element in absolutelyInclude:
                    count += 3
                count += 1
                usedWords.append(element)
    return count >= 3
