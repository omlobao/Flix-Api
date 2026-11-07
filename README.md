# Flix API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Django_REST_Framework-3.17-A30000?style=for-the-badge&logo=django&logoColor=white" alt="DRF" />
  <img src="https://img.shields.io/badge/JWT_Auth-SimpleJWT-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT" />
  <img src="https://img.shields.io/badge/Status-Concluido-success?style=for-the-badge" alt="Status" />
</p>

> **Flix API** e uma API RESTful desenvolvida com **Django** e **Django REST Framework (DRF)** para gerenciamento de catalogo cinematografico, contemplando filmes, generos, atores, avaliacoes e metricas analiticas.

---

## Funcionalidades

- **Autenticacao JWT:** emissao e renovacao de tokens de acesso (`access`) e atualizacao (`refresh`) utilizando `djangorestframework-simplejwt`.
- **Controle de Acesso Dinamico (RBAC):** classe de permissao customizada (`GlobalDefaultPermissions`) que mapeia automaticamente os metodos HTTP (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) para as permissoes nativas do Django (`<app>.<acao>_<modelo>`).
- **Analise e Estatisticas:**
  - Estatisticas de filmes com contagem geral, distribuicao por genero, total de avaliacoes e nota media calculada via agregacoes do Django ORM.
  - Estatisticas de atores agrupados por nacionalidade utilizando agregacao com `Count`.
- **Serializacao Inteligente:**
  - Leitura detalhada com objetos aninhados (`GenreSerializer`, `ActorSerializer`), notas medias e duracao formatada.
  - Escrita otimizada recebendo chaves estrangeiras diretamente por ID.
- **Comandos de Linha de Comando (CLI):**
  - Comando customizado (`python manage.py import_actors <arquivo.csv>`) para carga em lote de atores via terminal.
- **Integridade Referencial:** protecao contra exclusao acidental de generos com filmes vinculados (`on_delete=models.PROTECT`).

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Framework Web:** Django 6.0
- **Toolkit de API:** Django REST Framework (DRF) 3.17
- **Autenticacao:** JSON Web Tokens (`djangorestframework-simplejwt`)
- **Banco de Dados:** SQLite (padrao de desenvolvimento)

---

## Mapa de Endpoints da API

Todos os endpoints utilizam o prefixo versionado `/api/v1/`:

### Autenticacao
| Metodo | Endpoint | Descricao | Requer Auth |
|---|---|---|---|
| `POST` | `/api/v1/authentication/token/` | Obter par de tokens JWT (`access` e `refresh`) | Nao |
| `POST` | `/api/v1/authentication/token/refresh/` | Renovar token de acesso expirado | Nao |

### Generos (`genres`)
| Metodo | Endpoint | Descricao | Permissao Django |
|---|---|---|---|
| `GET` | `/api/v1/genres/` | Listar todos os generos cadastrados | `genres.view_genre` |
| `POST` | `/api/v1/genres/` | Criar um novo genero | `genres.add_genre` |
| `GET` | `/api/v1/genres/<id>/` | Obter detalhes de um genero | `genres.view_genre` |
| `PUT` / `PATCH` | `/api/v1/genres/<id>/` | Atualizar dados do genero | `genres.change_genre` |
| `DELETE` | `/api/v1/genres/<id>/` | Excluir um genero (com protecao de chave estrangeira) | `genres.delete_genre` |

### Atores (`actors`)
| Metodo | Endpoint | Descricao | Permissao Django |
|---|---|---|---|
| `GET` | `/api/v1/actors/` | Listar todos os atores | `actors.view_actor` |
| `POST` | `/api/v1/actors/` | Cadastrar novo ator | `actors.add_actor` |
| `GET` | `/api/v1/actors/<id>/` | Obter dados de um ator especifico | `actors.view_actor` |
| `PUT` / `PATCH` | `/api/v1/actors/<id>/` | Atualizar informacoes do ator | `actors.change_actor` |
| `DELETE` | `/api/v1/actors/<id>/` | Remover um ator do catalogo | `actors.delete_actor` |
| `GET` | `/api/v1/actors/stats/` | Estatisticas de atores por nacionalidade | `actors.view_actor` |

### Filmes (`movies`)
| Metodo | Endpoint | Descricao | Permissao Django |
|---|---|---|---|
| `GET` | `/api/v1/movies/` | Listar filmes com dados aninhados e nota media | `movies.view_movie` |
| `POST` | `/api/v1/movies/` | Cadastrar novo filme com vinculos de atores e genero | `movies.add_movie` |
| `GET` | `/api/v1/movies/<id>/` | Detalhes completos do filme | `movies.view_movie` |
| `PUT` / `PATCH` | `/api/v1/movies/<id>/` | Atualizar filme | `movies.change_movie` |
| `DELETE` | `/api/v1/movies/<id>/` | Remover filme | `movies.delete_movie` |
| `GET` | `/api/v1/movies/stats/` | Painel analitico geral (total, distribuicao e media) | `movies.view_movie` |

### Avaliacoes (`reviews`)
| Metodo | Endpoint | Descricao | Permissao Django |
|---|---|---|---|
| `GET` | `/api/v1/reviews/` | Listar todas as avaliacoes | `reviews.view_review` |
| `POST` | `/api/v1/reviews/` | Avaliar um filme (nota de 1 a 5 com comentario opcional) | `reviews.add_review` |
| `GET` | `/api/v1/reviews/<id>/` | Visualizar uma avaliacao | `reviews.view_review` |
| `PUT` / `PATCH` | `/api/v1/reviews/<id>/` | Atualizar avaliacao | `reviews.change_review` |
| `DELETE` | `/api/v1/reviews/<id>/` | Excluir avaliacao | `reviews.delete_review` |

---

## Como Executar o Projeto Localmente

### Pre-requisitos
- Python 3.10 ou superior instalado
- Git instalado

### Instrucoes de Instalacao

1. Clone o repositorio:
   ```bash
   git clone https://github.com/omlobao/Flix-Api.git
   cd flix-api
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   # macOS / Linux:
   python3 -m venv venv
   source venv/bin/activate

   # Windows:
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migracoes do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuario (administrador):
   ```bash
   python manage.py createsuperuser
   ```

6. (Opcional) Importe a base de atores via comando de gerenciamento:
   ```bash
   python manage.py import_actors actors.csv
   ```

7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

O servidor estara disponivel em: `http://localhost:8000/`  
Painel administrativo do Django: `http://localhost:8000/admin/`

---

## Autenticacao e Consumo da API

### 1. Obter Token JWT
Envie uma requisicao `POST` para `http://localhost:8000/api/v1/authentication/token/`:
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### 2. Utilizar Token nas Requisicoes
Nas rotas protegidas, inclua o token recebido no cabecalho HTTP `Authorization`:
```text
Authorization: Bearer <seu_access_token>
```

---

## Estrutura do Projeto

```text
flix-api/
|-- actors/            # Modulo de atores (models, views, serializers, comandos CLI)
|   `-- management/commands/import_actors.py
|-- app/               # Configuracao central do projeto Django
|   |-- permissions.py # Classe GlobalDefaultPermissions (RBAC)
|   |-- settings.py
|   `-- urls.py
|-- authentication/    # Rotas de integracao com SimpleJWT
|-- genres/            # Modulo de generos cinematograficos
|-- movies/            # Modulo de filmes e estatisticas
|-- reviews/           # Modulo de avaliacoes
|-- actors.csv         # Dados para carga inicial
|-- requirements.txt   # Dependencias do projeto
|-- .gitignore         # Regras de exclusao do Git
`-- manage.py
```

---

