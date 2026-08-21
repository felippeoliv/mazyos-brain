---
titulo: "ACESSO AO MAZYOS + INSTALAÇÃO"
curso: MazyOS
modulo: LETS GO! Tudo na prática
camada: ouro
fonte_prata: prata/1-lets-go/ACESSO AO MAZYOS + INSTALAÇÃO.md
tags: [mazyos, instalacao, cloud-code, vs-code, onboarding, referencia-tecnica]
---

# ACESSO AO MAZYOS + INSTALAÇÃO

> [!info] Camada ouro: destilação da aula 3 do módulo "LETS GO! Tudo na prática". Esta é, na prática, a aula de referência técnica do curso: o passo a passo completo de instalação do MazyOS, do zero até um projeto de cliente com contexto carregado. Vale a pena revisitar sempre que for iniciar um projeto novo.

## Tese central

Instalar o MazyOS não é "clonar um repositório e pronto" — é criar, para cada cliente (ou projeto pessoal), uma pasta com IA já configurada e um framework de memória que a IA lê antes de cada resposta. O valor da aula não está só nos comandos, mas na demonstração de que Vagner usa o MazyOS **antes mesmo de fechar o cliente**: ele monta site, contexto de negócio e ativos de venda com informações públicas (site do cliente, WhatsApp) para chegar pronto a uma call de vendas, e só depois enriquece o projeto com o que aprender na conversa. Instalação e prospecção acontecem juntas.

> "Tudo isso daqui é contexto de como instalar o MasOS, tá? O MasOS não é só, ah, instalei o repositório aqui, agora foda-se." — [11:37]

## Framework: passo a passo completo de instalação

### Pré-requisito (coberto na aula anterior "PREPARANDO O TERRENO PARA O MAZYOS")
VS Code já instalado e conectado (GitHub ou Google). Esta aula assume esse ambiente pronto e foca no setup do Claude Code + MazyOS em si.

### Passo 1 — Criar a pasta do cliente/projeto [00:00–00:40]
- Botão direito na área de trabalho (ou onde preferir) → Novo → Pasta.
- Nomear com o nome do cliente. No exemplo: `StarCard`.
- Regra prática: uma pasta = um projeto/cliente (ver seção "estrutura de repositórios" abaixo para a exceção).

### Passo 2 — Abrir a pasta na IDE [00:40–01:55]
- Botão direito sobre o ícone do Visual Studio Code → New Window (ou pesquisar "Visual Studio" no menu).
- Dentro do VS Code: ícone de "folhinhas" na esquerda → Open Folder → selecionar a pasta criada (`StarCard`).
- Vagner reforça que a IDE é opcional em termos de marca: "se você preferir o Antigravity, se você preferir Cursor, se você preferir qualquer uma. Use a sua" [00:40]. Ele usa VS Code por preferência pessoal, não por exigência técnica do MazyOS. Existe também caminho via Terminal, mas fica para aulas futuras.
- Ao abrir a pasta vazia pela primeira vez com VS Code, a IDE cria automaticamente uma subpasta `.vscode`.

### Passo 3 — Instalar extensões no VS Code [01:55–03:11]
Ir em Extensões (barra lateral esquerda) e instalar, nesta ordem de prioridade:
1. **Claude Code for VS Code** (obrigatória) — pesquisar "Cloud" (pronúncia de "Claude"), confirmar que é da Anthropic, clicar Instalar. Depois de instalada, aparece um botão "Claude Code Open" no canto superior direito do editor.
2. **Dracula** (opcional) — tema de cores, só estético.
3. **Material Icon Theme** (recomendada) — deixa os ícones de pasta organizados visualmente, útil quando o projeto cresce em subpastas.

Depois de instaladas as extensões, clicar em "Claude Code Open" abre o chat do Claude Code embutido na IDE — funcionalmente idêntico ao Claude Code instalado via terminal no PC.

### Passo 4 — Autenticação e escolha de plano [03:11–04:27]
- Na primeira abertura, o Claude Code pede para conectar a conta Anthropic.
- **Plano mínimo necessário: US$ 100/mês** (o plano gratuito não funciona com Claude Code).
- Vagner usa o plano de **US$ 500/mês** por rodar 5–6 projetos simultâneos sem estourar limite de tokens, mas recomenda começar pelo de US$ 100 e migrar depois se sentir o limite:

> "Começa com o de R$100,00, vai testando e tal, depois você vai pro de R$500,00 se precisar." — [03:11]

- Há aulas futuras no curso dedicadas a economizar token via skills.

### Passo 5 — Instalar o MazyOS via prompt [04:27–05:43]
- Link do repositório GitHub fica na descrição da aula (`mazzeoia/MazyOS`).
- Caminho recomendado ("mais rápido"): copiar o prompt de instalação da página do GitHub, colar direto no chat do Claude Code (dentro da pasta já aberta) e dar Enter.
- O agente então: clona o repositório do MazyOS, lê o skill de instalação e executa as instruções automaticamente.
- Se o agente não rodar sozinho: "você pede para ele. Você fala, ó, lê aí, meu amigo. E instala, né. Lê as instruções aí e dá play." [04:27] — ou seja, instruir explicitamente a ler o `SKILL`/instruções e executar.

### Passo 6 — Entrevista de onboarding (perfil do negócio) [05:43–08:15]
Após clonar, o MazyOS conduz uma "entrevista" para montar o perfil do cliente/projeto:
1. **Pergunta de perfil**: tipo de entidade (empresa, projeto pessoal, canal, etc.) — no exemplo Vagner responde "é uma empresa" (opção 4 do menu).
2. O MazyOS não serve só para empresas: Vagner cita usar o próprio MazyOS instalado no seu canal do YouTube (ajuda com tags, thumbs, ideias de vídeo) e menciona outros usos possíveis — finanças pessoais, criação de site, anotações de estudo. "Não fique preso a só essa maneira de usar." [06:59]
3. **Idioma**: se a IDE estiver em inglês e o usuário quiser gravar áudio em português, instalar a extensão "Portuguese (Brazil)" language pack pela aba Extensões — senão o microfone dita em inglês e a transcrição sai incorreta ("ele escreve achando que eu estou falando em inglês. Daí fica uma merda" [06:59]).
4. **Técnica de resposta recomendada**: em vez de responder pergunta por pergunta da entrevista, ativar o microfone (ditado de voz) e "soltar" o máximo de contexto de uma vez — o agente absorve e pula perguntas já respondidas.

### Passo 7 — Dar contexto bruto sobre o cliente [08:15–09:33]
Exemplo real de prompt ditado por voz (cliente StarCard, ainda não fechado):

> "Meu nome é Wagner. Eu trabalho com IA e marketing digital. Tenho uma agência de marketing. E a StarCard é uma cliente que eu vou fazer uma call segunda-feira. Ela ainda não fechou. Mas ela me disse que tem uma papelaria B2B. Tem muitos clientes grandes, como a Fiat. E ela disse que uma das maiores dores dela é o site. E ela quer que nesse site tenha uma aba para os clientes que fizeram um pedido conseguir rastrear o seu pedido no Correios. Outra coisa que quero criar para ela, para mostrar na call, é um gerador de carrosséis automático." — [08:15]

Regra: "Quanto mais informação você ir mandando para ele, mais ele vai entendendo." [08:15]

### Passo 8 — Estratégia para calls presenciais/gravadas [09:33–10:48]
Para clientes com reunião presencial, Vagner recomenda gravar a conversa inteira (ex.: gravador do iPhone por 2h) e depois jogar a transcrição completa na pasta do projeto, pulando quase toda a entrevista manual do MazyOS — dar só uma visão inicial curta e deixar a transcrição preencher o resto.

### Passo 9 — MazyOS confirma e sintetiza o contexto [09:33–10:48]
O agente devolve um resumo estruturado (papel do usuário, cliente foco, dor principal, entregáveis) e pergunta a próxima etapa. Nesse ponto o MazyOS já tinha identificado corretamente:
- Você: Wagner, agência de marketing focada em IA/marketing digital.
- Cliente foco: StarCard, papelaria B2B, clientes como Fiat, prospect com call agendada.
- Dor principal: site sem rastreio de pedido, sem ferramenta de marketing.
- Entregáveis para a call de segunda: novo site + gerador de carrosséis.

### Passo 10 — Enriquecer com material público do cliente [12:05–13:21]
Antes mesmo de ter feito a call, Vagner passa mais contexto copiando manualmente o conteúdo do site atual da cliente:
- Print do site atual → mandar para o chat, só para o agente ver o layout.
- Ctrl+C no texto de cada página do site (Home, Sobre, Contato) e colar no chat, rotulado por seção (`Home:`, `Sobre:`, `Contato:`).
- Resultado: o MazyOS entende do que se trata a empresa, tempo de mercado, produtos, foco e localização sem depender só da fala do usuário.

### Passo 11 — Decisão empresa vs. agência [12:05]
O MazyOS pergunta se deve trocar o perfil para "agência" e manter a "empresa" como cliente dentro dela. Resposta de Vagner: manter como empresa/conta separada, pensando em vender múltiplas implementações futuras para o mesmo cliente.

### Passo 12 — Revisar os arquivos de memória gerados [13:21–15:54]
Depois da entrevista, o MazyOS grava um arquivo de perfil da empresa dentro de uma pasta `memória`/`empresa`. Para ler formatado dentro do VS Code: clicar no arquivo e apertar **Ctrl+Shift+V** (preview do Markdown).

> "Memória central do negócio. O Cloud lê esse arquivo antes de cada resposta." — [13:21]

Esse arquivo, gerado automaticamente a partir do texto colado do site, já continha: nome da empresa (StarCard Brasil), segmento (fornecedor B2B de papelaria, material de escritório, suprimentos de informática, fabricante próprio de mochilas e brindes personalizados), e-mail profissional, WhatsApp, telefone fixo, localização e redes sociais — tudo extraído do conteúdo colado, sem Vagner ter digitado esses dados manualmente.

> "É por isso que o MaisOS é tão importante. Você criar esse framework aqui. Por isso que é importante você criar do zero, entendeu? Você munir de informação." — [15:54]

Campos que ficam para depois da call (preenchidos com a transcrição da reunião): nome do contato (Cristiane), outros clientes recorrentes, metas, escopo fechado (ex.: Google Meu Negócio).

### Passo 13 — Organizar a estrutura final de pastas [17:15]
O MazyOS, ao ser instalado dentro de uma pasta já nomeada (`StarCard`), cria uma subestrutura própria que pode duplicar o nome. Duas opções apresentadas pelo próprio agente:
- Deixar como está (funciona, só ignorar o nome duplicado).
- "Achatar" a estrutura — opção preferida por Vagner: uma pasta só chamada `StarCard` com tudo do MazyOS dentro, sem aninhamento redundante. Basta pedir em linguagem natural: "Pode achatar. Quero uma pasta só chamada StarCard com tudo do MasiOS dentro." [17:15]

### Passo 14 — Próximo passo indicado pelo próprio MazyOS
Ao final do setup, o agente já aponta o próximo movimento: mock-up do site novo e demo dos carrosséis (conteúdo das aulas seguintes do módulo: "CRIANDO SITE COM MAZYOS" e "CRIANDO CARROSSEL COM MAZYOS + PDF DE PROPOSTA").

## Estrutura de repositórios: um projeto por pasta vs. um repositório-guarda-chuva

Vagner apresenta as duas abordagens e sua preferência, mas deixa claro que ambas funcionam:
- **Um repositório por cliente/projeto** (preferência dele): "fica até menos coisa pesada e você gasta menos token" [18:34].
- **Um repositório único da agência** com vários clientes dentro: ele próprio mantém um assim, com vários clientes, o canal do YouTube e "várias paradas" [17:15]. Funciona, mas fica mais pesado.

> "Você não precisa criar um repositório pra cada projeto, dependendo. Às vezes, você pode criar um só da sua agência e lá dentro ter vários." — [17:15]

## Exemplo concreto usado na aula (case StarCard)

Cliente fictício/real usado como fio condutor: **StarCard**, papelaria B2B (material de escritório), atende clientes grandes como Fiat. Contexto de negócio da aula:
- Proposta de venda: site + gerador de carrossel + Google Meu Negócio, **sem** Google Ads, por **R$ 10.000**.
- Dor identificada pela própria cliente: falta de aba de rastreio de pedidos dos Correios no site.
- Cliente explicitamente não queria rede social/Instagram — mas Vagner decide entregar carrosséis "de brinde" mesmo assim, por julgar que agrega valor visual, e planeja refazer a logo dela também.
- Call de vendas ainda não realizada no momento da gravação (agendada para a segunda-feira seguinte) — o MazyOS foi montado **antes** do fechamento, para chegar à call com "site bonitinho" pronto, replicando a tática usada com outro cliente ("Tuba", fechado em R$ 13 mil, onde Vagner chegou à call com quatro sites já prontos).

> "Eu já vou chegar na Cal com um site bonitinho, com essa dor que ela me falou (...) você tem que já chegar na Cal com o máximo possível pro cliente ficar maluco." — [10:48]

## Filosofia de precificação e relacionamento com cliente (contexto, não tutorial técnico)

Embutido no meio da instalação, Vagner explica sua régua de decisão comercial por tipo de cliente, relevante para quem estiver montando o MazyOS pensando em modelo de cobrança:
- Alguns clientes: só cobra pela implementação e entrega pronto (site, carrossel).
- Outros: precisam gerar material continuamente — nesse caso ele entrega o Claude configurado para o cliente operar sozinho.
- Outros ainda: ele mesmo precisa operar continuamente, e aí avalia cobrar mensalidade ou percentual das vendas/da empresa.

> "Não tem uma receita de bolo. Você vai ter que ter o feeling ali." — [13:21]

Ele reconhece que hoje evita recorrência por já ter outras fontes de renda e preferir escolher clientes, mas orienta quem está começando a "pegar tudo" e ajustar depois. Esse tema é aprofundado nas aulas "COMO EU COBRO MEUS CLIENTES - FAZENDO 1 VENDA AO VIVO" e "CLIENTES INFINITOS PARTE 1" do mesmo módulo.

## Princípio de uso da IA (reforçado nesta aula)

Vagner insiste que instalação técnica sem entendimento de comunicação é inútil:

> "Entenda que a IA, ela é inteligente. (...) Qualquer dúvida que você tem, tira um print, pergunta pra ela (...) Se você não sabe o caminho seguir, não fala qual que é a baboseira, pergunta pra ela." — [12:05]

Isso é apresentado como parte do "framework mental" de uso do MazyOS: tratar a IA como interlocutora capaz de opinar sobre decisões, não só executar comandos.

## Citações relevantes (comandos, arquivos, URLs exatos)

- Comando de instalação: prompt copiado da página do GitHub do repositório `mazzeoia/MazyOS` (link na descrição da aula), colado direto no chat do Claude Code dentro da pasta do projeto, com Enter.
- Extensão obrigatória: **Claude Code for VS Code** (editora: Anthropic).
- Extensões recomendadas: **Material Icon Theme**; opcional: **Dracula** (tema); para ditado em português: **Portuguese (Brazil)** language pack.
- Atalho de preview Markdown no VS Code: **Ctrl+Shift+V**.
- Arquivo de memória gerado: perfil da empresa dentro da pasta `memória` do projeto instalado — "O Cloud lê esse arquivo antes de cada resposta" [13:21].
- Planos Anthropic citados: US$ 100/mês (mínimo viável), US$ 500/mês (usado por Vagner para rodar múltiplos projetos).

## Conexões com outras aulas

- **"PREPARANDO O TERRENO PARA O MAZYOS"** (aula anterior do mesmo módulo): cobre a instalação do VS Code em si e a conexão inicial com GitHub/Google — pré-requisito direto desta aula.
- **"CRIANDO SITE COM MAZYOS"**: dá sequência ao que fica anunciado no final desta aula (mock-up do site novo para StarCard).
- **"CRIANDO CARROSSEL COM MAZYOS + PDF DE PROPOSTA"**: dá sequência ao gerador de carrosséis mencionado como entregável combinado.
- **"COMO USAR O MAZYOS NO DIA A DIA / SKILLS"**: aprofunda o uso de skills para economizar token, tema levantado en passant nesta aula em relação ao plano de US$ 500.
- **"COMO EU COBRO MEUS CLIENTES - FAZENDO 1 VENDA AO VIVO"** e **"CLIENTES INFINITOS PARTE 1"**: aprofundam a filosofia de precificação e prospecção que aparece condensada nesta aula (chegar com entregável pronto antes de fechar o cliente).
- **"Coisinhas importantes que você precisa saber"**: provável complemento de ressalvas operacionais sobre o MazyOS, a validar ao destilar essa aula.
