---
titulo: "Como fazer disparos com o S-Zap"
curso: MazyOS
modulo: "KAPTAR: seus clientes no automático"
modulo_slug: 2-kaptar
camada: ouro
fonte_prata: prata/2-kaptar/Como fazer disparos com o S-Zap.md
tags: [mazyos, kaptar, s-zap, whatsapp, disparo-em-massa]
---

# Como fazer disparos com o S-Zap

## Tese central

O S-Zap é o módulo de disparo em massa do Kaptar: um "WhatsApp Web" embutido na ferramenta que conecta ao número real do usuário via QR Code e permite rodar campanhas segmentadas sobre os leads já captados pelo scrapper (aula anterior, "Como funciona a ferramenta Kaptar"). A tese operacional da aula é que a variável crítica de sucesso não é a mensagem em si, mas o ritmo de disparo: WhatsApp bane números que enviam volume alto em pouco tempo, então o intervalo entre mensagens (o instrutor usa 45 segundos) e um teto diário (mencionado como 100 leads/dia) funcionam como mecanismo de "despistar" a detecção de spam. É uma aula essencialmente técnica/operacional, curta (cerca de 6 minutos), sem aprofundar copywriting de script (isso já foi coberto na aula de introdução do módulo, por Vagner).

## Framework / passo a passo do disparo em massa

**1. Setup do servidor local do S-Zap** *(antes de qualquer campanha)*
- Abrir a aba S-Zap dentro do Kaptar, ir no painel, clicar em "servidor S-Zap" → "baixar".
- Extrair o arquivo baixado, clicar duas vezes em "iniciar".
- Uma janela de CMD abre para instalar dependências do servidor e fecha sozinha quando termina.
- Clicar em "iniciar" novamente: aí o servidor está de fato rodando.
- Regra operacional: **não fechar o CMD do servidor enquanto estiver usando o S-Zap** (pode minimizar, mas não fechar).

**2. Conexão do WhatsApp**
- Na aba WhatsApp, clicar em "ativar o WhatsApp" → aparece QR Code → escanear com o celular.
- Existem dois botões pós-conexão: "sincronizar histórico" (o instrutor recomenda **não clicar**, porque desconecta a sessão e exige escanear de novo) e "sair" (desconecta o número).
- Após escanear, as conversas do WhatsApp real carregam dentro da ferramenta.

**3. Montagem da campanha (aba "Vim Campanhas")**
- Segmentar os leads por filtro (tipo de lead, cidade, etc.) e definir um limite de envio (exemplo usado: limite de 20 leads).
- Escrever a mensagem: existe uma aba de "Scripts" para templates reutilizáveis, ou um campo de texto livre.
- Nomear a campanha (exemplo: "campanha 1").
- Inserir **variáveis de personalização**: `nome` (puxa o nome do lead/empresa) e `cidade` (puxa a cidade onde o lead foi prospectado) — cada lead recebe a mensagem com seus próprios dados substituídos automaticamente.
- Definir o **intervalo entre mensagens** (usado na demo: 45 segundos).
- Conferir o **preview** da mensagem como o cliente vai recebê-la antes de disparar.
- Clicar em disparar: a campanha roda, pulando automaticamente os números sem WhatsApp ativo ou desatualizado.

**Boas práticas de segurança de conta mencionadas:**
- Intervalo baixo entre mensagens aumenta risco de bloqueio; o WhatsApp "não deixa você fazer campanhas dessa forma" por natureza, então o objetivo é reduzir risco, nunca eliminá-lo.
- Volume alto (ex.: 100 leads em menos de uma hora) = risco alto de bloqueio.
- Combinação de volume moderado + intervalo alto entre mensagens = risco baixo (o padrão usado pelo instrutor é 45s).
- Limite seguro citado pela própria ferramenta: **100 leads por dia**.
- Leads sem WhatsApp (número desatualizado ou sem o app) são pulados automaticamente pela campanha, sem intervenção manual.

## Exemplos concretos

- Mensagem de teste enviada na demonstração: apenas **"oi"**, sem personalização com nome (o instrutor deliberadamente deixou o campo `nome` vazio no teste, mas mostrou no preview como ficaria se tivesse preenchido: "ele já vem o nome da empresa").
- Campanha de demonstração: filtro de lead, limite de 20 leads, intervalo de 45 segundos, nome da campanha "campanha 1".
- Resultado mostrado ao vivo: a campanha disparou, pulou os leads sem WhatsApp válido, e a mensagem chegou de fato no WhatsApp de teste do instrutor em tempo real.

## Citações com contexto

> "O SSAP é como se fosse um WhatsApp web, onde você consegue rodar campanhas aqui dentro da Capitar de uma forma muito mais fácil e também muito mais personalizada." **[00:00]**

Define o S-Zap: não é uma ferramenta nova de zero, é uma camada de automação sobre uma sessão real de WhatsApp Web, o que explica por que ele herda os riscos de bloqueio do próprio WhatsApp.

> "Porque realmente o WhatsApp não deixa você fazer campanhas dessa forma. Porém, se você coloca um volume de mensagens alto. E uma quantidade de intervalo alta entre essas mensagens. Você consegue meio que despistar um pouco esse bloqueio." **[03:19]**

O ponto mais importante tecnicamente da aula: o instrutor é honesto sobre o fato de que disparo em massa via WhatsApp é contra a política da plataforma, e a técnica ensinada (intervalo + volume controlado) é mitigação de risco, não uma brecha garantida.

> "Eu não vou vir aqui te falar que é garantido que você não vai ser bloqueado se você exagerar. Se você for fazer 100 leads em menos de uma hora a chance de ser bloqueado é grande." **[03:19]**

Reforça a mesma ideia com um número concreto de referência (100 leads/hora como zona de risco alto), calibrando a expectativa do aluno antes de soltá-lo para captar sozinho.

> "Legal aqui. É que ele pula os números que não tem o WhatsApp. [...] E ele pula as mensagens que não tem o WhatsApp. Os leads que não tem o WhatsApp. Que o WhatsApp está desatualizado." **[04:11]**

Detalhe funcional que economiza tempo do usuário: não é preciso limpar a lista manualmente antes de disparar, a ferramenta já filtra leads inválidos durante a campanha.

> "A aba de esse zap, cara. Ela não tem segredo. É realmente entre você ficar conectando. Abrir o seu servidor. E, cara. Fazer as suas campanhas. Conversar com seus clientes." **[04:11]**

Fecha o tom da aula: o S-Zap é posicionado como mecânica simples e repetível (conectar → disparar → conversar), não como algo que exige domínio técnico.

## Conexões com outras aulas

- **"Introdução Ferramenta Kaptar"** (Vagner, aula 1 do módulo): já havia alertado sobre o mesmo risco de bloqueio de WhatsApp por volume ("se você usar isso daqui, o S-Zap [...] e você enviar para muitas empresas de uma vez, vai cair o seu WhatsApp"), recomendando começar com 10-20 disparos/dia num número já maduro. Esta aula (3) traz a implementação concreta dessa cautela: campo de intervalo (45s) e teto diário (100 leads) dentro da própria interface do S-Zap.
- **"Introdução Ferramenta Kaptar"** também é a fonte do framework de copywriting que dá conteúdo às mensagens disparadas aqui: abertura → identificação do problema → solução/entrega rápida → CTA. A aula do S-Zap não repete esse framework, apenas mostra onde ele é operacionalizado (campo de mensagem/script da campanha, com variáveis `nome` e `cidade`).
- **"Como funciona a ferramenta Kaptar"** (aula 2, Eric): é o pré-requisito direto desta aula, os leads disparados aqui vêm do scrapper de Google Maps configurado e explicado ali (aba "Vim Campanhas" reaproveita os mesmos filtros de lead/qualificação descritos na aula 2). A própria aula 2 termina anunciando explicitamente esta aula 3 ("Na próxima aula, eu vou explicar como é que funciona o Sysap aqui dentro").
- Encerra o módulo "KAPTAR: seus clientes no automático" (3 aulas: introdução → scrapper → disparo), completando o ciclo captar → qualificar → contatar em massa.
