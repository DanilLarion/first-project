from gtts import gTTS


text = input("Welcome to Audio Downloader.\nWhat text would you like to download?: ")
languages = {
    "1": ("en", "English"),
    "2": ("ru", "Russian"),
    "3": ("fr", "French"),
    "4": ("tr", "Turkish"),
}

print("\nChoose a language:")
for key, (code, name) in languages.items():
    print(f"{key}. {name}")

choice = input("Enter number: ")
lang_code = languages.get(choice, ("en", "English"))[0]

tts = gTTS(text=text, lang=lang_code)
tts.save("audio.mp3")
print("Saved as audio.mp3")