import feedparser
import processing.textParsing
import processing.wordAnalytics

def parseFeed(urls):
    feedEntries = []
    for url in urls:
        d = feedparser.parse(url)
        for entry in d.entries:
            feedEntry = {}
            feedEntry["title"] = entry.title
            feedEntry["description"] = entry.description
            feedEntries.append(feedEntry)
    return feedEntries
def getActualitySubjects(urls, nlp):

    text = ""
    parsedFeed = parseFeed(urls)
    for entry in parsedFeed:
        text += entry["description"] + " " + entry["title"] + " "
    parsedText = processing.textParsing.breakdownSentenceIntoCategories(text, nlp)["concept"]
    wordbyRecurrence = {}
    for word in parsedText:
        if word not in wordbyRecurrence and len(word) > 1:
            wordbyRecurrence[word] = 1
        elif len(word) > 1:
            wordbyRecurrence[word] += 1
    political = ["politique", "gouvernement" "québec", "canada", "loi", "Plamondon", 'Nadeau', "Rodriguez", "Trump", "Ghazal" "pspp", "gnd" "Poilièvre", "libéral", "conservateur", "indépendance", "états-unis", "france", "qs",
            "municipal", "fédéral", "provincial", "environnement", 'israel', "infrastructure", "transport", "gouvernement", "sénat", "président", "ministre", "élection", "socialiste", "capitalisme", "démocratie"]
    actualitySubjects = [subject for subject in wordbyRecurrence.keys() if processing.wordAnalytics.wordIsIncluded([subject], political, nlp)]
    print(actualitySubjects)
    return actualitySubjects
