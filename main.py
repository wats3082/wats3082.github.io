import boto3
from tkinter import *
import customtkinter
from flask import Flask
import tkinter.messagebox
import sys
import speech_recognition as sr
from speech_recognition import Microphone

"""r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
"""
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "file1.wav"

audio = pyaudio.PyAudio()
"""
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("recording...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()"""
langselect ='fr'
translate = boto3.client(service_name='translate', region_name='us-west-1', use_ssl=True)
submitText = " Please enter text to translate"

"""


with open('phrases.csv') as f:
    s = f.read() + '/n'

    print(repr(s))

result = translate.translate_text(Text=s,
                                  SourceLanguageCode="en", TargetLanguageCode="fr")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

text = result.get('TranslatedText')



"""

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


def radio_button_event1():
    print("fr - pressed")
    rlangselect = 'fr'


class App(customtkinter.CTk):
    WIDTH = 850
    HEIGHT = 500

    def __init__(self):
        super().__init__()

        self.title("My Translator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0
                                                 )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="RW Translator",
                                              text_font=("Roboto Medium", 12))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Record 10s voice clip",
                                                fg_color=("green"),  # <- custom tuple-color
                                                command=self.button_event,
                                                text_font=("Roboto Medium", 12))
        self.button_1.grid(row=2, column=0, pady=20, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Upload text file",
                                                fg_color=("blue"),  # <- custom tuple-color
                                                command=self.button_event,
                                                text_font=("Roboto Medium", 12))
        self.button_2.grid(row=3, column=0, pady=20, padx=20)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Made using Python\n"
                                                   "Libraries include: \n"
                                                   "SpeechRecognition\n"
                                                   "AWS API's\n",

                                              text_font=("Roboto Medium", 12))  # font name and size in px
        self.label_2.grid(row=4, column=0, pady=10, padx=10)

        """self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Click here to test audio",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)"""

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode,
                                                text_font=("Roboto Medium", 12))
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=1)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=1)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right )
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Translation will appear here.\n" +
                                                        "Choose desired language --->\n",

                                                   height=400,
                                                   wraplength=240,
                                                   fg_color=("white", "black"),  # <- custom tuple-color
                                                   justify=tkinter.CENTER,
                                                   text_font=("Roboto Medium", 12))
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)



        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Translate to:",
                                                        text_font=("Roboto Medium", 14))
        self.label_radio_group.grid(row=0, column=2,  pady=5, padx=10, sticky="n")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text="French",
                                                           value=0,
                                                           command=radio_button_event1,
                                                           text_font=("Roboto Medium", 12)
                                                           )
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=10, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text="Spanish",
                                                           value=1,
                                                           command=self.radio_button_event2,
                                                           text_font=("Roboto Medium", 12)
                                                           )
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=10, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text="Mandarin",
                                                           value=2,
                                                           command=self.radio_button_event3,
                                                           text_font=("Roboto Medium", 12)

                                                           )
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=10, sticky="n")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="You can insert text to translate here",
                                            fg_color='black',
                                            text_font=("Roboto Medium", 12))
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Submit text",
                                                command=self.button_event,
                                                text_font=("Roboto Medium", 12),
                                                fg_color='green')
        self.button_5.grid(row=8, column=2,  pady=20, padx=20, sticky="we")

        # set default values
        self.radio_button_1.select()
        self.switch_2.select()



    def radio_button_event1(self):
        print("fr - pressed")
        langselect.format('es')
    def radio_button_event2(self):
        print("sp - pressed")
    def radio_button_event3(self):
        print("ch - pressed")



    def button_event(self):
        print("Button pressed")
        submitText = self.entry.get()
        print(submitText + " submitted..." + langselect)
        self.label_info_1.set_text("loading...")
        result = translate.translate_text(Text=submitText,
                                          SourceLanguageCode="en", TargetLanguageCode=langselect)
        self.label_info_1.set_text(result.get('TranslatedText'))

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()


