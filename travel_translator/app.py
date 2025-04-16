import streamlit as st
import translator
import time

# Page configuration
st.set_page_config(
    page_title="AI Language Translator for Travelers",
    page_icon="🌎",
    layout="wide"
)

# Custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.image("static/logo.png", width=100)
        st.title("Travel Translator")
        st.write("Your AI language companion for seamless travel communication")

        # Language selection
        source_lang = st.selectbox(
            "Your Language",
            options=translator.get_supported_languages(),
            index=translator.get_language_index("English")
        )

        target_lang = st.selectbox(
            "Translate To",
            options=translator.get_supported_languages(),
            index=translator.get_language_index("Spanish")
        )

        # Feature selection
        feature = st.radio(
            "Feature",
            options=["Text Translation", "Conversation", "Common Phrases"]
        )

        # Additional options
        st.subheader("Options")
        show_pronunciation = st.checkbox("Show pronunciation guide", value=True)
        enable_voice = st.checkbox("Enable voice output", value=False)

    # Main content area
    st.title("AI Language Translator for Travelers 🌎")

    # Display selected feature
    if feature == "Text Translation":
        display_text_translation(source_lang, target_lang, show_pronunciation, enable_voice)
    elif feature == "Conversation":
        display_conversation(source_lang, target_lang, show_pronunciation, enable_voice)
    else:  # Common Phrases
        display_common_phrases(source_lang, target_lang, show_pronunciation, enable_voice)

def display_text_translation(source_lang, target_lang, show_pronunciation, enable_voice):
    st.subheader("Text Translation")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**{source_lang}**")
        source_text = st.text_area("Enter text to translate", height=200)
        if st.button("Translate"):
            if source_text:
                with st.spinner("Translating..."):
                    # Simulate translation delay
                    time.sleep(0.5)

                    # Get translation
                    translation, pronunciation = translator.translate_text(
                        source_text, source_lang, target_lang
                    )

                    # Store in session state
                    st.session_state.translation = translation
                    st.session_state.pronunciation = pronunciation
            else:
                st.warning("Please enter some text to translate")

    with col2:
        st.write(f"**{target_lang}**")

        if 'translation' in st.session_state:
            st.text_area("Translation", st.session_state.translation, height=200)

            if show_pronunciation and 'pronunciation' in st.session_state:
                st.write("**Pronunciation Guide:**")
                st.write(st.session_state.pronunciation)

            if enable_voice:
                st.button("🔊 Listen", key="listen_translation")

def display_conversation(source_lang, target_lang, show_pronunciation, enable_voice):
    st.subheader("Travel Conversation")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            if message["role"] == "assistant" and show_pronunciation and "pronunciation" in message:
                st.write("*" + message["pronunciation"] + "*")

    # Chat input
    if prompt := st.chat_input("Say something..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("Translating..."):
                # Simulate response delay
                time.sleep(0.7)

                # Get translation
                translation, pronunciation = translator.translate_conversation(
                    prompt, source_lang, target_lang
                )

                # Display response
                st.write(translation)
                if show_pronunciation:
                    st.write("*" + pronunciation + "*")

                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": translation,
                    "pronunciation": pronunciation
                })

                if enable_voice:
                    st.button("🔊 Listen", key=f"listen_{len(st.session_state.messages)}")

def display_common_phrases(source_lang, target_lang, show_pronunciation, enable_voice):
    st.subheader("Common Travel Phrases")

    # Categories of common phrases
    categories = [
        "Greetings",
        "Transportation",
        "Accommodation",
        "Dining",
        "Shopping",
        "Emergencies",
        "Directions",
        "Numbers & Time"
    ]

    selected_category = st.selectbox("Select category", categories)

    # Get phrases based on selected category
    phrases = translator.get_common_phrases(selected_category, source_lang, target_lang)

    # Display phrases
    for i, phrase in enumerate(phrases):
        with st.expander(f"{phrase['source']}"):
            st.write(f"**{target_lang}:** {phrase['target']}")

            if show_pronunciation:
                st.write(f"**Pronunciation:** {phrase['pronunciation']}")

            if enable_voice:
                st.button("🔊 Listen", key=f"phrase_{i}")

    # Search for phrases
    st.write("---")
    search_term = st.text_input("Search for phrases")
    if search_term:
        search_results = translator.search_phrases(search_term, source_lang, target_lang)

        if search_results:
            st.write(f"Found {len(search_results)} results:")
            for i, result in enumerate(search_results):
                with st.expander(f"{result['source']}"):
                    st.write(f"**{target_lang}:** {result['target']}")

                    if show_pronunciation:
                        st.write(f"**Pronunciation:** {result['pronunciation']}")

                    if enable_voice:
                        st.button("🔊 Listen", key=f"search_{i}")
        else:
            st.info("No matching phrases found")

if __name__ == "__main__":
    main()