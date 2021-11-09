# fxn: getLanguages(fileName)
# parameter: fileName is a str containing name of CSV file to read from w/ default value of "languages.csv"
# return: list of str representing languages in header row
# side effect: none
# put the header row with languages into a list
def getLanguages(fileName="languages.csv"):
    # create empty list to represent languages
    langList = []
    # open the file
    fileIn = open(fileName, "r")
    for line in fileIn:
        line = line.strip()
        # make the str into lists of strings with comma as separator
        info = line.split(",")
        # language would be the first list so that is what we need
        # language = info[0]
        # langList.append(language)
        langList.append(info)

    # close the file
    fileIn.close()
    # only want the first row
    langList = langList[0]

    # return the list of languages
    return langList

# fxn: getSecondLanguage(langList)
# parameter: langList is a list of the languages
# return: str for the second language
# side effect: prints the user question for second language
# displays the languages to the user which are available for translation
def getSecondLanguage(langList):
    print("Translate English words to one of the following languages: ")

    # make the langList list into a str to print
    # prints half the languages in line one with an indent (get rid of English)
    print("\t",*langList[1:8], sep=' ')
    # prints the rest of the languages in the second line with an indent
    print("\t",*langList[8:], sep=' ')

    # ask user what language to translate from
    langStr = input("Enter a language: ")
    langStr = langStr.title()

    # error check where if the language is not present it will continue in loop else returns str value
    # for elements in langStr:
    while langStr not in langList:
        print("This program does not support", langStr)
        langStr = input("Enter a language: ")
        langStr = langStr.title()

    return langStr

# fxn: readFile(langList, langStr, fileName)
# parameter1: list of the languages
# Parameter 2: str containing the name of a language and it has a default value of "English"
# Parameter 3: str containing the name of a CSV file to read from and it has a default value of "languages.csv"
# return: list of words in language identified by parameter2
# side effect:
#
def readFile(langList, langStr="English", fileName="languages.csv"):
    # index for language column
    translate = langList.index(langStr)
    secondList = []
    fileIn = open(fileName, "r")
    for line in fileIn:
        line = line.strip()
        # make the str into lists of strings with comma as separator
        info = line.split(",")
        # language would be the first list so that is what we need
        # want the column of language
        secondList.append(info[translate])

        # close the file
    fileIn.close()
    # only want the language
    return secondList

# fxn: createResultsFile(language, resultsFile)
# parameter1: str containing name of second language
# parameter2: str containing name of results file
# return: none
# side effect:
#
def createResultsFile(language, resultsFile):
    # str = "Words translated from English to", language
    # if name is provided
    if len(resultsFile) > 0:
        # open the file to write
        fileOut = open(resultsFile, "w")
        print("Words translated from English to", language, file=fileOut)
        fileOut.close()

    # if name is not provided
    else:
        resultsFile = language + ".txt"
        fileOut = open(resultsFile, "w")
        print("Words translated from English to", language, file=fileOut)
        fileOut.close()

# fxn: translateWords(englishList, secondList, resultsFile)
# parameter1: list of words in English
# parameter2: list of words in the second language
# parameter3: str containing the name of the text file
# return: none
# side effect:
#
def translateWords(englishList, secondList, resultsFile):
    # continue translating words
    moreWrds = "y"
    # does not enter correct letters
    while moreWrds.lower() != "y" and moreWrds.lower() != "n":
        moreWrds = input("Another word (y or n)? ")

    # out of while loop
    while moreWrds.lower() == "y":
        translatedWord = input("\nEnter a word to translate: ")
        # find the word in the english words
        if translatedWord in englishList:
            # index value the word
            newWrd = englishList.index(translatedWord)
            # find the translated word
            translated = secondList[newWrd]
            # if there is "-" then there is no translation
            if translated == "-":
                print(translatedWord,"did not have a translation.")
            # if there is translation then present it
            else:
                # name of file depends on resultsFile name
                if len(resultsFile) > 0:
                    print(translatedWord, "is translated to", translated)
                    fileOut = open(resultsFile, "a")
                    # add the translated words to the file
                    print(translatedWord, "=", translated, file=fileOut)
                    fileOut.close()
                else:
                    # get language name to name file
                    language = secondList[0]
                    resultsFile = language + ".txt"
                    print(translatedWord,"is translated to",translated)
                    fileOut = open(resultsFile, "a")
                    # add the translated words to the file
                    print(translatedWord,"=",translated, file=fileOut)
                    fileOut.close()
        # not existent in English
        else:
            print(translatedWord,"is not in the English list.")
        # asking to to translate another word
        moreWrds = input("Another word (y or n)? ")

# fxn: main()
# parameter:
# return:
# side effect:
def main():
    print("Language Translator")
    # all the langs to be presented
    langList = getLanguages()

    # to get name of lang
    langStr = getSecondLanguage(langList)

    # prints list of words in new lang
    secondList = readFile(langList,langStr)

    # asks user for name of new file for the next fxn
    fileName = input("\nEnter a name for the results file (return key for " + langStr + ".txt): ")

    # makes the actual file w/ user name
    createResultsFile(langStr,fileName)

    # create the englishList
    englishList = []
    # open file to read
    fileIn = open("languages.csv", "r")
    for line in fileIn:
        line = line.strip()
        # make the str into lists of strings with comma as separator
        info = line.split(",")
        # index value of English is 0 therefore need all the words in that column
        englishList.append(info[0])

        # close the file
    fileIn.close()

    # translates words and adds to .txt file
    translateWords(englishList,secondList,fileName)
    print("Translated words have been saved to", fileName)
    # FIX THIS PART BECAUSE WILL NOT RUN AND DO ERROR CHECK FOR CONT
main()
