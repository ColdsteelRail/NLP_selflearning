# [Word2Vec] Efficient Estimation of Word Representations in Vector Space (Google 2013)
---
# 1. Introuduction
- =.=！略

# 2. Model Architecture 
- 利用distributed representations of words learned by neural networks表示
- 随机梯度下降 stochastic gradient descent和反向传播backpropagation
- 模型训练时间复杂度：$O = E × T × Q$
    1. $E$ is number of the training epochs
    2. $T$ is the number of the words in the training set
    3. $Q$ is defined further for each model architecture

# 3. New Log-Linear Models(Two)
**Purpose**:  learning distributed representations of words that try to minimize computational complexity
### Continuous Bag-of-Words Model
$Q = N × D + D × \log_2^V$
### Continuous Skip-gram Model

