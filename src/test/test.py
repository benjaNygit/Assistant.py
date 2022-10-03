from notifypy import Notify

notification = Notify()
notification.title = "Cool Title"
notification.message = "Even cooler message."
notification.audio = "./voices/buenos-dias.wav"
notification.icon = "./icons/icon3.png"

if __name__=='__main__':
    notification.send()
