import os
import sys

# pi install win32com
from win32com import client


# 报错 
# error (-2147352567, '发生意外。', (0, 'Kingsoft WPS', '文档打开失败。', '', 3010, -786427), None)

def docx2pdf(docName, pdfName):
  """
      :word文件转pdf
      :param docName word文件名称
      :param pdfName 转换后pdf文件名称
  """
  try:
      word = client.DispatchEx("Word.Application")
      if os.path.exists(docName):
          print('docName:', docName)
        #   os.remove(pdfName)
          worddoc = word.Documents.Open(docName, ReadOnly=1)
          worddoc.SaveAs(pdfName, FileFormat=17)
          worddoc.Close()
          return pdfName
  except Exception as e:
      print('error', e)
      return 1

docx2pdf(sys.argv[1], sys.argv[2])