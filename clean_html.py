# _*_ coding utf-8 _*_
'''
观察PDF2htmlEX程序处理PDF文件生成的HTML代码发现其中很多无用标签，既不会影响内容输出，也不会影响网页结构
输入PDF转换后生成到本地的HTML文件
正则化去除其中的空格标签<span></span>
输出清理后的HTML文件clean_html：str类型
'''

import re


def clean_html(html_file1):
    with open(html_file1, encoding='utf-8') as f:
        html_content = f.read()

    after_clean1 = html_content.replace('</span>', '')
    clean_str = r'\<span.*?\>'
    after_clean2 = re.sub(clean_str, '', after_clean1)
    return after_clean2


if __name__ == '__main':
    html_file = 'pdf2html/test.html'
    after_clean = clean_html(html_file)
    print(after_clean)
