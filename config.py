import win32com.client # required for win32 users
import Downloaders.MTS, Downloaders.URL
import Installer.Sims2Pack, Installer.Inteen, Installer.Sims3Pack
SM.Temp = "out" # usually not used
SM.Handlers["ModTheSims"] = Downloaders.MTS.Downloader
SM.Handlers["url"] = Downloaders.URL.Downloader
SM.Fogs = ["samples/inteen.fog", "samples/wideloading.fog"]
GameDocs = {"Sims2UltimateCollection":"EA Games\\The Sims™ 2 Ultimate Collection",
            "Sims3": "Electronic Arts\\The Sims 3"}
Documents = win32com.client.Dispatch("WScript.Shell").SpecialFolders("MyDocuments") + GameDocs['Sims2UltimateCollection']
SM.Scope['Directories'] = {
                            "Downloads": Documents+"Downloads",
                            "Cameras": Documents+"Cameras",
                            "LatestEPResUI": "C:\\Program Files (x86)\\Origin Games\\The Sims 2 Ultimate Collection\\Apartment Life\\TSData\\Res\\UI",
                            "Cache": "__cache",
                            "PetBreeds": Documents+"PetBreeds",
                            "ModsPackages": Documents+"Mods\\Packages\\",
                            "ModsOverrides": Documents+"Mods\\Packages\\",
                            "ALOverrides": "C:\\Program Files (x86)\\Origin Games\\The Sims 2 Ultimate Collection\\Apartment Life\\TSData\\Res\\Overrides"
			}
SM.Scope['FileTypes'] = {
                         'Txt': '*.txt',
                         'Package': '*.package',
                         'Sims2Pack': '*.Sims2Pack',
                         'Sims3Pack': '*.Sims3Pack',
                         'InTeenPackage': "*.package"
                        }
SM.Scope['Hooks'] = {
                     'InTeenPackage':
                      {
                        "Extracted": Installer.Inteen._
                      }
                    }
# The user agent may be required for some downloaders to work.
# Some servers decline user agents which look suspicious.
# By default, this is Chrome 51.0.2704.103.
# User agent does not specify what will download the file(s). It is used to represent the user's "browser".
SM.Scope['UserAgent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
# You can comment out (add # on line beginning) following line,
# if you do not want version information to be appended to user agent.
insmod("versionstring")
# Sleep after request - set 0 if you want to disable
# 0.5 may be not enough to keep servers away of thinking that your network/computer is a bot. Even if it is.
SM.Pause = 0.5