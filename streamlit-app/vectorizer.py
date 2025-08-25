def vectorize(cleaned_X):
    import tensorflow as tf
    import json

    with open('streamlit-app/tokenizer.json') as f:
        data = json.load(f)
        loaded_tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)

    # Create the sequences for each sentence, basically turning each word into its index position
    sequences = loaded_tokenizer.texts_to_sequences([cleaned_X])

    # Limiting our sequencer to only include 300 words
    max_length = 300

    # Convert the sequences to all be the same length of 300
    cleaned_X = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_length, padding='post')

    return cleaned_X
