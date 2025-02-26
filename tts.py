import pyttsx3


speaker = pyttsx3.init()

def stop_speech():
    """
    Stop the text-to-speech conversion.
    Returns:
        None
    """
    speaker.stop()
    if speaker._inLoop:
        speaker.endLoop()

def text_to_speech(page):
    """
    Convert text to speech using the pyttsx3 library.
    Args:
        page (str): The text content to be converted to speech.
    Returns:
        None
    """
    speaker.say(page)
    speaker.runAndWait()