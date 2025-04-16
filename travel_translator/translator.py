from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import platform

# Initialize the Google Translator
translator = Translator()

# Supported languages from Google Translate
SUPPORTED_LANGUAGES = list(LANGUAGES.values())

# Language code mapping for gTTS (not all languages supported by Google Translate are supported by gTTS)
GTTS_LANGUAGES = {
    'afrikaans': 'af',
    'arabic': 'ar',
    'bulgarian': 'bg',
    'bengali': 'bn',
    'bosnian': 'bs',
    'catalan': 'ca',
    'czech': 'cs',
    'welsh': 'cy',
    'danish': 'da',
    'german': 'de',
    'greek': 'el',
    'english': 'en',
    'spanish': 'es',
    'estonian': 'et',
    'finnish': 'fi',
    'french': 'fr',
    'gujarati': 'gu',
    'hindi': 'hi',
    'croatian': 'hr',
    'hungarian': 'hu',
    'indonesian': 'id',
    'icelandic': 'is',
    'italian': 'it',
    'hebrew': 'iw',
    'japanese': 'ja',
    'javanese': 'jw',
    'khmer': 'km',
    'kannada': 'kn',
    'korean': 'ko',
    'latin': 'la',
    'latvian': 'lv',
    'malayalam': 'ml',
    'marathi': 'mr',
    'malay': 'ms',
    'burmese': 'my',
    'nepali': 'ne',
    'dutch': 'nl',
    'norwegian': 'no',
    'polish': 'pl',
    'portuguese': 'pt',
    'romanian': 'ro',
    'russian': 'ru',
    'sinhala': 'si',
    'slovak': 'sk',
    'albanian': 'sq',
    'serbian': 'sr',
    'sundanese': 'su',
    'swedish': 'sv',
    'swahili': 'sw',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'filipino': 'tl',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'vietnamese': 'vi',
    'chinese': 'zh'
}


def get_language_code(language_name):
    """Get the language code for gTTS from language name"""
    return GTTS_LANGUAGES.get(language_name.lower(), 'en')  # Default to English if not found


def get_language_index(language):
    try:
        return SUPPORTED_LANGUAGES.index(language)
    except ValueError:
        return 0  # Default to English


def get_supported_languages():
    return SUPPORTED_LANGUAGES


def translate_text(text, source_lang, target_lang):
    if source_lang == target_lang:
        return text, "Same pronunciation"

    # Translate using googletrans
    translation = translator.translate(text, src=source_lang, dest=target_lang)

    # Return translated text and pronunciation
    translated_text = translation.text
    pronunciation = translation.pronunciation if translation.pronunciation else translated_text

    return translated_text, pronunciation


def translate_conversation(text, source_lang, target_lang):
    return translate_text(text, source_lang, target_lang)


def get_common_phrases(category, source_lang, target_lang):
    COMMON_PHRASES = {
        "Greetings": [
            "Hello", "Good morning", "Good evening", "Thank you",
            "You're welcome", "How are you?", "Nice to meet you"
        ],
        "Transportation": [
            "Where is the bus station?", "How much is the ticket?",
            "Is this the train to the airport?"
        ],
        "Accommodation": [
            "Do you have a room available?", "How much is a night?",
            "Do you accept credit cards?"
        ],
        "Dining": [
            "A table for two, please", "What do you recommend?",
            "The bill, please"
        ],
        "Shopping": [
            "How much does this cost?", "Do you have this in another color?",
            "Can I try this on?"
        ],
        "Emergencies": [
            "Help!", "I need a doctor", "Call the police"
        ],
        "Directions": [
            "Where is the restroom?", "How do I get to the museum?",
            "Is it far from here?"
        ],
        "Numbers & Time": [
            "One, two, three", "What time is it?", "When does the store open?"
        ]
    }

    phrases = COMMON_PHRASES.get(category, [])
    translated_phrases = []
    for phrase in phrases:
        target_text, pronunciation = translate_text(phrase, source_lang, target_lang)
        translated_phrases.append({
            "source": phrase,
            "target": target_text,
            "pronunciation": pronunciation
        })
    return translated_phrases


def search_phrases(search_term, source_lang, target_lang):
    all_phrases = []
    for category in ["Greetings", "Transportation", "Accommodation", "Dining",
                     "Shopping", "Emergencies", "Directions", "Numbers & Time"]:
        all_phrases.extend(get_common_phrases(category, source_lang, target_lang))

    results = [phrase for phrase in all_phrases if search_term.lower() in phrase["source"].lower()]
    return results


def speak(text, lang_name):
    try:
        lang_code = get_language_code(lang_name)
        tts = gTTS(text=text, lang=lang_code)
        tts.save("output.mp3")

        # Play audio based on the operating system
        system = platform.system()
        if system == "Windows":
            os.system("start output.mp3")
        elif system == "Darwin":  # macOS
            os.system("afplay output.mp3")
        else:  # Linux
            os.system("mpg321 output.mp3")
    except Exception as e:
        print(f"Error in text-to-speech: {e}")













# from googletrans import Translator, LANGUAGES
# from gtts import gTTS
# import os
#
# # Initialize the Google Translator
# translator = Translator()
#
# # Supported languages from Google Translate
# SUPPORTED_LANGUAGES = list(LANGUAGES.values())
#
#
# # Function to get index of a language
# def get_language_index(language):
#     try:
#         return SUPPORTED_LANGUAGES.index(language)
#     except ValueError:
#         return 0  # Default to English
#
#
# # Function to get all supported languages
# def get_supported_languages():
#     return SUPPORTED_LANGUAGES
#
#
# # Translate text between source and target languages
# def translate_text(text, source_lang, target_lang):
#     if source_lang == target_lang:
#         return text, "Same pronunciation"
#
#     # Translate using googletrans
#     translation = translator.translate(text, src=source_lang.lower(), dest=target_lang.lower())
#
#     # Return translated text and mock pronunciation
#     translated_text = translation.text
#     pronunciation = translation.pronunciation if translation.pronunciation else f"Mock {target_lang} pronunciation"
#
#     return translated_text, pronunciation
#
#
# # Handle translations for conversations
# def translate_conversation(text, source_lang, target_lang):
#     return translate_text(text, source_lang, target_lang)
#
#
# # Get common phrases based on category
# def get_common_phrases(category, source_lang, target_lang):
#     COMMON_PHRASES = {
#         "Greetings": [
#             "Hello", "Good morning", "Good evening", "Thank you", "You're welcome", "How are you?", "Nice to meet you"
#         ],
#         "Transportation": [
#             "Where is the bus station?", "How much is the ticket?", "Is this the train to the airport?"
#         ],
#         "Accommodation": [
#             "Do you have a room available?", "How much is a night?", "Do you accept credit cards?"
#         ],
#         # Add other categories similarly
#     }
#
#     phrases = COMMON_PHRASES.get(category, [])
#     translated_phrases = []
#     for phrase in phrases:
#         target_text, pronunciation = translate_text(phrase, source_lang, target_lang)
#         translated_phrases.append({
#             "source": phrase,
#             "target": target_text,
#             "pronunciation": pronunciation
#         })
#     return translated_phrases
#
#
# # Function to search phrases based on input
# def search_phrases(search_term, source_lang, target_lang):
#     # You can integrate a real search functionality here if needed.
#     # For simplicity, let's search in the common phrases.
#     all_phrases = []
#     for category in ["Greetings", "Transportation", "Accommodation"]:
#         all_phrases.extend(get_common_phrases(category, source_lang, target_lang))
#
#     # Filter phrases containing the search term
#     results = [phrase for phrase in all_phrases if search_term.lower() in phrase["source"].lower()]
#     return results
#
#
# # Text-to-Speech for voice output (using gTTS)
# def speak(text, lang="en"):
#     tts = gTTS(text=text, lang=lang)
#     tts.save("output.mp3")
#     os.system("start output.mp3")  # This will play the audio on Windows, for Linux or MacOS use "open output.mp3"
