#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:      thepoy
# @Email:       thepoy@163.com
# @File Name:   font.pyi
# @Created At:  2023-03-20 16:41:45
# @Modified At: 2023-03-20 18:14:52
# @Modified By: thepoy

from docx.dml.color import ColorFormat
from docx.shared import ElementProxy, Pt

class Font(ElementProxy):
    @property
    def size(self) -> Pt: ...
    @size.setter
    def size(self, emu: Pt) -> None: ...
    @property
    def color(self) -> ColorFormat: ...
