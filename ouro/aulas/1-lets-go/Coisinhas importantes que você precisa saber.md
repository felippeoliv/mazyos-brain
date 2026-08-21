---
titulo: "Coisinhas importantes que você precisa saber"
curso: MazyOS
modulo: LETS GO! Tudo na prática
camada: ouro
fonte_prata: prata/1-lets-go/Coisinhas importantes que você precisa saber.md
tags: [mazyos, claude-code, gestao-de-tokens, workflow]
---

# Coisinhas importantes que você precisa saber

## Tese central

Antes de partir para a prática (sites, carrosséis, propostas), Vagner faz uma aula de "manual de operação" do Claude Code enquanto interface do MazyOS: como a interface funciona, o que são os modos de edição, o que são os modelos (Opus/Sonnet/Haiku) e, principalmente, como gerenciar o consumo de tokens trocando de chat com frequência. A ideia central que perpassa toda a aula é que dominar esses detalhes operacionais (modos, modelos, `/clear`, `/atualizar`) é o que separa um uso "certeiro" do MazyOS de um uso caro e desorganizado. Ele deixa claro que isso é "o básico" e que uma aula futura vai aprofundar economia de tokens.

## Pontos-chave e avisos práticos

- **Anexar arquivos/imagens**: dá para usar o botão "+" para enviar foto/arquivo, mas Vagner prefere `Ctrl+V` para colar prints direto, ou arrastar o arquivo para uma das abas.
- **Menu de opções (botão embaixo)**: permite limpar a conversa, trocar o modelo, mudar o "esforço" do modelo, ativar o modo Thinking (cadeia de pensamento) e ver o gasto em "Account Usage".
- **Skills do MazyOS aparecem como comandos de barra**: ex. `/carrossel`. Aviso importante: "Se o seu MazyOS não tiver aparecendo essas skills, carrossel, não sei o que, é porque você instalou errado" — hoje existe uma aula específica do módulo para checar instalação incorreta.
- **`/init`**: usado para trocar/gerar o `CLAUDE.md` (ele cita "cloud.md", referindo-se ao arquivo de instruções do projeto).
- **`/context`**: mostra quanto de token está sendo gasto no chat atual ("um pouquinho mais avançado").
- **`/compact`**: compacta o chat quando a conversa já está longa.
- **`/clear`**: limpa todo o chat para parar de gastar token acumulado na mesma conversa.
- **Os quatro modos de operação do Claude Code**:
  - *Ask Before Edits*: pergunta antes de cada edição.
  - *Edit Automatically*: edita sozinho sem perguntar.
  - *Plan Mode*: "muito importante" — antes de começar um projeto, o Claude cria um plano; você aprova, pede ajustes ou só depois manda executar ("agora pode meter marcha, meu amigo").
  - *Auto Mode*: não pergunta nada, "ele vai fuzilando". Vagner avisa que vai usar esse modo nas próximas aulas do curso, o que pode deixar a experiência do aluno "um pouco diferente" da tela dele. Para tarefas complexas/delicadas ele prefere ficar em Ask Before Edits ou Edit Automatically; para tarefas mais simples/repetitivas, deixa em Auto Mode.
  - Para ativar o Auto Mode: basta perguntar ao próprio Claude ("Como eu ativo o Auto Mode no meu Cloud?") ou pesquisar no Google.
- **Terminal / PowerShell**: `Ctrl+"` (aspas) abre o terminal. No Windows é o PowerShell; Mac e Linux têm terminais com outros nomes. Quando o Claude pergunta "posso mandar esse comando no PowerShell?" ou "posso prosseguir com o PowerShell?", a orientação é clicar em Yes e deixar o Claude "tocar o barco".
- **Escolha de modelo (Opus/Sonnet/Haiku)**:
  - Opus é o padrão (default), o mais inteligente, mas o que mais gasta token.
  - Sonnet é descrito na própria interface como "best for everyday tasks" — mais executável, para "fuzilar" tarefas do dia a dia.
  - Haiku serve para coisas mais simples.
  - Recomendação prática de Vagner: "se você está aprendendo, deixa no Opus ali"; se estiver gastando token demais (ex. no plano Pro), use Opus para elaborar o trabalho e depois troque para Sonnet para executar e economizar. Uma prática comum que ele cita (sem necessariamente adotar sempre): usar Opus para planejar e Sonnet para executar.
  - Troca de modelo: botão "+" > *Switch Model*. Sobre o "esforço" do modelo, recomenda deixar em *High* ("já está ótimo").
- **Gestão de tokens entre tarefas (ponto mais enfático da aula)**:
  - Quando o chat já está longo, rodar `/atualizar` (comando específico do MazyOS) antes de `/clear`. O `/atualizar` joga para o MazyOS tudo que for importante da conversa; só depois disso deve rodar `/clear`.
  - Motivo: "quanto mais mensagem você tem ali no chat, mais tokens vai gastar", porque cada novo prompt reprocessa todo o histórico da conversa.
  - Fluxo recomendado: terminar uma tarefa (ex. criar um site) → `/atualizar` → confirmar → `/clear` → abrir tarefa seguinte (ex. blog) em aba/chat novo, repetindo o ciclo.
  - Regra geral: cada tarefa nova (site, blog, carrossel) deveria começar em um chat novo, não continuar acumulando no mesmo chat.
  - Vagner classifica isso como "o básico" e promete uma aula futura dedicada exclusivamente a economia de token.

## Citações relevantes com contexto

> "Se o seu MazyOS não tiver aparecendo essas skills, carrossel, não sei o que, é porque você instalou errado." **[01:20]**
Contexto: ao mostrar o comando `/carrossel`, ele antecipa um problema comum de instalação e direciona para a aula de correção.

> "No Auto Mode, ele nem pergunta. Ele vai fuzilando. Então, dependendo do que eu estou criando, eu deixo no Auto Mode para ele ir criando tudo. Se for uma coisa um pouco mais complexa, mais delicada, eu deixo em um desses dois." **[03:17]**
Contexto: explicação dos quatro modos de edição, com critério prático de quando usar cada um (complexidade/delicadeza da tarefa).

> "Deixa o Claudinho tocar o barco." **[04:13]**
Contexto: orientação sobre confiar no Claude ao aprovar comandos de PowerShell/terminal.

> "Se você está aprendendo, deixa no Opus ali, estou orando mesmo. Se estiver gastando muito token, você vai para o Sone." **[05:32]**
Contexto: critério de escolha de modelo baseado no estágio de aprendizado do aluno e no orçamento de tokens (plano Pro).

> "Quanto mais mensagem você tem ali no chat, mais tokens vai gastar. Então, lembre-se de sempre que terminar uma tarefa (...) abra um chat novo." **[06:47]**
Contexto: a regra prática central da aula sobre organização de chats para controlar custo.

> "Comece a desenvolver, terminou de criar o site, dá um barra atualizar, e depois confirma, e barra clear, limpa o chat." **[07:50]**
Contexto: sequência exata do fluxo recomendado (`/atualizar` → confirmar → `/clear`) entre tarefas.

## Conexões com outras aulas

- **PREPARANDO O TERRENO PARA O MAZYOS** e **ACESSO AO MAZYOS + INSTALAÇÃO**: pré-requisitos técnicos antes desta aula; a aula de instalação é referenciada diretamente quando Vagner comenta sobre skills não aparecendo por instalação incorreta.
- **COMO USAR O MAZYOS NO DIA A DIA — SKILLS**: aprofunda os comandos de barra (`/carrossel` e outros) só mencionados de passagem aqui.
- **CRIANDO SITE COM MAZYOS** e **CRIANDO CARROSSEL COM MAZYOS + PDF DE PROPOSTA**: são exemplos práticos das "tarefas" (site, carrossel) que Vagner usa como referência ao explicar o fluxo `/atualizar` + `/clear` + chat novo por tarefa.
- **Aula futura de economia de token** (mencionada mas não nomeada nesta transcrição): promete aprofundar o que aqui é tratado como "o básico" de gestão de tokens.
- **CLIENTES INFINITOS PARTE 1** e **COMO EU COBRO MEUS CLIENTES**: fazem parte do mesmo módulo "Lets Go", mas tratam de prospecção/venda, não têm conexão temática direta com esta aula operacional.
