# random-forest

### Python

Deve ser utilizada a versão Python 3.6 ou superior

### Estrutura 

#### Passo a passo

```
Precisamos validar os passos a seguir com os professores 
e garantir que estão corretos
```

1. Ler arquivo de dataset
2. Dividir o dataset em grupos e agrupá-los de maneira estratificada em: 
    - dataset de treino
    - dataset de validação
    - dataset de teste
3. Para cada configuração de hiperparâmetros, 
criar uma Floresta Aleatória passando o dataset de treinamento
4. Cada Floresta deve, a partir do dataset de treinamento, através do método
de Bootstrap com reposição, gerar outros sets de treinamento, que devem ser
usados para a indução de suas árvores de decisão
5. Utilizando o dataset de validação, avaliar o desempenho de cada Floresta
na predição das classes do mesmo
6. Compilar os desempenhos das florestas e selecionar a configuração de hiperparâmetros
com melhor desempenho
7. Re-treinar o modelo escolhido com o set de treinamento + validação 

8. Validar o modelo escolhido com  o dataset de teste

( Repetir os passos 2  ~ 5 até que todos os agrupamentos do dataset original 
tenham sido utilizados para treinamento, validação e teste ) `É isso mesmo? 
`
 
 
```
Duvidas:

1. Quais são as métricas que devemos utilizar para avaliar desempenho?
Devemos diferenciar entre classificação e regressão? Que média e desvio padrão
são esses comentados na especificação?
2. Como compilaremos as métricas, dado que sabemos quais métricas utilizarmos 
(duvida 1)
3. Para a Validação Cruzada Estratificada, devemos primeiro separar em 
treino e teste para, depois, dividirmos treino em grupos utilizaros para treino
e validação? Temos que repetir os passos de cross validation para cada configuração
de hiperparâmetros? Se não, como deve funcionar a separação e a utilização dos sets
de treinamento, validação e teste?
```

  