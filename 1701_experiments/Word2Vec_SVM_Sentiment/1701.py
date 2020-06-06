import os, sys
import numpy as np
import jieba
from gensim.models.word2vec import Word2Vec
from sklearn import svm

#分词
def split_content(txt_dir):
    root = txt_dir
    txt_name_list = os.listdir(root)#获得txt_dir里的所有文件名字
    invalid_list = []#无效txt文件的名字
    for name in txt_name_list:
        try:
            with open(root + '\\' + name,"r") as f:
                content = f.read()
                seg_list = jieba.cut(content,cut_all=False)#分词
            with open(root + '\\' + name,"w+") as f1:#重新写入txt文档
                f1.write(' '.join(seg_list))
        except:
            invalid_list.append(root + '\\' + name)
            continue
    #删除无效的文件
    for file in invalid_list:
        os.remove(file)

# 读取停用词表
def get_custom_stopwords(stopwords_file):
    with open(stopwords_file,'r',encoding='utf8') as f:
        text = f.read().split('\n')
    return text

# 去停用词
def stopwords_content(txt_dir,stopwords_dir):
    root = txt_dir
    txt_name_list = os.listdir(root)#获得txt_dir里的所有文件名字
    for name in txt_name_list:   
        try:
            with open(root + '\\' + name, 'r') as f2:
                content = f2.read()
            outstr =''
            stopwords = get_custom_stopwords(stopwords_dir)
            stopwords.append(' ')
            stopwords.append('\n')
            stopwords.append('\t')
            stopwords.append('~')
            for word in jieba.cut_for_search(content):
                if word not in stopwords:
                    outstr += word
                    outstr += " "
            with open(root + '\\' + name, 'w+') as f3:
                f3.write(outstr)
        except:
            continue
#获取文本内容里的句子向量
def get_sentences_vec(txt_dir, labels_train):
    root = txt_dir
    txt_name_list = os.listdir(root)#获得txt_dir里的所有文件名字
    #读取文本内的内容
    # 读入内容
    lines = []
    for name in txt_name_list:
        list_c = []
        with open(root + '\\' + name) as f:
            content = f.read()
            for word in jieba.cut_for_search(content):
                if word == " ":
                    continue
                else:
                    list_c.append(word)
            lines.append(list_c)
    #利用Word2Vec获得句子的向量
    model = Word2Vec(lines,sg=1,size=200,window=5,min_count=5,negative=3,hs=1)#维度为50
    vecs_sentences = []
    invalid_sentence_count = 0
    for line in lines:
        vec = np.zeros(200)
        i = 0
        for word in line:
            try:
                vec += model[word]
                i += 1
            except:
                continue
        if i > 0:
            vec /= i
            vecs_sentences.append(vec)
        else:
            del labels_train[invalid_sentence_count] 
        invalid_sentence_count += 1
    return vecs_sentences
    
#获得各个文本的标签
def get_label(txt_dir):
    root = txt_dir
    txt_name_list = os.listdir(root)#获得txt_dir里的所有文件名字
    labels_train = []#标签
    for txt_name in txt_name_list:
        label = float(txt_name[len(txt_name)-7:len(txt_name)-4])
        labels_train.append(label)
    return labels_train
        
if __name__ == '__main__':
    train_dir = 'E:\\Mywindows\\NLP\\1701_实验\\data(1)\\train'
    test_dir = 'E:\\Mywindows\\NLP\\1701_实验\\data(1)\\test'
    stopwords_dir = 'E:\\Mywindows\\NLP\\1701_实验\\data(1)\\stopwords\\哈工大停用词表.txt'
    #分词
    split_content(train_dir)
    split_content(test_dir)
    #去停用词
    stopwords_content(train_dir,stopwords_dir)
    stopwords_content(test_dir,stopwords_dir)
    #获取标记
    train_label = get_label(train_dir)
    test_label = get_label(test_dir)
    #获取句子向量
    train_vecs_sentences =  get_sentences_vec(train_dir,train_label)
    test_vecs_sentences =  get_sentences_vec(test_dir,test_label)
    print(len(train_vecs_sentences))
    print(len(test_vecs_sentences))
    print(len(train_label))
    print(len(test_label))


    #标签：labels_train
    #句子向量：vecs_sentences
    #支持向量机回归
    #回归训练
    from sklearn import svm
    clf_regression = svm.SVR()
    print(type(train_vecs_sentences))
    print(type(train_label))
    clf_regression.fit(train_vecs_sentences, train_label)

    results = []
    for i in range(100):
        result = clf_regression.predict([test_vecs_sentences[i]])[0] - test_label[i]
        print('{:.3f}'.format(result),end="/")
        results.append(abs(result))
    print('\n')
    print(np.mean(results))

    #标签：labels_classes
    #句子向量：vecs_sentences
    #分类训练
    clf_classifier = svm.SVC(gamma='scale')
    train_label_classes = []
    test_label_classes = []
    for label in train_label:
        if 0<=label and label<=1:
            label = 1
        elif 1<label and label<=2:
            label = 2
        elif 2<label and label<=3:
            label = 3
        elif 3<label and label<=4:
            label = 4
        elif 4<label and label<=5:
            label = 5
        train_label_classes.append(label)
    for label in test_label:
        if 0<=label and label<=1:
            label = 1
        elif 1<label and label<=2:
            label = 2
        elif 2<label and label<=3:
            label = 3
        elif 3<label and label<=4:
            label = 4
        elif 4<label and label<=5:
            label = 5
        test_label_classes.append(label)
    clf_classifier.fit(train_vecs_sentences, train_label_classes)
    for i in range(100):
        print('{:.3f}'.format(clf_classifier.predict([test_vecs_sentences[i]])[0]-test_label_classes[i]),end="/")