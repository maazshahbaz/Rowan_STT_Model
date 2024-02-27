# Rowan_STT_Model

1. This Repository contains an Inference code. To use this inference code on data call the model from hugging face using the following links:
             1. Model_1: ashfaq93/Model_1
             2. Model_2: ashfaq93/Model_2
                
2. Load the model from the hugging face in the 9th line of the Inference code. It will look like this:
    model = WhisperForConditionalGeneration.from_pretrained("ashfaq93/Model_1").to("cuda:1")
    
3. Load the model from the Hugging face in the 8th line of the Inference code. It will look like this: 
    processor = WhisperProcessor.from_pretrained("ashfaq93/Model_1")
    
4. After loading model_1/2 in the inference code, load your data in the 13th line.
5. Run Inference.py
6. After successful inference. There will be a Word Error Rate calculated in the Terminal.

