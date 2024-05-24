# Projeto Ouvidoria
Este projeto é um sistema de Ouvidoria desenvolvido em Python com a utilização de banco de dados MySQL, seguindo a arquitetura MVC (Model-View-Controller). O sistema foi criado como projeto final da disciplina "Programar em linguagem estruturada com Python".

## Funcionalidades do Sistema:
O sistema de Ouvidoria apresenta um menu com as seguintes opções:
* Listagem das Manifestações: 
    Lista todas as manifestações cadastradas.
    Tratamento: Caso não haja manifestações cadastradas, informar ao usuário que não existem manifestações.
* Listagem de Manifestações por tipo:
    Permite ao usuário escolher o tipo de manifestação que deseja listar (reclamação, elogio ou sugestão).
    Exibe as manifestações do tipo escolhido.
* Criar uma nova manifestação:
    Solicita ao usuário todos os campos necessários para a criação de uma nova manifestação.
    Tratamento: Após a inclusão, exibir a mensagem “Nova manifestação criada com sucesso!”.
* Exibir quantidade de manifestações:
    Mostra a quantidade total de manifestações cadastradas.
* Pesquisar uma manifestação por código:
    Solicita o código da manifestação e exibe os detalhes da manifestação correspondente.
* Excluir uma Manifestação pelo Código:
    Solicita o código da manifestação a ser excluída e realiza a exclusão no banco de dados.
* Sair do Sistema:
    Encerra a execução do sistema.

## Arquitetura MVC
O sistema foi desenvolvido utilizando a arquitetura MVC, que separa o código em três componentes principais:
* Model: Responsável pela lógica de acesso aos dados e comunicação com o banco de dados MySQL.
* View: Responsável pela apresentação dos dados e interação com o usuário.
* Controller: Gerencia a comunicação entre Model e View, processando as entradas do usuário e atualizando a visualização.

# Estrutura do Projeto
* models/ - Contém as funções agrupadas em módulos relacionadas ao acesso e manipulação dos dados.
* views/ - Contém as funções responsáveis pela interface com o usuário.
* controllers/ - Contém as funções que gerenciam a lógica do aplicativo e a interação entre Model e View.
* query_db/ - Contém as instruções SQL para criar o banco de dados.
* main.py - Arquivo principal para execução do sistema.

# Instruções de Instalação
* Clone o repositório.
* Instale as dependências MySql.
* Configure o banco de dados MySQL usando a query disponibilizada no arquivo DBConnection.
* Inicialize o banco de dados.
* Execute o aplicativo.

## Tratamentos Necessários
* Feedback ao usuário: Todas as operações realizadas pelo sistema fornecem um feedback ao usuário, por exemplo, confirma a criação de uma nova manifestação ou informa sobre a exclusão de uma manifestação.
* Mensagens informativas: Informa ao usuário quando não houver manifestações cadastradas durante as listagens.

## Conclusão
* Este sistema de Ouvidoria oferece funcionalidades básicas para gerenciar manifestações, permitindo criar, listar, pesquisar e excluir manifestações. A implementação em Python com MySQL garante um gerenciamento eficiente dos dados, enquanto a arquitetura MVC proporciona uma organização clara e modular do código.