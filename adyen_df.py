import math
import base64
import hashlib


class Fingerprint:
    def __init__(self):
        # Default
        self.plugins = 10
        self.nrOfPlugins = 3
        self.fonts = 10
        self.nrOfFonts = 3
        self.timeZone = 10
        self.video = 10
        self.superCookies = 10
        self.userAgent = 10
        self.mimeTypes = 10
        self.nrOfMimeTypes = 3
        self.canvas = 10
        self.cpuClass = 5
        self.platform = 5
        self.doNotTrack = 5
        self.webglFp = 10
        self.jsFonts = 10

        # Artificial
        self.userAgentString = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0"

        self.pluginsString = "Plugin 0: Chrome PDF Viewer; Portable Document Format; internal-pdf-viewer; (Portable Document Format; application/pdf; pdf) (Portable Document Format; text/pdf; pdf). Plugin 1: Chromium PDF Viewer; Portable Document Format; internal-pdf-viewer; (Portable Document Format; application/pdf; pdf) (Portable Document Format; text/pdf; pdf). Plugin 2: Microsoft Edge PDF Viewer; Portable Document Format; internal-pdf-viewer; (Portable Document Format; application/pdf; pdf) (Portable Document Format; text/pdf; pdf). Plugin 3: PDF Viewer; Portable Document Format; internal-pdf-viewer; (Portable Document Format; application/pdf; pdf) (Portable Document Format; text/pdf; pdf). Plugin 4: WebKit built-in PDF; Portable Document Format; internal-pdf-viewer; (Portable Document Format; application/pdf; pdf) (Portable Document Format; text/pdf; pdf). "
        self.pluginCount = 5

        self.screenWidth = 1440
        self.screenHeight = 900
        self.screenColorDepth = 30

        self.deviceStorage = 'DOM-LS: Yes, DOM-SS: Yes'
        self.oXMLStorage = ', IE-UD: No'

        self.mimeTypesString = "Portable Document Formatapplication/pdfpdfPortable Document Formattext/pdfpdf"
        self.mimeTypesLength = 2

        self.platformString = "MacIntel"

        self.doNotTrackString = "1"

        self.entropy = "40"

    def getSuperCookies(self):
        superCookiesPadding = math.floor(self.superCookies / 2)

        deviceStorageValue = self.calculate_md5(self.deviceStorage, superCookiesPadding)
        IEUDValue = self.calculate_md5(self.oXMLStorage, superCookiesPadding)

        superCookies = deviceStorageValue + IEUDValue
        return superCookies

    def getEntropy(self):
        mobile = ["iPad", "iPhone", "iPod"]
        if self.userAgent in mobile:
            return "20"
        return "40"

    def padString(self, string, num):
        paddedString = string.rjust(num, "0")
        if len(paddedString) > num:
            return paddedString[0:num]
        return paddedString

    def calculate_md5(self, string, num):
        a = hashlib.md5(string.encode())
        hashed_string = base64.b64encode(a.digest()).decode()
        return_string = self.padString(hashed_string, num)
        return return_string

    def generateFingerprint(self):
        self.plugins = self.calculate_md5(self.pluginsString, self.plugins)
        self.nrOfPlugins = self.padString(str(self.pluginCount), self.nrOfPlugins)
        self.fonts = self.padString("", self.fonts)
        self.nrOfFonts = self.padString("", self.nrOfFonts)
        self.timeZone = "CK1aUgqatB"
        self.video = self.padString(str((self.screenWidth + 7) * (self.screenHeight + 7) * self.screenColorDepth),
                                    self.video)
        self.superCookies = self.getSuperCookies()
        self.userAgent = self.calculate_md5(self.userAgentString, self.userAgent)
        self.mimeTypes = self.calculate_md5(self.mimeTypesString, self.mimeTypes)
        self.nrOfMimeTypes = self.padString(str(self.mimeTypesLength), self.nrOfMimeTypes)
        self.canvas = "rKkEK1Ha8P"
        self.cpuClass = self.padString("", self.cpuClass)
        self.platform = self.calculate_md5(self.platformString, self.platform)
        self.doNotTrack = self.calculate_md5(self.doNotTrackString, self.doNotTrack)
        self.jsFonts = "iZCqnI4lsk"
        self.webglFp = "fKkhnraRhX"
        self.entropy = self.getEntropy()

        adyenFingerprint = f"{self.plugins}{self.nrOfPlugins}{self.fonts}{self.nrOfFonts}{self.timeZone}{self.video}{self.superCookies}{self.userAgent}{self.mimeTypes}{self.nrOfMimeTypes}{self.canvas}{self.cpuClass}{self.platform}{self.doNotTrack}{self.webglFp}{self.jsFonts}:{self.entropy}".replace(
            "+", "G").replace("/", "D")
        """
        c = a.plugins + 
        a.nrOfPlugins + 
        a.fonts + 
        a.nrOfFonts + 
        a.timeZone + 
        a.video + 
        a.superCookies + 
        a.userAgent + 
        a.mimeTypes + 
        a.nrOfMimeTypes + 
        a.canvas + 
        a.cpuClass + 
        a.platform + 
        a.doNotTrack + 
        a.webglFp + 
        a.jsFonts;

        """

        print("Plugins:", self.plugins)
        print("Plugins NR:", self.nrOfPlugins)
        print("Fonts:", self.fonts)
        print("Fonts NR:", self.nrOfFonts)
        print("timeZone:", self.timeZone)
        print("Video:", self.video)
        print("Super Cookies:", self.superCookies)
        print("User Agent:", self.userAgent)
        print("Mime Types:", self.mimeTypes)
        print("Mime Types NR:", self.nrOfMimeTypes)
        print("Canvas:", self.canvas)
        print("CPU Class:", self.cpuClass)
        print("Platform:", self.platform)
        print("doNotTrack:", self.doNotTrack)
        print("WebGLFp:", self.webglFp)
        print("jsFonts:", self.jsFonts)
        print("Entropy:", self.entropy)

        print("Adyen Fingerprint:", adyenFingerprint)
        return adyenFingerprint
    
