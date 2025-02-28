# AULA 01 !

## NOMENCLATURA
- Um arquivo .py em python, chamamos de módulo.
- Uma pasta dentro do workspace, chamamos de diretório.

1. Cases
``snake_case`` -> Tudo minúsculo, palavras separadas por underline.
``camelCase`` -> Primeira letra da primeira palavra em minúsculo e toda 
próxima palavra a primeira letra em maiúsculo.

## OBSERVAÇÕES
1. Python é uma linguagem fracamente tipada.

================================================================================

# AULA 02 !

1. Para informar quantas casas decimais você quer após a virgula,
utilizamos o comand :.2f (ou o número que desejar).
2. Ao dividirmos dois números inteiros, caso seja necessário, ocorre uma
conversão implícita [casting]

## VARIÁVEIS
``String`` -> Conjunto de caracteres especiais ou não.
``Number int`` -> Números inteiros.
``Number float`` -> Números decimais.
``Boolean`` -> Verdadeiro ou falso.

## MÉTODOS
``Input()`` -> Entrada de dados.
``Print()`` -> Saída de dados.
``Def()`` -> Função.

================================================================================

# AULA 03 !
1. Em Python, no momento que vamos realizar alguma operação, existe uma precedência.
 Primeiramente, realizamos a * e a /.
 Depois, a + e a - .
Podemos utilizar os () para quebrar ou organizar uma operação.

2. Em Python, toda vez que utilizamos o método `input()`, a entrada automaticamente será do tipo `string`.

3. Para converter uma string para `int` ou `float`, podemos utilizar os métodos 
`int()` ou `float()`.

================================================================================

# AULA 05 !

## ESTRUTURAS DE REPETIÇÃO

1. for
-> Você ira utilizar quando de antemão se sabe a quantidade de vezes que a repetição irá acontecer.
Normalmente, é utilizada para `iterar` sobre elementos de uma sequência.
  1.1 - range() -> Gera uma sequência de números. (inclusivo, exclusivo).

2. while
->  Será utilizado quando você não sabe ao certo quantas vezes a repetição irá acontecer.
Será executado enquanto a condição for verdadeira.

================================================================================

# AULA 06 !

## COMANDO DE DESVIO

1. continue -> Significa continuar, basicamente se uma condição for favorável, ela será desconsiderada.
2. break -> Significa quebrar, quando uilizado irá finalizar o loop mais próximo.

## FUNÇÕES

-> É um bloco de código que é reutilizável. Serve para deixar o código mais organizado e eficiente. `Executam uma tarefa específica`


## OBSERVAÇÕES 

1. .lower() -> Quando utilizado, transforma uma string em minúscula.
  ex: "sair" pode ser inserido como "Sair", "SAIR", "sAIR", etc...

================================================================================

# AULA 07 !

## PRINCÍPIOS DA PROGRAMAÇÃO ORIENTADA A OBJETOS (P.O.O)

1. ENCAPSULAMENTO
2. HERANÇA -> é um conceito de POO que permite que uma classe herde atributos e métodos de outra, evitando a repetição de código.
3. POLIMORFISMO
4. ABSTRAÇÃO

## PALAVRAS RESERVADAS EM POO

1. class -> é uma palavra-chave em python onde você cria um molde. Toda classe pode ter atributos e métodos, sendo que os atributos precisam estar dentro de um método chamado construtor (__init__).
2. object -> é o nome dado a cada `cópia` criada da classe. Também conhecido como instância.
3. __init__ -> é um inicializador(construtor) onde você informa que toda cópia precisar passar aqueles valores no momento da criação. é um método especial.
4. self -> referencia o atributo atual da classe (o valor).

## TERMOS UTILIZADOS EM POO

1. método -> é uma função que está dentro de uma classe. É uma ação.
2. atributo -> são as características de uma classe.

## HERANÇA
Teremos dois tipos de classes:

- superclass -> é a classe pai, é a que oferece a herança.
- subclass -> é a classe filha, que herda a herança.

================================================================================

# Atalhos no VScode
``CTRL + B`` -> Oculta ou exibe o explorador.
``CTRL + ;`` -> Comentário de linha.
``CTRL + C`` -> Copiar.
``CTRL + V`` -> Colar.
``CTRL + Z`` -> Desfazer a última ação.
``SHIFT + ALT + SETA`` -> Duplica a linha.
``CTRL + "`` -> Abre ou fecha o terminal.
``ALT + Z`` -> Quebra linha sem pular linha.
``CTRL + D`` -> Permite alterar a mesma palavra ao mesmo tempo.
``ALT + SETA`` -> Mover a linha para cima ou para baixo.
``CTRL + SHIFT + U`` -> Transforma o texto em maiúsculo.
``SHIFT + ALT + F`` -> Ajusta a estrutura do código.

## Atalhos no Windows
``Windows + .`` -> Exibe emojis e caricteres especiais.
``Windows + R`` -> Escrever CMD abre o terminal.


