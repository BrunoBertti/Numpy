########## Pré-requisitos ##########

    # Você precisará conhecer um pouco de Python. Para uma atualização, consulte o tutorial do Python.

    # Para trabalhar os exemplos, você precisará do matplotlib instalado além do NumPy.

##### Perfil do aluno

    # Esta é uma visão geral rápida de matrizes no NumPy. Ele demonstra como arrays n-dimensionais (n >= 2) são representados e podem ser manipulados. Em particular, se você não souber como aplicar funções comuns a arrays n-dimensionais (sem usar loops for), ou se quiser entender as propriedades de eixo e forma para arrays n-dimensionais, este artigo pode ser útil.

##### objetivos de aprendizado

    # Após a leitura, você deverá ser capaz de:

        # Entenda a diferença entre arrays unidimensionais, bidimensionais e n-dimensionais no NumPy;

        # Entender como aplicar algumas operações de álgebra linear a arrays n-dimensionais sem usar loops for;

        # Compreender as propriedades de eixo e forma para matrizes n-dimensionais. 



########## O básico ##########

    # O objeto principal do NumPy é o array multidimensional homogêneo. É uma tabela de elementos (geralmente números), todos do mesmo tipo, indexados por uma tupla de inteiros não negativos. Em NumPy as dimensões são chamadas de eixos.

    # Por exemplo, a matriz para as coordenadas de um ponto no espaço 3D, [1, 2, 1], tem um eixo. Esse eixo tem 3 elementos nele, então dizemos que tem um comprimento de 3. No exemplo mostrado abaixo, o array tem 2 eixos. O primeiro eixo tem um comprimento de 2, o segundo eixo tem um comprimento de 3.        

        # [[1., 0., 0.],
        # [0., 1., 2.]]


    # A classe array do NumPy é chamada ndarray. Também é conhecido pela matriz de alias. Observe que numpy.array não é o mesmo que a classe array.array da Biblioteca Python Padrão, que lida apenas com arrays unidimensionais e oferece menos funcionalidade. Os atributos mais importantes de um objeto ndarray são:

    # ndarray.ndim
        # o número de eixos (dimensões) da matriz.

    # ndarray.shape (forma)
        # as dimensões da matriz. Esta é uma tupla de inteiros indicando o tamanho da matriz em cada dimensão. Para uma matriz com n linhas e m colunas, a forma será (n,m). O comprimento da tupla de forma é, portanto, o número de eixos, ndim.

    # ndarray.size
        # o número total de elementos da matriz. Isso é igual ao produto dos elementos de forma.

    # ndarray.dtype
        # um objeto que descreve o tipo dos elementos na matriz. Pode-se criar ou especificar dtypes usando tipos padrão do Python. Além disso, o NumPy fornece tipos próprios. numpy.int32, numpy.int16 e numpy.float64 são alguns exemplos.

    # ndarray.itemsize
        # o tamanho em bytes de cada elemento da matriz. Por exemplo, um array de elementos do tipo float64 tem tamanho de item 8 (=64/8), enquanto um do tipo complex32 tem tamanho de item 4 (=32/8). É equivalente a ndarray.dtype.itemsize.

    # ndarray.data
        # o buffer contendo os elementos reais do array. Normalmente, não precisaremos usar esse atributo porque acessaremos os elementos em um array usando recursos de indexação.


##### Um exemplo

import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
b = np.array([6, 7, 8])
print(b)
type(b)


##### Criação de matriz 

    # Existem várias maneiras de criar matrizes.

    # Por exemplo, você pode criar um array a partir de uma lista ou tupla regular do Python usando a função array. O tipo da matriz resultante é deduzido do tipo dos elementos nas sequências. 

import numpy as np
a = np.array([2, 3, 4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])

    # Um erro frequente consiste em chamar array com vários argumentos, em vez de fornecer uma única sequência como argumento. 

a = np.array(1, 2, 3, 4)  # ERRADO!


a = np.array([1, 2, 3, 4]) # Correto!!

    # array transforma sequências de sequências em matrizes bidimensionais, sequências de sequências de sequências em matrizes tridimensionais e assim por diante. 

b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)

    # O tipo do array também pode ser especificado explicitamente no momento da criação: 

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)


    # Muitas vezes, os elementos de uma matriz são originalmente desconhecidos, mas seu tamanho é conhecido. Portanto, o NumPy oferece várias funções para criar matrizes com conteúdo de espaço reservado inicial. Estes minimizam a necessidade de matrizes crescentes, uma operação cara.

    # A função zeros cria um array cheio de zeros, a função uns cria um array cheio de uns e a função vazia cria um array cujo conteúdo inicial é aleatório e depende do estado da memória. Por padrão, o dtype do array criado é float64, mas pode ser especificado através do argumento da palavra-chave dtype. 

np.zeros((3, 4)) # Matriz 3 x 4

np.ones((2, 3, 4), dtype=np.int16) # 2 Matriz 3x4

np.empty((2, 3)) # Matriz 2x3 de números aleatórios

    # Para criar sequências de números, NumPy fornece a função arange que é análoga ao intervalo interno do Python, mas retorna um array. 

np.arange(10, 30, 5) # Vai de 10 a 30 de 5 em 5 (30 nao entra na matriz)

np.arange(0, 2, 0.3) # ele aceita argumentos float. Vai de 0 a 2 de 0.3 em 0.3 (2 nao entra na matriz)

    # Quando arange é usado com argumentos de ponto flutuante, geralmente não é possível prever o número de elementos obtidos, devido à precisão finita do ponto flutuante. Por esse motivo, geralmente é melhor usar a função linspace que recebe como argumento o número de elementos que queremos, ao invés do passo: 

from numpy import pi
np.linspace(0, 2, 9) # 9 números de 0 a 2 


x = np.linspace(0, 2 * pi, 100)        # útil para avaliar a função em muitos pontos 
f = np.sin(x)



##### Printing Matrizes 

    # Quando você imprime uma matriz, o NumPy a exibe de maneira semelhante às listas aninhadas, mas com o seguinte layout:

        # o último eixo é impresso da esquerda para a direita,

        # o penúltimo é impresso de cima para baixo,

        # o restante também é impresso de cima para baixo, com cada fatia separada da próxima por uma linha vazia.

    # Arrays unidimensionais são então impressos como linhas, bidimensionais como matrizes e tridimensionais como listas de matrizes. 

a = np.arange(6)                    # 1d array
print(a)

b = np.arange(12).reshape(4, 3)     # 2d array
print(b)

c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)

    # Veja abaixo para obter mais detalhes sobre a remodelação.

    # Se uma matriz for muito grande para ser impressa, o NumPy pula automaticamente a parte central da matriz e imprime apenas os cantos: 


print(np.arange(10000))

print(np.arange(10000).reshape(100, 100))

    # Para desabilitar esse comportamento e forçar o NumPy a imprimir todo o array, você pode alterar as opções de impressão usando set_printoptions. 

#np.set_printoptions(threshold=sys.maxsize) # # o módulo sys deve ser importado 



##### Operações Básicas

    # Operadores aritméticos em arrays aplicam-se elemento a elemento. Um novo array é criado e preenchido com o resultado. 

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)

c = a - b
print(c)

print(b**2)

print(10 * np.sin(a))

print(a < 35)

    # Ao contrário de muitas linguagens de matriz, o operador de produto * opera elementwise em matrizes NumPy. O produto da matriz pode ser executado usando o operador @ (em python >=3.5) ou a função ou método dot: 

A = np.array([[1, 1],
              [0, 1]])

B = np.array([[2, 0],
              [3, 4]])


print(A * B) # produto elementar 

print(A @ B) # produto da matriz 


print(A.dot(B)) # outro produto de matriz 

    # Algumas operações, como += e *=, atuam no local para modificar uma matriz existente em vez de criar uma nova. 


rg = np.random.default_rng(1)  # criar instância do gerador de números aleatórios padrão 
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
a

b += a
b

a += b 



    # Ao operar com arrays de tipos diferentes, o tipo do array resultante corresponde ao mais geral ou preciso (um comportamento conhecido como upcasting). 



a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
b.dtype.name


c = a + b
c

c.dtype.name


d = np.exp(c * 1j)
d


d.dtype.name


    # Muitas operações unárias, como calcular a soma de todos os elementos do array, são implementadas como métodos da classe ndarray. 


a = rg.random((2, 3))
a

a.sum()


a.min()



a.max()


    # Por padrão, essas operações se aplicam ao array como se fosse uma lista de números, independentemente de sua forma. No entanto, especificando o parâmetro axis, você pode aplicar uma operação ao longo do eixo especificado de uma matriz: 

b = np.arange(12).reshape(3, 4)
b

b.sum(axis=0)     # soma de cada coluna 

b.min(axis=1)     # min de cada linha 

b.cumsum(axis=1)  # soma cumulativa ao longo de cada linha 



##### Funções Universais 

    # NumPy fornece funções matemáticas familiares, como sin, cos e exp. No NumPy, elas são chamadas de “funções universais” (ufunc). Dentro do NumPy, essas funções operam elemento a elemento em uma matriz, produzindo uma matriz como saída. 

B = np.arange(3)
B

np.exp(B)

np.sqrt(B)

C = np.array([2., -1., 4.])

np.add(B, C)



##### Indexação, fatiamento e iteração 

    # Arrays unidimensionais podem ser indexados, fatiados e iterados, assim como listas e outras sequências Python. 

a = np.arange(10)**3
a

a[2]

a[2:5]

# equivalente a a[0:6:2] = 1000;
# do início à posição 6, exclusivo, defina cada 2º elemento para 1000 

a[:6:2] = 1000
a

a[::-1]  # reverter a

for i in a:
    print(i**(1 / 3.))


    # Arrays multidimensionais podem ter um índice por eixo. Esses índices são dados em uma tupla separada por vírgulas: 

def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
b

b[2, 3]

b[0:5, 1]  # cada linha na segunda coluna de b

b[:, 1]    # equivalente ao exemplo anterior

b[1:3, :]  # cada coluna na segunda e terceira linha de b

    # Quando menos índices são fornecidos do que o número de eixos, os índices ausentes são considerados fatias completas: 


b[-1]   # a última linha. Equivalente a b[-1, :] 

    # A expressão entre colchetes em b[i] é tratada como um i seguido por quantas instâncias de : forem necessárias para representar os eixos restantes. O NumPy também permite que você escreva isso usando pontos como b[i, ...].

    # Os pontos (...) representam quantos dois-pontos forem necessários para produzir uma tupla de indexação completa. Por exemplo, se x é uma matriz com 5 eixos, então 


        # x[1, 2, ...] is equivalent to x[1, 2, :, :, :],

        # x[..., 3] to x[:, :, :, :, 3] and

        # x[4, ..., 5, :] to x[4, :, :, 5, :].


c = np.array([[[  0,  1,  2],  # uma matriz 3D (duas matrizes 2D empilhadas) 
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
c.shape



c[1, ...]  # igual a c[1, :, :] ou c[1] 

c[..., 2]  # igual a c[:, :, 2] 

    # A iteração sobre matrizes multidimensionais é feita em relação ao primeiro eixo: 

for row in b:
    print(row)


    # No entanto, se alguém quiser realizar uma operação em cada elemento do array, pode-se usar o atributo flat que é um iterador sobre todos os elementos do array: 

for element in b.flat:
    print(element)
    




########## Manipulação da Forma ##########

##### Mudando a forma de um array

    # Uma matriz tem uma forma dada pelo número de elementos ao longo de cada eixo: 

a = np.floor(10 * rg.random((3, 4)))
a

a.shape


    # A forma de uma matriz pode ser alterada com vários comandos. Observe que os três comandos a seguir retornam uma matriz modificada, mas não alteram a matriz original: 

a.ravel()  # retorna o array, achatado

a.reshape(6, 2)  # retorna o array com uma forma modificada

a.T   # retorna o array, transposto 

a.T.shape

a.shape

    # A ordem dos elementos no array resultante de ravel é normalmente “estilo C”, ou seja, o índice mais à direita “muda mais rápido”, então o elemento depois de a[0, 0] é a[0, 1]. Se a matriz for remodelada para outra forma, novamente a matriz será tratada como “estilo C”. O NumPy normalmente cria arrays armazenados nesta ordem, então o ravel normalmente não precisará copiar seu argumento, mas se o array foi feito pegando fatias de outro array ou criado com opções incomuns, pode ser necessário copiá-lo. As funções ravel e reshape também podem ser instruídas, usando um argumento opcional, a usar arrays no estilo FORTRAN, nos quais o índice mais à esquerda muda mais rapidamente.

    # A função reshape retorna seu argumento com uma forma modificada, enquanto o método ndarray.resize modifica o próprio array: 

a

a.resize((2, 6))

a


##### Empilhando diferentes arrays 

    # Vários arrays podem ser empilhados ao longo de diferentes eixos: 

a = np.floor(10 * rg.random((2, 2)))
a

b = np.floor(10 * rg.random((2, 2)))
b

np.vstack((a, b))

np.hstack((a, b))

    # A função column_stack empilha arrays 1D como colunas em um array 2D. É equivalente ao hstack apenas para matrizes 2D: A função column_stack empilha arrays 1D como colunas em um array 2D. É equivalente ao hstack apenas para matrizes 2D: 

from numpy import newaxis
np.column_stack((a, b))  # with 2D arrays

a = np.array([4., 2.])
b = np.array([3., 8.])
np.column_stack((a, b))  # returns a 2D array

np.hstack((a, b))        # the result is different

a[:, newaxis]  # view `a` as a 2D column vector

np.column_stack((a[:, newaxis], b[:, newaxis]))

np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same


    # Por outro lado, a função row_stack é equivalente a vstack para qualquer array de entrada. Na verdade, row_stack é um alias para vstack: 

np.column_stack is np.hstack

np.row_stack is np.vstack

    # Em geral, para arrays com mais de duas dimensões, hstack empilha ao longo de seus segundos eixos, vstack empilha ao longo de seus primeiros eixos e concatenate permite argumentos opcionais fornecendo o número do eixo ao longo do qual a concatenação deve ocorrer.

    # Nota: Em casos complexos, r_ e c_ são úteis para criar arrays empilhando números ao longo de um eixo. Eles permitem o uso de literais de intervalo

np.r_[1:4, 0, 4]

    # Quando usado com arrays como argumentos, r_ e c_ são semelhantes a vstack e hstack em seu comportamento padrão, mas permitem um argumento opcional fornecendo o número do eixo ao longo do qual concatenar. 


##### Dividindo uma matriz em várias menores 


    # Usando hsplit, você pode dividir uma matriz ao longo de seu eixo horizontal, especificando o número de matrizes de formato igual a serem retornadas ou especificando as colunas após as quais a divisão deve ocorrer: 

a = np.floor(10 * rg.random((2, 12)))
a

# Divida `a` em 3
np.hsplit(a, 3)

# Dividir `a` após a terceira e a quarta coluna 
np.hsplit(a, (3, 4))

    # vsplit divide ao longo do eixo vertical, e array_split permite especificar ao longo de qual eixo dividir. 



########## Cópias e visualizações  ########## 


    # Ao operar e manipular arrays, seus dados às vezes são copiados para um novo array e às vezes não. Isso geralmente é uma fonte de confusão para iniciantes. Existem três casos: 



##### Nenhuma cópia 

    # Atribuições simples não fazem cópia de objetos ou seus dados. 

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
b = a            # nenhum novo objeto é criado
b is a           # a e b são dois nomes para o mesmo objeto ndarray 



    # Python passa objetos mutáveis como referências, então chamadas de função não fazem cópia.
    # 
    #  
def f(x):
    print(id(x))

id(a)  # id é um identificador único de um objeto 

f(a)   


##### Ver ou cópia rasa

    # Diferentes objetos de matriz podem compartilhar os mesmos dados. O método view cria um novo objeto array que analisa os mesmos dados 

c = a.view()
c is a

c.base is a            # c é uma visão dos dados de propriedade de um

c.flags.owndata

c = c.reshape((2, 6))  # a forma de a não muda
a.shape

c[0, 4] = 1234         # alterações de dados de a 
a


    # Fatiar uma matriz retorna uma visão dela: 

s = a[:, 1:3]
s[:] = 10  # s[:] é uma visão de s. Observe a diferença entre s = 10 e s[:] = 10 
a


##### Cópia profunda

    # O método copy faz uma cópia completa do array e seus dados. 


d = a.copy()  # um novo objeto array com novos dados é criado
d is a

d.base is a  # d não compartilha nada com a

d[0, 0] = 9999
a

    # Às vezes, a cópia deve ser chamada após o fatiamento se a matriz original não for mais necessária. Por exemplo, suponha que a seja um resultado intermediário enorme e o resultado final b contenha apenas uma pequena fração de a, uma cópia profunda deve ser feita ao construir b com fatiamento: 


a = np.arange(int(1e8))
b = a[:100].copy()
del a  # a memória de ``a`` pode ser liberada.

    # Se b = a[:100] for usado, a será referenciado por b e persistirá na memória mesmo se del a for executado. 


##### Visão geral de funções e métodos

    # Aqui está uma lista de alguns nomes úteis de funções e métodos NumPy ordenados em categorias. Consulte Rotinas para obter a lista completa. 


    # Criação de matriz
        # arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r_, zeros, zeros_like

    # Conversões
        # ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat

    # Manipulações
        # array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack

    # Perguntas
        # all, any, nonzero, where

    # Ordenação
        # argmax, argmin, argsort, max, min, ptp, searchsorted, sort

    # Operações
        # choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum

    # Estatísticas básicas
        # cov, mean, std, var

    # Álgebra Linear Básica
        # cross, dot, outer, linalg.svd, vdot

