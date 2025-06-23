from server.controllers.base_controller import BaseController
from server.models.guest import Guest

class GuestController(BaseController):
    model = Guest
