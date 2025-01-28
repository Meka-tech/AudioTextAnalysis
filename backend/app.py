import gradio as gr
import whisper
from transformers import pipeline

# Load models
model = whisper.load_model("base")
sentiment_analysis = pipeline("sentiment-analysis", framework="pt", model="SamLowe/roberta-base-go_emotions")

def analyze_sentiment(text):
    results = sentiment_analysis(text)
    sentiment_results = {result['label']: result['score'] for result in results}
    return sentiment_results

# Define sentiment emojis (same as before)
def get_sentiment_emoji(sentiment):
    emoji_mapping = {
        "disappointment": "😞",
        "sadness": "😢",
        "annoyance": "😠",
        "neutral": "😐",
        "disapproval": "👎",
        "realization": "😮",
        "nervousness": "😬",
        "approval": "👍",
        "joy": "😄",
        "anger": "😡",
        "embarrassment": "😳",
        "caring": "🤗",
        "remorse": "😔",
        "disgust": "🤢",
        "grief": "😥",
        "confusion": "😕",
        "relief": "😌",
        "desire": "😍",
        "admiration": "😌",
        "optimism": "😊",
        "fear": "😨",
        "love": "❤️",
        "excitement": "🎉",
        "curiosity": "🤔",
        "amusement": "😄",
        "surprise": "😲",
        "gratitude": "🙏",
        "pride": "🦁"
    }
    return emoji_mapping.get(sentiment, "")

# Display sentiment results
def display_sentiment_results(sentiment_results, option):
    sentiment_text = ""
    for sentiment, score in sentiment_results.items():
        emoji = get_sentiment_emoji(sentiment)
        if option == "Sentiment Only":
            sentiment_text += f"{sentiment} {emoji}\n"
        elif option == "Sentiment + Score":
            sentiment_text += f"{sentiment} {emoji}: {score}\n"
    return sentiment_text

# Inference function for speech recognition
def inference(audio, sentiment_option):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    _, probs = model.detect_language(mel)
    lang = max(probs, key=probs.get)

    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    sentiment_results = analyze_sentiment(result.text)
    sentiment_output = display_sentiment_results(sentiment_results, sentiment_option)

    return lang.upper(), result.text, sentiment_output

# New function for text-based sentiment analysis
def text_sentiment_analysis(text, sentiment_option):
    if not text:
        return "Please enter some text to analyze."
    
    sentiment_results = analyze_sentiment(text)
    return display_sentiment_results(sentiment_results, sentiment_option)

# Interface settings
title = """<h1 align="center">🎤 Multilingual Automatic Speech Recognition and Sentiment Analyzer 💬</h1>"""
description = """
💻 This demo showcases a speech recognition and sentiment analysis tool.<br><br>
⚙️ Components of the tool:<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Real-time multilingual speech recognition<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Language identification<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Sentiment analysis of transcriptions and text<br>
<br>
🎯 The sentiment analysis results are provided with different emotions and their corresponding scores.<br>
<br>
😃 Sentiment results are displayed with representative emojis.<br>
<br>
✅ Higher scores indicate stronger presence of that emotion in the text.<br>
"""

custom_css = """
#banner-image {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
#chat-message {
    font-size: 18px;
    min-height: 300px;
}
"""

# Create tabbed interface
with gr.Blocks(title="Sentiment Analyzer", css=custom_css) as demo:
    gr.Markdown(title)
    gr.Markdown(description)
    
    with gr.Tab("Speech Recognition"):
        with gr.Column():
            audio_input = gr.Audio(
                label="Input Audio",
                show_label=True,
                sources=["microphone"],
                type="filepath"
            )
            speech_sentiment_option = gr.Radio(
                choices=["Sentiment Only", "Sentiment + Score"],
                label="Select an option",
                value="Sentiment Only"
            )
            speech_submit = gr.Button("Analyze Speech")
            
            lang_output = gr.Textbox(label="Language")
            speech_sentiment_output = gr.Textbox(label="Sentiment Analysis Results")
            
            def custom_inference(audio, sentiment_option):
                audio = whisper.load_audio(audio)
                audio = whisper.pad_or_trim(audio)

                mel = whisper.log_mel_spectrogram(audio).to(model.device)

                _, probs = model.detect_language(mel)
                lang = max(probs, key=probs.get)

                options = whisper.DecodingOptions(fp16=False)
                result = whisper.decode(model, mel, options)

                sentiment_results = analyze_sentiment(result.text)
                sentiment_output = display_sentiment_results(sentiment_results, sentiment_option)

                return lang.upper(), sentiment_output
            
            speech_submit.click(
                custom_inference, 
                inputs=[audio_input, speech_sentiment_option], 
                outputs=[lang_output, speech_sentiment_output]
            )
    
    with gr.Tab("Text Sentiment Analysis"):
        with gr.Column():
            text_input = gr.Textbox(
                label="Enter text for sentiment analysis",
                lines=4,
                placeholder="Type or paste your text here..."
            )
            text_sentiment_option = gr.Radio(
                choices=["Sentiment Only", "Sentiment + Score"],
                label="Select an option",
                value="Sentiment Only"
            )
            text_submit = gr.Button("Analyze Text")
            
            text_sentiment_output = gr.Textbox(label="Sentiment Analysis Results")
            
            text_submit.click(
                text_sentiment_analysis, 
                inputs=[text_input, text_sentiment_option], 
                outputs=text_sentiment_output
            )

# Launch the interface
demo.launch()