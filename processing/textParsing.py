def breakdownSentenceIntoCategories(sentence, nlp):
    doc = nlp(sentence)
    wordBreakdown = {}
    for token in doc:
        if token.pos_  not in wordBreakdown:
         wordBreakdown[token.pos_] = []
        wordBreakdown[token.pos_].append(token.text)

    personalizedWordBreakDown = {}

    if "NOUN" in wordBreakdown or "PROPN" in wordBreakdown or "VERB" in wordBreakdown or "ADJ" in wordBreakdown :
        personalizedWordBreakDown["interest"] = (wordBreakdown.get("NOUN") or []) + (wordBreakdown.get("PROPN") or []) + (wordBreakdown.get("VERB") or []) + (wordBreakdown.get("ADJ") or [])
    if "NOUN" in wordBreakdown or "PROPN" in wordBreakdown:
        personalizedWordBreakDown["concept"] = (wordBreakdown.get("NOUN") or []) + (wordBreakdown.get("PROPN") or [])
    if "ADJ" in wordBreakdown or "ADV" in wordBreakdown:
        personalizedWordBreakDown["ad"] = (wordBreakdown.get("ADJ") or []) + (wordBreakdown.get("ADV") or [])
    return personalizedWordBreakDown;
