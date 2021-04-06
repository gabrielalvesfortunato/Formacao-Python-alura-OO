# Para se nomear objetos usa-se o padrão Camel Case.
class ContaCorrente:

    # Definindo o Construtor da classe
    def __init__(self, numero, titular, limite = 1000, saldo = 0):
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    def extrato(self):
        print("\nConta: {} \nTitular: {} \nSaldo: R${} \nLimite: R${}\n".format(self.__numero, self.__titular,
                                                                              self.__saldo, self.__limite))

    def depositar(self, valor):
        if self.__limite < 1000:
            deposito_limite = abs(valor - self.__limite)
            self.__saldo = self.__saldo + deposito_limite
            self.__limite = 1000.00
            print("\nDepósito no valor de {} realizado com sucesso!".format(valor))

        elif self.__limite == 1000:
            self.__saldo += valor
            print("\nDepósito no valor de {} realizado com sucesso!".format(valor))


    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_disponivel_para_saque >= valor_a_sacar


    def sacar(self, valor):
        if self.__pode_sacar():
            if self.__saldo >= valor:
                self.__saldo -= valor
                print("\nSaque no valor de {} realizado com sucesso!".format(valor))

            else:
                retira_limite = abs(self.__saldo - valor)
                self.__limite -= retira_limite
                self.__saldo = 0.0
                print("\nSaque no valor de {} realizado com sucesso!".format(valor))

        else:
            print("\nO valor que deseja sacar e maior que o valor disponível em conta.")


    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)