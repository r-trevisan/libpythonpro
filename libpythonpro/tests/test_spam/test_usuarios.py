from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Rafael', email='email@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Rafael', email='email1@gmail.com'),
        Usuario(nome='Henrique', email='email2@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()