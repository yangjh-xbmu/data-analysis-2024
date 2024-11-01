def xfllm(content):
    from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
    from sparkai.core.messages import ChatMessage

    #星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
    #星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
    SPARKAI_APP_ID = ''
    SPARKAI_API_SECRET = ''
    SPARKAI_API_KEY = ''
    #星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
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
            content=content
        )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    return a.generations[0][0].text
    # print(a)

# result = xfllm('你好')

# print(result)
