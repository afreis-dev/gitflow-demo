# Gitflow Demo

Repositório de demonstração do fluxo **Gitflow**. O projeto é fictício (um
gerenciador de tarefas em linha de comando) e existe apenas para praticar
branches, pull requests e commits padronizados.

## Branches

| Branch      | Função                                                      |
| ----------- | ----------------------------------------------------------- |
| `main`      | Produção: somente código estável, pronto para release       |
| `develop`   | Desenvolvimento: integração contínua das features           |
| `feature/*` | Novas funcionalidades, criadas a partir da `develop`        |

Veja o [guia de contribuição](CONTRIBUTING.md) para o fluxo completo e o
padrão de commits.

## Gerenciador de tarefas

Requisitos: Python 3.9 ou superior, sem dependências externas.

```bash
python -m tarefas adicionar "estudar gitflow"
python -m tarefas listar
python -m tarefas listar --pendentes
python -m tarefas concluir 1
python -m tarefas remover 1
```

As tarefas ficam salvas em `tarefas.json` (use `--arquivo` para trocar o
caminho).

## Testes

```bash
python -m unittest discover -s tests -v
```
