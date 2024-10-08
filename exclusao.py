import time

class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario

class BancoDeDados:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario

    def excluir_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f'Usuário {id_usuario} excluído com sucesso.')
        else:
            print('Usuário não encontrado.')

class ExclusaoDeConta:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def confirmar_exclusao(self, id_usuario):
        tentativas = 0
        while tentativas < 3:
            resposta = input(f"Você realmente deseja excluir a conta do usuário {id_usuario}? (s/n): ").strip().lower()
            if resposta == 's':
                self.banco_de_dados.excluir_usuario(id_usuario)
                return
            elif resposta == 'n':
                print('Exclusão cancelada.')
                return
            else:
                print('Resposta inválida. Tente novamente.')
                tentativas += 1
        print('Número máximo de tentativas atingido. Exclusão não realizada.')

def main():
    
    #teste
    banco = BancoDeDados()
    usuario1 = Usuario("Teste", 1)
    banco.adicionar_usuario(usuario1)
    exclusao = ExclusaoDeConta(banco)
    exclusao.confirmar_exclusao(1)

if __name__ == "__main__":
    main()
