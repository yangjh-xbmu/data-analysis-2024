import mykey  # mykey.py文件中存放SPARKAI_APP_ID等变量的值，例如：SPARKAI_APP_ID = '575a00d1'
import pandas as pd
import pdfplumber
import random

from IPython.display import Markdown as render
from typing import Optional

systemprompt = "基于已有知识，回答用户的问题。如果不了解，请直接回答不了解。"

def mdContent(content: str, cssFile: str = "githubTheme.css") -> str:
    """
    为Markdown文本增加指定的CSS文件。

    参数:
    content (str): 要渲染的Markdown内容
    cssFile (str, optional): 要应用的CSS文件路径，默认为"githubTheme.css"

    返回值:
    str: 渲染后的HTML内容
    """

    markdown_text = f"""
<link rel="stylesheet" href="{cssFile}">

{content}
"""
    return markdown_text


def xfllm(xfchatmessage: str) -> str:
    """
    使用星火认知大模型Spark Max生成对话回复。

    参数:
    xfchatmessage (str): 用户输入的对话消息。

    返回值:
    str: 生成的对话回复。
    """
    from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
    from sparkai.core.messages import ChatMessage

    # 星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
    # 星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
    SPARKAI_APP_ID = mykey.SPARKAI_APP_ID
    SPARKAI_API_SECRET = mykey.SPARKAI_API_SECRET
    SPARKAI_API_KEY = mykey.SPARKAI_API_KEY
    # 星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_DOMAIN = '4.0Ultra'

    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    prompt = xfchatmessage
    messages = [ChatMessage(
        role="user",
        content=prompt
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    return a.generations[0][0].text


def cognitive_load_explain(message: str) -> None:
    """
    根据认知负荷理论，通俗易懂地解释用户的提问，并生成两个测试题。

    参数:
    message (str): 用户提出的问题或主题。

    返回值:
    None: 该函数仅打印解释和测试题，不返回任何值。
    """
    prompt = f'''
    请扮演经验丰富的Python教学专家，我是一个Python的初学者，没有任何编程经验。
    请依据认知负荷理论，通俗易懂地解释我的提问:{message}，并在最后生成2个测试题，但不要给出答案。'''
    return mdContent(dsllm(prompt))


def detect_text_errors(text: str) -> str:
    """
    检测文本中的错别字和标点符号错误。

    参数:
    text (str): 需要检测的文本

    返回值:
    检查结果
    """
    prompt = f'''
    请扮演严谨的文字校对编辑，就提供的文本：
    <txt>
    {text}
    </txt>，
    查找错别字、标点符号错误。将错误和纠正的内容，用Markdown表格的形式呈现。
    '''
    return dsllm(prompt)


def dsllm(message: str) -> str:
    """
    使用 DeepSeek 的聊天模型生成回复。

    参数:
    message (str): 用户输入的消息

    返回值:
    str: 模型生成的回复
    """
    from openai import OpenAI

    client = OpenAI(api_key=mykey.api_key,
                    base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": f"请按照{systemprompt}进行内容生成前的准备工作。但不要将该过程作为内容输出"},
            {"role": "user", "content": message},
        ],
        stream=False
    )

    return response.choices[0].message.content


def translate(中文内容: str) -> str:
    """
    将给定的中文内容翻译成英语，并提供音标和例句。

    参数:
    中文内容 (str): 需要翻译的中文文本

    返回值:
    str: 包含翻译结果、音标和例句的字符串
    """
    提示词 = f'''
    请扮演地道美国语言专家，并且精通汉语，请将以下内容翻译成英语：

    <content>
    {中文内容}
    </content>

    要求：

    1. 给出音标、例句等内容。
    2. 用Markdown表格整理内容，表头为中文、英文、音标、例句。
    '''
    return dsllm(提示词)


def genAnkiCardFile(学习内容: str, 文件名称: str) -> str:
    """
    根据给定的学习内容生成Anki学习卡片，并将结果保存到指定文件中。

    参数:
    学习内容 (str): 需要生成Anki卡片的学习内容。
    文件名称 (str): 保存生成的Anki卡片内容的文件名。

    返回值:
    生成的卡片内容
    """

    提示词 = f'''
    ## 角色

    请扮演教学专家，能熟练应用各种学习相关的理论。

    ## 任务

    请根据【卡片格式资料】，为【学习内容】<content>{学习内容}</content>生成 Anki 学习卡片。

    ### 卡片格式资料
    """markdown

    ## headline. For example, below markdown will generate 2 cards where headlines will be on the front side and its description - on the back.
    Anki for VSCode splits cards by

    ## What's the Markdown?

    Markdown is a lightweight markup language with plain-text-formatting syntax.
    Its design allows it to be converted to many output formats,
    but the original tool by the same name only supports HTML.

    ## Who created Markdown?

    John Gruber created the Markdown language in 2004 in collaboration with
    Aaron Swartz on the syntax.
    """

    ### 要求

    1. 一张卡片一个知识点
    2. 卡片的标题必须为`##`开头
    
    '''
    result = dsllm(提示词)
    with open(文件名称, "w", encoding='UTF-8') as file:
        # 将Markdown内容写入文件
        file.write(result)
    return result


def openFile(文件名称: str) -> str:
    """
    打开并读取指定文件的内容。

    参数:
    文件名称 (str): 要打开的文件的名称或路径

    返回值:
    str: 文件的内容
    """
    with open(文件名称, 'r', encoding='UTF-8') as file:
        # 读取文件内容
        content = file.read()
        # 返回文件内容
        return content


def refineFunction(functionName: callable) -> str:
    """
    根据传入的函数内容，补充函数的说明内容，并打印优化后的函数源代码。

    参数:
    functionName (callable): 需要优化的函数

    返回值:
    str: 优化后的函数源代码
    """
    import inspect

    # 获取函数的源代码
    source_code = inspect.getsource(functionName)

    提示词 = f'''
    ## 角色

    Python编程专家

    ### 任务

    根据传入的函数内容和功能，重写函数的Docstring。

    ### 步骤

    1. 删除传入函数的已有Docstring
    2. 然后根据实际功能，重写Docstring，函数的参数要有变量类型，要有函数返回值的类型
    3. 优化函数的代码

    ###  案例

    Python 3.5 引入了类型提示（Type Hints），可以在函数定义中指定参数和返回值的类型。结合文档字符串，可以更清晰地描述函数的使用方法。

    def add(a: int, b: int) -> int:
        """
        返回两个数的和。

        参数:
        a (int): 第一个加数
        b (int): 第二个加数

        返回值:
        int: 两个数的和
        """
        return a + b

    ### 需要完善的函数

    <function>
    {source_code}
    </function>
    '''
    return dsllm(提示词)


def saveContent(学习内容: str, 文件名称: str) -> str:
    """
    将指定的Markdown内容写入文件，并返回写入的内容。

    参数:
    学习内容 (str): 要写入文件的Markdown内容。
    文件名称 (str): 目标文件的名称，包含文件路径。

    返回值:
    str: 写入文件的Markdown内容。
    """
    with open(文件名称, "w", encoding='UTF-8') as file:
        file.write(学习内容)
    return 学习内容


def voc_txt_to_markdown(text):
    lines = text.strip().split('\n')
    markdown_lines = []

    for line in lines:
        if line.strip():
            word, definition = line.split('/', 1)
            word = word.strip()
            markdown_lines.append(f"## {word}\n\n{line.strip()}\n")

    return '\n'.join(markdown_lines)


def extract_table_from_pdf(pdf_path: str, start: int, end: Optional[int] = None) -> pd.DataFrame:
    """
    从PDF文件中提取指定页码范围内的表格数据，并返回一个DataFrame。

    参数:
    pdf_path (str): PDF文件的路径。
    start (int): 开始提取表格的页码（包含）。
    end (Optional[int]): 结束提取表格的页码（不包含）。如果未提供，则提取从start页开始的所有页面。

    返回值:
    pd.DataFrame: 包含提取表格数据的DataFrame。
    """
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        # 如果end参数没有值，则提取从start页开始的所有页面
        if end is None:
            pages = pdf.pages[start:]
        else:
            pages = pdf.pages[start:end]

        for page in pages:
            tables = page.extract_tables()
            all_tables.extend(tables)

    # 将所有表格数据合并为一个DataFrame
    df = pd.DataFrame()
    for table in all_tables:
        df = pd.concat([df, pd.DataFrame(table)], ignore_index=True)

    return df


def goodmanKruska_tau_y(df, x: str, y: str) -> float:
    """ 取得条件次数表 """
    cft = pd.crosstab(df[y], df[x], margins=True)
    """ 取得全部个案数目 """
    n = cft.at['All', 'All']
    """ 初始化变量 """
    E_1 = E_2 = tau_y = 0

    """ 计算E_1 """
    for i in range(cft.shape[0] - 1):
        F_y = cft['All'][i]
        E_1 += ((n - F_y) * F_y) / n
    """ 计算E_2 """
    for j in range(cft.shape[1] - 1):
        for k in range(cft.shape[0] - 1):
            F_x = cft.iloc[cft.shape[0] - 1, j]
            f = cft.iloc[k, j]
            E_2 += ((F_x - f) * f) / F_x
    """ 计算tauy """
    tau_y = (E_1 - E_2) / E_1

    return tau_y


def 相关系数强弱判断(相关系数值):
    """ 相关系数强弱的判断 
    补充参考文献
    """
    if 相关系数值 >= 0.8:
        return '极强相关'
    elif 相关系数值 >= 0.6:
        return '强相关'
    elif 相关系数值 >= 0.4:
        return '中等程度相关'
    elif 相关系数值 >= 0.2:
        return '弱相关'
    else:
        return '极弱相关或无相关'


def 制作交叉表(数据表, 自变量, 因变量):
    return pd.crosstab(数据表[自变量], 数据表[因变量], normalize='columns', margins=True)


def calling_the_roll(名册):
    # 读取Excel文件
    file_path = 名册  # 替换为你的Excel文件路径

    # 读取Excel文件中的数据
    df = pd.read_excel(file_path)

    # 假设学生姓名在第一列，列名为 'Name'
    students = df['姓名'].tolist()

    # 随机选择一个学生姓名
    selected_student = random.choice(students)

    print(f"随机抽取的学生姓名是: {selected_student}")

def 两个无序类别变量的统计分析(数据表, 自变量, 因变量):
    """ 对两个无序类别变量进行描述统计和推论统计，并给出辅助结论 """
    # 计算相关系数
    tau_y = goodmanKruska_tau_y(数据表, 自变量, 因变量)
    # 制作交互分类表
    交互表 = pd.crosstab(数据表[F"{自变量}"], 数据表[F"{因变量}"])
    # 进行卡方检验
    chi2, p, dof, ex = stats.chi2_contingency(交互表)

    print(F"tau_y系数:{tau_y: 0.4f}", 相关系数判断(tau_y))
    print(tabulate(交互表))
    print(F"卡方值：{chi2: .2f}, p值：{p: .4f},自由度:{dof}。")
    print(p值判断(p))

def p值判断(p: float, α=0.05):
    """ p值判断 """
    if p <= α:
        return '拒绝虚无假设'
    else:
        return '接受虚无假设'