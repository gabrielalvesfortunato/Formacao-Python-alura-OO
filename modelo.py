# OBS: Usamos a classe mãe para colocar aquilo que há em comum entre as outras classes: generalização
# Nas classes Filhas podemos ter os atributos e métodos próprios: Especialização

from abc import ABCMeta, abstractmethod

# Criando uma super classe ou classe mae
class Programa(metaclass = ABCMeta):

    def __init__(self, nome, ano):
        self._nome   = nome.title()
        self._likes  = 0
        self.ano     = ano

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @abstractmethod # Isso obriga as subclasses a implementarem esse método da classe mae
    def __str__(self):
        return f'{self._nome} - {self.ano}: {self._likes} Likes'


# Usando Herança 'Entre parenteses a classe mae'
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #Com o metodo super() pegamos os atributos do __init__ da classe mae
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min: {self._likes} Likes'


# Usando Herança 'Entre parenteses a classe mae'
class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) #Com o metodo super() pegamos os atributos do __init__ da classe mae
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas: {self._likes} Likes'


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Transforma o objeto em um iterable
    def __getitem__(self, item):
        return self._programas[item]

    # Transforma o objeto em um sized
    def __len__(self):
        return len(self._programas)



vingadores = Filme("vingadores - guerra infinita", 2018, 160)
greys_anatomy = Serie("grey´s anatomy", 2009, 10)
todo_mundo_em_panico = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

todo_mundo_em_panico.dar_like()
todo_mundo_em_panico.dar_like()
todo_mundo_em_panico.dar_like()
todo_mundo_em_panico.dar_like()

demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

greys_anatomy.dar_like()
greys_anatomy.dar_like()
greys_anatomy.dar_like()
greys_anatomy.dar_like()
greys_anatomy.dar_like()


filmes_e_series = [vingadores, greys_anatomy, todo_mundo_em_panico]

playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}\n')

for programa in playlist_fim_de_semana:
    print(programa)