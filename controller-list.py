import sys

from guizero import App, Box, Text
import pygame

def render_controllers():
    for child in app.children:
        child.destroy()
    box = Box(app)
    message = Text(box, text="Detected Controllers")
    count = pygame.joystick.get_count()
    controllers = [pygame.joystick.Joystick(x) for x in range(count)]
    i = 0
    for controller in controllers:
        controller_name = controller.get_name()
        controller_guid = controller.get_guid()
        name_text = Text(box, controller_name)
        guid_text = Text(box, controller_guid)
        i += 1

def check_controllers():
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.JOYDEVICEADDED or event.type == pygame.JOYDEVICEREMOVED:
            render_controllers()

pygame.display.init()
pygame.joystick.init()
app = App(title="Controller Lister")
app.repeat(1000, check_controllers)
app.display()
