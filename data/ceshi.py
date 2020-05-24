import re,jieba,random,time
import numpy as np
# maxSentenceWordsNum=-1
# with open('qingyun.tsv', 'r', encoding='utf8') as f:
#     txt = f.readlines()
#     data = [i.split('\t') for i in txt]
#     # 判断是否是字符，使用jieba进行分词
#
#     data = [[jieba.lcut(i[0]), jieba.lcut(i[1])] for i in data]
#     data = [i for i in data if
#             (len(i[0]) < maxSentenceWordsNum and len(i[1]) < maxSentenceWordsNum) or maxSentenceWordsNum == -1]
#     print(data[0])
#     chatDataId = [[[self.word2id[w] for w in qa[0]], [self.word2id[w] for w in qa[1]]] for qa in data]

import pkg_resources
a=pkg_resources.Corpus()