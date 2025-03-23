# VLM Fine-Tuning Results

## Baseline vs. Fine-tuned Model

| Metric                     | Baseline | Fine-tuned | Improvement |
| -------------------------- | -------- | ---------- | ----------- |
| Average WER                | 6.0228   | 0.3940     | ↓ 93.5%     |
| Average CER                | 6.9800   | 0.3442     | ↓ 95.1%     |
| Exact Sequence Accuracy    | 0.0047   | 0.5357     | ↑ 113x      |
| Flexible Sequence Accuracy | 0.0143   | 0.6137     | ↑ 42x       |

The fine-tuning dramatically improved all metrics:

- **WER/CER**: Error rates decreased by over 90% (lower is better)
- **Exact Accuracy**: Improved from virtually no exact matches (0.47%) to over 53%
- **Flexible Accuracy**: Improved from 1.43% to 61.37% of outputs having ≥95% similarity

## MODEL AND DATASET

- this model is not merged properly so wont work if performed inference on it
- https://huggingface.co/Aditya-Khedekar/SarvamAI-VLM
- https://huggingface.co/datasets/Aditya-Khedekar/SarvamAI-VLM-dataset

## TO Rerun the Metrics and perform inference on the model

- So you will have to push the (lora_model_V2) folder to drive and mount the drive to colab copy the path and then run the
- Also upload the test folder and use the path
- https://colab.research.google.com/drive/1zRZdxaEs5tajuk0FrLX_LvLZGUBGdGXZ?usp=sharing

## To use the fine-tuned model:

- Push the lora_model_V2 folder to Google Drive
- Mount the drive in Google Colab
- Upload the test folder and use the path in the notebook

## Project Directory Structure

```makdown
SarvamAI-VLM-FineTuning/
├── baseline_metrics_v2.txt # Baseline model evaluation metrics
├── Fine_tune_V2.ipynb # Main fine-tuning notebook (v2)
├── Fine_tune.ipynb # Initial fine-tuning notebook
├── Fine_tuned_metrics.txt # Fine-tuned model evaluation metrics
├── ground_truth.py # Script to generate ground truth data
├── HF.ipynb # Notebook for Hugging Face integration
├── metrics.py # Script to calculate evaluation metrics
├── Readme.md # This README file
├── split_dataset.py # Script to split dataset into train/test
├── test_ground_truth.json # Ground truth data for testing
├── dataset/ # Dataset directory
│ ├── processed_dataset_V6.json # Processed dataset for training
│ ├── test/ # Test images
│ └── train/ # Training images
└── lora_model_V2/ # Fine-tuned model files
├── adapter_config.json # LoRA adapter configuration
├── adapter_model.bin # LoRA adapter weights
├── README.md # Model card
├── chat_template.json # Chat template for inference
└── tokenizer.json # Tokenizer configuration

```
