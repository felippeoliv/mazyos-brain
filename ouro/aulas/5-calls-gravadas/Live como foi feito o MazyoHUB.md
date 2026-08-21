---
titulo: "Live como foi feito o MazyoHUB!"
curso: MazyOS
modulo: "Calls gravadas (ouro escondido)"
camada: ouro
fonte_prata: prata/5-calls-gravadas/Live como foi feito o MazyoHUB!.md
---

# Live como foi feito o MazyoHUB!

## Tese central

Eric (19 anos, web designer desde 2003, aluno que virou parceiro de Wagner/"Mazel") conta como transformou um entregável manual e trabalhoso (acesso remoto ao PC do cliente via AnyDesk para instalar Cloud Code, site e posts) em um produto white label: o MazyoHub. A tese central da call é dupla. Primeiro, uma tese de produto: "juntar todo o entregável do MazyOS em um lugar só" — site, geração de conteúdo para Instagram, Cloud Code e um SaaS financeiro próprio — elimina a fricção do cliente (ele não baixa nada, não cria conta na Anthropic, não abre múltiplos apps) e justifica um ticket mais alto. Segundo, uma tese de método: tudo foi construído sem saber programar, só "conversando" com o Cloud Code em modo plano e modo automático, pedindo para ele ensinar, revisar segurança e até recomendar a própria arquitetura. Como ele resume perto do fim: "Não usei nenhuma outra IA, não usei GPT, não usei nenhuma outra coisa. Foi só o MazeOS, Cloud Code, como construí o Hub inteiro, do zero." **[01:55:06]**

## O que é o MazyoHub e como foi construído

### Origem: do Swift Hub ao convite de Wagner

Eric viu Wagner vendendo o MazeOS por 5, 6, 8, 10 mil reais e percebeu que o entregável padrão exigia AnyDesk, instalação manual do Cloud e do VS Code no PC do cliente: "Mano, trampo, trampo do caralho, assim." **[00:00]** Para se diferenciar, construiu um protótipo chamado **Swift Hub** ("100% criado com IA, sem nenhum direcionamento... tipo MVP do MVP") que já reunia site, métricas, Instagram e gerador de posts. Ao mostrar isso a Wagner, a resposta foi direta: "cara, não dá. Vem trabalhar comigo... A gente fica milionário." **[01:59]** Eric topou na hora, cobrando só o custo do Cloud, e em cerca de duas semanas com Cloud Max entregou a primeira versão funcional do MazyoHub.

### Arquitetura de acessos: Owner, Workspaces e Hubs

A plataforma tem um painel de **Owner** que controla todos os clientes, workspaces, tipos de Hub (MazyoHub, **Odonto Hub** para clínicas odontológicas, **3D Hub** para clínicas em geral), contas e assentos de Cloud, tokens consumidos por cliente, suporte e segurança. **[03:15]** Cada cliente cadastrado vira automaticamente um **workspace** — o Hub personalizado daquele cliente, com: Cloud Code integrado (IDE tipo VS Code no navegador), site exibido via iframe/link (o site em si roda na pasta do cliente no MazeOS, o Hub só exibe), perfil e métricas de Instagram via API da Meta, gerador de conteúdo com templates do Canva, módulo financeiro (SaaS próprio "Alumes"/Lumis) e, em versões mais completas, CRM.

### Cadastro de cliente: um formulário, não uma reconstrução

Criar um cliente novo não é reconstruir nada — é preencher um formulário: tipo de Hub, logo, nome comercial, apelido, segmento, cor da marca (o Hub herda a cor do cliente, não a do MazyOS — "não deixar algo meio tipo, é o Maisel Hub com as cores do Mazeu. Não, as cores da sua empresa" **[10:02]**), módulos contratados (CRM sim/não, financeiro sim/não, site, Instagram), status de recorrência, score e conta Cloud vinculada. "Cada Hub é um white label. Quando eu preencho esse formulário aqui, ele vai e vai com todas as informações do cliente e só muda o que tem que mudar." **[11:19]**

### Como o Cloud Code chega ao cliente sem ele instalar nada

Esse é o ponto técnico mais perguntado no chat. Existem dois planos da Anthropic usados: **Team** (R$138/mês por assento padrão, R$688 pelo premium, mínimo de 2 assentos) e **Enterprise**. Em vez de a empresa fornecer assentos para funcionários, a MazyoHub usa a lógica invertida: cada cliente vira um "assento" da conta Team. O fluxo é: criar um e-mail em domínio próprio (ex.: contahub.mazeuia.com, porque a conta Team não aceita e-mails pessoais), vincular esse e-mail a um assento, entrar na VPS, criar a conta Cloud lá dentro e rodar `cloud setup-token` — comando que gera um token para vincular a conta a outra aplicação/máquina. Assim "o cliente não precisou baixar o cloud, não precisou baixar a VS Code, não precisou fazer nada." **[22:25]** Quando o cliente já tem uma conta Cloud própria (caso do "Tuba", cliente-exemplo usado na demo), o processo é o mesmo setup-token, só que pegando a conta existente dele e colando-a na VPS.

### Segurança: duas camadas pedidas ao próprio Cloud

Eric não é desenvolvedor. O processo de segurança que descreve: antes de começar qualquer projeto, abre uma janela separada do Cloud, dá o contexto completo da aplicação e pede que ele gere, em blocos, os prompts para um back-end seguro (usa Supabase com RLS). Depois de construída a plataforma, faz uma segunda passada: dá ao Cloud "várias formas de burlar o meu sistema" e pede que ele blinde contra cada uma (injeção SQL etc.). Descreve a analogia: "eu coloquei o lençol na cama... Agora eu vou começar a criar a plataforma... no final, eu vou lá e coloco a colcha por cima... deixo a cama blindada, que é o que? Mais uma camada de segurança." **[01:19:24]** Além disso, tem um amigo desenvolvedor que revisa esporadicamente ("nunca deu nada"). Reforça o risco para quem ignora isso: "um errinho que dá você pode se fuder, você pode perder o SaaS, você pode ter que fechar, levar até o processo." **[12:35]**

### Instagram: API da Meta, passo a passo documentado

Todo o card de Instagram (perfil, posts, curtidas, comentários, métricas) vem de uma única API gratuita da Meta. O processo, documentado num tutorial interno visível só para o Owner dentro de cada workspace (para nunca depender de memória): (1) no Instagram do cliente, mudar para conta profissional e vincular uma página do Facebook (pedindo login e senha da página ao cliente); (2) criar um app em Facebook Developers; (3) gerar um token de usuário no ambiente da Meta; (4) colar esse token na aba de configuração do cliente no Hub. Feito isso, o card de Instagram carrega sozinho.

### Geração de conteúdo: de "engessado" a biblioteca de 300+ templates do Canva

A primeira tentativa foi pedir ao Cloud para gerar posts diretamente (trocar título, mover elemento) — "Eu senti muito engessado... É bem melhor construir do zero do Canva do que pedindo pro Cloud." **[38:32]** A segunda tentativa (print do Canva → HTML → Cloud interpretar) gastou toda a sessão de tokens em 5 minutos e foi descartada: "Era uma papagaiada, mano... Não dava, era inviável." **[38:32]** A solução final, sugerida pelo próprio Cloud numa conversa longa: criar uma pasta no Canva Pro, encher com templates por nicho (advogado, moda, fotógrafo, construção, imobiliária, barbearia — mais de 300 modelos ao todo) e importar o link da pasta inteira dentro do Hub. O Cloud então organiza a listagem, permite ao cliente escolher um template, "implantar como post" (converte o design para PPTX e exporta para dentro do Hub) e editar dentro de um mini-editor tipo Canva construído do zero ("Eric, porra, como é que você fez um Canva, caralho?" — "é só você chegar no seu Cloud e pedir pra ele fazer isso" **[42:28]**), com opção de edição manual ou "modificar com IA" (mantendo ou não rosto, fundo, tipografia). Consequência de negócio: substituiu o trabalho de um social media (~R$1.000/mês) delegando a escolha de tema e edição ao próprio cliente. **[41:03]**

### CRM: fork do Frappé CRM + funil + WhatsApp não-oficial + agentes

O CRM parte de um clone do **Frappé CRM** (open source, do GitHub) pedido diretamente ao Cloud: "preciso que tenha um CRM dentro do hub... vá lá no Git, e clone ele aqui... vamos fazer alterações nele, e vamos deixar ele personalizado." **[01:32:54]** Duas adições próprias sobre o Frappé padrão: (1) um **módulo de funil visual** com cards conectáveis, onde cada etapa pode disparar uma "ação" (ex.: mensagem automática de boas-vindas no WhatsApp quando o lead entra numa etapa) ou ativar um **agente de conversação** (ex.: "Lia" e "Bob", personas com objetivo definido — recepção, qualificação, agendamento, recuperação de lead) que conversa via WhatsApp usando o próprio Cloud Code do cliente como motor; (2) uma **aba de integrações** para captar leads externos (ex.: formulário embutido no header do site do cliente, ou API do MazyoHub para outras plataformas). O funil completo foi construído em cerca de "duas horas, três horas de trabalho." **[01:29:40]**

O WhatsApp em si não usa API oficial: é pedido ao Cloud para abrir uma sessão de WhatsApp Web dentro da aplicação/VPS via QR Code. Risco explícito: disparos em massa levam a restrição/banimento (Eric relata ter sido restringido depois de ~500 números); uso "normal" (não automatizado em massa) não teria motivo para banir.

### Financeiro: SaaS próprio ("Alumes"/Lumis), não open source

O módulo financeiro não foi construído para o Hub — é um SaaS empresarial que Eric já tinha ("Lumis"), com assistente próprio chamado **Alumbot**. Ele reaproveitou esse produto existente dentro do Hub, ilustrando o conselho central de estratégia que dá aos alunos: "você já fez um SaaS, já fez o entregável para um cliente... pega esses SaaS, essas plataformas que você já criou antes, integra no seu entregável." **[01:13:06]** O Alumbot está em processo de migração de um "módulo de IA" externo para rodar sobre o próprio Cloud Code do cliente, como uma persona diferente do mesmo motor.

### Infraestrutura e stack

Tudo roda numa única VPS Hostinger, plano **KVM4** (cerca de R$130–200/mês, 16 TB de banda, 200 GB de armazenamento), usando Docker/Coolify. O Cloud recomendou o plano menor KVM2, mas Eric preferiu superdimensionar para não pensar em capacidade por um tempo. Ferramentas pagas usadas no total: **Hostinger** (VPS), **Canva Pro**, **Cloud Code** e **Supabase**. Backend com RLS no Supabase.

## Exemplos concretos e números

- **Preço do serviço:** instalação em torno de R$4.000 + mensalidade (a partir de ~R$3.000/mês), substituindo a lógica antiga de cobrar um valor único alto (ex.: 16 mil) — "é melhor a gente cobrar mensal... como tem outros SaaS." **[23:43]**
- **Ticket adaptável ao cliente:** cliente do Wagner pagou 16 mil e tem tudo liberado; outro cliente ("de costura") pagou 7–8 mil e não tem CRM, por ser "uma operação à parte... pesa mais na nossa VPS." **[32:11]/[33:28]**
- **Assento Cloud Team:** R$138/mês (padrão) ou R$688/mês (premium); mínimo de 2 assentos para abrir uma conta Team.
- **Prazo de entrega "seguro":** 3 dias corridos para integrar tudo (Alumes incluso), fazendo uma etapa por dia.
- **Timeline pessoal:** comprou o MazeOS em 28 de maio e, com um mês e meio de curso, já tinha construído todo o MazyoHub mostrado na call — "80 conto mais bem gasto da minha vida." **[57:10]**
- **Canva:** biblioteca com 311+ templates organizados por nicho (7–8 posts por nicho, para o cliente não sentir falta de opções nem quebrar a identidade visual do Instagram).
- **Google Maps API (Kaptar, mencionado de passagem):** atualização recente reduziu a cota para 1.000 requisições e 20.000 leads gratuitos por mês.
- **Case de resultado citado (não é do Hub, é ilustração de "agregar valor"):** loja de carros do Bertoli, que estava 50 dias sem vender, recebeu um SaaS gratuito do Wagner e vendeu 8–9 carros em seguida — usado para justificar por que "agregar valor" gera indicação e não só receita direta. **[29:33]**
- **Skill de segurança citada por aluno no chat:** Luiz relata ter pedido ao Cloud para "criar skills de cibersegurança pra instalar proteção e testes" — Eric valida como exemplo de uso "fora da caixa" do Cloud Code. **[17:39]**

## Citações relevantes com contexto

> "Eu vi que o entregável dele, ele tinha que chegar lá no PC do cliente... instalar o cloud. Mano, trampo, trampo do caralho, assim." **[00:00]**

Abre a call explicando a dor original que motivou o produto: o entregável manual via AnyDesk era operacionalmente pesado, e essa dor é o motivo de existir do Hub.

> "Basicamente, cada Hub é um white label. Quando eu preencho esse formulário aqui, ele vai e vai com todas as informações do cliente e só muda o que tem que mudar." **[11:19]**

Define a arquitetura de replicação do produto: não se reconstrói nada por cliente, apenas se preenche um formulário que gera uma instância isolada e personalizada.

> "O cliente não precisou baixar o cloud, não precisou baixar a VS Code, não precisou fazer nada... O entregável é nosso, não é dele." **[22:25]**

Resume a proposta de valor central do Hub frente ao processo antigo: a complexidade técnica fica inteiramente do lado do prestador, escondida atrás de uma URL com login.

> "Eu peço pro Cloud fazer essas duas etapas. E pra mim, isso sempre serviu, sempre deu certo." **[16:03]/[17:03]**

Contexto: pergunta do chat sobre segurança. Eric descreve seu processo de duas camadas (blindagem de back-end + simulação de ataques) pedindo tudo ao próprio Cloud Code, sem ser desenvolvedor — mostra que segurança "amadora, mas sistemática" é viável com IA guiando o processo.

> "Era uma papagaiada, mano... Eu gastei todos os meus tokens da minha sessão em cinco minutos fazendo isso. Não dava, era inviável pro meu cliente fazer isso." **[38:32]**

Contexto: primeira tentativa fracassada de integrar Canva (print → HTML). É um exemplo raro e valioso porque mostra o caminho errado antes do certo — útil para o aluno não repetir o erro.

> "Não é só porque o Wagner entrega e faz o entregável dele que custa 16 mil ou o Diogo faz 50 mil recorrente que você tem que falar não, só passo acima de 10. Não, cara. Você consegue adaptar o seu entregável." **[33:28]**

Contexto: pergunta sobre quanto cobrar. É o núcleo da tese de precificação da aula: adaptar o ticket à fase financeira real do cliente, inclusive fazendo "só um site" por valores baixos quando necessário, em vez de forçar um pacote padrão.

> "Ajudando que a gente consegue fazer mais dinheiro... Não faz sentido eu fazer um site feio... para depois eu chegar ali e cobrar 8 mil reais, cara." **[29:33]/[30:53]**

Contexto: reflexão sobre o case do Bertoli (loja de carros). Articula a lógica de "agregar valor primeiro, cobrar depois" como estratégia de crescimento por indicação, não só transação isolada.

> "Não usei nenhuma outra IA, não usei GPT, não usei nenhuma outra coisa. Foi só o MazeOS, Cloud Code, como construí o Hub inteiro, do zero." **[01:55:06]**

Fecha o argumento demonstrativo da call: toda a plataforma (CRM, funil, WhatsApp, editor tipo Canva, financeiro, segurança) foi construída só com Cloud Code guiando um não-programador.

> "Não se sentir vergonha para falar com o seu próprio Claudio, porque ele é um professor." **[01:59:53]**

Fechamento da aula, resumindo a postura recomendada frente ao Cloud Code: tratá-lo como professor que ensina de volta, não como ferramenta que só executa comandos prontos.

## Conexões com outras aulas

- **Kaptar (módulo "Kaptar: seus clientes no automático")**: mencionado de passagem na call ("Prospecção do captar, gasta com a API do Google Maps?" **[01:45:32]**) — reforça que a cota gratuita da API do Google Maps usada no Kaptar (ver nota "Como funciona a ferramenta Kaptar") teve atualização recente para 1.000 requisições / 20.000 leads grátis por mês, informação que atualiza aquela aula.
- **Aula anterior de Wagner sobre o entregável "antigo"**: a call inteira é construída em contraste direto com o processo manual via AnyDesk descrito por Wagner em aulas anteriores do curso — o MazyoHub é explicitamente a evolução desse entregável.
- **Segurança em SaaS (tema recorrente pedido por alunos no chat)**: um aluno (Luiz) relata ter criado uma "skill de cibersegurança" com o Cloud Code — sinaliza que esse é um padrão que pode render uma aula dedicada; Eric reconhece não ter aprofundado o tema em aula própria até esta call.
- **Promessa de aula futura**: a própria call termina com um pedido explícito do chat por "uma aula passo a passo ensinando como fazer o MazyoHub numa sequência mais lógica" **[01:21:30]**, que Eric admite ser válido, pois esta call foi guiada pelas perguntas do chat e não por uma ordem didática — é um gancho aberto para conteúdo futuro do módulo "Calls gravadas".
- **Uso do modo plano e modo automático do Cloud Code**: citado aqui como rotina diária de Eric ("Meu dia inteiro é modo plano e modo automático" **[31:31]**) — conceito operacional que provavelmente é ensinado em profundidade em aulas introdutórias do MazyOS (módulo "Let's go") e aqui aparece só como prática já assumida.
