---
titulo: "COMO USAR O MAZYOS NO DIA A DIA / SKILLS"
curso: MazyOS
modulo: LETS GO! Tudo na prática
camada: ouro
fonte_prata: prata/1-lets-go/COMO USAR O MAZYOS NO DIA A DIA SKILLS.md
---

# COMO USAR O MAZYOS NO DIA A DIA / SKILLS

## Tese central

Aula gravada às pressas (Vagner admite estar atrasado para o aniversário da namorada) para resolver duas dúvidas recorrentes dos alunos: **(1) em qual IA/interface o MazyOS roda** e **(2) se é preciso montar uma pasta do zero para cada cliente novo**. A resposta central é que o MazyOS não é uma ferramenta amarrada a uma IA específica, é um *framework de orquestração* que funciona sobre qualquer IA (Claude, Antigravity, Codex) e sobre qualquer interface (Claude direto, VS Code, Cursor, terminal). E o segundo ponto, mais importante na prática: o MazyOS já vem com uma skill própria ("novo projeto") que cria e isola a pasta de cada cliente automaticamente, então o aluno não precisa reinstalar nem reorganizar nada manualmente a cada cliente novo — ele só precisa escrever em linguagem natural o que quer fazer, e o sistema reconhece qual skill ativar.

A aula funciona também como um índice de referência: Vagner passa rapidamente pela lista de skills documentadas no GitHub do MazyOS e cobra explicitamente que o aluno leia o repositório ("a maioria de vocês não leram nada").

## Framework / passo a passo: como usar no dia a dia + todas as skills citadas

### Onde/como rodar o MazyOS

1. **Escolher a IA**: o MazyOS "orquestra a sua IA", funciona com Claude, Antigravity ou Codex. Há alunos usando Antigravity de graça e já conseguindo os primeiros clientes.
2. **Escolher a interface**:
   - **Claude direto**: abrir o Claude, "selecionar pasta", apontar para a pasta do MazyOS instalado, confiar no workspace. A partir daí a IA já puxa toda a arquitetura de pastas existente.
   - **VS Code** (a preferida de Vagner, e a que ele ensina no curso): acesso lateral a todas as pastas, visualização de arquivos/imagens, arrastar arquivos para dentro, terminal integrado via **CTRL+J**.
   - **Cursor** ou **terminal puro**: também funcionam, é questão de preferência. A recomendação dele é clara: "é melhor você utilizar no Claude seco aqui, direto, do que não usar" — ou seja, a interface importa menos do que simplesmente usar.

### A dúvida "preciso criar uma pasta para cada cliente?" — Não

O MazyOS é descrito como um **workspace único**, o jeito de "acordar e trabalhar" na agência: não é necessário abrir uma pasta nova do zero por cliente. Isso é resolvido pela skill **Novo projeto**.

### Lista de skills mencionadas na aula (referência)

- **Novo projeto**: skill principal do dia a dia. Cria pasta isolada para cada cliente ou iniciativa nova dentro da estrutura já existente do MazyOS. É ativada automaticamente só de o usuário escrever algo como "tem um novo projeto de um cliente chamado X" ou "tenho um novo cliente". A partir daí o sistema conduz uma "entrevista" (briefing): tipo de negócio, se já é cliente ou é prospecção, se há proposta enviada, informações do site, etc. Ao final, cria a pasta nova automaticamente sem misturar com dados de outros clientes.
- **Mapear rotinas**: identifica tarefas que o usuário repete manualmente (ex.: responder um e-mail todo dia) e as transforma em uma skill nova, para não precisar refazer o processo do zero toda vez.
- **Criação de carrossel**: skill de conteúdo/SEO para gerar carrosséis (referenciada como já usada ou a ser vista em aulas seguintes).
- **Publicar tema**: cria o blog/post e já transforma o conteúdo em carrossel e três legendas.
- **SEO**: roda um fluxo completo de 8 passos/pastas: demanda, concorrência, Google Meu Negócio, on page, conteúdo, ads, monitoramento e GAO.
- **GAO** (dentro do fluxo de SEO, mas tratado como conceito distinto): segundo Vagner, "é diferente de SEO"; resumidamente, é otimização para "a IA te achar" (equivalente ao SEO, mas voltado a mecanismos de IA em vez de buscadores tradicionais).
- **Responder avaliações**: usada originalmente para responder avaliações do Google Meu Negócio, mas Vagner relata ter usado também para responder comentários do YouTube que não sabia como responder — ou seja, a skill é reaproveitável fora do caso de uso original.
- **Aprovar post**: publica o blog e replica em Instagram e Facebook.
- **Anúncios pagos** (skill de relatórios de Ads): descrita como "ouro". Recebe o relatório exportado em CSV (ex.: últimos 90 dias de uma conta de Google Ads) e devolve um relatório completo: campanhas erradas, o que deveria estar pausado, onde dá para aumentar orçamento. Também monta a campanha inteira pronta para subir via planilha no Google Editor.
- **Analisar dados**: recebe planilhas (e múltiplos arquivos, inclusive PDF) e devolve um resumo completo do conteúdo.
- **E-mail profissional**: rascunha e-mails a partir de contexto livre fornecido pelo usuário.
- **Skills de atualizar contexto**: mencionadas de passagem, sem detalhamento nesta aula ("tirando as skills de atualizar o contexto... que eu uso nas outras aulas").

### Regra prática de uso

Não é preciso decorar comandos exatos: basta descrever em linguagem natural o que se quer fazer ("tem um novo projeto de cliente tal") que o MazyOS reconhece a skill correspondente e a aciona sozinho. A recomendação final e repetida é ler o GitHub/README do MazyOS na íntegra para entender o núcleo do sistema e o catálogo completo de skills, algo que, segundo ele, a maioria dos alunos ainda não fez.

## Exemplos concretos

- **Onboarding de cliente simulado ao vivo**: Vagner abre um chat novo no VS Code e digita que tem "um novo projeto de um cliente chamado João Kleber, dono de uma sapataria", para o qual fará tráfego e site. Só esse texto já dispara a skill "Novo projeto", que cria a pasta "Kleber" dentro de "clientes" e inicia o briefing perguntando o tipo de sapataria (conserto de sapatos vs. loja de calçados), se já é cliente fechado ou proposta em andamento, etc.
- **Organização real da conta dele**: ele mostra ter várias pastas de clientes já criadas (frigorífico, apartamento, loja) mais pastas separadas para projetos mais complexos (cita o próprio canal do YouTube) que prefere manter isoladas "no feeling", mas deixa claro que isso é exceção, não regra.
- **Caso do mentorado com Google Ads**: um mentorado pagava R$ 2.000 para uma agência de tráfego cuidar do Google Ads e o resultado "tava uma bagunça". Vagner pegou o relatório dos últimos 90 dias, exportou em CSV, jogou no MazyOS e usou a skill de relatórios de anúncios. O MazyOS com Claude devolveu um relatório completo: campanhas erradas, o que devia travar, onde podia aumentar o budget. O mentorado reagiu com "cara, não é possível isso". Em seguida, a skill de anúncio monta a campanha inteira, e o usuário só precisa subir a planilha gerada dentro do Google Editor para publicar a campanha de tráfego.
- **Skill de responder avaliações fora do escopo original**: usada também para responder comentários do YouTube que ele não sabia como responder, mostrando reaproveitamento de skill fora do caso de uso descrito na documentação.

## Citações relevantes com contexto

> "Entenda que o MasOS é um framework que vai orquestrar a sua IA que você está utilizando. Então você pode usar com Antigravity. Você pode usar com Cloud. Você pode usar com Codex." **[00:34]**

Define o ponto central da aula: MazyOS não é uma IA, é uma camada de orquestração agnóstica de modelo/interface.

> "É melhor você utilizar no Cloud seco aqui, direto, do que não usar." **[01:51]**

Vagner relativiza a preferência por VS Code: o importante é usar o sistema, a interface é secundária.

> "Preciso criar uma pasta para cada cliente. Não. Não precisa." **[03:07]**

Resposta direta à principal dúvida que motivou a aula.

> "É importante você ler. A maioria de vocês não leram nada." **[03:07]**

Cobrança explícita para que o aluno leia a documentação/GitHub do MazyOS antes de reclamar de dúvidas já respondidas ali.

> "Só de eu ter escrito. Novo projeto. Ele já ativa. A skill. Novo projeto." **[04:11]**

Demonstra o mecanismo de ativação de skill: não é um comando fixo, é reconhecimento de intenção em linguagem natural.

> "Ele é inteligente. Ele é orquestrado. Entenda que o Cloud, ou qualquer outro A que você estiver utilizando, com o MasioS, ele é mais inteligente que você. Então ele não vai comer bola." **[05:27]**

Argumento de confiança no sistema: tranquiliza o aluno de que múltiplos clientes na mesma base não geram confusão de dados.

> "Já fez isso aqui mais de uma vez. Deixa eu transformar em uma skill." **[06:44]**

Descreve o comportamento da skill "Mapear rotinas": o próprio sistema identifica repetição e propõe automação.

> "Isso daqui é ouro... Wagner, tem como você me ajudar com uma consultoria de Google Meu Negócio? Eu falo: cara, para que? Você já tem as skills que já faz tudo isso para você dentro de uma ZOS." **[07:44]**

Ilustra o posicionamento de valor da skill de anúncios pagos/relatórios: substitui uma consultoria paga.

> "Cara, não é possível isso." **[07:44]**

Reação relatada do mentorado ao ver o relatório de Google Ads gerado pelo MazyOS a partir do CSV exportado, usada como prova social do resultado da skill.

## Conexões com outras aulas

- É a **aula 6 do módulo "LETS GO! Tudo na prática"**, funcionando como uma aula de organização/referência no meio do módulo prático, não como aula de conteúdo novo isolado.
- Referencia explicitamente que **criação de carrossel** e **publicar tema** já foram vistas ou serão vistas "nas próximas aulas" do mesmo módulo.
- Anuncia conteúdo futuro fora deste módulo: uma **aula de quatro horas** (a ser publicada) detalhando o uso da skill de anúncios pagos com o caso real do mentorado do Google Ads.
- Anuncia módulos futuros de **GitHub** (conectar CRM e outros repositórios ao projeto), reforçando que o curso ainda vai aprofundar a parte de integração técnica além do uso básico das skills.
- Reforça, na prática, algo que provavelmente é dito de forma mais teórica em aulas de introdução: a ideia de "workspace único orquestrado" em vez de "uma instalação por cliente", que é a peça central da arquitetura de pastas do MazyOS ensinada ao longo do curso.
