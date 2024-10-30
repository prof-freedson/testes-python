class CalculadoraIMC:
    
    #criar o método calcular
    def calcular(self, peso, altura):
        
        imc = peso / (altura * altura)
        
        if imc < 19:
            return "Magreza"
        elif imc >= 19 and imc < 24:
            return "Normal"
        elif imc >= 24 and imc < 29:
            return "Sobrepeso"
        else:
            return "Obesidade"
        