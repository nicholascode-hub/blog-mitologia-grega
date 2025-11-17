# ⚡ Blog da Mitologia Grega ⚡

Um blog educacional sobre os Deuses do Olimpo e suas histórias fascinantes da mitologia grega.

🌐 **[Acesse o site ao vivo](https://yetifofo777.pythonanywhere.com)**

![Django](https://img.shields.io/badge/Django-5.2.8-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Sobre o Projeto

Este blog apresenta informações detalhadas sobre os 12 Deuses do Olimpo e outras divindades importantes da mitologia grega. Cada deus possui uma página dedicada com:

- ⚡ **Domínio e poderes**
- 🎭 **Símbolos característicos**
- 👨‍👩‍👧‍👦 **Genealogia**
- 📜 **História e características**
- 🏛️ **Equivalente na mitologia romana**

### Deuses Disponíveis

**Os 12 Olimpianos:**
- Zeus (Rei dos Deuses)
- Hera (Rainha dos Deuses)
- Poseidon (Deus dos Mares)
- Atena (Deusa da Sabedoria)
- Ares (Deus da Guerra)
- Deméter (Deusa da Colheita)
- Apolo (Deus do Sol)
- Ártemis (Deusa da Caça)
- Hefesto (Deus da Forja)
- Afrodite (Deusa do Amor)
- Hermes (Mensageiro dos Deuses)
- Dionísio (Deus do Vinho)

**Fora do Olimpo:**
- Hades (Deus do Submundo)

---

## 🚀 Tecnologias Utilizadas

- **Backend:** Django 5.2.8
- **Frontend:** HTML5, CSS3 (Design responsivo)
- **Banco de Dados:** SQLite3
- **Hospedagem:** PythonAnywhere
- **Versionamento:** Git & GitHub

---

## 🎨 Características

✅ Design responsivo e moderno com tema mitológico  
✅ Interface intuitiva com cards interativos  
✅ Navegação simples e direta  
✅ URLs amigáveis (`/deuses/nome-do-deus/`)  
✅ Sistema de templates reutilizável  
✅ Otimizado para SEO  

---

## 💻 Instalação Local

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/nicholascode-hub/blog-mitologia-grega.git
cd blog-mitologia-grega
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Execute as migrações:**
```bash
python manage.py migrate
```

6. **Colete os arquivos estáticos:**
```bash
python manage.py collectstatic
```

7. **Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

8. **Acesse no navegador:**
```
http://127.0.0.1:8000
```

---

## 📁 Estrutura do Projeto

```
blog-mitologia-grega/
├── mitologia_grega/        # Configurações do projeto
│   ├── settings.py         # Configurações Django
│   ├── urls.py             # Roteamento de URLs
│   ├── views.py            # Lógica das views
│   └── wsgi.py             # Configuração WSGI
├── templates/              # Templates HTML
│   ├── base.html           # Template base
│   ├── index.html          # Página inicial
│   └── deuses/
│       └── detalhes.html   # Página de detalhes
├── staticfiles/            # Arquivos estáticos coletados
├── venv/                   # Ambiente virtual (não versionado)
├── db.sqlite3              # Banco de dados
├── manage.py               # Utilitário Django
├── requirements.txt        # Dependências do projeto
├── .gitignore              # Arquivos ignorados pelo Git
├── LICENSE                 # Licença MIT
└── README.md               # Este arquivo
```

---

## 🌐 Deploy

O projeto está hospedado no **PythonAnywhere** e pode ser acessado em:

**🔗 [yetifofo777.pythonanywhere.com](https://yetifofo777.pythonanywhere.com)**

### Como Fazer Deploy no PythonAnywhere

1. Crie uma conta gratuita em [PythonAnywhere](https://www.pythonanywhere.com)
2. Clone o repositório no Bash Console
3. Configure o ambiente virtual
4. Configure o WSGI file
5. Configure os arquivos estáticos
6. Reload o web app

Para instruções detalhadas, consulte a [documentação do PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

---

## 🛠️ Desenvolvimento

### Adicionar Novo Deus

Para adicionar um novo deus ao blog:

1. Abra `mitologia_grega/views.py`
2. Adicione as informações no dicionário `DEUSES`:

```python
'nome_do_deus': {
    'nome': 'Nome do Deus',
    'emoji': '🔱',
    'titulo': 'Título',
    'dominio': 'Descrição do domínio',
    'simbolos': 'Símbolos associados',
    'genealogia': 'Árvore genealógica',
    'caracteristicas': 'Características principais',
    'descricao': 'Descrição detalhada'
}
```

3. O deus será automaticamente adicionado à página inicial!

### Comandos Úteis

```bash
# Executar testes
python manage.py test

# Criar superusuário (admin)
python manage.py createsuperuser

# Verificar problemas
python manage.py check

# Fazer migrações
python manage.py makemigrations
python manage.py migrate
```

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Siga estes passos:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Nicholas**

- GitHub: [@nicholascode-hub](https://github.com/nicholascode-hub)
- Projeto: [Blog Mitologia Grega](https://github.com/nicholascode-hub/blog-mitologia-grega)
- Website: [yetifofo777.pythonanywhere.com](https://yetifofo777.pythonanywhere.com)

---

## 🙏 Agradecimentos

- Inspirado pela rica mitologia grega
- Comunidade Django
- PythonAnywhere por hospedar o projeto gratuitamente

---

## 📊 Status do Projeto

✅ **Versão 1.0 - Concluído**

- [x] Estrutura básica do Django
- [x] Sistema de templates
- [x] Informações dos 13 deuses
- [x] Design responsivo
- [x] Deploy no PythonAnywhere
- [ ] Sistema de busca (futuro)
- [ ] Área de comentários (futuro)
- [ ] Painel administrativo (futuro)

---

## 📧 Contato

Para dúvidas, sugestões ou feedback, abra uma [issue](https://github.com/nicholascode-hub/blog-mitologia-grega/issues) no GitHub.

---

<div align="center">

**⚡ Feito com ❤️ e Django ⚡**

[⬆ Voltar ao topo](#-blog-da-mitologia-grega-)

</div>
