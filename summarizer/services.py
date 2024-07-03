import torch
from transformers import pipeline


class SimpleSummarizer:
    """
    A class used to summarize text using a pre-trained transformer model.
    """

    def __init__(self):
        device = self._get_device()
        self._pipeline = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

    @staticmethod
    def _get_device() -> int:
        """
        Determine the device (GPU) to use for the pipeline.

        :return: The device index to use (-1 for CPU, 0 or higher for GPU).
        """
        if torch.cuda.is_available():
            num_gpus = torch.cuda.device_count()
            if num_gpus > 1:
                return 0  # Select the first GPU
            else:
                return 0  # Only one GPU available
        else:
            return -1  # CPU only

    def summarize(self, text: str) -> str:
        """
        Summarizes the input text.

        :param text: The input text to be summarized.

        :return: The summarized text.
        """
        summary = self._pipeline(text, min_length=30, max_length=150, do_sample=False)

        return summary[0]["summary_text"]
