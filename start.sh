#!/bin/bash

echo "🔽 Baixando o adapter_model.safetensors da Release do GitHub..."
mkdir -p model

wget -O model/adapter_model.safetensors https://github.com/vinisaraiva/mianga-api/releases/download/modelo-final/adapter_model.safetensors

echo "✅ Arquivo baixado com sucesso."

echo "🚀 Iniciando aplicação..."
python app.py
