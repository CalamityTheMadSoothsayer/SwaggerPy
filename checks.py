from colors import Color

def checkBarcode(inputStr):
    if inputStr.isdigit() and len(inputStr) == 46:
        return True
    else:
        return False

if __name__ == "__main__":
    print(Color.RED, "DO NOT RUN THIS SCRIPT DIRECTLY.", Color.RESET)