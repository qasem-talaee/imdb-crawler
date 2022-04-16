import platform

def recognize_os():
    os = platform.system()
    if os == 'Linux':
        return 'driver/linux/geckodriver'
    elif os == 'Windows':
        return 'driver/windows/geckodriver.exe'
    else:
        return 'driver/mac/geckodriver'