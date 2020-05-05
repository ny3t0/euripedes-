font = CurrentFont()

glyphName = 'uni021B'

# before removing a glyph, make sure it actually exists in the font
if glyphName in font:
    del font[glyphName]
else:
    print("font does not contain a glyph named '%s'" % glyphName)

# if we try to remove a glyph which is not in the font,
# and error will be raised
del font['spam']