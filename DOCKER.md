# 🐳 Guia Docker - Dashboard Financeiro

## 🚀 Execução Rápida com Docker

### Opção 1: Docker Compose (Recomendado)
```bash
# Construir e executar
docker-compose up --build

# Executar em background
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar
docker-compose down
```

### Opção 2: Docker Direto
```bash
# Construir imagem
docker build -t dashboard-financeiro .

# Executar container
docker run -p 8501:8501 -v $(pwd)/uploads:/app/uploads dashboard-financeiro

# Executar em background
docker run -d -p 8501:8501 --name dashboard-financeiro dashboard-financeiro
```

## 🌐 Acesso
Após executar, acesse: **http://localhost:8501**

## 📁 Volumes e Persistência

### Uploads de CSV
```bash
# Criar diretório para uploads
mkdir uploads

# Volume mapeado automaticamente pelo docker-compose
# Arquivos CSV carregados ficam em ./uploads/
```

### Dados Persistentes
```bash
# Para manter configurações entre restarts
mkdir data
# Volume mapeado em ./data/
```

## 🔧 Configurações Avançadas

### Variáveis de Ambiente
```yaml
# docker-compose.yml
environment:
  - STREAMLIT_SERVER_ADDRESS=0.0.0.0
  - STREAMLIT_SERVER_PORT=8501
  - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
  - SELIC_API_TIMEOUT=30  # Timeout da API SELIC
```

### Customizar Porta
```bash
# Usar porta diferente (ex: 9000)
docker run -p 9000:8501 dashboard-financeiro
```

## 🐛 Troubleshooting

### Docker não está executando
```bash
# Windows: Verifique se Docker Desktop está executando
# Procure "Docker Desktop" no menu iniciar

# Verificar status
docker info

# Se não funcionar, reinicie Docker Desktop
```

### Script de Verificação Automática
```bash
# Windows
docker-test.bat

# Linux/Mac
bash docker-test.sh
```

### Porta já em uso
```bash
# Verificar quem usa a porta 8501
netstat -tulpn | grep 8501

# Usar porta alternativa
docker run -p 8502:8501 dashboard-financeiro
```

### Erro de build
```bash
# Limpar cache do Docker
docker builder prune

# Build sem cache
docker build --no-cache -t dashboard-financeiro .
```

### Problemas de permissão (Linux/Mac)
```bash
# Ajustar permissões
sudo chown -R $USER:$USER uploads data
```

### Logs do container
```bash
# Ver logs em tempo real
docker logs -f dashboard-financeiro

# Ver últimas 50 linhas
docker logs --tail 50 dashboard-financeiro
```

## 📊 Vantagens do Docker neste Projeto

### ✅ Prós
- **Isolamento**: Não afeta outras instalações Python
- **Portabilidade**: Roda igual em Windows, Linux, Mac
- **Deploy fácil**: Sobe rapidamente em qualquer servidor
- **Versionamento**: Cada versão fica "congelada"

### ❌ Contras
- **Overhead**: Consome mais recursos que execução direta
- **Complexidade**: Mais arquivos para manter
- **Debug**: Mais difícil debugar problemas

## 🎯 Quando Usar Docker

### ✅ Use Docker quando:
- Quer fazer deploy em servidor
- Tem problemas de dependências
- Quer distribuir para outros usuários
- Planeja usar em produção

### ❌ Não precisa Docker quando:
- Só usa localmente
- Ambiente Python já configurado
- Primeira vez experimentando o projeto
- Quer desenvolvimento ágil

## 🚀 Deploy em Cloud

### AWS ECS/Fargate
```bash
# Tag para ECR
docker tag dashboard-financeiro:latest your-account.dkr.ecr.region.amazonaws.com/dashboard-financeiro:latest

# Push para ECR
docker push your-account.dkr.ecr.region.amazonaws.com/dashboard-financeiro:latest
```

### Google Cloud Run
```bash
# Deploy direto
gcloud run deploy dashboard-financeiro --source .
```

### Azure Container Instances
```bash
# Deploy no Azure
az container create --resource-group myResourceGroup --name dashboard-financeiro --image dashboard-financeiro
```

---

## 💡 Recomendação

Para **uso pessoal**: Execute diretamente com `streamlit run main.py`

Para **produção/compartilhamento**: Use Docker

**O melhor dos dois mundos**: Mantenha ambas as opções disponíveis!
