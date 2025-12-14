from abc import ABC,abstractmethod
class phone:
    def voice_call(self):
        print("make voice calls")
    def sms(self):
        print("we can send sms")
class camera(ABC):
    @abstractmethod
    def click(self):
        pass
    @abstractmethod
    def record(self):
        pass
class musicplayer(ABC):
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def pause(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class oppo(phone,camera,musicplayer):
    def click(self):
        print("you can make multile clicks")
    def record(self):
        print("you can record videos")
    def play(self):
        print("play music")
    def pause(self):
        print("Pause the song")
    def stop(self):
        print("you have option to stop the song")
class redmi(phone):
    pass
if __name__=="__main__":
    o=oppo()
    o.voice_call()
    o.sms()
    o.pause()
    o.click()
    o.play()
    o.record()
    o.stop()
