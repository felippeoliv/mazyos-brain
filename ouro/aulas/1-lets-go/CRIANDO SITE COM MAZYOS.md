---
titulo: "Criando Site com MazyOS"
curso: MazyOS
modulo: LETS GO! Tudo na prática
modulo_slug: 1-lets-go
camada: ouro
fonte_prata: prata/1-lets-go/CRIANDO SITE COM MAZYOS.md
cliente_exemplo: StarCard (papelaria e material de escritório, B2B)
tags: [mazyos, site, claude-code, skill-abrir, netlify, geracao-de-imagem, ouro]
---

# Criando Site com MazyOS

> [!info] Camada ouro: destilação da aula 4 do módulo "LETS GO! Tudo na prática". Transcrição integral em `prata/1-lets-go/CRIANDO SITE COM MAZYOS.md`.

## Tese central

Um site B2B vendável (o Vagner fala em cobrar **10 mil reais**) nasce de **um único prompt inicial** ("Vamos começar a criar o site da StarCard") porque toda a inteligência de contexto já está armazenada no MazyOS (skill `/abrir`), não no prompt. A partir daí o trabalho não é "programar", é **direção de arte e negócio em loop curto**: o instrutor olha o resultado, corta o que soa "cara de site de IA" (ícones genéricos, seção de clientes sem dado real, headline floreada demais) e mantém o site funcional e simples, porque o cliente é B2B e "não precisa florear muito". A aula defende explicitamente que **falta de material do cliente não é motivo de trava**: você gera imagens (ChatGPT/GPT Imagem), testa, descarta, itera, e chega a algo apresentável em cerca de 1 a 2 horas (ele estima 1h/1h15 sem estar gravando).

Segunda tese implícita: o Claude Code dentro do MazyOS funciona como **parceiro criativo de brainstorm**, não só executor. Vagner descreve literalmente conversar com ele quando está "sem criatividade" ou "meio perdido" ("o que você acha de eu fazer isso? o que você acha de eu fazer aquilo?").

## Framework / passo a passo

### 1. Setup do ambiente
- Abre o VS Code (Open Folder → pasta do projeto/cliente, ex. "StarCard").
- Abre o Claude Code dentro do VS Code.
- Organiza a tela: Claude Code de um lado, preview do site do outro lado (arrasta as janelas).

### 2. Ativação automática de contexto via skill
- Basta escrever algo como "Vamos começar a criar o site da StarCard" sem dar nenhum contexto adicional.
- A skill `/abrir` (mencionada no vídeo pelo nome de invocação) já puxa contexto da empresa: preferências, estratégia, design, linhas de produto — tudo o que já foi levantado/armazenado antes na pasta do cliente.
- Citação: *"Ele já ativou a skill barra abrir, tá vendo? Então ele já pegou todo o contexto da empresa, preferência, estratégia, design. Olha que simples, só escrevi isso."* [00:00]

### 3. Primeira geração (site completo em um prompt)
- Com um único prompt o Claude Code já entrega: linhas de produto (papelaria, cadernos, canetas etc.), formulário de cotação, seção "central do cliente / rastreio de pedido", CTA "falar com o comercial".
- Para visualizar: pasta de saídas → `site novo` → `index.html` → botão direito → Copy Path → colar na barra do navegador.
- Citação: *"Eu só escrevi, vamos começar a criar o site da StarCard. Eu não falei mais nada. Olha aqui. (...) foi um prompt. Um prompt."* [02:35]

### 4. Iteração por comandos diretos e curtos (curadoria, não geração)
Padrão recorrente da aula: frases-comando objetivas, quase sempre no imperativo, direcionadas a uma seção específica. Exemplos literais usados:
- "No formulário, tire volume estimado, prazo desejado, e-mail corporativo. Deixe somente e-mail." [01:17]
- "Na primeira sessão, tire o card de pedido na direita." [03:28]
- "Estou pensando em remover essa sessão dos clientes, Fiat." [04:46]
- "Na seção diferencial StarCard, vamos remover esse azul. Deixar o site somente com as cores vermelha, branca e preta." [15:39]
- "Na terceira sessão, remova esses cards com ícones. Vamos deixar somente o texto." [20:53]
- "Deixe impossibilitado de dar zoom e copiar os textos." [23:09] — prompt padrão dele para mobile, evitar zoom acidental e cópia de texto em toque.
- "Remova todos esses traços [travessões] nos textos." [23:09]

Princípio de estética repetido: tirar ícones genéricos e elementos "mirabolantes" porque isso "fica muito cara de site de IA, sabe? Muito infantil." [20:53]

### 5. Geração de imagens (fora do Claude Code, com prompts feitos pelo Claude)
Fluxo específico e repetido várias vezes na aula:
1. Pede ao Claude Code um prompt de imagem: *"Me ajude a criar um prompt para gerar um fundo (...) O que podemos utilizar para ficar com a cara de B2B e papelaria? Temos que tomar cuidado para não colocar um produto que eles não têm."* [07:23]
2. Cola o prompt no ChatGPT (GPT Imagem) — ferramenta de preferência dele: *"O GPT Imagem 2 está muito bom. Eu estou preferindo muito mais ele do que o Gemini, o Nano Banana."* [15:39]
3. Baixa a imagem, arrasta para a pasta `Assets` do projeto (drag and drop direto no VS Code).
4. Avisa o Claude Code onde a imagem está e pede para aplicar (ex.: como fundo de seção, imagem de card de produto).
5. Repete o loop com feedback textual sobre o que não gostou (ex.: "não fez sentido essa imagem (...) tem que ser marcas que existem mesmo" [17:43]; "ah, mas daí ele tirou as mochilas, pô. Não gostei." [13:07]).

Detalhe técnico citado: nomes de arquivo com `.png` duplicado quebravam a exibição — precisa apagar a extensão repetida manualmente. [19:00]

Importante: o próprio Claude Code, tendo o "framework com a memória" do que a empresa vende, corrige o prompt de imagem quando o resultado foge do catálogo real do cliente — ele sinaliza que a referência trazida (mochila, caderno, mousepad) não bate com os produtos da StarCard e sugere um kit mais fiel. [09:38]

### 6. Geração de logo (paralela, também iterativa)
- Print da logo antiga do cliente + pedido de versão "mais moderna".
- Comentário técnico: *"Normalmente eu não uso versão 2.0. Eu falo uma versão ultra."* [06:05] (indício de preferência por variações mais avançadas/agressivas de modelo de imagem).
- Depois de gostar de uma logo gerada pelo próprio Claude ("a login aqui que o próprio Claudio fez"), usa-a como base visual (estrela vermelha + texto branco) para orientar a paleta do site inteiro.

### 7. Fechamento e organização
- Pede para o Claude Code organizar a pasta do site e checar performance: *"Organize a pasta do site. Veja se está carregando rápido. Tudo certinho e funcional."* [23:09]
- Comando de encerramento de sessão de trabalho: *"Agora atualize o contexto."* — repetido duas vezes ao fim [26:32] e [27:48], reforçando que atualizar o contexto (provavelmente outra skill/rotina do MazyOS) é passo obrigatório antes de trocar de tarefa (ex. ir criar o carrossel em outro chat).

### 8. Deploy
- Hospedagem via **Netlify** (ele cita usar também Vercel e Hostinger, mas prefere Netlify no momento).
- Processo manual: abre o Netlify no navegador, localiza a pasta local do site (ex. "StarCard site Netlify" dentro da pasta do cliente) e arrasta a pasta para a área de deploy do Netlify (drag and drop) — gera link sem domínio próprio ainda, só para apresentar ao cliente.
- Para atualizar depois de nova alteração: repete o drag and drop da pasta atualizada; o Netlify substitui o deploy.
- Testa no celular abrindo o link recebido via WhatsApp, para simular a experiência real do cliente.

## Exemplos concretos citados na aula

- **Cliente-exemplo**: StarCard, papelaria e material de escritório B2B (cadernos, blocos, agendas, post-its, canetas, lápis, marca-texto, organizadores, mochilas/lancheiras, produtos personalizados).
- **Problema de negócio real identificado durante a criação**: pesquisando o nome da empresa no Google, ela não aparece; não tem LinkedIn. Isso vira gancho de venda adicional (proposta de criação de LinkedIn e Google Meu Negócio) além do site. [26:32], [28:28]
- **Formulário original do cliente**: considerado complexo demais (campos como volume estimado, prazo desejado); simplificado para pedir só e-mail.
- **Feature que o cliente pediu de fato**: um "código de rastreio" visível no site — citado como o item que ela mais queria e que acaba virando destaque funcional (seção "central do cliente / rastreie seu pedido" com bolinha vermelha pulsante). [20:53], [26:32]
- **Concorrentes**: pesquisados durante a aula, descritos como parecendo "loja/e-commerce", um inclusive com aviso de "site em manutenção". [03:28]
- **Precificação mencionada**: ele planeja cobrar cerca de R$ 10.000 pelo pacote (site + possivelmente LinkedIn/GMN), citado duas vezes como piada/meta ("eu fiz 10 mil reais em duas horas"). [00:00], [30:34]
- **Tempo real de execução**: aula gravada levou ~2h; ele estima que sem parar para explicar levaria cerca de 1h a 1h15 para um site desse porte.

## Citações relevantes com contexto

> "Ele já ativou a skill barra abrir, tá vendo? Então ele já pegou todo o contexto da empresa, preferência, estratégia, design. Olha que simples, só escrevi isso." [00:00]
Mostra que o ganho de velocidade vem da skill de contexto persistente do MazyOS, não de um prompt elaborado.

> "É aqui para criar o site a gente está com pouquíssimo material. (...) Só que o site dela está tão ruimzinho que eu não tenho nem material para usar. Mas beleza. Vamos fazer com o que a gente tem." [04:46]
Postura pragmática central do método: material insuficiente do cliente não paralisa o processo, o instrutor complementa gerando imagens e textos plausíveis para a call de venda, deixando claro (para si mesmo, na aula) que o material real virá depois do fechamento.

> "Isso que é bom você ter um framework com a memória, com tudo que ele vende aqui. (...) porque daí eu mandei uma imagem e ele já me disse as coisas que naquela imagem ali ele não vende." [09:38]
Evidência de que a base de conhecimento/contexto do cliente dentro do MazyOS é usada ativamente pelo Claude Code para validar imagens geradas contra o catálogo real, evitando prometer produtos inexistentes.

> "Eu vou conversando. Ele começou uma chuva da porra." [11:50]
Ilustra o uso do Claude Code como parceiro de brainstorm quando falta direção criativa, não só executor de comandos.

> "Eu gosto de arrancar aqueles íconezinhos porque senão fica muito cara de site de IA, sabe? Muito infantil." [20:53]
Princípio de design recorrente: remover ícones/elementos genéricos de template para não parecer "gerado por IA".

> "Deixe impossibilitado de dar zoom e copiar os textos. (...) porque às vezes também o cara bate o dedo, fica alguma coisa marcada, feio." [23:09]
Prompt padrão de UX mobile que ele reaplica em todos os sites, focado em evitar interação acidental no celular.

> "Já dá para eu fechar com a cliente. (...) Eu confio no meu produto, no meu serviço. Eu vou mostrar para ela que jogando o nome dela no Google não aparece ela." [28:28]
Estratégia de venda: usar o próprio site pronto + lacunas de presença digital do cliente (sem Google, sem LinkedIn) como argumento de fechamento.

> "Cara, lembra que é uma empresa B2B. Não precisa florear muito. Não precisa criar um negócio mirabolante não. Faz algo funcional." [29:29]
Resumo da filosofia de design aplicada ao nicho B2B: funcional > vistoso, atender a necessidade concreta do cliente (rastreio de pedido) em vez de "over-design".

> "Agora atualize o contexto." [26:32] / [27:48]
Comando repetido ao final da sessão, antes de trocar de tarefa (ir para o carrossel em outro chat) — indica um passo de encerramento/persistência de contexto tratado como rotina obrigatória no fluxo MazyOS.

## Conexões com outras aulas

- **`ACESSO AO MAZYOS + INSTALAÇÃO`** e **`PREPARANDO O TERRENO PARA O MAZYOS`** (mesmo módulo): pré-requisito de setup que explica de onde vem a skill `/abrir` e a estrutura de pastas por cliente usada aqui.
- **`COMO USAR O MAZYOS NO DIA A DIA SKILLS`**: explica a skill **"novo projeto"**, que cria a pasta isolada por cliente (ex. o caso hipotético "João Kleber, sapataria" citado nessa aula de skills) — é o passo que antecede o que se vê nesta aula (a pasta "StarCard" já existia/foi criada por essa skill antes da gravação). Também confirma que o workspace é "orquestrado" para não misturar contexto entre clientes.
- **`CRIANDO CARROSSEL COM MAZYOS + PDF DE PROPOSTA`** (próxima aula do módulo): continuação direta anunciada no fim desta aula ("depois vou criar o carrosselzinho dela" [20:17]; "agora a próxima vai ser o Criando os Carrocéis" [31:18]). As mesmas imagens de produto geradas para o site são reaproveitadas para os carrosséis.
- **`COMO EU COBRO MEUS CLIENTES - FAZENDO 1 VENDA AO VIVO`**: dá continuidade ao gancho comercial iniciado aqui (o valor de ~R$10 mil citado como meta de cobrança e a estratégia de fechar na call mostrando o site pronto).
- **`CLIENTES INFINITOS PARTE 1`**: relevante para a lógica de prospecção que justifica por que ele cria o site *antes* de fechar com a cliente (estratégia de "chegar com o produto pronto na call" para converter).
