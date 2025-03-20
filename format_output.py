def format_emotion_output(emotions):
    """
    Formats the output to display the dominant emotion along with detailed scores.
    """
    if not emotions:
        return {"error": "No emotions detected"}

    dominant_emotion = max(emotions, key=emotions.get)
    return {
        "dominant_emotion": dominant_emotion,
        "detailed_emotions": emotions
    }
