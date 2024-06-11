from MCprompts import loadPlant, loadPayload
from colors import Color

class MoveComplete:
    def __init__(self) -> None:
        self.plant = ""
        self.url = ""

    def moveEm(self):
        self.plant = loadPlant()

        self.url = f'https://{self.plant}qa.jbssa.com/API/iws/inbound/movecomplete'

        loadPayload(self.url)

if __name__ == "__main__":
    print(Color.RED, "DO NOT RUN THIS SCRIPT DIRECTLY.", Color.RESET)