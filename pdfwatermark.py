from io import BytesIO
from re import match

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
from webcolors import hex_to_rgb
import click


@click.command()
@click.argument('filename')
@click.option('-w', '--watermark', default='TEST',
              help='Annotation text, use {} to include parts of file name if '
                   'you are using --regex')
@click.option('-r', '--regex', default='',
              help='Regex to run on file name, annotation is used as template')
@click.option('-f', '--font-name', default='Helvetica-Bold',
              help='Font name')
@click.option('-s', '--font-size', default=85, type=int,
              help='Font size')
@click.option('-c', '--color', default='#000000',
              help='Font colour')
@click.option('-o', '--opacity', default=1.0,
              help='Opacity from 0 (transparent) to 1 (solid)')
@click.option('-x', default=250,
              help='X coordinate')
@click.option('-y', default=250,
              help='Y coordinate')
@click.option('-d', '--destination-file-name', default='',
              help='Destination file, by default files are modified in place')
@click.option('-p', '--page-number', default='1',
              help='page number')
def annotate(filename, watermark, regex, font_name, font_size, color, opacity,
             x, y, destination_file_name, page_number):
    print ("page number:", page_number)
    mask_stream = BytesIO()
    watermark_canvas = canvas.Canvas(mask_stream, pagesize=A4)
    watermark_canvas.setFont(font_name, font_size)
    r, g, b = hex_to_rgb(color)
    c = Color(r, g, b, alpha=opacity)
    watermark_canvas.setFillColor(c)

    if regex:
        groups = match(regex, filename)
        watermark = watermark.format(*groups.groups())
    watermark_canvas.rotate(10)
    for index in range(0, 10):
        x1 = x + index * 40
        x0 = x1 - 300
        x2 = x1 + 300
        x3 = x2 + 300

        watermark_canvas.drawString(x1, y + index * 100, watermark)
        watermark_canvas.drawString(x2, y + index * 100, watermark)
        watermark_canvas.drawString(x0, y + index * 100, watermark)

   
    watermark_canvas.save()

    mask_stream.seek(0)

    mask = PdfFileReader(mask_stream)
    src = PdfFileReader(filename)
    output = PdfFileWriter()

    for index in range(0, src.getNumPages()):
        page = src.getPage(index)
        page.mergePage(mask.getPage(0))
        output.addPage(src.getPage(index))

    if not destination_file_name:
        destination_file_name = filename

    with open(destination_file_name, "wb") as output_stream:
        output.write(output_stream)


if __name__ == '__main__':
    annotate()
