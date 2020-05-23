import gi
import math

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class TrayIcon(Gtk.StatusIcon):
    def __init__(self):
        Gtk.StatusIcon.__init__(self)
        self.set_from_icon_name('rescue-widget')
        self.set_has_tooltip(True)
        self.set_visible(True)
        self.connect("popup_menu", self.on_secondary_click)

    def on_secondary_click(self, widget, button, time):
        menu = Gtk.Menu()

        menu_item1 = Gtk.MenuItem("Settings")
        menu.append(menu_item1)


        menu_item2 = Gtk.MenuItem("Quit")
        menu.append(menu_item2)
        menu_item2.connect("activate", Gtk.main_quit)

        menu.show_all()
        menu.popup(None, None, None, self, 3, time)


class MainWidget(Gtk.Window):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_app_paintable(True)
        self.set_resizable(False)
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_titlebar()
        self.screen = self.get_screen()
        self.visual = self.screen.get_rgba_visual()
        self.set_visual(self.visual)
        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(400, 300)
        darea = Gtk.DrawingArea()
        darea.connect("draw", self.expose)
        self.add(darea)
        self.show_all()

    def expose(self, widget, event):
        width = self.get_allocated_width()
        height = self.get_allocated_height()
        cr = widget.get_property('window').cairo_create()
        cr.set_source_rgb(0.6, 0.6, 0.6)
        cr.translate(width / 2, height / 2)
        cr.arc(0,
               0, 50,
               0, 2 * math.pi)
        cr.fill()


if __name__ == '__main__':
    tray = TrayIcon()
    MainWidget()
    Gtk.main()
