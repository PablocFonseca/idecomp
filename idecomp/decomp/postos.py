from cfinterface.files.registerfile import RegisterFile
from idecomp.decomp.modelos.postos import RegistroPostos
import pandas as pd  # type: ignore


from typing import TypeVar, List, Optional, Union, IO

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Postos(RegisterFile):
    """
    Armazena os dados de entrada do DECOMP referentes ao postos
    e seus históricos.
    """

    T = TypeVar("T")

    REGISTERS = [RegistroPostos]
    POSTOS = 320
    STORAGE = "BINARY"

    def __init__(self, data=...) -> None:
        super().__init__(data)
        self.__df: Optional[pd.DataFrame] = None
        RegistroPostos.set_postos(self.POSTOS)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="postos.dat") -> "Postos":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="postos.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def write(self, to: Union[str, IO], *args, **kwargs):
        self.__atualiza_registros()
        super().write(to, *args, **kwargs)

    def __monta_df_de_registros(self) -> Optional[pd.DataFrame]:
        registros: List[RegistroPostos] = [
            r for r in self.data.of_type(RegistroPostos)
        ]
        if len(registros) == 0:
            return None
        df = pd.DataFrame(
            data={
                "Nome": [r.data[0] for r in registros],
                "Ano Inicial Historico": [r.data[1] for r in registros],
                "Ano Final Historico": [r.data[2] for r in registros],
            }
        )

        df = df.astype(
            {
                "Nome": str,
                "Ano Inicial Historico": int,
                "Ano Final Historico": int,
            }
        )
        return df

    def __atualiza_registros(self):
        registros: List[RegistroPostos] = [r for r in self.data][1:]
        n_registros = len(registros)
        n_meses = self.postos.shape[0]
        # Deleta os registros que sobraram
        for i in range(n_meses, n_registros):
            self.data.remove(registros[i])
        # Cria registros se faltaram
        for i in range(n_registros, n_meses):
            self.data.append(RegistroPostos())
        # Atualiza os dados
        for (_, linha), r in zip(self.postos.iterrows(), registros):
            r.data = linha.tolist()

    @property
    def postos(self) -> pd.DataFrame:
        """
        Obtém a tabela com os dados dos postos existentes no arquivo
        binário.

        - Nome (`str`)
        - Ano Inicial Histórico (`int`)
        - Ano Final Histórico (`int`)

        :return: A tabela com os postos
        :rtype: pd.DataFrame
        """
        if self.__df is None:
            self.__df = self.__monta_df_de_registros()
        return self.__df

    @postos.setter
    def postos(self, df: pd.DataFrame):
        self.__df = df
