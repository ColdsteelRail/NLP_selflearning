1. Introduction
BERT(Bidirectional Encoder Representation from Transformers)从未标注的文本同时向左右两边对所有层次进行深度双向表达预处理。
BERT可以对输出层微调就能解决很多任务，比如问题回答、句子推理命名体识别而不需要大量特定于任务的框架修改。
对于处理下游任务有两种策略：基于特征（EMLo）、模型微调（GPT from OpenAI）
BERT利用MLM(Masked Language Model)预处理方法缓解了GPT预处理无向的弱点；除此之外还运用了next sentence prediction对联合文本的表示。

2. Related Work
Unsupervised Feature-based Approaches
Unsupervised Fine-tuning Approaches
Transfer Learning from Supervised Data

3. BERT
结构分为两部分：pre-training, fine-tuningWordPiece embeddings
在预处理中BERT通过对未标记的文本进行训练；在微调阶段BERT模型用预处理中的参数进行初始化，并且在所有下游任务中参数都需要微调
模型架构：
变量和模型：
    number of layers: L
    hidden size: H
    number of self-attention heads:A
    BERT(BASE) (L=12, H=768, A=12, Total Parameters=110M)
    BERT(LARGE) (L=24, H=1024,A=16, Total Parameters=340M)
base的大小和OpenAI的GPT的模型大小一样，用于作比较
Input/Output Representation:
    为了可以让BERT模型解决大量的下游任务，输入层能够明确地用一个token sequence表示单个句子或一对句子。
    (A “sequence” refers to the input token sequence to BERT, which may be a single sentence or two sentences packed together.)
    sentence可以是任意的连续文本，而不仅限于语言上的一个句子，它是BERT的输入。
    利用WordPiece Embeddings方法，词库数量为30000。每一个句子的第一个token总是classification token。
    这个token的隐藏作用是未分类任务做准备，一个句子对被当作一个sentence。
    从两种方式区别这些句子：首先用一个特殊的token将两个句子分开。其次对每一个token嵌入一个学习过的向量来表示是属于哪一个句子的。
3.1 pre-training BERT
利用两种无监督学习任务来进行预处理。
任务1：Masked LM
    为了可以训练一个深度双向的representation，在句子中随机抽取一定百分比的tokens进行masked，并且预测这些masked
    这个比例通常是15%
    利用masked的预测方法以代替重新构造全局的输入
    尽管这个方法可以提供一个双向预训练的模型，但是有一个缺点是pre-training和fine-tuning无法匹配的问题。原因是masked tokens在后者未出现
    为了缓解这个问题，我们不会每一次都用真实地masked token来替换随机抽取的token。
    在选中的15%的token中，80%会用真实masked token替换，10%随机选择token替换，10%不会做出任何改变
    然后Ti会被通过交叉熵来预测原始的token
任务2：Next Sentence Prediction
    许多下游任务需要处理两个相关联的句子，比如机器回答和词语推理等。因此引入了NSP、
    在A、B两个句子中如果B是A的真实下一句话，则被标记为（IsNext）否则（NotNext）

Pre-training data
BooksCorpus and English Wikipedia

3.2 Fine-tuning BERT

4 Experiments


