# EventPass API (Gestão de Eventos)

> **Foco:** Integridade de dados e concorrência simples.

## 1. Gestão de Eventos

- **RF01 - Criar Evento:** O sistema deve permitir o cadastro de eventos contendo: título, descrição, data, local e, obrigatoriamente, `capacidade_maxima` (número inteiro).
- **RF02 - Listar Eventos (Catálogo):** Deve retornar uma lista de eventos.
  - **Diferencial:** Cada item da lista deve ter um campo calculado dinamicamente chamado `vagas_restantes` (capacidade - total inscritos).
- **RF03 - Status de Lotação:** Se as vagas chegarem a 0, o evento deve aparecer na listagem com um status visual ou texto "SOLD OUT".

## 2. Inscrições (O Core)

- **RF04 - Registrar Participante:** Rota para inscrever uma pessoa (nome, email) em um evento.
  - **Regra de Ouro:** Antes de salvar, a API deve contar quantos inscritos já existem para aquele ID de evento. Se `contagem >= capacidade`, a API deve bloquear a inscrição e retornar **HTTP 400 (Bad Request)** com a mensagem "Evento Lotado".
- **RF05 - Cancelamento:** Permitir que um usuário cancele a inscrição através do e-mail ou ID. Isso deve liberar imediatamente uma vaga no cálculo de `vagas_restantes`.
