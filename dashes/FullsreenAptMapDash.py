from GlobalVariables import *
from ui_image_kit.FullscreenView import *
import os
from PIL import Image, ImageDraw, ImageFont
import datetime
from dashes.Dash import Dash


class FullScreenAptMapDash(Dash):
    def __init__(self, context, loader, dash_type, seconds_in_advance):
        Dash.__init__(self, dash_type, seconds_in_advance)
        self.context = context
        self.loader = loader
        self.apt_map = loader.get_bw_image('apt.png')
        # There would be an image resize, but this image is exact fit for the display
        self.font_big = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 48)
        self.font_small = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)


    def drawContent(self):
        # Fill white over everything
        self.context.draw.rectangle((0, 0, self.context.width, self.context.height), fill=255)
        time = datetime.datetime.now()
        adjusted_time = time - datetime.timedelta(seconds=self.seconds_in_advance)
        formatted_time = adjusted_time.strftime("%H:%M")

        self.draw_map()
        self.draw_clock(formatted_time)

    def draw_map(self):
        apt_map_offset = (0, 0)
        self.context.image.paste(self.apt_map, apt_map_offset)

    def draw_clock(self, time_string):
        clock_offset = (72, 24)
        self.context.draw.text(clock_offset, time_string, font=self.font_big, fill=0)
        message_offset = (72, 24+48)
        self.context.draw.text(message_offset, 'broker offline', font=self.font_small, fill=0)
