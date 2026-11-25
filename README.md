🏦 Banco Oi — Conversor de Moedas

O Banco Oi Conversor de Moedas é uma aplicação de terminal desenvolvida em Python para ajudar os clientes a converterem valores entre Real (BRL), Dólar (USD) e Euro (EUR) de maneira simples, rápida e com a cotação atual do mercado.

A ferramenta reúne a escolha das moedas, a leitura do valor e o cálculo da conversão em um único fluxo guiado por menus.

🔧 Esse projeto foi desenvolvido por:
Guilherme César

🎯 1. Objetivo do Projeto
Desenvolver uma aplicação que permita ao usuário escolher a moeda que possui, escolher a moeda para a qual deseja converter e obter o valor convertido com base na cotação real do dia.
O projeto busca oferecer clareza e praticidade em operações básicas de câmbio.

👥 2. Público-alvo
O projeto é direcionado a:
Clientes do banco que precisam saber quanto vale um valor em outra moeda.
Pessoas que viajam ou compram em moeda estrangeira.
Estudantes que querem entender como funciona a conversão entre moedas.
Usuários que desejam consultar cotações de forma rápida.

❗ 3. Problema que a Solução Pretende Resolver
Muitas pessoas têm dificuldade para saber quanto vale um valor em outra moeda, pois as cotações mudam constantemente. Fazer a conta manualmente, ou usar uma cotação desatualizada, pode gerar erros e decisões ruins.
O Conversor de Moedas resolve isso consultando a cotação atual e fazendo o cálculo automaticamente, em qualquer combinação entre Real, Dólar e Euro.

🖥️ 4. Planejamento e Organização das Interfaces
A aplicação funciona no terminal e é organizada em três telas principais, todas baseadas em menus numerados.

4.1. Tela Inicial
Tela de entrada do sistema.

Opções:
1 — Converter moeda
0 — Sair

4.2. Escolha das Moedas
Exibida duas vezes durante a conversão: primeiro para a moeda de origem ("Qual moeda você TEM?") e depois para a de destino ("Para qual moeda quer CONVERTER?").
Opções:
1 — Real (BRL)
2 — Dólar (USD)
3 — Euro (EUR)
0 — Sair

4.3. Resultado da Conversão
Depois de informar o valor, a tela exibe:

A cotação utilizada (ex.: 1 USD = 5,0000 BRL).
O valor informado e o valor convertido, já formatados no padrão brasileiro (ex.: R$ 1.234,56).
🗺️ 5. Fluxo de Navegação
Etapa	O que acontece
1	O usuário escolhe 1 - Converter moeda na tela inicial.
2	Escolhe a moeda que possui.
3	Escolhe a moeda para a qual quer converter.
4	Digita o valor (aceita vírgula ou ponto como separador decimal).
5	O sistema busca a cotação atual e mostra o resultado.
6	O programa volta para a tela inicial.

⚙️ 6. Como a Conversão Funciona
A cotação é obtida em uma única chamada à API, que informa quanto vale 1 Dólar e 1 Euro em reais. Com isso, qualquer combinação é calculada passando pelo real como moeda base:
resultado = valor × (taxa da moeda de origem) ÷ (taxa da moeda de destino)
Assim, as seis combinações (BRL↔USD, BRL↔EUR e USD↔EUR) usam a mesma lógica.

🛡️ 7. Tratamento de Erros
Opções de menu inválidas são recusadas e o menu é exibido novamente.
Valores não numéricos ou negativos são recusados.
Se a moeda de origem e a de destino forem iguais, o sistema avisa o usuário.
Se não for possível obter a cotação (sem internet ou falha na API), o sistema exibe uma mensagem e volta ao menu, sem encerrar o programa.
🏗️ 8. Estrutura do Projeto
ConversorMoedas/
│
├── conversor_moedas.py
│
└── README.md
Arquivo	Responsabilidade
conversor_moedas.py	Menus, busca da cotação, cálculo e exibição do resultado.
README.md	Documentação do projeto.

Principais funções do código:
Função	Responsabilidade
obter_cotacoes()	Consulta a API e devolve o valor de cada moeda em reais.
escolher_moeda()	Exibe o menu de moedas e valida a opção.
ler_valor()	Lê e valida o valor digitado.
formatar()	Formata o valor no padrão brasileiro.
converter()	Conduz todo o fluxo de uma conversão.
tela_inicial()	Menu principal do sistema.

🧰 9. Tecnologias Utilizadas
Python 3: linguagem do projeto.
urllib e json (biblioteca padrão): requisição e leitura dos dados da API, sem necessidade de instalar dependências.
AwesomeAPI: fonte das cotações em tempo real (economia.awesomeapi.com.br), gratuita e sem chave de acesso.

🚀 10. Funcionalidades Implementadas e Pendentes
Funcionalidades implementadas
[x] Tela inicial com menu.
[x] Escolha da moeda de origem e da moeda de destino.
[x] Conversão entre Real, Dólar e Euro (todas as combinações).
[x] Cotação em tempo real via API.
[x] Leitura de valores com vírgula ou ponto.
[x] Formatação dos valores no padrão brasileiro.
[x] Validação de entradas e tratamento de falhas de conexão.

Funcionalidades pendentes (ideias para próximas versões)

[ ] Histórico das conversões realizadas.
[ ] Inclusão de novas moedas.
[ ] Exibição da data e hora da cotação.
[ ] Opção de fazer várias conversões em sequência sem voltar ao menu inicial.
▶️ 11. Como Executar o Projeto
Tenha o Python 3 instalado.
Acesse a pasta do projeto:
bash
cd ConversorMoedas
Execute o programa:
bash
python conversor_moedas.py

É necessária conexão com a internet para obter a cotação atual.

📌 12. Status do Projeto
✅ Primeira versão funcional.
A conversão entre Real, Dólar e Euro com cotação em tempo real está implementada. As próximas etapas envolvem registrar o histórico e ampliar as moedas disponíveis.

Banco Oi — Converta com segurança, decida com clareza. 🏦
