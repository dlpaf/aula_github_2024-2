import json

class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def para_dicionario(self):
        return {'id': self.id, 'nome': self.nome, 'email': self.email}

    @staticmethod
    def de_json(dados):
        return Usuario(dados['id'], dados['nome'], dados['email'])

class GerenciadorUsuarios:
    def __init__(self, arquivo='usuarios.json'):
        self.arquivo = arquivo
        self.carregar_usuarios()

    def carregar_usuarios(self):
        try:
            with open(self.arquivo, 'r') as f:
                self.usuarios = {u['id']: Usuario.de_json(u) for u in json.load(f)}
        except FileNotFoundError:
            self.usuarios = {}

    def salvar_usuarios(self):
        with open(self.arquivo, 'w') as f:
            json.dump([u.para_dicionario() for u in self.usuarios.values()], f)

    def adicionar_usuario(self, usuario):
        self.usuarios[usuario.id] = usuario
        self.salvar_usuarios()

    def atualizar_usuario(self, id_usuario, novo_nome=None, novo_email=None):
        usuario = self.usuarios.get(id_usuario)
        if usuario is None:
            print('Usuário não encontrado.')
            return False
        
        if novo_nome:
            usuario.nome = novo_nome
        if novo_email:
            usuario.email = novo_email

        self.salvar_usuarios()
        print(f'Usuário atualizado com sucesso: {usuario}')
        return True


if __name__ == "__main__":

    gerenciador = GerenciadorUsuarios()
    gerenciador.adicionar_usuario(Usuario(1, 'Nome Teste', 'teste@gcorreio.com'))
    gerenciador.atualizar_usuario(id_usuario=1, novo_nome="Jao Caminhao", novo_email='novo@bol.com')