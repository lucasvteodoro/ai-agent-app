# 🤖 ai-agent-app

Um app construído com [LangChain](https://www.langchain.com/), que integra ferramentas para conectar com o Google e realizar buscas avançadas usando IA. Ideal para construir agentes autônomos que interagem com múltiplas fontes de informação.

---

## 🚀 Funcionalidades

- 🔗 Integração com a API de Pesquisa Personalizada do Google (Google CSE)
- 🧠 Suporte à IA via LangChain + Anthropic API
- 🌐 Interface interativa usando [Streamlit](https://streamlit.io/)
- 🐳 Contêiner Docker pronto para rodar

---

## 🛠️ Requisitos

- Python 3.11+
- Docker (opcional, mas recomendado)
- Conta com:
  - Chave da Google API
  - Google CSE ID (Custom Search Engine)
  - Chave da Anthropic API (Claude)

---

## 📦 Instalação com Docker

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/ai-agent-app.git
cd ai-agent-app
```

2. **Build o container**
```bash
docker build -t ai-agent-app .
```
3. **Execute o container**
```bash
docker run -p 8501:8501 -e GOOGLE_API_KEY=your_google_api_key -e GOOGLE_CSE_ID=your_google_cse_id -e ANTHROPIC_API_KEY=your_anthropic_api_key ai-agent-app
```
4. ***Acesse o browser**
```bash
http://localhost:8501/
```
