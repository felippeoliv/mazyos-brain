---
titulo: "CRIANDO CARROSSEL COM MAZYOS + PDF DE PROPOSTA"
curso: MazyOS
modulo: LETS GO! Tudo na prática
camada: ouro
fonte_prata: prata/1-lets-go/CRIANDO CARROSSEL COM MAZYOS + PDF DE PROPOSTA.md
---

# Criando carrossel com MazyOS + PDF de proposta

## Tese central

Esta aula não ensina "como usar uma feature", ensina um método de trabalho: criar peças (carrossel, proposta em PDF) com prompts mínimos e frases soltas, deixando a skill do MazyOS carregar a estrutura, e refinando por iteração curta, quase sempre uma linha de comando por ajuste. Vagner grava a aula minutos antes de uma call real com uma cliente (Cristiane, da StarCard), então o conteúdo é literalmente "trabalho ao vivo, sem preparo": ele cria carrossel institucional e proposta comercial em menos de 30 minutos, no meio de trocar mensagem de WhatsApp com a cliente confirmando horário.

A tese de fundo, repetida de formas diferentes, é dupla:

1. **Gestão de contexto é parte do ofício.** Antes de qualquer coisa criativa, ele ensina a rodar a skill "atualizar" (para persistir tudo que foi feito num chat antes de abandoná-lo) e a olhar `/context` / `/clear` para não desperdiçar tokens carregando conversa velha. Isso não é aparte técnico, é pré-requisito: sem isso o agente "esquece" o que já foi combinado sobre a marca do cliente.
2. **Para B2B, o objetivo não é volume de posts, é estrutura fixa e bem direcionada.** Ele é explícito em dizer que não fica "gerando carrossel pro cara infinito": o valor entregue é a empresa aparecer arrumada (Google Meu Negócio, Instagram, Facebook, LinkedIn) com poucos posts que fazem sentido para aquele público, não postagem diária.

## Framework / passo a passo

### A. Preparar o contexto antes de criar

1. Ainda no chat onde o site do cliente já foi construído, digitar **"use a skill atualizar"**. Isso faz o MazyOS varrer tudo que foi produzido naquele chat (site, imagens, textos, logo) e salvar/atualizar a estratégia, o design e o `.md` de contexto do projeto.
2. Rodar **`/context`** para ver quanto dos tokens está sendo consumido só pelo histórico de mensagens (no exemplo, 21,3%).
3. Rodar **`/clear`** para zerar esse consumo (caiu para 0,1% no exemplo) e abrir espaço de contexto antes de iniciar uma tarefa nova, já que o agente relê toda a conversa a cada prompt.
4. Regra prática dada: fazer isso "de tempos em tempos", sempre que perceber que está há muito tempo no mesmo chat.

### B. Criar o carrossel

1. Com o chat limpo, escrever só uma frase solta, ex.: **"vamos começar a criar os carrosséis da StarCard"**. A palavra "carrossel" (ou `/carrossel`) já é suficiente para ativar a skill de carrossel automaticamente.
2. A skill devolve uma proposta de carrossel (nesse caso, institucional/apresentação, 7 slides, formato texto puro sem imagem) e **opções de capa** (A, B, C) para escolher.
3. Responder em linguagem natural e curta qual opção prefere e por quê (ex.: "gostei mais da opção B... tem que ter cara de papelaria B2B"), depois **"pode gerar"**.
4. Ajustar slide a slide, referenciando explicitamente o número: "slide 1", "slide 2" etc., recomendando fazer isso no VS Code (ou outra IDE) para navegar entre os arquivos dos slides.
5. Pedidos de ajuste são sempre frases diretas e específicas: mover elemento visual, tirar travessão, aumentar arroba, remover slide, trocar cor de fundo, ajustar posição de imagem. A skill aplica e regenera.
6. A cada carrossel gerado o design "aprende": segundo Vagner, cada novo carrossel a skill entende melhor o padrão visual e o processo de correção fica mais rápido, quase automático.
7. A skill gera sozinha, junto dos slides, um `legenda.md` (Ctrl+Shift+V para pré-visualizar) já pronto para Instagram/Facebook.
8. Estrutura de pastas: fica organizada por tipo de conteúdo e por data (ex. `Marketing > Conteúdo > [nome do carrossel]`), o que facilita localizar campanhas antigas.
9. Nível atual descrito como "nível 1": imagens de capa são coladas manualmente (ex. imagem gerada antes no ChatGPT). O próximo passo evolutivo citado é **conectar a skill a uma API de geração de imagem** (ChatGPT, NanoBanana, Higgsfield etc.) para a própria skill gerar a imagem da capa durante a criação do carrossel.
10. Promessa de automação futura (ainda não coberta nesta aula): aprovar o carrossel e ele postar sozinho no Instagram, Facebook e LinkedIn, já usando a legenda gerada.

### C. Criar a proposta comercial em PDF

1. Abrir **outro chat** (separado do carrossel) e descrever a proposta em um parágrafo corrido, sem formatar nada: nome da cliente, horário da call, o que está sendo vendido (site completo + Google Meu Negócio + redes sociais), preço e condições (10k no Pix ou 3x de 4 mil), e a ideia de destinar 1k do valor para tráfego pago no Google.
2. A skill devolve não só PDF: no mesmo fluxo ele lista que dá para gerar carrossel, slide, apresentação, stories, post para Instagram, PDF ou PowerPoint a partir do mesmo tipo de descrição solta. A skill de conteúdo não é só "gerador de carrossel", é um gerador de formatos.
3. Revisão do PDF segue o mesmo padrão de comandos curtos e diretos: trocar prazo ("30 dias" → "instantâneo"), simplificar jargão ("kick-off" removido porque "ninguém sabe o que é isso"), tirar palavras em inglês, ajustar tom de frases que soam negativas ("de volta ao mapa" trocado porque sugere que a empresa "está fora do mapa"), alinhar cards, cortar imagem mal centralizada.
4. Decisão de enviar ou não o PDF pronto é por "feeling": ele só solta o material na call se sentir que está bom o suficiente; se achar que precisa modificar mais, guarda e refina depois, sem pressa de mandar algo malfeito.

## Exemplos concretos

- **Carrossel institucional da StarCard (7 slides, texto puro):** capa com título "25 anos abastecendo empresas no Brasil"; slide de prova social citando cliente âncora ("Empresas que não aceitam atraso confiam na StarCard. Inclusive a Fiat."); CTA final "Sua empresa, um fornecedor só. Peça sua cotação."
- **Iteração de estilo:** primeira versão da capa tinha fundo vermelho forte; Vagner pediu para trocar por preto/escuro porque achou "muito forte"; a skill concordou e recomendou a variante A porque batia melhor com o diferencial da empresa (fornecedor único). Ele aceitou a recomendação só respondendo "pode seguir".
- **Segundo carrossel, sobre fabricação própria:** usa a foto "hero" do site (mochilas personalizadas com a logo) como imagem de capa em vez de texto puro, reaproveitando asset já existente do projeto do site.
- **Precificação real ensinada:** proposta de 10k à vista no Pix ou 3x de 4 mil (12k parcelado); dentro dos 10k, 1k é alocado para investimento em Google Ads no primeiro mês, apresentado como bônus "de graça" para o cliente, mas na prática é ferramenta de geração de lead que abre porta para upsell (ex.: solução de resposta automática de WhatsApp quando o cliente não conseguir dar conta do fluxo de leads).
- **Uso simultâneo de múltiplos chats/projetos:** ele descreve deixar vários chats abertos ao mesmo tempo (um resolvendo YouTube, outro uma empresa, outro fechamento de reunião), mas nesta aula opta por ir devagar, um passo de cada vez, para fins didáticos.

## Citações relevantes com contexto

> "Aqui no caso eu vou falar pra ele, use a skill atualizar. O que é essa skill atualizar? Ele vai atualizar todo o contexto. [...] Por que que isso é importante? Porque agora, pra gente abrir outro chat aqui, se eu falar pra ele, ah, o que que tem escrito no site em tal parte? Ele vai saber." **[00:00]**

Fundamenta por que persistir contexto é passo obrigatório antes de trocar de chat: sem isso o agente "esquece" decisões já tomadas sobre o cliente.

> "Se você der um barra context aqui, você vai ver aqui o quanto está sendo usado dos seus tokens [...] só de mensagens, tá vendo? Olha o quanto que tá sendo gasto só de mensagens. 21,3%." **[01:20]**

Mostra o hábito operacional de monitorar consumo de tokens via `/context` antes de decidir limpar o chat com `/clear`.

> "Qualquer coisa você escrever, carrossel, ele já vai ativar a skill de carrossel." **[02:36]**

Explica o gatilho de ativação da skill: não é um comando fixo obrigatório, basta a palavra aparecer no prompt.

> "A maioria das empresas que eu pego, eu não fico gerando carrossel pro cara infinito. Ainda mais se for empresa B2B assim. Ela não precisa ficar postando todo dia carrosselzinho. Ela precisa de uma estrutura fixa." **[03:53]–[05:09]**

É a tese estratégica da aula sobre entrega para clientes B2B: qualidade e direcionamento de poucos posts, não cadência diária.

> "Eu sempre gosto de, quando eu tô criando o carrossel, eu escrevo assim, tipo, slide 1 pra ele entender, né? Depois, slide 2. [...] Por isso que é bom você usar o VS Code aqui, ou qualquer outra IDE." **[06:10]**

Descreve a técnica de edição granular por slide referenciado por número, e por que usar uma IDE ajuda a navegar entre os arquivos gerados.

> "O legal é que nessa skill de carrossel, ele já gera aqui, ó, se você olhar, ó, legenda.md." **[07:31]**

Mostra que a skill entrega, por padrão, também a legenda pronta para postar, não só as imagens dos slides.

> "Depois, o próximo passo pra você melhorar a skill do carrossel é conectar alguma API de outro gerador de imagem. Então, você pode conectar com a API do ChatGPT, ou com o NanoBanana, ou Higgs Field, qualquer outro IA. [...] Aqui a gente ainda tá no nível 1." **[14:35]**

Explicita que o fluxo mostrado é uma versão manual/inicial e que existe um caminho de evolução técnica (integração de API de imagem) fora do escopo desta aula.

> "Nesse primeiro momento, você tem que ficar pensando muito em lucro. [...] E desse 1k, eu ainda entrego de graça em anúncio pra ela no Google pra trazer mais clientes. Por que que isso é interessante? Ela vai ver o cliente chegando. [...] Depois eu consigo vender outras soluções pra ela." **[16:17]–[17:15]**

Revela a lógica comercial por trás do "bônus" de Google Ads: não é generosidade pura, é isca de geração de lead que cria a necessidade seguinte (upsell) a ser vendida depois.

> "Entende que não é só carrossel, tá? Você cria o que você quiser. É só você pedir pro bicho." **[17:15]–[18:31]**

Reforça que a skill de conteúdo do MazyOS é multiformato (carrossel, slide, apresentação, stories, post, PDF, PowerPoint), e o carrossel é só o exemplo usado na aula.

> "Kick off. [...] Ninguém sabe o que é kick-off, não, velho. Tem que deixar o mais simplificado possível [...] Sem palavras em inglês para o cliente." **[25:42]**

Princípio de copywriting para propostas B2B locais: eliminar jargão de mercado (mesmo termos comuns em agência) porque o cliente final não entende.

> "Se eu sentir que ainda preciso modificar. Se ela precisa de outras coisas. Eu não envio esse PDF. Eu penso. Estruturo melhor. [...] É feeling. Se você achar que você já consegue soltar ali. Na cal você solta." **[26:59]–[28:15]**

Deixa claro que o critério final de "está pronto para enviar" não é uma checklist, é julgamento do próprio vendedor sobre o momento da call.

## Conexões com outras aulas

- **`prata/1-lets-go/CRIANDO SITE COM MAZYOS.md`**: pré-requisito direto desta aula. O carrossel e a proposta em PDF reaproveitam ativos já criados na aula do site (logo, imagens "hero", textos, estratégia de marca da StarCard), inclusive citando explicitamente "terminei de criar o site dela" como ponto de partida.
- **`prata/1-lets-go/COMO USAR O MAZYOS NO DIA A DIA SKILLS.md`**: onde o conceito de skills (e provavelmente a skill "atualizar" e o padrão de ativar skills por palavra-chave) deve ter sido introduzido de forma mais didática; esta aula é a aplicação prática desse conceito em um caso real.
- **`prata/1-lets-go/COMO EU COBRO MEUS CLIENTES - FAZENDO 1 VENDA AO VIVO.md`**: continuação natural do raciocínio de precificação esboçado aqui (10k Pix / 3x4k, 1k de Ads como isca, ausência de recorrência inicial); vale conferir se a aula de cobrança aprofunda ou contradiz a lógica de "não cobrar recorrência de início" mencionada nesta aula.
- **Próxima aula do módulo, "Fazendo a Call com a Cliente"** (mencionada no fechamento, "[28:15]": *"Vamos agora para a próxima aula. Que vai ser o Fazendo a Cal com a Cliente."*) — ainda não presente na camada prata desta base no momento da escrita desta nota. É o desfecho natural do case StarCard/Cristiane iniciado aqui: o carrossel e o PDF gerados nesta aula são material de apoio para essa call.
- **`prata/5-calls-gravadas/`**: módulo de calls reais gravadas com clientes/parceiros; útil para comparar se o padrão de proposta enxuta e sem jargão técnico ensinado aqui se repete em negociações reais mostradas nesse módulo.
