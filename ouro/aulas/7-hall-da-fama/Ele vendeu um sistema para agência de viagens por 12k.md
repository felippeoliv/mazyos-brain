---
titulo: "Ele vendeu um sistema para agência de viagens por 12k"
curso: MazyOS
modulo: "Hall da Fama"
camada: ouro
fonte_prata: "prata/7-hall-da-fama/Ele vendeu um sistema para agência de viagens por 12k.md"
---

# Ele vendeu um sistema para agência de viagens por 12k

## Tese central

Aula de estreia do módulo "Hall da Fama": Vagner traz o aluno White (brasileiro morando no Chile, já experiente no digital) para mostrar um CRM completo para agências de viagens, construído com Cloud Code + MazyOS e vendido por **R$12.000** para um cliente que ele conheceu por acaso, trabalhando no restaurante de outro cliente. O ponto da aula não é só o case de venda: é a trajetória completa, da venda de implementação pontual (12k) até a transformação do projeto em **SaaS com recorrência mensal (R$290/mês)** mirando agências do Chile, do Brasil e de toda a América Latina. O critério do módulo, dito por Vagner na abertura, define o espírito: **"eu vou colocar só quem vendeu, vendeu alguma coisa por um certo valor [...] até pra te dar um insight pra você olhar e falar 'putz, como que eu não tinha pensado nisso?' ou pra você entender o que é possível fazer com o MaisOS, o que é possível fazer com o Cloud Code"** **[01:05]**.

## A origem da venda: prospecção por proximidade

A venda não veio de tráfego nem de prospecção ativa, veio de estar trabalhando em público, em contexto de negócio:

> "Eu tava num restaurante de um cliente meu, tava resolvendo algumas coisas pra ele, tô fazendo um sistema de mesas pra ele, pros garçons poderem fazer pedidos na mesa, já sair na cozinha o pedido. [...] Esse cara chegou, tava lá, e viu que eu tava trabalhando, e a gente começou a conversar. Aí falou que precisava de um CRM. [...] A gente acabou fechando esse projeto. O projeto saiu por 12k." **[04:32]**

Detalhes operacionais da venda:

- **Cliente**: dono de agência de viagens, brasileiro morando no Chile.
- **Valor**: R$12.000, pagos "em efetivo" (dinheiro físico, "na plata"), não via Pix nem gateway. **[23:35]**
- **Regra de pagamento do White**: **50% adiantado antes de iniciar qualquer projeto** ("senão eu nem inicio o projeto"). Se o cliente não conseguir pagar 50% na entrada, ele negocia caso a caso "pra não perder o cliente também". **[23:35]**
- **Status**: já entregue e em uso pelo cliente no momento da gravação. **[26:05]**

## Da implementação de 12k ao SaaS recorrente

O framework de evolução do projeto, em passos:

1. **Primeira versão crua** construída em cima do **Frappé** (CRM open source que Vagner tinha indicado). White não gostou: "ele tem muita informação". **[04:32]**
2. **Reconstrução do zero**: "eu peguei o design do Frappé, somente o design, e construí tudo do zero, do meu jeito". **[05:48]**
3. **Venda da implementação** por 12k para o cliente da agência.
4. **Produtização**: "agora eu transformei em empresa mesmo, agora eu tô colocando recorrência mensal, então não serve só pra agência do Chile, mas também pro Brasil e da América Latina toda". O White cria contas para clientes pelo painel admin, modelo SaaS de verdade. **[05:48]**

### Precificação do SaaS

- Primeira ideia: **R$500/mês**. Ele mesmo recuou: "acho que é muito pra começar".
- Preço de lançamento definido: **R$290/mês**, com plano de aumentar depois que o produto estiver redondo ("quando eu terminar, deixar tudo bonitinho ali pra atendimento, eu aumento o volume"). **[27:20]**
- Benchmark de Vagner validando que nem é caro: "quando eu tava vendendo o Hub, eu tava fazendo umas pesquisas, cara, tem gente vendendo só CRM por 800 conto mês, mano, só CRM". **[28:36]**
- Estratégia acordada pelos dois: começar barato, validar, pegar os primeiros clientes, depois subir o preço. **[28:36]**

### Custo de operação: praticamente zero

> "O legal daqui é que eu não tenho um custo nenhum, entendeu? Tá na VPS que o cliente paga." **[28:36]**

A VPS hospeda todos os projetos dele (o CRM, o gateway/checkout próprio, projetos de outros clientes), então a margem do SaaS é quase integral. Dá para colocar mais clientes na mesma VPS.

## Stack e método de construção

- **Stack citada**: Docker + PostgreSQL, hospedado em VPS. **[07:49]**
- **Método com o Cloud Code**: como o MazyOS já guarda todo o contexto do projeto, ele nem usa Plan Mode: "como o Cloud já tem todo o meu contexto lá no MyOS, então eu só falo: Cláudio, vamos criar isso, isso, e ele começa a criar, e eu vou ajustando do meu jeito". **[07:49]**
- **Ressalva do Vagner** (importante para iniciante): "é bom colocar no Plan Mode pra quem não tem um plano bom do Cloud, e pra quando a pessoa também não sabe, tipo, qual banco de dados usar, como fazer tal coisa. Acho que Plan Mode é melhor mesmo." **[08:00 aprox., bloco 07:49 a 09:05]**
- **Tradução e transcrição**: API da OpenAI ("sai baratinho"), não API de tradutor do Google. **[26:05]**

### Truque do Framer para landing pages (abertura da aula)

Antes da gravação "oficial", White ensina um atalho para sites bonitos: entrar no Framer, escolher qualquer modelo gratuito ("use free"), publicar, **pegar o link do site publicado e mandar pro Cloud, que copia tudo, todas as animações**. Foi assim que ele fez o próprio site pessoal (que tem página de projeto no estilo "o desafio que construí, a parte que ninguém vê"). **[00:00]**

## Anatomia do produto: o CRM de agência de viagens (Fluxnave)

Esta é a parte mais valiosa da aula como referência de escopo: o que cabe num sistema vendido por 12k e transformado em SaaS. Funcionalidade por funcionalidade:

### Landing page de vendas

Página com animações de scroll, toggle liga/desliga, seção "agente de atendimento com IA" e, o destaque: um **preview interativo da plataforma dentro da própria página de vendas**, onde o visitante clica no chat e vê o sistema por dentro antes de comprar, no lugar de liberar teste grátis. **[03:36]**

### Painel admin (visão do dono do SaaS)

- Estatísticas gerais de tudo.
- Contas dos clientes: acesso à conta de cada cliente, quantas conversas, quantas mensagens nos últimos 30 dias, negócios; ele consegue entrar na conta do cliente para dar suporte. **[06:33]**
- Sistema de cobrança automática dos clientes do SaaS.
- Sistema de avisos (informações, manutenção) e painel de "saúde do CRM" (o que está ativo, o que não está configurado). **[07:49]**

### Gateway de pagamento próprio + multi-moeda

White tem gateway de pagamento próprio e estava negociando com o diretor de uma casa de câmbio online que atende a América Latina. O plano: integrar o gateway ao CRM para que **as agências cobrem o cliente final direto pelo sistema, em qualquer moeda**: "eu tô no Chile e o cliente tá vindo do México, eu consigo cobrar o cliente na moeda dele e receber em peso chileno". **[07:49]**

### Módulo WhatsApp (praticamente um WhatsApp Web completo)

Evolução visível: a primeira versão era "crua, feia, não tinha nada"; a atual tem **[09:05]** e **[10:20]**:

- Visualização de grupos, resposta a mensagens específicas, envio de áudio, emojis.
- **Mensagens rápidas** cadastráveis com atalho (digita "/teste" e envia o texto salvo).
- Envio de foto, vídeo, documento, qualquer coisa.
- Notificação sonora no navegador quando chega mensagem, igual WhatsApp Web.
- Marcar mensagem como não lida.
- **Instagram** como canal de atendimento vinculável em configurações. **[10:20]**
- **Tradução automática de mensagens** (via OpenAI): recebe "hello", traduz para o idioma da interface do usuário (português ou espanhol), com indicação "traducido del inglés". Caso de uso: agência recebendo cliente gringo. **[26:05]**
- **Transcrição de mensagens de áudio**. **[26:05]**
- Versão **mobile responsiva**: "no celular parece um WhatsApp mesmo", para o atendente atender pelo celular. **[27:20]**

### Leads com temperatura automática

Toda mensagem que chega (de anúncio ou qualquer origem) vira lead automaticamente numa tela própria, com filtro por temperatura e regras de tempo sem intervenção humana **[10:20]** e **[11:35]**:

- **Quente**: em conversa ativa nas últimas 48 horas.
- **Morno**: passou de 48 horas sem resposta do cliente, muda sozinho.
- **Frio**: depois de 30 dias, muda sozinho.

### Passeios + Vitrine (bio link)

- A agência cadastra os passeios: foto (com biblioteca de imagens salvas), nome, preço. **[11:35]**
- Passeio preenchido vai para a **Vitrine**: um bio link (estilo Linktree) que mostra o catálogo completo de passeios da empresa sem precisar de site, com **4 templates** de layout à escolha. Vagner destaca o uso: colocar no Instagram da agência ou mandar direto pra cliente. **[11:35]** e **[24:50]**

### IA de primeiro atendimento

Diferencial que, segundo White, nenhum outro CRM tem: IA treinada para fazer **todo o primeiro atendimento e qualificar o lead**, inclusive **ouvindo áudio e respondendo**; quando o lead quiser fechar, passa para uma pessoa da agência. Além disso, a IA fará o **preenchimento automático do negócio** (destino, quantos adultos, quantas crianças, data de chegada) antes do humano assumir. **[12:50]** e **[13:29]**

### Negócios (Kanban de vendas)

- Kanban por etapas (ex.: "aguardando enviar orçamento"); a agência move o cliente entre colunas direto do chat. **[13:29]**
- No negócio: adicionar passeios cadastrados, quantidade de adultos e crianças, datas (ex.: chega dia 8, sai dia 15, sete dias de viagem), responsável pelo negócio, origem do lead (ex.: indicação) e **anotações que ficam visíveis pro atendente** (exemplo usado: "esse cliente precisa de ajuda para o filho que necessita de uma cadeira de rodas"). **[14:45]**

### Geração de documentos (o recurso que mais impressionou Vagner)

Com o negócio preenchido, o sistema gera e envia pelo chat, em PDF pronto: **documento de orçamento, proposta comercial, contrato, nota de serviço e voucher do passeio**, tudo com nome da empresa, logo, garantia e cláusulas. **[14:45]** e **[16:00]**

A personalização vem do **perfil do negócio**, preenchido uma vez pelo dono da agência: nome da empresa, CNPJ, razão social, contatos, **assinatura desenhada pelo dono**, cor do PDF e os textos das cláusulas. **[16:00]**

Vagner valida com experiência própria de comprador: "eu acabei de fechar uma viagem com um amigo meu que ele tem uma agência de viagem, e ele manda literalmente daquele jeito mesmo [...] depois eu vou mostrar esse vídeo pra ele, imagina ele ter um sisteminha desse onde ele já clica, já gera". **[24:50]**

### Ficha do passeio (formulário para o cliente final)

- A agência envia um link; o cliente final preenche: hotel onde vai ficar, se precisa de transfer do aeroporto, nome dos passageiros, passaporte, assinatura e observações. **[18:54]**
- Enviada a ficha, aparece automaticamente para a agência.
- **Validação inteligente**: se a venda foi para 3 pessoas e a ficha tem menos, o sistema avisa ("faltam duas pessoas"). **[19:45]**

### Financeiro

- **Recebimentos**: lançamento com forma de pagamento da empresa (ex.: Pix), valor, taxa de embarque, total. **[17:09]** e **[18:08]**
- **Multi-idioma e multi-moeda**: empresa com idioma português residindo no Chile lança em outras moedas, com classificação por moeda (recebeu em peso ou em real). **[17:09]**
- **Comprovante anexado direto da conversa**: o cliente manda o comprovante no WhatsApp, a agência clica em "usar como comprovante", escolhe o recebimento, e ele fica anexado ao lançamento. Foi o momento "caraca, doideiros, eu nunca tinha visto não" do Vagner. **[18:08]**
- **Custos**: lançamento com data, destinatário (da agência ou de uma pessoa), categoria (guia, alimentação, hospedagem, comissão, salário), filtros por pagos/a receber/vencidos, por pessoa, por meio de pagamento. **[21:03]**
- Histórico de todos os documentos já emitidos para o cliente. **[19:45]**

### Equipe, comissões e permissões

- Cadastro de comissão por pessoa da equipe. **[21:03]**
- **Convite por link/e-mail**: o dono convida, escolhe papel (**vendedor ou gerente**), a pessoa recebe e-mail, aceita, cria senha e entra. **[22:19]**
- **Permissões por papel**: vendedor não vê financeiro e não consegue excluir mensagem (isso é do dono ou do gerente). **[22:19]**

### Tarefas

Criação e designação de tarefas com data (ex.: "precisa buscar no aeroporto"), visíveis numa tela própria. **[19:45]**

## O contraste com o concorrente (Kommo)

White mostra o CRM que o cliente usava antes (Kommo, "muita gente usa esse"): "olha a diferença: feio, não é intuitivo, a pessoa não dá vontade de mexer", além de ser menos completo. **[27:20]** Mesma lógica de vantagem competitiva por simplicidade e estética que aparece em outras aulas do vault: ganhar não por ter mais features, e sim por interface limpa que dá vontade de usar, e nesse caso ele ainda é mais completo.

## Números citados

- **R$12.000**: valor da implementação vendida para a agência (pago em dinheiro físico, 50% adiantado). **[04:32]** / **[23:35]**
- **R$290/mês**: preço de lançamento do SaaS (recuo da ideia inicial de R$500/mês). **[27:20]**
- **R$800/mês**: benchmark de mercado citado por Vagner para "só CRM". **[28:36]**
- **48 horas / 30 dias**: régua automática de temperatura de lead (quente → morno → frio). **[11:35]**
- **4 templates** de vitrine/bio link. **[11:35]**
- **Custo operacional ~zero**: VPS paga pelo cliente hospeda todos os projetos. **[28:36]**
- Métricas do painel admin por conta: conversas, mensagens dos últimos 30 dias, negócios. **[06:33]**

## Citações relevantes com contexto

> "Eu peguei o design do Frappé, somente o design, e construí tudo do zero, do meu jeito." **[05:48]**

O padrão de trabalho que resume a aula: usar ferramenta pronta como referência visual, mas ser dono do código para poder virar produto próprio depois.

> "Eu sempre, antes de iniciar qualquer projeto, eu cobro metade, 50% do valor, senão eu nem inicio o projeto." **[23:35]**

Regra comercial simples e inegociável (com flexibilidade caso a caso para não perder cliente).

> "Como o Cloud já tem todo o meu contexto lá no MyOS, então eu só falo: Cláudio, vamos criar isso, isso, e ele começa a criar, e eu vou ajustando do meu jeito." **[07:49]**

O valor do MazyOS como repositório de contexto: para quem já domina, dispensa até o Plan Mode.

> "O legal daqui é que eu não tenho um custo nenhum. Tá na VPS que o cliente paga." **[28:36]**

A economia do modelo: infra rateada em projetos de clientes, margem quase integral no SaaS.

> "Se você quiser aparecer aqui no Hall da Fama, meu amigo, mete marcha, vende alguma coisa aí." **[31:06]**

Fechamento de Vagner: o módulo é vitrine de execução, o ingresso é vender. Ele também reforça a comunidade do WhatsApp como canal onde essas trocas acontecem (foi lá que White mostrou o CRM pela primeira vez).

## Conexões com outras aulas

- [[ouro/aulas/5-calls-gravadas/Live com Gustavo Barbosa (Simplu) QUENTE|Live com Gustavo Barbosa (Simplu)]]: mesma trajetória em estágio mais avançado: sair de serviço pontual para SaaS vertical de nicho com recorrência (Simplu para clínicas, Fluxnave para agências de viagens), incluindo a mesma disciplina de simplicidade de interface contra concorrentes "com muita janela" (aqui, o Kommo) e a mesma lógica de começar com preço acessível e subir depois.
- [[ouro/aulas/1-lets-go/COMO EU COBRO MEUS CLIENTES - FAZENDO 1 VENDA AO VIVO|COMO EU COBRO MEUS CLIENTES]]: a regra dos 50% adiantado do White e a negociação caso a caso são aplicação direta do raciocínio de cobrança e precificação ensinado por Vagner.
- [[ouro/aulas/1-lets-go/CLIENTES INFINITOS PARTE 1|CLIENTES INFINITOS PARTE 1]]: a venda nasceu de proximidade e demonstração (trabalhando no restaurante de um cliente, outro empresário viu e pediu CRM), exemplo real de que projeto entregue gera o próximo cliente.
- [[ouro/aulas/1-lets-go/CRIANDO SITE COM MAZYOS|CRIANDO SITE COM MAZYOS]]: o truque do Framer (publicar template gratuito e mandar o link pro Cloud copiar layout e animações) é um atalho complementar ao fluxo de criação de sites do curso, e a landing com preview interativo da plataforma é referência de página de vendas.
- [[ouro/aulas/1-lets-go/COMO USAR O MAZYOS NO DIA A DIA SKILLS|COMO USAR O MAZYOS NO DIA A DIA]]: o relato de White ("o Cloud já tem todo o meu contexto no MazyOS") e a ressalva de Vagner sobre Plan Mode para iniciantes são o uso prático do fluxo de contexto ensinado nessa aula.
- [[ouro/aulas/6-extras/SISTEMA PARA LOJA DE CARRO + SITES QUENTES|SISTEMA PARA LOJA DE CARRO + SITES QUENTES]]: mesmo padrão de produto: sistema de gestão vertical para um nicho específico, vendido como projeto e demonstrado por dentro, útil para comparar escopos e preços.
- [[ouro/aulas/4-como-vender-infoprodutos/INFOPRODUTO + MAZYOS = OURO|INFOPRODUTO + MAZYOS = OURO]]: a produtização do White (de entrega única de 12k para receita recorrente escalável) é a mesma tese de transformar capacidade de execução em ativo que vende sozinho.
