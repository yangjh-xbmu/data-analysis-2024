from openai import OpenAI


def xfllm(prompt: str):
    '''
    调用星火认知大模型4.0Ultra
    参数prompt：传入到大模型的提示词，应为字符串
    返回值：大模型返回的文本值
    '''
    from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
    from sparkai.core.messages import ChatMessage

    # 星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
    # 星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
    SPARKAI_APP_ID = '575a00d1'
    SPARKAI_API_SECRET = 'NDIzNGRlNjUwNjhlNDg4MThjNWM3OGYz'
    SPARKAI_API_KEY = '6730233db135955bbbaf55901b3f296e'
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
    messages = [ChatMessage(
        role="user",
        content=prompt
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    return a.generations[0][0].text

# print(xfllm('你的版本是多少'))

# Please install OpenAI SDK first: `pip3 install openai`


# Please install OpenAI SDK first: `pip3 install openai`

def dsllm(userprompt: str, sysprompt="请回答用户的问题，如不知道，请不要虚构"):
    '''
    调用Deepseek大模型

    参数：

    userprompt：用户角色提示词
    sysprompt： system 角色提示词

    返回值：
    返回大模型生成的文本内容
    '''
    client = OpenAI(api_key="sk-f5801b0ee8a946b18e93029e76e0dd99",
                    base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": sysprompt},
            {"role": "user", "content": userprompt},
        ],
        stream=False
    )

    return (response.choices[0].message.content)


# print(dsllm('请问2024年10月11日，中国的重要新闻'))
