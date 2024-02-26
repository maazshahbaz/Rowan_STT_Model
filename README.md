# Rowan_STT_Model

1. This Repository contains an Inference code. To use this inference code on data download the model Checkpoint from these Google Drive links:
             1. Model_1: https://drive.google.com/file/d/1XHW4lQb0syNwzpawxkhkKKnfiBmw1t0T/view?usp=drive_link
             2. Model_2: https://drive.google.com/file/d/1VwBNnIsS_ZKUkzwMzdvyoMskEKh2xSz0/view?usp=drive_link

2. There are two folders in each checkpoint.
     1. adapter_model
     2. tokenizer
                
5. Load the adapter_model folder from the checkpoint in the 9th line of the Inference code. It will look like this:
    model = WhisperForConditionalGeneration.from_pretrained("Model_checkpoint_path/adapter_model").to("cuda:1")
    
6. Load the tokenizer from the checkpoint in the 8th line of the Inference code. It will look like this: 
    processor = WhisperProcessor.from_pretrained("/Model_checkpoint_path/tokenizer")
    
    
7. After loading adapter_model & tokenizer folders in the inference code you need to load your data in the 13th line.
8. Run Inference.py
9. After successful inference. There will be a Word Error Rate calculated in the Terminal.

