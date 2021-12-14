FATEC SÃO JOSÉ DOS CAMPOS

Otimização de Sistemas de Banco de Dados

Laboratório 04

Reproduzir em laboratório a teoria apresentada em sala de aula quanto ao parse de comandos e custo gerado no servidor.

O laboratório consiste na implementação de um código-fonte acessando o banco de dados via um driver capaz de processar 
"prepared statements". Ex: Java e JDBC. O aluno deve elaborar duas versões do mesmo código alternando o modo de acesso
aos dados conforme explicado em aula (hardcoded e softcoded).

O processamento consiste em executar 100.000 vezes ou mais um mesmo select numa tabela criada pelo aluno.

Para cada modo de acesso o aluno deve computar o tempo gasto para processar o total dos comandos.

Ao final deve-se montar um gráfico comparativo entre as duas versões implementadas e demonstrar a diferença entre elas.
