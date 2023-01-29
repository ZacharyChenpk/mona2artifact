# Artifact from Mona (YAS) to Genmo Calculator

本repo的代码可以将莫娜占卜铺（及YAS，Yet Another Genshin Impact Scanner）中导出的圣遗物json文件转化成原魔计算器可以读取的格式。

莫娜占卜铺提供了YAS插件，使用cv算法扫描原神背包中的圣遗物。而提供圣遗物伤害精确计算与配装的原魔计算器只能手动输入圣遗物，或是通过外源OCR账户来进行扫描，较为麻烦。本repo可以使用户利用YAS插件自动导出的圣遗物载入原魔计算器进行计算。

在使用中遇到任何问题，请与作者联系或直接issue。

### 如何使用
1. 使用YAS获得json文件
2. 将mona2artifact.json第5行的文件名改为YAS获得的json文件
3. 将mona2artifact.json第6行的文件名改为需要输出的文件名
4. 运行 ```python mona2artifact.py ```
5. 将获得的新文件导入原魔计算器

### 相关链接
莫娜占卜铺：https://mona-uranai.com/

Yet Another Genshin Impact Scanner：https://github.com/wormtql/yas

原魔计算器：https://genshin.mingyulab.com/artifact_set_compare/artifact_set_compare?r=9bdf8cd94ece43eca2d023504baa4086