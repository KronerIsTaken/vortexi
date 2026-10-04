import platform

class Config:
    BaseURL = "https://www.vortexi.cc"
    AuthorizationToken = "AfterTheFate"
    CommPort = 3000

    if platform.system() == "Linux":
        RCCServicePath = "./RCCService/RCCService.exe"
        RCCService2018Path = "./RCCService2018/RCCService.exe"
        RCCService2020Path = "./RCCService2020/RCCService.exe"
        RCCService2021Path = "./RCCService2021/RCCService.exe"
        Client2014Path = "./Player2014/SyntaxPlayerBeta.exe"
    else:
        RCCServicePath = "./RCCService/RCCService.exe"
        RCCService2018Path = "./RCCService2018/RCCService.exe"
        RCCService2020Path = "./RCCService2020/RCCService.exe"
        RCCService2021Path = "./RCCService2021/RCCService.exe"
        Client2014Path = "./Player2014/SyntaxPlayerBeta.exe"

    RCCStartingPort = 53640
    RCCEndingPort = 53900
    RCCStartingComPort = 64989
    RCCEndingComPort = 65200
    ThumbnailWorkerCount = 2
    PortOffset = 400
