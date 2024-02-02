# Data-sus-WebScrapper

## Requerimentos
Antes de executar o programa verifique se tem o python instalado corretamente na sua máquina!
Instale a biblioteca do Selenium através do comando 'pip install selenium'
Instale a biblioteca do pandas através do comando 'pip install pandas'

## Variáveis e seus significados
**i** : é a variável que indica a posição das opções do arquivo, ele inicia em 10 pois devemos começar a pegar as tabelas de JAN/2023 para baixo. Caso o código tenha rodado por um certo tempo e já tenha baixado um numero x de arquivos, antes de rodar novamente, atribua o valor de x(numero de arquivos já baixados) para a variável **i**.


**id_col** : Como vamos pegar somente os subgrupos ela pode permanecer como 7. pois subgrupo é a oitava posição(SIM OITAVA POIS OS INDEXES INICIAM COM 0).


**COMO TROCAR DE QUANTIDADE APROVADA PARA VALOR, ATENÇÃO ISSO É IMPORTANTE!**

É bem simples na realidade. Tem uma parte do código onde tem o seguinte comentário **"SELECIONANDO CONTEÚDO"**, na linha 35, trocar o 0(primeira opção é quantidade aprovada) para o 1(que é o indice da opção de valor total).

# Espero de coração que meu código ajude a baixar os arquivos necessários!!
