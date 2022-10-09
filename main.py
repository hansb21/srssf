import feedparser

def pprint(entry):

    print(entry.title)
    print(f"{entry.published} {entry.author}")
    print(f"Tag {entry.tags[0]['term']}")
    print(" ")   
    print(entry.summary)

    #print(entry.summary_detail.value)





OsDev = feedparser.parse("https://www.osnews.com/feed/");
#print(OsDev)

for i in range(0, len(OsDev.entries)):
    print("")
    print("*" * len(OsDev.entries[i].title))
    pprint(OsDev.entries[i])
       
# 'text/html', 'language': None, 'base': 'https://www.osnews.com/feed/', print(OsDev.entries[0])
