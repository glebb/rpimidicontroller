import platform

class BaseConfig:
    MODULES = ('web', 'numpad')
    SERVERNAME = '0.0.0.0:5000'
    MIDICHANNEL = 1
    
    @staticmethod
    def shutdown():
        pass

class Linux(BaseConfig):
    SERVERNAME = '0.0.0.0:80'

    @staticmethod
    def shutdown():
        call("echo heartbeat | sudo tee /sys/class/leds/led0/trigger", shell=True)
        call("echo heartbeat | sudo tee /sys/class/leds/led1/trigger", shell=True)
        call("sudo shutdown -h now", shell=True)


class Darwin(BaseConfig):
    @staticmethod
    def shutdown():
        print "quitting"
    pass

class Windows(BaseConfig):
    pass

Config = eval(platform.system())