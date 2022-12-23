import eel


def init_eel():
    eel.init('web')
    eel.start('index.html', app_mode=True, mode="chrome")


if __name__ == "__main__":
    init_eel()