import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_enviador_de_email():
    enviador= Enviador()
    assert Enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['email1@gmail.com', 'email10@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'email2@gmail.com',
        'Curso PythonPro',
        'Turma Thiago Avelino'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'email']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'email2@gmail.com',
            'Curso PythonPro',
            'Turma Thiago Avelino'
        )