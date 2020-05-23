import gi

from gi.repository import Gtk, Gdk

class SettingsWidget(Gtk.Window):
    def __init__(self):
        super(SettingsWidget, self).__init__()
        self.set_position(Gtk.WindowPosition.CENTER)
        self.screen = self.get_screen()
        self.visual = self.screen.get_rgba_visual()
        self.set_default_size(600, 300)
        self.show_all()
        print("Init")