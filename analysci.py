import jieba    #分词               
import pandas as pd
from collections import Counter
from os import path

#数据的读取
def get_content(file):
    with open(file,'r',encoding='utf-8') as f:
        content = ''
        for i in f:
            i = i.strip()
            i = i.replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            content += i
    return content


#高频词统计的函数
def get_TF(words,topK=150):
    tf_dic ={}
    for w in words:
        tf_dic[w] = tf_dic.get(w,0)+1
    return sorted(tf_dic.items(),key=lambda x:x[1],reverse=True)[:topK]


def stop_words(path):
    with open(path,encoding='utf-8') as f:
        return [l.strip() for l in f]


# 分词
def main():
    import glob
    import random
    import jieba

    files = glob.glob('data/content.txt')  # 查找符合特定规则的文件路径名 意思是后缀为.txt全部使用
    print("使用文本为", files)

    try:
        corpus = [get_content(x) for x in files]
      
        sample_inx = 0

        split_words = [x for x in jieba.cut(corpus[sample_inx],cut_all=False,HMM=True) if x not in stop_words('data/stop_words_new.utf8')]
        print(" ".join( split_words))

        print('样本的topK150)词:\n' + str(get_TF(split_words)))
        print(type(str(get_TF(split_words))))

     
        # 高频词写入txt文件
        with open('data/word.txt', 'w',encoding='utf-8') as f:
            f.write(str(get_TF(split_words)))
            print("完成")

    except Exception as err:
        print("err 1")
        print(err)


if __name__ == '__main__':
    main()




