from processing.constants import actualitySubjects, nlp
import processing.feedparsing

import processing.feedparsing
import schedule
import time


def setActualitySubjects():
    actualitySubjects = processing.feedparsing.getActualitySubjects(["https://www.ledevoir.com/rss/section/politique.xml?id=51",
        "https://www.noovo.info/bin/noovoinfo/rss.theme.xml?theme=politique",
        "https://www.lapresse.ca/actualites/politique/rss",
        "https://www.journaldemontreal.com/actualite/politique/rss.xml",
        "https://ici.radio-canada.ca/rss/4175",
        "https://www.lemonde.fr/politique/rss_full.xml",
        "https://lequotidien.sn/category/politique/feed/",
        "https://www.laprosperite.cd/category/politique/feed/"],nlp)


schedule.every().day.at("00:00").do(setActualitySubjects)
print("initialized")
