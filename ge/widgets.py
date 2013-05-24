from pyvi.editor import Editor
import urwid


class GE(urwid.MainLoop):
    def __init__(self, editor=None):
        if editor is None:
            editor = Editor()
        self.editor = editor

        super(GE, self).__init__(
            widget=Tab(self.editor.active_tab),
            event_loop=urwid.TwistedEventLoop(),
        )

    def process_input(self, keys):
        for key in keys:
            self.editor.keypress(key)
        super(GE, self).process_input(keys)


class Tab(urwid.WidgetWrap):
    def __init__(self, tab):
        self.tab = tab
        self.windows = [
            urwid.Pile([Window(window) for window in row]) for row in tab
        ]
        super(Tab, self).__init__(urwid.Columns(self.windows))


class Window(urwid.WidgetWrap):
    def __init__(self, window):
        super(Window, self).__init__(urwid.ListBox(WindowWalker(window)))
        self.window = window


class WindowWalker(object):
    def __init__(self, window):
        self.buffer = window.buffer
        self.window = window
        self.set_focus(0)

    def get_next(self, position):
        position += 1
        if position == self.focus:
            widget = self.focus_widget
        else:
            widget = Line(self.window, position)
        return widget, position

    def get_prev(self, position):
        if position <= 0:
            return None, None
        else:
            position -= 1
            if position == self.focus:
                widget = self.focus_widget
            else:
                widget = Line(self.window, position)
            return widget, position

    def get_focus(self):
        return self.focus_widget, self.focus

    def set_focus(self, focus):
        # if self.buffer.done_reading:
        #     focus = max(focus, len(self.buffer) - 1)
        self.focus = focus
        self.focus_widget = Line(self.window, focus)


class Line(urwid.Text):

    _align_mode = urwid.LEFT
    _cache_maxcol = None
    _wrap_mode = urwid.ANY
    layout = urwid.text_layout.default_layout

    def __init__(self, window, index):
        self.window = window
        self.buffer = window.buffer
        self.index = index

    def render(self, size, focus=False):
        canvas = super(Line, self).render(size, focus=focus)
        if focus:
            canvas = urwid.CompositeCanvas(canvas)
            canvas.cursor = self.get_cursor_coords(size)
        return canvas

    def selectable(self):
        return True

    def get_text(self):
        try:
            return self.buffer[self.index], []
        except IndexError:
            return u"", []

    def set_text(self, new):
        self.buffer[self.index] = new

    def get_cursor_coords(self, size):
        return tuple(reversed(self.window.cursor))

    def keypress(self, size, key):
        self._invalidate()
