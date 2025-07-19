import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

BASE = "Qwen/Qwen1.5-1.8B-Chat"
ADAPTER = "model/adapter_model.safetensors"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

print("🔧 Carregando modelo base...")
model = AutoModelForCausalLM.from_pretrained(BASE, quantization_config=bnb_config, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(BASE)
model = PeftModel.from_pretrained(model, ADAPTER)

@app.route("/gerar", methods=["POST"])
def gerar():
    dados = request.json.get("dados", "")
    prompt = f"Você é um analista ambiental especializado em qualidade da água. Gere um relatório técnico com base nos seguintes dados:\n{dados}"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=512)
    resposta = tokenizer.decode(output[0], skip_special_tokens=True)
    return jsonify({"relatorio": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7860)))
