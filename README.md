# Projeto 2 - Data Engineering
O objetivo do projeto de Data Engineering é coletar e organizar dados.

## Programas utilizados: 
- Visual Studio Code
- Python(Pandas, BeautifulSoup, Selenium)
- Jupyter Notebook 

## Dados utilizados: 
Os dados para serem coletados e armazenados, estão disponíveis neste site.
http://books.toscrape.com/

## Contexto do projeto: 
A Book Club é uma Startup de troca de livros. O modelo de negócio funciona com base na troca de livros pelos usuários, cada livro cadastrado pelo usuário, dá o direito à uma troca, porém o usuário também pode comprar o livro, caso ele não queira oferecer outro livro em troca.

Umas das ferramentas mais importantes para que esse modelo de negócio rentabilize, é a recomendação. Uma excelente recomendação aumenta o volume de trocas e vendas no site.

Você é um Data Scientist contrato pela empresa para construir um Sistema de Recomendação que impulsione o volume de trocas e vendas entre os usuários. Porém, a Book Club não coleta e nem armazena os livros enviados pelos usuários.

Os livros para troca, são enviados pelos próprios usuários através de um botão “Fazer Upload”, eles ficam visíveis no site, junto com suas estrelas, que representam o quanto os usuários gostaram ou não do livro, porém a Startup não coleta e nem armazena esses dados em um banco de dados.

Logo, antes de construir um sistema de recomendação, você precisa coletar e armazenar os dados do site. Portanto seu primeiro trabalho como um Data Scientist será coletar e armazenar os seguintes dados:

- O nome do livro.
- O preço do livro.
- O número de estrelas que o livro recebeu.
- Se o livro está em Estoque ou não.

## Roteiro: 
- Encontrar no código do site, HTML, onde fica localizado o nome, preço, nivel de estrelas e disponibilidade  
- Construir o coóigo de forma ordenada e o mais refinado possivel 
- Conseguir organizar de forma correta as linhas da tabela
- Salvar o arquivo em formato CSV


## Graficos 
| Imagem da tabela, utilizando o Pandas |
|-|
|<img src="https://github.com/mathnr7/Projeto-2-Data-Engineering/blob/main/Imagem%20da%20tabela%20pelo%20Pandas.PNG" width="500" height="500" />|

License
----

MIT
