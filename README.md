📘 API de Alunos — FastAPI + Jinja2

Este projeto é uma aplicação web simples desenvolvida com FastAPI, Jinja2 e HTML/CSS, que permite listar alunos e cadastrar novos alunos com suas respectivas notas.

🚀 Tecnologias Utilizadas

FastAPI
 — Framework moderno e rápido para APIs em Python

Uvicorn
 — Servidor ASGI de alto desempenho

Jinja2
 — Template engine para renderizar páginas HTML

Python Multipart — Suporte a formulários HTML

HTML + CSS — Interface e estilização das páginas

⚙️ Instalação
3️⃣ Instalar as dependências
pip install fastapi uvicorn jinja2 python-multipart

▶️ Executar o servidor

Use o comando abaixo para iniciar o servidor localmente:

python -m uvicorn main:app --reload


Após iniciar, acesse no navegador:

👉 http://127.0.0.1:8000

📄 Estrutura de Pastas
api-alunos/
│
├── main.py                 # Código principal da aplicação FastAPI
│
├── templates/              # Páginas HTML (usando Jinja2)
│   ├── alunos.html
│   └── cadastro.html
│
├── static/                 # Arquivos estáticos (CSS, imagens, JS)
│   └── style.css
│
└── README.md               # Este arquivo

💡 Funcionalidades

✅ Listar alunos:
Exibe uma tabela com o nome e a nota de cada aluno.

✅ Cadastrar novo aluno:
Formulário para adicionar um novo aluno à lista.

✅ Classificação automática:
As linhas da tabela mudam de cor conforme o desempenho:

🟢 Aprovado: nota ≥ 6.0

🔴 Reprovado: nota < 6.0

✅ Interface moderna e responsiva:
Desenvolvida com CSS limpo e amigável.

🧩 Exemplo de Rotas
Método	Rota	Descrição
GET	/	Exibe a lista de alunos
GET	/cadastro	Mostra o formulário de cadastro
POST	/cadastro	Cadastra um novo aluno e redireciona
🖼️ Telas do Projeto
🏫 Lista de Alunos (/)

Exibe todos os alunos com suas notas e o botão para cadastrar novos.

✏️ Cadastro de Aluno (/cadastro)

Permite adicionar um novo aluno com nome e nota.

👨‍💻 Autor

Kauã Santos
📧 Email: (kaua7santos7oliveiraa@gmail.com)
💼 GitHub: github.com/kaua-santos

📝 Licença

Este projeto é de uso livre para fins educacionais.
Sinta-se à vontade para modificar e expandir.