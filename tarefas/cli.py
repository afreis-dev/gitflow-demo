"""Interface de linha de comando do gerenciador de tarefas."""

import argparse
import sys

from tarefas.gerenciador import GerenciadorDeTarefas

ARQUIVO_PADRAO = "tarefas.json"


def criar_parser():
    parser = argparse.ArgumentParser(
        prog="tarefas", description="Gerenciador de tarefas de demonstração."
    )
    parser.add_argument(
        "--arquivo", default=ARQUIVO_PADRAO, help="arquivo JSON com as tarefas"
    )
    comandos = parser.add_subparsers(dest="comando", required=True)

    adicionar = comandos.add_parser("adicionar", help="adiciona uma tarefa")
    adicionar.add_argument("titulo", help="título da tarefa")

    listar = comandos.add_parser("listar", help="lista as tarefas")
    listar.add_argument(
        "--pendentes", action="store_true", help="mostra só as pendentes"
    )

    concluir = comandos.add_parser("concluir", help="conclui uma tarefa")
    concluir.add_argument("id", type=int, help="id da tarefa")

    remover = comandos.add_parser("remover", help="remove uma tarefa")
    remover.add_argument("id", type=int, help="id da tarefa")

    return parser


def main(argv=None):
    args = criar_parser().parse_args(argv)
    gerenciador = GerenciadorDeTarefas(args.arquivo)

    try:
        if args.comando == "adicionar":
            print(f"Adicionada: {gerenciador.adicionar(args.titulo)}")
        elif args.comando == "listar":
            tarefas = gerenciador.listar(apenas_pendentes=args.pendentes)
            print("\n".join(str(t) for t in tarefas) or "Nenhuma tarefa.")
        elif args.comando == "concluir":
            print(f"Concluída: {gerenciador.concluir(args.id)}")
        elif args.comando == "remover":
            print(f"Removida: {gerenciador.remover(args.id)}")
    except (ValueError, KeyError) as erro:
        print(f"Erro: {erro.args[0]}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
