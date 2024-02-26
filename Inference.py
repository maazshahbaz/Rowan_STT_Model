from datasets import load_dataset, Audio
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torch
from evaluate import load
from jiwer import wer

# Load the processor and model
processor = WhisperProcessor.from_pretrained("Model_Checkpoint_Path/tokenizer")
model = WhisperForConditionalGeneration.from_pretrained("Model_Checkpoint_Path/adapter_model").to("cuda:1")

# Load the dataset
dataset = load_dataset("Jzuluaga/atco2_corpus_1h")

# Remove unnecessary columns
dataset = dataset.remove_columns(["id", "segment_start_time", "segment_end_time", "duration"])

# Cast the "audio" column to the Audio type
dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))

# Initialize a list to store the original and generated transcriptions
original_transcriptions = []
generated_transcriptions = []

# Loop over all samples in the dataset
for i in range(len(dataset["test"])):
    # Get the audio sample and its original transcription
    sample = dataset["test"][i]
    original_transcription = sample["text"]

    # Process the audio sample to get the input features
    input_features = processor(sample["audio"]["array"], sampling_rate=sample["audio"]["sampling_rate"], return_tensors="pt").input_features 

    # Move the input features to the GPU
    input_features = input_features.to("cuda:1")

    # Generate token IDs using the model
    predicted_ids = model.generate(input_features)

    # Decode the token IDs to get the generated transcription
    generated_transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

    # Add the original and generated transcriptions to the lists
    original_transcriptions.append(original_transcription)
    generated_transcriptions.append(generated_transcription)

# Calculate the WER
total_wer = wer(original_transcriptions, generated_transcriptions)

# Print the WER
print("WER:", total_wer)
