import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplication():
        baseurl = config.get('COMMON INFO', 'baseurl')
        return baseurl

    @staticmethod
    def getusername():
        username = config.get('COMMON INFO', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('COMMON INFO', 'password')
        return password


















