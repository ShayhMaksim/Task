from Signal import Signal
from SignalWrapper import SignalWrapper
import random

audio = Signal(category=0,length=random.uniform(2, 10),nature='audio',hazardous=True)
audio.speed=40
audio.launch(list([4,23,5,6]))

video = Signal(category=1,length=random.uniform(0.5, 1.0),nature='video',hazardous=False)
video.speed=7
video.launch(list([7,41,5]))

audioWrapper=SignalWrapper(audio,0)
videoWrapper=SignalWrapper(video,1)

audioWrapper.run()
videoWrapper.run()


