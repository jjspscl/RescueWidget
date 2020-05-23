import gi

from gi.repository import Gtk, Gdk

class SettingsWidget(Gtk.Window):
    def __init__(self):
        self.self_position(Gtk.WindowPosition.CENTER)
        print("Init")