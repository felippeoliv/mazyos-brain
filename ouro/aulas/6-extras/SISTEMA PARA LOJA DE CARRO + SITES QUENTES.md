---
titulo: "SISTEMA PARA LOJA DE CARRO + SITES QUENTES"
curso: MazyOS
modulo: EXTRAS
modulo_slug: 6-extras
camada: ouro
fonte_prata: prata/6-extras/SISTEMA PARA LOJA DE CARRO + SITES QUENTES.md
tags: [mazyos, site, sistema, crm, kanban, supabase, 21st-dev, skills, extras, ouro]
---

# SISTEMA PARA LOJA DE CARRO + SITES QUENTES

> [!info] Camada ouro: destilação de uma live/call gravada às 2h da manhã no Discord, módulo "EXTRAS". Transcrição integral em `prata/6-extras/SISTEMA PARA LOJA DE CARRO + SITES QUENTES.md`.

## Tese central

Efeitos visuais "mirabolantes" (partículas que viram rosto, entrada tipo showroom 3D) e sistemas de gestão completos (estoque, CRM em Kanban, metas, relatórios) não exigem nenhuma skill extra do MazyOS: nascem de **descrever o que se quer com clareza** (por texto ou áudio) e, quando necessário, **apontar uma referência visual concreta** (uma imagem gerada no ChatGPT, um efeito achado em um site catálogo como o 21st.dev). O instrutor repete isso como o fio condutor da aula inteira: "Todos os chats que eu fiz até hoje, não usei nenhum skill. Só o Maze." A skill, na definição dele, não é um superpoder embutido na ferramenta, é apenas "um direcionamento pro Claude Code" — ou seja, quem já sabe pedir bem não precisa da skill pronta, porque consegue chegar ao mesmo resultado só descrevendo a intenção em linguagem natural.

Segunda tese, aplicada ao caso da loja de carros: o sistema entregue foi deliberadamente **simples e do tamanho do cliente**. Ele escolhe Supabase mesmo sabendo que "não é o melhor dos bancos de dados" porque a loja é pequena e o objetivo é destravar um problema de negócio real e imediato (o dono estava 38 dias sem vender um carro), não construir arquitetura para escalar. "Simples é o que funciona (...) não precisa criar nada mirabolante" é o resumo que ele dá do próprio trabalho.

## O que foi construído e como (passo a passo)

### 1. Site institucional da loja de carros (vitrine)
- Site "simplezinho" conectado ao estoque completo de carros do cliente.
- Efeito de entrada: transição visual estilo "showroom" — ao interagir, a imagem de fundo se move como se o visitante estivesse entrando fisicamente no showroom ("Entre no showroom, escolha o seu").
- Cada carro tem página própria: fotos, ano, quilometragem, descrição, botão "falar com o vendedor".
- Redes sociais linkadas no rodapé.
- Fonte do efeito visual: o instrutor cita ter usado o site **21st.dev** como catálogo de referência de efeitos/componentes prontos para "achar ideias" e depois pedir ao Claude Code que reproduza algo parecido — não copia código, usa como inspiração visual.

### 2. Painel administrativo (o "sisteminha" por trás do site)
Construído para o dono da loja ou um funcionário operar no dia a dia, sem estar pronto/finalizado no momento da gravação:
- **Dashboard inicial**: lista todos os carros do estoque, valor total se vendesse tudo pela tabela FIPE (patrimônio), e destaque dos carros parados há mais tempo no estoque.
- **Adicionar carro**: formulário com marca, modelo, cor, ano, preço; ao salvar, o carro aparece automaticamente no site público (testado ao vivo na call: adiciona um "Corolla preto do Vagninho" por R$ 180 mil, dá F5 no site e o carro já aparece publicado).
- **Campo de custo/margem**: ao lançar o custo do carro, o painel calcula o desconto possível e a margem que o funcionário pode negociar com o cliente.
- **Marcar como vendido / remover carro**: ao remover, o carro some do site em tempo real (também demonstrado ao vivo).
- **CRM em Kanban**: cadastro de cliente/lead com telefone, status (lead novo, vendeu, comprou), cartões arrastáveis entre colunas.
- **Agenda** para compromissos.
- **Metas**: define uma quantidade de carros a vender; cada carro marcado como vendido atualiza a meta automaticamente.
- **Relatórios e sincronização de tráfego**: métricas do site (visitas etc.) integradas ao painel; ainda em expansão no momento da gravação.
- **Stack técnica citada**: Supabase como banco de dados, escolhido por simplicidade e adequação ao porte da empresa, não por ser tecnicamente o melhor.

### 3. Efeito da "borboleta" (exemplo citado no início, de outro contexto)
- Um aluno (Rael) mandou um site com um efeito de partículas em formato de borboleta que, ao rolar o mouse, se transforma no rosto de uma mulher.
- Perguntado se usou alguma skill, a resposta foi não: usou só o MazyOS. O processo foi gerar uma imagem de exemplo no ChatGPT ("quero assim, quero esse exemplo, gera essas partículas e as partículas têm que gerar o rosto da mulher") e deixar o Claude Code ajustando a partir dali.

## O que significa "sites quentes" nesse contexto

Na fala do instrutor, "quente" tem dois usos que se reforçam:

1. **"Site quente" como fonte de efeitos valiosos**: ao mostrar o 21st.dev, ele diz "esse aqui é ouro tá, sitezinho aqui é quente, ele é bom mesmo. Você consegue pegar vários efeitos, várias paradinhas." Ou seja, um "site quente" é um catálogo/galeria de componentes e efeitos de interface (animações, transições, micro-interações) que serve de banco de referências visuais para pedir ao Claude Code que replique algo parecido em um projeto real — sem precisar baixar nenhuma skill ou biblioteca externa.
2. **"Estar quente" como elogio ao aluno/comunidade**: ao final, quando alguém da call pergunta como replicar a lógica para o painel de uma clínica, ele responde "não, mas vocês estão quentes, vocês estão quentes" — usando o termo também como reconhecimento de que a comunidade já está captando o método (pedir bem, buscar referência, deixar o Maze construir) sem depender de receita pronta.

O aviso embutido junto ao primeiro uso é importante: catálogos como o 21st.dev têm efeito quase infinito de coisas para explorar, e ele avisa para não se perder nisso — "se você ficar caçando aqui o dia inteiro, você acha coisa da hora, tá ligado, lembre do feijão com arroz, não adianta ficar também tacando coisa infinita." Ou seja, "quente" é fonte de inspiração pontual, não desculpa para over-engineering.

## Exemplos concretos citados na aula

- **Cliente-exemplo principal**: loja de carros, dono "38 dias sem vender um carro" — motivação de negócio explícita por trás do sistema (gerar lead/venda, não só "ficar bonito").
- **Teste ao vivo de cadastro**: Corolla preto do "Vagninho", R$ 180 mil, cadastrado no painel e verificado aparecendo no site com F5.
- **Teste ao vivo de remoção**: o mesmo Corolla removido do painel, confirmado sumindo do site com F5.
- **Caso do aluno com a borboleta** (Rael): efeito de partículas + rosto de mulher, feito só com MazyOS + imagem de referência gerada no ChatGPT, sem skill.
- **Caso levantado por outro participante**: uma clínica no Rio (Barra), cujos clientes ainda são controlados em planilha; pedido de dica para replicar a lógica de painel administrativo com Kanban/CRM.
- **Ferramentas/sites citados como referência técnica**: 21st.dev (catálogo de efeitos de UI), RD Station e Pipedrive (citados como exemplos de "estilos de CRM" que dá para pesquisar e pedir para "clonar" a funcionalidade, não o código).

## Citações relevantes com contexto

> "Você usou alguma skill? (...) Só com o Maze. Só usei o Maze. Nada mais que isso. Usou o ChatGPT pra gerar imagem, usou o ChatGPT pra gerar uma imagem de exemplo e falei: quero assim, quero esse exemplo, gera essas partículas e as partículas tem que gerar o rosto da mulher. E o Maze foi me dando, e eu fui só ajeitando ali e acabou. Nenhum skill." [00:00]
Estabelece de saída a tese central: o resultado visual sofisticado veio de descrever bem a intenção e fornecer uma imagem de referência, não de uma skill especial.

> "Esse aqui é ouro tá. Sitezinho aqui é quente. Ele é bom mesmo. Você consegue pegar vários efeitos, várias paradinhas." [02:33]
Define o conceito de "site quente" como catálogo de referências de UI (o 21st.dev) usado para alimentar pedidos ao Claude Code.

> "Se você ficar caçando aqui o dia inteiro, você acha coisa da hora, tá ligado. Lembre do feijão com arroz, não adianta ficar também tacando coisa infinita." [02:33]
Contrapeso ao entusiasmo pelo catálogo de efeitos: alerta contra perder tempo/complexidade desnecessária em vez de entregar o funcional.

> "Isso daqui é bom, que o funcionário consegue saber (...) você coloca o custo, vai aparecer o desconto, quanto que o cliente consegue, quanto que o funcionário consegue colocar de margem." [05:04]
Detalha a lógica de negócio embutida no painel: não é só cadastro de carro, é ferramenta de precificação/negociação para o vendedor.

> "Tudo isso daqui feito com o MasOS, sem skill nenhuma. Top demais, tá ligado. Sem skill nenhuma, não precisa de skill nenhuma cara. Simples. Simples é o que funciona, tá ligado. Não precisa criar nada mirabolante." [06:20]
Fechamento do caso da loja de carros, resumindo a filosofia: entrega funcional e simples resolve o problema de negócio (venda parada) sem exigir sofisticação técnica extra.

> "É só usar o Cloud Code, você já tem tudo. Entenda que uma skill é um direcionamento pro Cloud Code. Você não tá dando um superpoder pro bicho, você só tá dando um direcionamento pra ele. Então se você sabe já usar o direcionamento do que você quer, mano, tipo assim, eu não precisava nem ter usado (...) esse 21 [21st.dev] aqui." [07:35]
Definição mais explícita do curso inteiro sobre o que é (e não é) uma skill: um atalho de direcionamento, não uma capacidade exclusiva — reforça que o mesmo resultado seria alcançável só com um pedido bem descrito, inclusive por áudio.

> "Não, mas vocês estão quentes, vocês estão quentes." [08:50]
Segundo sentido de "quente" na aula: elogio à comunidade por já estar captando o método de pedir/referenciar sem depender de receita pronta.

> "Se quiser ser eu, você tira um print aqui pra fazer tipo um painel administrativo (...) você pode pesquisar estilos de CRM, você entra aqui em vários sites, tem RD Station, tem Pipeline [Pipedrive], é infinito, é só se jogar no Google. (...) Eu quero clonar esse estilo de CRM ou eu quero essa funcionalidade." [09:06]/[10:06]
Receita generalizável para replicar o caso da loja de carros em outro nicho (a clínica citada): usar um print ou uma referência de CRM existente como direcionamento para o Claude Code, e deixar que ele proponha a stack (ex. Supabase) sozinho.

> "Isso daqui, gente, pelo amor de Deus, estou falando um bagulho simples que (...) ninguém vai ter acesso, isso daqui é só o filho dele que vai usar, que é o funcionário dele. E ele, tipo assim, eu não preciso criar um bagulho mirabolante, entende? Então, óbvio que vai do tamanho da empresa, do que eles estão usando." [10:06]
Princípio explícito de dimensionamento: a complexidade do sistema deve ser proporcional ao porte real do cliente, não ao que tecnicamente seria "ideal".

## Conexões com outras aulas

- **`CRIANDO SITE COM MAZYOS`** (módulo 1-lets-go): mesmo padrão de trabalho — pedir em linguagem natural, iterar com feedback curto, gerar imagens de referência no ChatGPT e aplicar via Claude Code; lá o princípio de design é "não precisa florear muito, não precisa criar um negócio mirabolante", quase a mesma frase usada aqui sobre o painel da loja de carros ("não precisa criar nada mirabolante").
- **`COMO USAR O MAZYOS NO DIA A DIA SKILLS`** (módulo 1-lets-go): contraste direto de perspectiva sobre skills — aquela aula lista e defende o catálogo de skills prontas do MazyOS como atalhos valiosos (ex. skill de relatórios de Ads, "novo projeto"); esta aula argumenta o oposto na prática, mostrando que os mesmos resultados (site com efeito complexo, sistema completo) saem sem usar nenhuma skill, só com direcionamento bem feito — as duas leituras se complementam: skill acelera quando existe, mas não é pré-requisito.
- **`SE SEU MAZYOS ESTA SEM SKILL ASSISTA`** (módulo 3-importante): aula de troubleshooting sobre skills que não carregam por erro de estrutura de pastas; esta aula relativiza a gravidade desse problema ao mostrar que, mesmo sem nenhuma skill ativa, dá para construir efeitos visuais e sistemas completos só descrevendo bem o pedido.
- **`Mindset Avançado`** e **`Ferramenta de áudio para falar com a IA`** (mesmo módulo 6-extras): completam o padrão do módulo "EXTRAS" como conteúdo complementar e mais pessoal/informal (lives noturnas no Discord, indicações externas), fora do fluxo estruturado de aulas técnicas dos módulos principais. Nesta aula em particular, o comentário "se eu mando um áudio falando assim (...) no Whisper Flow" conecta diretamente com a aula de ferramenta de áudio, reforçando que o ditado por voz é usado no mesmo fluxo de "direcionamento" descrito aqui.
- **Conceito de "site quente" (21st.dev)** também aparece implicitamente ligado ao título de outra aula do curso, **`Live com Gustavo Barbosa (Simplu) QUENTE`** — o uso da palavra "quente" no título de outra aula do módulo de lives sugere que é um adjetivo recorrente do instrutor para conteúdo/referência de alto valor, não um termo técnico exclusivo desta aula.
