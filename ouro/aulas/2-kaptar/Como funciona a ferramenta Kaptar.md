---
titulo: "Como funciona a ferramenta Kaptar"
curso: MazyOS
modulo: "KAPTAR: seus clientes no automático"
camada: ouro
fonte_prata: prata/2-kaptar/Como funciona a ferramenta Kaptar.md
---

# Como funciona a ferramenta Kaptar

## Tese central

Esta é a aula operacional (a segunda do módulo, ministrada por Eric) que mostra o fluxo completo do Scrapper de leads do Kaptar: configurar uma fonte de dados de geolocalização (Google Maps API ou OpenStreetMap), rodar uma busca por nicho e região, e depois gerenciar os leads captados dentro da aba "Leads" até o contato via WhatsApp. A tese implícita é que captação de clientes vira um processo repetível e barato: com uma cota gratuita de 5 mil requisições/mês é possível captar até 100 mil leads, e a ferramenta já qualifica o lead automaticamente por meio de um "score de site" que aponta quem tem a pior presença digital, ou seja, quem mais precisa (e mais provavelmente vai comprar) o serviço do aluno.

## Framework / passo a passo de funcionamento

1. **Configurar a fonte de dados antes de tudo.** Ao entrar no site, o usuário cai direto na aba "Scrapper de leads / buscar", mas nada funciona até configurar a fonte de dados em "Configurações".
2. **Escolher entre duas fontes de dados:**
   - **Google Maps API (recomendada por Eric):** gratuita até 5 mil requisições/mês, permite prospectar até 100 mil leads/mês. Precisa ser ativada com cartão de crédito (cobrança simbólica de R$1) ou depósito de R$200 via Pix, que vira saldo dentro do Google Console e pode ser resgatado depois. Há um tutorial in-app com links diretos para as páginas do Google Console.
   - **OpenStreetMap:** opção 100% gratuita, sem precisar de cartão nem depósito, descrita como "um pouco mais fraca" que a API do Google, mas funcional, para quem não tem cartão de crédito disponível.
3. **Colar a API key e testar conexão.** Botão "testar conexão" valida a chave na hora e aponta erro se ela estiver incorreta.
4. **Rodar a busca (Scrapper):**
   - Escolher a **categoria/nicho** (exemplo usado na aula: cardiologista, depois dentista).
   - Escolher os **filtros de qualidade do lead**: por exemplo, exigir que o lead tenha telefone, ou telefone + site.
   - Escolher a **região no mapa**, podendo clicar em vários pontos para selecionar várias localidades (exemplo: São Paulo).
   - Definir **quantos leads captar** na busca (exemplo: 120 leads).
   - O painel mostra em tempo real quantas requisições já foram gastas no mês e quantos leads ainda podem ser captados.
   - Importante: **uma busca não equivale a uma requisição** — o sistema faz buscas em blocos, então pedir 120 leads pode consumir de 7 a 18 requisições.
5. **Resultado vai para a aba "Leads".** Os leads captados na busca aparecem consolidados com os leads de buscas anteriores (exemplo da aula: 117 novos leads somados a uma base anterior, totalizando 216).
6. **Gerenciar cada lead na aba Leads**, onde é possível ver:
   - nome da empresa e segmento;
   - se tem presença digital (site) ou não;
   - número de contato (WhatsApp);
   - **score do site**: quanto maior o score, pior o site — e portanto melhor a oportunidade de venda (exemplo: score 87 e score 91 usados como leads "quentes" por terem sites ruins).
   - Ações disponíveis por lead: abrir WhatsApp direto, ver o site, ver a página no Google Maps, marcar como qualificado (estrela, reversível), marcar que já entrou em contato, limpar o lead, ou arquivar o lead.
7. **Diferença entre "limpar" e "arquivar" um lead** (ponto de atenção operacional):
   - **Limpar:** o lead some da aba de leads, mas pode ser reprospectado numa busca futura.
   - **Arquivar:** o lead vai para a aba "Arquivados" e nunca mais é reprospectado — é um banimento definitivo daquele lead do scrap.
8. **Fluxo de fechamento da aula:** qualificar o lead (marcar estrela) → verificar o site do lead para confirmar que o score bate com a realidade → contatar via WhatsApp clicando no botão que abre a conversa diretamente.

## Exemplos concretos citados na aula

- Busca de **cardiologistas** usada para demonstrar a configuração de filtros (telefone / telefone + site).
- Busca de **120 leads em São Paulo**, consumindo entre 7 e 18 requisições, retornando 117 novos leads (base total foi para 216 leads acumulados).
- Lead de exemplo: **"Dentista 24 horas, extração de dente, solo"**, score de site 91, marcado como qualificado; Eric confirma visualmente que "o site realmente precisa de uma reformulação. Ou precisa fazer um site novo para esse cliente" — validando o score como proxy confiável de oportunidade comercial.

## Citações com contexto

> "Então, aí você já todo mês vai ter uma recarga de 5 mil requisições que você pode ter até 100 mil leads captados." **[00:00]**

Abre a aula estabelecendo a economia da ferramenta: cota mensal gratuita e teto de captação, ancorando a decisão de qual fonte de dados usar.

> "Esse depósito de 200 reais no Pix, ele fica como saldo dentro do Google Console. Então, você não perde esses 200 reais." **[00:00]**

Contorna a objeção de custo/risco: o depósito para ativar a API do Google não é gasto, é caução resgatável, o que reduz a fricção de configuração para o aluno.

> "Nem sempre uma busca significa uma requisição. Porque ele tem que fazer várias buscas em blocos para conseguir o número de leads que você quer." **[02:26]**

Explica por que o consumo de cota não é 1:1 com o número de leads pedidos, informação prática para o aluno planejar quantos leads pedir por busca sem estourar a cota mensal.

> "Quanto maior o score for, pior é o site. Então, é melhor para você oferecer o serviço." **[03:27]**

É o núcleo do critério de priorização de leads dentro do Kaptar: o score de site inverte a lógica intuitiva (score alto parece bom, mas aqui significa site ruim) e serve como filtro automático de oportunidade comercial.

> "Quando você limpa o lead, ele some aqui da sua aba de leads. Só que ele pode ser reprospectado novamente." **[03:27]**

> "Quando você arquiva, o lead vai aqui para arquivados. E aí, ele não vai ser mais reprospectado. E você meio que bane aquele lead do seu scrap." **[04:45]**

Par de citações que define a diferença operacional crítica entre "limpar" (temporário, reversível por nova busca) e "arquivar" (permanente) — um erro de escolha aqui pode fazer o aluno perder ou reganhar leads sem perceber.

> "Você faz o controle. Você faz a checagem. Você vê se o site está legal. Você vê se ele não tem site. E aí, você oferece o seu serviço." **[05:21]**

Resume o loop de trabalho esperado do aluno: captar → checar → qualificar → oferecer serviço, sem atalhos automatizados nessa etapa (o disparo automatizado fica para a próxima aula).

## Conexões com outras aulas

- **Aula anterior, "Introdução Ferramenta Kaptar"** (mesmo módulo): já adianta o mesmo scrapper de Google Maps e alerta sobre uso comedido do disparo (10 a 20 mensagens/dia) para não derrubar o WhatsApp — contexto que esta aula não repete, mas pressupõe.
- **Próxima aula, "Como fazer disparos com o S-Zap"**: anunciada explicitamente no fechamento desta aula ("Na próxima aula, eu vou explicar como é que funciona o Sysap aqui dentro. Que é o disparador de campanhas que a gente tem" **[05:21]**) — é o passo seguinte do funil: depois de captar e qualificar o lead aqui, o disparo de campanhas personalizadas via WhatsApp integrado é o assunto da aula seguinte.
- O **score de site** e a distinção **limpar vs. arquivar** são conceitos operacionais centrais desta aula que provavelmente reaparecem como pré-requisito em qualquer aula futura sobre otimização de prospecção ou funil de vendas dentro do Kaptar.
