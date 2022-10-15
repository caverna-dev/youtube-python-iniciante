# Obtendo todos os arquivos deste repositório
Se voceê já possui familiaridade com o Git, então não precisa ler este documento.
Mete bronca, e clone o repositório para obter todos os arquivos que desenvolvemos ao longo da playlist [Python Iniciante](https://www.youtube.com/watch?v=Y4uNyBKJpPY&list=PLfyimYNc1Xl2PQXQSKQSEtyXa3tYhTLhM) no canal do YouTube do **caverna_dev**.
Mas se este não é o seu caso, siga o passo a passo aqui para saber como fazer isto.

## Verificando se o Git está instalado
É bem provável que seu sitema já tenha Git instalado (principalmente se voceê usa MacOS ou Linux). 
Para verificar se a ferramenta está instalada, abra um prompt de comandos (CLI) e digite `git --version`.
Se você obtiver um output informando qual versão do Git está instalada, significa que você já o possui e pode pular esta sessão. Caso contrário, continue com "Instalando o Git".

## Instalando o Git (se já não estiver)
Existem diversos excelentes tutoriais de como instalar o Git já disponíveis na Internet.
E eu, como um desenvolvedor, prefiro reusar coisas que já existem do que reinventar a roda.
Portanto, deixarei linkado aqui um guia para instalação do Git nos Sistemas Operacionais mais comums (Windows, MacOS & Linux). 
[Basta seguir este passo a passo](https://www.hostinger.com.br/tutoriais/tutorial-do-git-basics-introducao#1o_Passo_-_Instalar_o_GIT_em_Sistemas_Diferentes) que não vai ter erro.


## Clonando este repositório para o seu computador
Se esta é a primeira vez que voceê está aqui para obter o código da playlist [Python Iniciante](https://www.youtube.com/watch?v=Y4uNyBKJpPY&list=PLfyimYNc1Xl2PQXQSKQSEtyXa3tYhTLhM), ou se você por algum motivo deletou o diretório que clonou anteriormente e gostaria de clonar de novo agora, faça o seguinte:
1 - Abra seu programa de terminal e navegue para um diretório no seu sistema onde deseja armazenar a pasta `youtube-python-iniciante` que conterá todos os arquivos `.py` desenvolvidos ao longo da playlist.
2 - Uma vez dentro deste diretório, execute o comando
```bash
git clone https://github.com/caverna-dev/youtube-python-iniciante.git
```
O git iniciará o processo de clonagem (cloning), que basicamente significa que ele fará o download deste repositório.
Quando o processo conluir, você verá uma pasta nomeada `youtube-python-iniciante` e dentro dela estarão todos os arquivos que você vê aqui.


## Mantendo seus arquivos locais atualizados com este repositório
É importante que você eventualmente domine os conceitos do Git para ser capaz de tanto trabalhar localmente e fazer as alterações que desejar, ao mesmo tempo que consegue manter todos os seus arquivos locais sincronizados com este repositoório "pai" aqui.
Para isto, novamente, existem muitas fontes disponiíveis na Internet. E no próprio **caverna_dev** em breve teremos conteúdo a respeito. 
Por ora, eu sugiro que dedique algum tempo estudando [este documento](https://www.hostinger.com.br/tutoriais/tutorial-do-git-basics-introducao#2o_Passo_-_Como_Usar_o_GIT).

Mas, como um guia MUITO simples (e certamente insuficiente) de como você pode trabalhar com o Git localmente editando seus arquivos e ainda assim mantendo sincronia com este repositório, eu sugiro o seguinto *work flow*:

1 - Saiba que o Git trabalha com o conceito de **branches**. Uma branch, falando muito grosseiramente, é como se fosse uma versão "virtual" do seu diretório local, contento todos os arquivos (OBS: isto não é uma definição formal e adequada do que é de fato uma *branch*, mas apenas uma analogia).
Por *default*, existe uma branch chamada **main** que você pode entender como sendo a "versão mestre" do coódigo. Desenvolvedores costumam tratar a **main** como sendo a versão "aprovada" do código de um sistema, isto é: a versão que vai para produção e é consumida pelos usuários (OBS: o nome desta branch "mestre" naão precisa ser *main*, mas tipicamente é. Também é bastante comum ser nomeada como **master**. Na prática, pode receber qualquer nome.)
Para saber em qual branch voceê está a qualquer momento, basta usar o comando:
```bash
git branch


*main
```
Se você acabou de clonar este repositório, verá apenas as branches que existem aqui (que no momento é apenas a **master** mesmo).
Mas a medida que você for criando suas próprias branches, elas aparecerão no output do comando acima.

Antes de fazer qualquer mudança em qualquer arquivo, crie uma **branch** sua e trabalhe fazendo suas alterações e experimentações apenas dentro dela.
```bash
git checkout -B minha_branch
Switched to a new branch 'minha_branch'
```

Agora, se você usar o comando `git branch` novamente:
```bash
  main
* minha_branch
```

Note que o asterisco (*) indica em qual branch você está num dado momento.

2 - Uma vez na branch criada por você, faça as alterações desejadas nos arquivos que quiser.

3 - Após alterar o que gostaria, voceê tem duas possibilidades:
caso queira persistir suas alterações:
```bash
git add --all
git commit -m "Um pequeno texto que descreva quais alteracoes foram realizadas"
```

caso nao tenha interesse em manter as altearações que fez:
```bash
git restore <nome do arquivo_1> <nome_do_arquivo_2> ... <nome_do_arquivoN>
```

Pronto, suas alterações permaneceram salvas na sua branch.

**Neste pequeno e absolutamente incompleto guia, nao veremos como fundir (merge) mudanças realizadas numa branch paralela novamente para **main** (ou vice versa). Mas saiba que isto é perfeitamente possível (na verdade, necessário no dia a dia de times distribuidos e autonomos que trabalham com desenvolvimento de software).**

