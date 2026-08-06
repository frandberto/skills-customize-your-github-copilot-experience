# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construir uma API REST com FastAPI para praticar rotas, métodos HTTP, validação com Pydantic e códigos de status. Ao final, você terá um pequeno serviço pronto para criar, listar, atualizar e remover recursos.

## 📝 Tarefas

### 🛠️ Criar a Estrutura Base da API

#### Descrição

Inicie um projeto com FastAPI e implemente endpoints iniciais para validar que a aplicação está rodando corretamente.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI no arquivo starter
- Implementar o endpoint GET /health retornando status de funcionamento
- Implementar o endpoint GET / com uma mensagem de boas-vindas
- Rodar localmente com Uvicorn sem erros

### 🛠️ Implementar CRUD de Tarefas

#### Descrição

Implemente endpoints para gerenciar tarefas (to-do items) em memória, com campos como título, descrição e concluída.

#### Requisitos
O programa concluído deve:

- Criar modelos Pydantic para entrada e saída
- Implementar POST /tasks para criar uma tarefa
- Implementar GET /tasks para listar tarefas
- Implementar GET /tasks/{task_id} para buscar uma tarefa específica
- Implementar PUT /tasks/{task_id} para atualizar uma tarefa
- Implementar DELETE /tasks/{task_id} para remover uma tarefa

### 🛠️ Validar Dados e Respostas HTTP

#### Descrição

Adicione validações de dados e retorne códigos HTTP apropriados para sucesso e erro.

#### Requisitos
O programa concluído deve:

- Validar que o título da tarefa não pode ser vazio
- Retornar 201 ao criar recurso com sucesso
- Retornar 404 quando task_id não existir
- Retornar 204 ao remover recurso com sucesso
- Incluir mensagens de erro claras no corpo da resposta
