from StratifiedDivisor import StratifiedDivisor
from ModelPerformance import ModelPerformance

class CrossValidation:
    def __init__(self, hyper_parameters, model_class, n_divisions, dataset):
        self.hyper_parameters_options = hyper_parameters
        self.model_klass = model_class
        self.divisions = n_divisions
        self.dataset = dataset
        pass


    def get_best_hyper_parameter(self):
        self.__calculate_performances()

        # é assim mesmo que vamos validar o melhor modelo?
        performance_indicators = map(lambda performance: performance.indicator, performances)
        best_performance_index = performance_indicators.index(min(performance_indicators))
        best_hyper_parameters = self.hyper_parameters_options[best_performance_index]

    def __calculate_performances(self):
        for parameters_index in range(len(self.hyper_parameters_options)):
            for division_version in range(self.divisions):
                model = self.__create_model(parameters_index, division_version)
                performance = self.__create_performance(model, division_version)
                self.__append_performance(performance)

    def __hyperparameters_at(self, i):
        return self.hyper_parameters_options[i]

    def __create_model(self, hyper_parameters_index, division_version):
        hyper_parameters = self.__hyperparameters_at(hyper_parameters_index)
        divisor = self.__dataset_divisor()
        training_set = divisor.get_training_set(division_version)
        return self.model_klass(hyper_parameters, training_set)

    def __create_performance(self, model, division_version):
        divisor = self.__dataset_divisor()
        test_set = divisor.get_test_set(division_version)
        return ModelPerformance(model, test_set)

    def __dataset_divisor(self):
        return StratifiedDivisor(self.dataset, self.divisions)

    def __append_performance(self, hyper_parameters_index, performance):
        if not self.performances:
            self.performances = []
        if not self.performances[hyper_parameters_index]:
            self.performances[hyper_parameters_index] = []
        self.performances[hyper_parameters_index].append(performance)
