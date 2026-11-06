# Guia de contribuição

Este repositório segue o fluxo **Gitflow** e o padrão **Conventional Commits**.

## Fluxo de branches

```
main      ●───────────────────────────●──────  produção (releases)
           \                         /
develop     ●───●───────────●───────●────────  desenvolvimento
                 \         /
feature/*         ●───●───●                    novas funcionalidades
```

1. A `main` guarda apenas código de produção, estável e versionado.
2. A `develop` recebe a integração de todas as features concluídas.
3. Cada funcionalidade nasce de uma branch `feature/<nome-curto>` criada a
   partir da `develop`.
4. Ao terminar, abre-se um **pull request** da feature para a `develop`, com
   revisão obrigatória antes do merge.
5. Quando a `develop` está pronta para release, ela é integrada à `main`.

Depois da configuração inicial do repositório, nenhum código entra direto na
`main` ou na `develop`: tudo passa por pull request.

## Nome das branches

| Tipo      | Padrão                  | Exemplo                       |
| --------- | ----------------------- | ----------------------------- |
| Feature   | `feature/<descricao>`   | `feature/gerenciador-tarefas` |
| Correção  | `bugfix/<descricao>`    | `bugfix/ordem-da-listagem`    |
| Hotfix    | `hotfix/<descricao>`    | `hotfix/falha-ao-salvar`      |

## Padrão de commits

```
<tipo>(<escopo opcional>): <descrição curta no imperativo>

<corpo opcional explicando o porquê da mudança>
```

| Tipo       | Quando usar                                          |
| ---------- | ---------------------------------------------------- |
| `feat`     | Nova funcionalidade                                  |
| `fix`      | Correção de bug                                      |
| `docs`     | Mudanças somente em documentação                     |
| `test`     | Criação ou ajuste de testes                          |
| `refactor` | Mudança de código sem alterar comportamento          |
| `chore`    | Tarefas de manutenção (configuração, dependências)   |

Regras:

- Descrição em letras minúsculas, sem ponto final e com até 72 caracteres.
- Um commit por mudança lógica: não misture assuntos diferentes.
- Cada commit deve deixar o projeto funcionando.

## Pull requests

- O título segue o mesmo padrão dos commits.
- A descrição explica o que mudou, por quê e como testar.
- Pelo menos uma pessoa revisora deve ser adicionada antes do merge.
