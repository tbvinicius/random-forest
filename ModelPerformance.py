class ModelPerformance:
    def __init__(self, model, test_set):
        # Model pode ser forest ou decision_tree
        # model deve implementar o método predict

        # para cada exemplo do test_set, utilizar o modelo para prever
        # sua classe e comparar com o resultado esperado.
        # por fim, calcular a média e desvio padrão do erro (ver nos slides como fazer isso)
        self.model = model
        self.test_set = test_set
        self.mean = 1
        self.std = 1
        pass

    def evaluate(self):
        # avaliar uma instância no test_set e acumular a performance
        # nos valores da classe
        pass

    def reset(self):
        # resetar os valores internos de controle de performance
        pass

    def indicator(self):
        # indicador principal de performance
        pass