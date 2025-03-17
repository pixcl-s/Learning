
class PowerOutlet:
    def connect_device_to_power_outlet(self, device): pass


class HDMICable(PowerOutlet):
    def connect_to_device_via_hdmi_cable(self, device): pass


class RCACable(PowerOutlet):
    def connect_to_device_via_rca_cable(self, device): pass


class Ethernet(PowerOutlet):
    def connect_to_device_via_ethernet_cable(self, device): pass


class Television(RCACable, HDMICable):
    def connect_to_dvd(self, dvd_player): self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console): self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self): self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMICable):
    def connect_to_tv(self, television): self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self): self.connect_device_to_power_outlet(self)


class GameConsole(HDMICable, Ethernet):
    def connect_to_tv(self, television): self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router): self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self): self.connect_device_to_power_outlet(self)


class Router(Ethernet):
    def connect_to_tv(self, television): self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console): self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self): self.connect_device_to_power_outlet(self)


# We have been hired to create a game where the player sets up entertainment systems.
# Each piece of the system (television, game console, etc.) uses a specific cable to connect to another device.
# The TV uses an HDMI cable to connect to a game console.
# Both the game console and TV connect to a router via an ethernet cable to access the internet.
# And lastly, all the devices are connected to the wall via a power cable so they can turn on.
# Your job is to extend this behavior in the device classes.

# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass
#
#
# class Television(EntertainmentDevice):
#     def connect_to_dvd(self, dvd_player):
#         self.connect_to_device_via_rca_cable(dvd_player)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_hdmi_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class DVDPlayer(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class GameConsole(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def connect_to_router(self, router):
#         self.connect_to_device_via_ethernet_cable(router)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class Router(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_ethernet_cable(television)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_ethernet_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
