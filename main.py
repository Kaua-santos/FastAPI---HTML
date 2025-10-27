from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

# rodar servidor : python -m uvicorn main:app --reload

app = FastAPI(title="API de alunos")

# configurar o diretorio dos tampletes jinja2
templates = Jinja2Templates(directory="templates")

# pasta static para servir os arquivos (CSS , imagens ou JS )
app.mount("/static", StaticFiles(directory="static"), name="static")

alunos = [
    {"nome": "Kauã", "nota": 10.0},
    {"nome": "Felipe", "nota": 8.5},
    {"nome": "Laura", "nota": 9.0},
    {"nome": "Yasmin", "nota": 4.0},
    {"nome": "Luis", "nota": 1.0},
    {"nome": "Lohan", "nota": 0.0},
]

# rota inicial 
@app.get("/", response_class=HTMLResponse)
def exibir_alunos(request: Request):
    return templates.TemplateResponse(
       "alunos.html", {"request": request, "lista_alunos": alunos} 
    )

# rota cadastrar (tela de cadastro)
@app.get("/cadastro",response_class=HTMLResponse)
def cadastro_aluno(request: Request):
        return templates.TemplateResponse(
       "cadastro.html", {"request": request} 
    )

# rota de cadastro 
@app.post("/cadastro")
def salvar_aluno(nome: str = Form(...), nota:float = Form(...)):
      alunos.append({"nome": nome, "nota": nota})
      return RedirectResponse(url="/", status_code=303)




