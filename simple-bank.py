###

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.conta = None
    
    def abrir_conta(self, tipo, numero, banco, agencia):
        self.conta = Conta(tipo, numero, banco, agencia)

    def __repr__(self) -> str:
        if self.conta:
            
            return f"Pessoa é {self.nome} | Idade {self.idade} | \
Conta tipo {self.conta.tipo} | Numero {self.conta.numero} | Banco {self.conta.banco} | \
Agencia {self.conta.agencia}"
        
        return f"Pessoa é {self.nome} | Idade {self.idade}"

class Conta:
    def __init__(self, tipo, numero, banco, agencia) -> None:
        self.tipo = tipo
        self.numero = numero
        self.banco = banco
        self.agencia = agencia
    
    def __repr__(self) -> str:
        return f"Conta tipo {self.tipo} | Numero {self.numero} | Banco {self.banco} | \
Agencia {self.agencia}"

class Banco:
    def __init__(self, nome_banco, agencia) -> None:
        self.nome_banco = nome_banco
        self.agencia = agencia
    
    def __repr__(self) -> str:
        return f"Banco {self.nome_banco} | Agencia {self.agencia}"


p1 = Pessoa("Vergil", 29)
print(p1)
p1.abrir_conta("corrente", 5678, "do Brasil", "Inferno")
print(p1.conta)
print()
print(p1)