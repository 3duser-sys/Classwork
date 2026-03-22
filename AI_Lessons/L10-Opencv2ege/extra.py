import pyglet
from pyglet import gl
import win32gui, win32con
import time

# Find Minecraft window
hwnd = None
while not hwnd:
    hwnd = win32gui.FindWindow(None, "Minecraft")
    time.sleep(0.5)
print("Minecraft found!")

# Get window size
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
width, height = right-left, bottom-top

# Create transparent click-through window
config = pyglet.gl.Config(double_buffer=True)
window = pyglet.window.Window(width, height,
                              style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS,
                              resizable=False,
                              vsync=True,
                              config=config)
window.set_location(left, top)

# Click-through
hwnd_overlay = window._hwnd
win32gui.SetWindowLong(hwnd_overlay, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd_overlay, win32con.GWL_EXSTYLE) |
                       win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
win32gui.SetLayeredWindowAttributes(hwnd_overlay, 0, 255, win32con.LWA_ALPHA)

@window.event
def on_draw():
    window.clear()
    gl.glColor3f(1, 0, 0)  # red points
    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2f(width/2, height/2)
    gl.glEnd()

pyglet.app.run()