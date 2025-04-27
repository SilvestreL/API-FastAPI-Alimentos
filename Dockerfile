# Usar imagem oficial do Python
FROM python:3.11-slim

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta da aplicação
EXPOSE 8000

# Comando para iniciar o backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]