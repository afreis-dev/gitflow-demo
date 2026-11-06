"""Regras de negócio do gerenciador de tarefas."""

import json
from pathlib import Path

from tarefas.modelos import Tarefa


class GerenciadorDeTarefas:
    """Mantém a lista de tarefas, opcionalmente salva em um arquivo JSON."""

    def __init__(self, caminho=None):
        self._caminho = Path(caminho) if caminho else None
        self._tarefas = []
        if self._caminho and self._caminho.exists():
            self._carregar()

    def adicionar(self, titulo):
        """Cria uma nova tarefa pendente e a devolve."""
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("O título da tarefa não pode ser vazio.")
        tarefa = Tarefa(id=self._proximo_id(), titulo=titulo)
        self._tarefas.append(tarefa)
        self._salvar()
        return tarefa

    def listar(self, apenas_pendentes=False):
        """Devolve as tarefas, opcionalmente só as ainda pendentes."""
        if apenas_pendentes:
            return [t for t in self._tarefas if not t.concluida]
        return list(self._tarefas)

    def _proximo_id(self):
        return max((t.id for t in self._tarefas), default=0) + 1

    def _carregar(self):
        with self._caminho.open(encoding="utf-8") as arquivo:
            self._tarefas = [Tarefa(**dados) for dados in json.load(arquivo)]

    def _salvar(self):
        if not self._caminho:
            return
        dados = [vars(t) for t in self._tarefas]
        with self._caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
