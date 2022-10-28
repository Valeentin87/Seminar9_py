from PIL import Image, ImageDraw
import draw_line
import view

# ------------- модуль, задающий область для рисования и проводящий отрезок по двум точкам ---------------------


def lenght():
    list = view.coordinate()
    # Пустой желтый фон.
    im = Image.new('RGB', (500, 300), (219, 193, 27))
    draw = ImageDraw.Draw(im)
    # рисуем отрезок по введенным координатам
    draw.line((list[0], list[1], list[2], list[3]), fill='pink', width=10)
    im.show()


# ------------- модуль, задающий область для рисования и рисующий эллипс ---------------------


def ellips():
    list = view.coordinate_ellips()
    # Пустой желтый фон.
    im = Image.new('RGB', (500, 300), (219, 193, 27))
    draw = ImageDraw.Draw(im)
    # рисуем отрезок по введенным координатам
    draw.ellipse((list[0], list[1], list[2], list[3]), 'yellow', 'blue')
    im.show()

