from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
        Usuario(nome='Rafael', email='email1@gmail.com'),
        Usuario(nome='Henrique', email='email2@gmail.com')
        ],
        [
        Usuario(nome='Rafael', email='email1@gmail.com'),
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'email1@gmail.com',
        'Curso Python Pro',
        'Confira os Módulos Fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


    def test_parametros_de_spam(sessao):
        usuario=Usuario(nome='Rafael', email='email1@gmail.com')
        sessao.salvar(usuario)
        enviador = Mock()
        enviador_de_spam = EnviadorDeSpam(sessao, enviador)
        enviador_de_spam.enviar_emails(
            'email2@gmail.com',
            'Curso Python Pro',
            'Confira os Módulos Fantásticos'
        )
        enviador.enviar.assert_called_once_with(
            'email2@gmail.com'
            'email1@gmail.com'
            'Curso Python Pro',
            'Confira os Módulos Fantásticos'
        )