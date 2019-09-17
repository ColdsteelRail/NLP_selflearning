## 1. DatasetReader/Model
再利用AllenNLP实现模型之前，必须写两部分代码：DatasetReader/Model。
在这个教程中，需要预测一篇学术论文发表场合。具体来说，就是给出一篇论文摘要，判断它是“自然语言处理领域”、“机器学习领域”还是“人工智能领域”的论文。
### DatasetReader
数据是JSON格式，每个文件都包含title，paperAbstract和venue

    {
        "title": "A review of Web searching studies and a framework for future research",
        "paperAbstract": "Research on Web searching is at an incipient stage. ...",
        "venue": "{AI|ML|ACL}"
    }
接下来需要编写读取文件的代码，并且对这些代码进行测试。测试代码要采用AllenNLP中提供的测试接口。