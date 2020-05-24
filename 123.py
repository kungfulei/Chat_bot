#导入库
from model.model import ChatBot
import torch

if __name__ == "__main__":
    print('Loading the model...')
    chatBot = ChatBot("./modelB.pkl", device=torch.device('cpu'))
    print('Finished...')

    allRandomChoose,showInfo = False, False
    #在控制端显示的词语
    while True:
        inputSeq = input("主人: ")
        if inputSeq=='_crazy_on_':
            allRandomChoose = True
            print('德洛丽丝: ','成功开启聊天模式...')
        elif inputSeq=='_crazy_off_':
            allRandomChoose = False
            print('德洛丽丝: ','成功关闭疯狂模式...')
        elif inputSeq=='_showInfo_on_':
            showInfo = True
            print('德洛丽丝: ','成功开启日志打印...')
        elif inputSeq=='_showInfo_off_':
            showInfo = False
            print('德洛丽丝: ','成功关闭日志打印...')
        else:
            outputSeq = chatBot.predictByBeamSearch(inputSeq, isRandomChoose=True, allRandomChoose=allRandomChoose, showInfo=showInfo)
            # outputSeq = chatBot.predictByGreedySearch(inputSeq)
            print('德洛丽丝: ',outputSeq)
        print()