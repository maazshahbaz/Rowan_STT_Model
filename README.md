# Rowan_STT_Model

1.  This Repository contains an Inference code. To use this inference code on your data you need to download the model_Checkpoint from         this Google Drive link: https://drive.google.com/file/d/1XHW4lQb0syNwzpawxkhkKKnfiBmw1t0T/view?usp=drive_link

2.  There are two folders in the checkpoint.
     1. adapter_model
     2. tokenizer
                
3.  Load the adapter_model folder from the checkpoint in the 9th line of the Inference code. It will look like this:
    model = WhisperForConditionalGeneration.from_pretrained("Model_checkpoint_path/adapter_model").to("cuda:1")
    
4.  Load the tokenizer from the checkpoint in the 8th line of the Inference code. It will look like this: 
    processor = WhisperProcessor.from_pretrained("/Model_checkpoint_path/tokenizer")
    
    
6. After loading adapter_model & tokenizer in the inference code you need to load your data in the 13th line of the inference code.
7.  Run Inference.py
8.  After successful inference. there will be a Word Error Rate calculated.

