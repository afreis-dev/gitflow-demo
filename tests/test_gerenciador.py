import tempfile
import unittest
from pathlib import Path

from tarefas.gerenciador import GerenciadorDeTarefas


class GerenciadorDeTarefasTest(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorDeTarefas()

    def test_adicionar_cria_tarefa_pendente_com_id_sequencial(self):
        primeira = self.gerenciador.adicionar("estudar gitflow")
        segunda = self.gerenciador.adicionar("abrir pull request")

        self.assertEqual((primeira.id, segunda.id), (1, 2))
        self.assertFalse(primeira.concluida)

    def test_adicionar_rejeita_titulo_vazio(self):
        with self.assertRaises(ValueError):
            self.gerenciador.adicionar("   ")

    def test_listar_apenas_pendentes(self):
        feita = self.gerenciador.adicionar("feita")
        self.gerenciador.adicionar("pendente")
        self.gerenciador.concluir(feita.id)

        titulos = [t.titulo for t in self.gerenciador.listar(apenas_pendentes=True)]

        self.assertEqual(titulos, ["pendente"])

    def test_concluir_marca_tarefa_como_concluida(self):
        tarefa = self.gerenciador.adicionar("estudar")

        self.gerenciador.concluir(tarefa.id)

        self.assertTrue(self.gerenciador.listar()[0].concluida)

    def test_remover_tira_tarefa_da_lista(self):
        tarefa = self.gerenciador.adicionar("estudar")

        self.gerenciador.remover(tarefa.id)

        self.assertEqual(self.gerenciador.listar(), [])

    def test_id_inexistente_levanta_erro(self):
        with self.assertRaises(KeyError):
            self.gerenciador.concluir(42)
        with self.assertRaises(KeyError):
            self.gerenciador.remover(42)

    def test_novo_id_segue_o_maior_id_existente(self):
        primeira = self.gerenciador.adicionar("a")
        self.gerenciador.adicionar("b")
        self.gerenciador.remover(primeira.id)

        terceira = self.gerenciador.adicionar("c")

        self.assertEqual(terceira.id, 3)

    def test_persistencia_em_arquivo(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "tarefas.json"
            original = GerenciadorDeTarefas(caminho)
            tarefa = original.adicionar("salvar em disco")
            original.concluir(tarefa.id)

            recarregado = GerenciadorDeTarefas(caminho)

            self.assertEqual(recarregado.listar(), original.listar())


if __name__ == "__main__":
    unittest.main()
