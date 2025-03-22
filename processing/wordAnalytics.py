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

def wordIsIncluded(wordList1, wordList2, nlp):
    analyticMatrix = makeAnalyticMatrix(wordList1, wordList2, nlp)
    if isinstance(analyticMatrix, np.ndarray):
        max = analyticMatrix.max()
        if max >= 0.4:
            return True
    else:
        return False


def skeetIsIncluded(wordList1, wordList2, nlp):
    """
    analyticMatrix = makeAnalyticMatrix(wordList1, wordList2, nlp)
    aboveThreshold = True
    if not (isinstance(analyticMatrix, np.ndarray)):
        return False

    analyticVector = analyticMatrix.flatten()
    sortedSimilarity = np.flip(np.sort(analyticVector))[0:min(len(analyticVector), 2)]
    for value in sortedSimilarity:
        if value <= 0.7:
            aboveThreshold = False
    return aboveThreshold
    """
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
