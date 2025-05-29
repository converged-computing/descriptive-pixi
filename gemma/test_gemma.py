from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def dinosaur_test(model_name="google/gemma-2b-it"):
    """
    Let's just make this one fun :)
    """
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto")
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, torch_dtype="auto", padding_side="left"
    )
    tokenizer.pad_token = tokenizer.eos_token

    prompt = """
    You are a space explorer. You've just landed on an alien planet and need to
    report your findings back to earth. Your task is to describe the plant and animal life,
    and since this is fictional I want you to be creative and funny.
    """
    inputs = tokenizer(prompt, return_tensors="pt")

    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"

    model.to(device)

    # move inputs to device
    inputs = inputs.to(device)
    print(device)

    # Generate text
    generation_output = model.generate(
        **inputs,
        max_new_tokens=1000,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
    )
    return tokenizer.decode(generation_output[0], skip_special_tokens=True)


if __name__ == "__main__":
    print(dinosaur_test())

