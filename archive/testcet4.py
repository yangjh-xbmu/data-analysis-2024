def convert_to_markdown(text):
    lines = text.strip().split('\n')
    markdown_lines = []

    for line in lines:
        if line.strip():
            word, definition = line.split('/', 1)
            word = word.strip()
            markdown_lines.append(f"## {word}\n\n{line.strip()}\n")

    return '\n'.join(markdown_lines)

# 输入文本
txt_text = """
abandon /ə’bændən/ vt.丢弃;放弃，抛弃
aboard /ə’bɔ:d/ ad.在船(车)上;上船
"""

# 转换为Markdown格式
markdown_output = convert_to_markdown(txt_text)

# 输出结果
print(markdown_output)
