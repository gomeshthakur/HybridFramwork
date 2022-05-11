import configparser

config=configparser.RawConfigParser()
config.read("D:\pythonProject\HybridFramwork\Configuration\config.ini")

class ReadConfig:
    # def __init__(self):
    #     print("Success")

    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getUserName():
        username=config.get('common info','usermail')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password