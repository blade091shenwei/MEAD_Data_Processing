#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     对已经产生的docsent文件生成cluster文件
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

if __name__ == "__main__":
    
    folderPath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/MEAD数据预处理/cleaned/'
    
    writeFile = open('Religious.cluster', 'a')
    writeFile.write('<CLUSTER LANG=\'ENG\'>\n')
    for file in os.listdir(folderPath):
        fileName = file.split('.')[0]
        writeLine = '<D DID=\'' + str(fileName) + '\' />\n'
        writeFile.write(writeLine) 
    writeFile.write('</CLUSTER>')
    writeFile.close()