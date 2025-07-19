# 💧 Miãga: Modelo Leve de IA para Análise da Qualidade da Água

Miãga é um modelo de inteligência artificial treinado com fine-tuning no Qwen2.5-3B, desenvolvido especificamente para interpretar dados de qualidade da água e gerar relatórios técnicos em linguagem natural, com base nos parâmetros físico-químicos e nos índices ambientais (como IQA e IET). É voltado para aplicações públicas e privadas, sendo compatível com ambientes de baixo custo (CPU) e escalável para ambientes com GPU.

---

## 📦 Estrutura deste Repositório

```bash
.
├── model/                   # Arquivos do modelo LoRA adaptado (Miãga)
│   ├── adapter_model.safetensors
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   ├── vocab.json
│   ├── merges.txt
│   ├── added_tokens.json
│   └── chat_template.jinja
├── app.py                   # FastAPI com endpoint para inferência
├── requirements.txt         # Dependências da aplicação
├── start.sh                 # Script de inicialização para o Render
└── README.md                # Este arquivo
