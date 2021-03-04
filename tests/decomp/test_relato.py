# Rotinas de testes associadas ao arquivo relato.rvx do DECOMP
from idecomp.decomp.relato import LeituraRelato


leitor = LeituraRelato("tests/_arquivos")
leitor.le_arquivo()


def test_leitura():
    n_semanas = leitor.relato.dados_gerais.numero_semanas_1_mes
    assert n_semanas == 5


def test_cmo():
    cmo_medio = leitor.relato.cmo.custo_medio_subsistema
    assert len(cmo_medio.keys()) == 5


def test_eq_relato():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo()
    assert leitor2.relato == leitor.relato


def test_leitura_rv1():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv1")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 4
    tabela_cmo = leitor2.relato.cmo.tabela
    assert tabela_cmo.shape[1] == 4


def test_leitura_rv2():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv2")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 3
    tabela_cmo = leitor2.relato.cmo.tabela
    assert tabela_cmo.shape[1] == 3


def test_leitura_rv3():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv3")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 2
    tabela_cmo = leitor2.relato.cmo.tabela
    assert tabela_cmo.shape[1] == 2


def test_leitura_rv4():
    leitor2 = LeituraRelato("tests/_arquivos")
    leitor2.le_arquivo("relato.rv4")
    n = leitor2.relato.dados_gerais.numero_semanas_1_mes
    assert n == 1
    tabela_cmo = leitor2.relato.cmo.tabela
    assert tabela_cmo.shape[1] == 1
