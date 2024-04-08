# Rowan_STT_Model

1. This Repository contains an Inference code.
2. There are two models available on Hugging Face:
             1. Model_1: https://huggingface.co/ashfaq93/Adapter_1
             2. Model_2: https://huggingface.co/ashfaq93/Adapter_2
                
3. Load the processor and model from the hugging face in the 9th and 10th line of code. It will look like this:
             processor = WhisperProcessor.from_pretrained("ashfaq93/Adapter_1")
             model = WhisperForConditionalGeneration.from_pretrained("ashfaq93/Adapter_1").to(device)
    
4. Load the data in the 13th line.

5. Run Inference.py
 
6. After successful inference. There will be a WER printed in the Terminal.

