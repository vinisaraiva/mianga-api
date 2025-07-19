import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Token de acesso (pode trocar por uma variável de ambiente)
API_TOKEN = "#tikatu"

BASE = "Qwen/Qwen2.5-3B-Instruct"
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

@app.route('/gerar', methods=['POST'])
def gerar():
    # Verifica se o token foi enviado e está correto
    token = request.headers.get('Authorization')
    if token != f"Bearer {API_TOKEN}":
        return jsonify({'erro': 'Acesso não autorizado'}), 401

    dados = request.json.get('dados', '')
    if not dados:
        return jsonify({'erro': 'Dados ausentes'}), 400

    # Geração do relatório
    prompt_final = (
        "Você é um analista ambiental especializado em qualidade da água..."
        f"\n\nDados: {dados}\n\nRelatório:\n"
    )
    inputs = tokenizer(prompt_final, return_tensors="pt").to(model.device)
    with torch.no_grad():
        saida = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id
        )
    resposta = tokenizer.decode(saida[0], skip_special_tokens=True)
    return jsonify({'relatorio': resposta.replace(prompt_final.strip(), "").strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7860)))
