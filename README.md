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
```

---

## 🧠 Modelo Base

- **Modelo base:** [`Qwen/Qwen2.5-3B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
- **Técnica:** Fine-tuning com QLoRA
- **Arquitetura:** Causal LM (decoder-only)
- **Tamanho do adapter:** ~390MB
- **Tokenização:** AutoTokenizer compatível com Qwen
- **Formato de resposta:** Texto técnico estruturado com três seções:
  - Diagnóstico
  - Causas/Impactos
  - Recomendações

---

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/miaga-api.git
cd miaga-api
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o servidor de inferência

```bash
python app.py
```

### 4. Use a API (via `curl`, `Postman` ou front-end)

**Endpoint:** `POST /gerar`

**Corpo da requisição:**

```json
{
  "entrada": "Rio Chamagunga - Ponto: C1 - IQA: 55, C2 - IQA: 70"
}
```

---

## 🌐 Deploy no Render

Este repositório está pronto para ser hospedado no [Render.com](https://render.com/). Basta seguir os passos:

1. Crie um novo serviço **Web Service** com linguagem **Python**.
2. Aponte para este repositório do GitHub.
3. Configure a porta como `8000`.
4. No campo **Start Command**, use:

```bash
bash start.sh
```

5. Defina a branch como `main` e clique em "Create Web Service".

---

## 📊 Benchmarks Operacionais

### Ambiente de Teste

| Recurso        | GPU (Colab Pro)        | CPU (Colab Pro)        |
|----------------|------------------------|------------------------|
| Memória RAM    | 15.2 GB                | 51.0 GB                |
| Sistema        | Ubuntu 22.04           | Ubuntu 22.04           |

### Indicadores

| Métrica                        | GPU           | CPU           |
|-------------------------------|---------------|---------------|
| Latência média (s)            | 77.04         | 199.04        |
| Tempo mínimo (s)              | 67.63         | 177.16        |
| Tempo máximo (s)              | 81.94         | 218.16        |
| Desvio-padrão (s)             | 4.63          | 16.81         |
| Throughput (relatórios/min)   | 0.78          | 0.30          |
| Pico estimado de RAM (MB)     | 300           | 5800          |
| Tamanho do adapter (MB)       | 390           | 390           |

---

## 🧪 Exemplo de Inferência

```python
entrada = "Rio das Contas - Ponto: R01 - IQA: 80"
resposta = gerar_relatorio(entrada)
print(resposta)
```

---

## 📚 Referência Técnica

Este modelo foi treinado com um dataset composto por 5700 exemplos sintéticos e reais (dados do SEIA/INEMA), validado com testes manuais e métricas técnicas como `loss` e `perplexidade`.

---

## 🧠 Aplicações

- Monitoramento automático de rios e reservatórios
- Apoio a relatórios de órgãos ambientais
- Ferramentas educacionais para ensino de sustentabilidade

---

## 📝 Licença

Este projeto está sob a licença MIT e faz parte da plataforma **Tikatu**, com fins científicos e educacionais.

---

## 🤝 Colaboração

Sugestões, colaborações e forks são bem-vindos!  
Para dúvidas e suporte: **contato@tikatu.com.br**

---
