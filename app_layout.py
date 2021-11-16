from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import cv2
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

from moviepy.editor import *

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")

clip1 = VideoFileClip("1.mp4")
clip2 = VideoFileClip("2.mp4")


class VideoEditor(App):

    def build(self):
        self.window = GridLayout()
        #add widgets to window

        self.button = Button(text="Add Text",
                             size=(64, 64),
                             pos=(68, 350))
        self.button.bind(on_press=self.textf)
        self.window.add_widget(self.button)

        self.button= Button(text="Mix",
                            size= (64,64),
                            pos= (268,350))
        self.button.bind(on_press=self.mix)
        self.window.add_widget(self.button)

        self.button = Button(text="Mirror",
                             size=(64, 64),
                             pos=(468,350))
        self.button.bind(on_press=self.mirror)
        self.window.add_widget(self.button)

        self.button = Button(text="Resize",
                             size=(64, 64),
                             pos=(68, 200))
        self.button.bind(on_press=self.resize)
        self.window.add_widget(self.button)

        self.button = Button(text="Speed",
                             size=(64, 64),
                             pos=(268, 200))
        self.button.bind(on_press=self.speed)
        self.window.add_widget(self.button)

        self.button = Button(text="Trim Start",
                             size=(64, 64),
                             pos=(468, 200))
        self.button.bind(on_press=self.trim)
        self.window.add_widget(self.button)

        self.button = Button(text="Trim End",
                             size=(64, 64),
                             pos=(668, 200))
        self.button.bind(on_press=self.trim)
        self.window.add_widget(self.button)

        self.button = Button(text="Audio",
                             size=(64, 64),
                             pos=(668, 350))
        self.button.bind(on_press=self.audio)
        self.window.add_widget(self.button)

        self.r = TextInput(multiline=False,
                           pos=(50, 100))
        self.s = TextInput(multiline=False,
                           pos=(250, 100))
        self.t1 = TextInput(multiline=False,
                           pos=(450, 100))
        self.t2 = TextInput(multiline=False,
                           pos=(650, 100))
        self.window.add_widget(self.r)
        self.window.add_widget(self.s)
        self.window.add_widget(self.t1)
        self.window.add_widget(self.t2)
        return self.window

    def mix(self, event):
        final_clip = concatenate_videoclips([clip1, clip2])
        final_clip.write_videofile("mix.mp4")

    def mirror(self, event):
        clip_mirror = clip1.fx(vfx.mirror_x)
        clip_mirror.write_videofile("mirror.mp4")

    def resize(self, event):
        val=float(self.r.text)
        clip_resize = clip1.resize(val)
        clip_resize.write_videofile("resize.mp4")

    def speed(self, event):
        speed = float(self.s.text)
        clip_speed = clip1.fx(vfx.speedx, speed)
        clip_speed.write_videofile("speed.mp4")

    def trim(self, event):
        starting = float(self.t1.text)
        ending = float(self.t2.text)
        clip_trim = clip1.cutout(starting, ending)
        clip_trim.write_videofile("trim.mp4")

    def audio(self, event):
        audioclip = AudioFileClip("audio.mp3")
        videoclip = clip1.set_audio(audioclip)
        final_clip = videoclip.set_audio(audioclip)
        final_clip.write_videofile("audio.mp4")

    def textf(self, event):
        cap = cv2.VideoCapture("1.mp4")
        while (True):
            ret, frame = cap.read()
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            cv2.putText(frame, 'hello', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
            cv2.imshow('video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    VideoEditor().run()