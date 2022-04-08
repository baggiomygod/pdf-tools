# 使用
# py ./docxToPdf/index.py -t ./example.docx ./example.pdf

from docx2pdf import convert
import click
@click.command()
# 输出文件名
@click.argument('filename')
# 目标文件
@click.option('-df', '--docx-file', help='target file')
def docxToPdf(docx_file, filename):
  convert(docx_file, filename)

if __name__ == '__main__':
  docxToPdf()