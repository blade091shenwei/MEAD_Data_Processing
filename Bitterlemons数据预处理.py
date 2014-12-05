#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     针对Bitterlemons数据集的数据处理
#     由单纯的文本文件生成docsent文件
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

from lxml.builder import E
from lxml import html 

if __name__ == "__main__":
    
    folderPath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/MEAD数据预处理/docsNew/'
    writeFolderPath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/MEAD数据预处理/data/'
    files = os.listdir(folderPath)
    docID = 0
    for fileName in files:
        docID = docID + 1
        writePath = writeFolderPath + str(docID) + '.docsent'
        writeFile = open(writePath, 'a') 
        writeLine = '<DOCSENT DID=\'' + str(docID) + '\' ' \
            + 'LANG=\'ENG\'>\n' + '<BODY>\n' + '<TEXT>\n'
        writeFile.write(writeLine)
        parNumber = 0
        snoNumber = 0
        filePath = folderPath + fileName
        text = open(filePath).read()
        paragraphs = text.split('\n')
        for paragraph in paragraphs:
            rsntNumber = 0
            parNumber = parNumber + 1
#             print "parNumbner", parNumber
            if cmp(paragraph,'') == 0:
                pass
            else:
                sentences = paragraph.split('. ')
                for sentence in sentences:
                    snoNumber = snoNumber + 1
                    rsntNumber = rsntNumber + 1
#                     print "snoNumber",snoNumber,"rsntNumber",rsntNumber
                    if cmp(sentence,'') == 0:
                        pass
                    else:
                        sentenceElement = E.S(sentence, PAR=str(parNumber), \
                            RSNT=str(rsntNumber), SNO=str(snoNumber)\
                            )
                        writeFile.write(html.tostring(sentenceElement, pretty_print = True))
                        pass
#                         print sentence
        writeLine = '</TEXT>\n' + '</BODY>\n' + '</DOCSENT>\n'
        writeFile.write(writeLine)
        writeFile.close()