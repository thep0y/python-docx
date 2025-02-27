#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:      thepoy
# @Email:       thepoy@163.com
# @File Name:   shared.pyi
# @Created At:  2023-03-20 18:42:36
# @Modified At: 2023-03-20 19:04:30
# @Modified By: thepoy

from docx.oxml.styles import CT_Style

class ElementProxy:
    _element: CT_Style

class Length(int): ...
class Inches(Length): ...
class Cm(Length): ...
class Mm(Length): ...
class Pt(Length): ...
class Twips(Length): ...
class Emu(Length): ...

class RGBColor(tuple[int, int, int]):
    def __new__(cls, r: int, g: int, b: int) -> RGBColor: ...
