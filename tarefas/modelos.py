"""Modelos de dados do gerenciador de tarefas."""

from dataclasses import dataclass


@dataclass
class Tarefa:
    """Uma tarefa da lista."""

    id: int
    titulo: str
    concluida: bool = False

    def __str__(self) -> str:
        marca = "x" if self.concluida else " "
        return f"[{marca}] {self.id}. {self.titulo}"
