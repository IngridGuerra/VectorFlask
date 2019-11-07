import re
import os, sys

def processDocument():
    with open('cran.qry','r') as file:
        docs = file.read().split('\n.I')
    return docs

def getOnlyQueries(alldocs): 
    queryList = []
    # key = 'query'
    options = []

    for doc in alldocs:
         queryList.append(doc.split('.W')[1])
    onlyLetters = [re.sub(r'[^a-z]', ' ', query) for query in queryList]
    cleanQueries= [" ".join(query.split())for query in onlyLetters]

    for query in cleanQueries:
        options.append(query)

    return options

def createTxt(cleanQueries):
    f = open("output.txt", 'w+')
    for query in cleanQueries:
        f.write(query +'\n')
    f.close()
    return f

def main():
    docs = processDocument()
    queries = getOnlyQueries(docs)
    # txt = createTxt(queries)
    #print(docs)
    # print(queries)
    return queries
    # print(txt)

if __name__ == "__main__":
    main()