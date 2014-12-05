#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     针对Yahoo结构化数据的处理
#     把评论整理成MEAD的输入的形式，具体：
#         每一条评论是一个句子
#         评论及其回复是一个段落
#     分割句子可能产生的情况：
#         省略号，产生空字符串
#         ？！ 产生空字符串等
#     
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

from lxml import html 
from lxml.builder import E
import re

if __name__ == "__main__":
    
    folderPath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/comments数据预处理/data/'
    writeFolderPath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/comments数据预处理/cleaned/'
    files = os.listdir(folderPath)
    docID = 0
    for fileName in files:
        docID = docID + 1
        filePath = folderPath + fileName
        writePath =  writeFolderPath + str(docID) + '.docsent'
        writeFile = open(writePath, 'a')
        writeLine = '<DOCSENT DID=\'' + str(docID) + '\' ' \
            + 'LANG=\'ENG\'>\n' + '<BODY>\n' + '<TEXT>\n'
        writeFile.write(writeLine)
        Text = open(filePath).read()
        Html = html.fromstring(Text)
        
        parNumber = 0
        snoNumber = 0
        
        commments = Html.xpath('//comment')
        for comment in commments:
            rsntNumber = 0
            parNumber = parNumber + 1
            commentText = html.tostring(comment)
            commentRoot = html.fromstring(commentText)
            
            comment_text = commentRoot.text
            sentences = re.split('\! |\? |\. ', comment_text)
            for sentence in sentences:
                if cmp(sentence, '')== 0:
                    pass
                else:
                    snoNumber = snoNumber + 1
                    rsntNumber = rsntNumber + 1
#             print comment_text
                    sentenceElement = E.S(sentence, PAR=str(parNumber), \
                                RSNT=str(rsntNumber), SNO=str(snoNumber)\
                                )
                    writeFile.write(html.tostring(sentenceElement, pretty_print = True))
            
            commentReplies = commentRoot.xpath('//reply')
            for commentReply in commentReplies:
                sentences = re.split('\! |\? |\. ', commentReply.text)
                for sentence in sentences:
                    if cmp(sentence,'') == 0:
                        pass
                    else:
                        snoNumber = snoNumber + 1
                        rsntNumber = rsntNumber + 1
                        sentenceElement = E.S(sentence, PAR=str(parNumber), \
                                    RSNT=str(rsntNumber), SNO=str(snoNumber)\
                                    )
                        writeFile.write(html.tostring(sentenceElement, pretty_print = True))
                        pass
        writeLine = '</TEXT>\n' + '</BODY>\n' + '</DOCSENT>\n'
        writeFile.write(writeLine)
        writeFile.close()
            
