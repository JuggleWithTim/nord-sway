#!/usr/bin/env python3
"""Rebuild seamless center strips and wallpaper from the checked-in sources."""
from pathlib import Path
import cairo
import gi
gi.require_version('Rsvg', '2.0')
from gi.repository import Rsvg

assets = Path(__file__).resolve().parent.parent / 'assets'
for state in ['normal', 'over', 'down', 'disabled']:
    image = cairo.ImageSurface.create_from_png(str(assets / 'buttons' / f'button_{state}_middle.png'))
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 2048, image.get_height())
    context = cairo.Context(surface)
    pattern = cairo.SurfacePattern(image)
    pattern.set_extend(cairo.EXTEND_REPEAT)
    pattern.set_filter(cairo.FILTER_NEAREST)
    context.set_source(pattern)
    context.paint()
    surface.write_to_png(str(assets / 'buttons' / f'button_{state}_middle_wide.png'))

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 2560, 1440)
viewport = Rsvg.Rectangle()
viewport.x = viewport.y = 0
viewport.width, viewport.height = 2560, 1440
Rsvg.Handle.new_from_file(str(assets / 'wallpaper.svg')).render_document(cairo.Context(surface), viewport)
surface.write_to_png(str(assets / 'wallpaper.png'))
print('Regenerated button strips and wallpaper.')
