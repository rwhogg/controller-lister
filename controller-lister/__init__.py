# Copyright 2021 Bob "Wombat" Hogg
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import sys

from guizero import App, Box, Text
import pygame

def render_controllers():
    for child in app.children:
        child.destroy()
    box = Box(app)
    message = Text(box, text="Detected Controllers\n")
    count = pygame.joystick.get_count()
    controllers = [pygame.joystick.Joystick(x) for x in range(count)]
    i = 0
    for controller in controllers:
        controller_name = controller.get_name()
        controller_guid = controller.get_guid()
        controller_power_level = controller.get_power_level()
        name_text = Text(box, controller_name)
        guid_text = Text(box, controller_guid)
        power_level_text = Text(box, "Power Level: " + controller_power_level)
        i += 1

def check_controllers():
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.JOYDEVICEADDED or event.type == pygame.JOYDEVICEREMOVED:
            render_controllers()

if __name__ == "__main__":
    pygame.display.init()
    pygame.joystick.init()
    app = App(title="Controller Lister")
    app.repeat(1000, check_controllers)
    app.display()
