#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     去除Bitterlemons数据集中每一行的回车符号
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

if __name__ == "__main__":
    
    readFolderPath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/MEAD数据预处理/docs/'
    writeFolderPath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/MEAD数据预处理/docsNew/'
    files = os.listdir(readFolderPath)
    for fileName in files:
        writePath = writeFolderPath + fileName 
        writeFile = open(writePath, 'a')
        readPath = readFolderPath + fileName
        readFile = open(readPath)
        for line in readFile.xreadlines():
            if cmp(line,'\n') == 0:
                writeFile.write('\n')
            else:
                newLine = line.replace('\n',' ')
                writeFile.write(newLine)
        readFile.close()
        writeFile.close()