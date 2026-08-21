---
titulo: "Introdução Ferramenta Kaptar"
curso: MazyOS
modulo: "KAPTAR: seus clientes no automático"
camada: ouro
fonte_prata: prata/2-kaptar/Introdução Ferramenta Kaptar.md
---

# Introdução Ferramenta Kaptar

## Tese central

Esta é a aula de abertura do módulo Kaptar, gravada por Vagner (não pelo criador da ferramenta) para apresentar o Eric, "um membro da comunidade" que construiu o Kaptar e que vai ensinar tecnicamente nas próximas aulas. A tese central não é técnica, é comportamental: a ferramenta por si só não gera clientes, é a *disciplina no uso* que gera. Vagner insiste três vezes em variações da mesma ideia: comece devagar (10 a 20 disparos por dia), teste scripts diferentes, e use com "calma, com sabedoria" para não derrubar o WhatsApp. O argumento de fundo é de prova social + urgência: pessoas da comunidade já pegaram clientes em poucos dias usando o Kaptar de graça, então o gargalo não é a ferramenta nem o dinheiro, é a execução consistente. A aula funciona como um teaser motivacional que entrega um framework de script de prospecção (abertura, identificação do problema, solução/entrega rápida, CTA) antes mesmo de mostrar a interface da ferramenta, que fica para a próxima aula.

## O que é a ferramenta Kaptar e para que serve

O Kaptar é descrito como um scraper de Google Maps combinado com um disparador de WhatsApp (S-Zap). Funcionalmente, tem duas partes que aparecem separadas nas aulas seguintes do módulo:

- **Scraper de leads**: você escolhe nicho e região, e ele busca empresas daquele segmento, retornando se a empresa tem site ou não e o número de WhatsApp, entre outros dados.
- **S-Zap (disparador)**: ferramenta de disparo em massa via WhatsApp para contatar os leads captados.

É possível usar totalmente de graça, mas Vagner recomenda investir um pouco para ter resultados melhores, comparando o custo com uma campanha de tráfego pago ("é um valor muito bem gasto comparado a uma campanha de tráfego, por exemplo, que você for fazer"). O risco operacional citado explicitamente é o bloqueio do WhatsApp por volume de disparos: a recomendação é usar um número já maduro ("que você já tem há mais tempo") e escalar aos poucos.

## Exemplos concretos

- **Case do amigo com relatório de análise**: um comprador do MazyOS que "está tendo muito resultado" usa uma abordagem em duas etapas: primeiro pergunta ao lead se ele quer uma "análise profunda do negócio dele"; se o lead topa, ele roda um framework que verifica site, localização e concorrentes, gera um relatório completo e manda de volta. No fim do relatório, oferece contato para quem quiser um site, marca uma call e só depois passa o preço.
- **Framework de script de abordagem fria** (ensinado passo a passo na aula, [03:19]-[04:35]):
  1. Abertura (nome, com quem trabalha)
  2. Identificação do problema ("vi aqui que você não está na primeira página do Google", "vi aqui que você não tem um site", "vi aqui que seu site está fora do ar")
  3. Solução na mão ou entrega rápida ("Em uma hora eu te entrego um site que vai atrair mais clientes")
  4. CTA ("você quer o seu site?", "vamos fazer uma call", "faz o Pix aí que eu te entrego")
- **Case do "moleque" da comunidade (o próprio Eric)**: entrou na comunidade, testou o Kaptar, pegou dois clientes em menos de 3 dias, já criou 3 sistemas com o MazyOS usando o plano de 100 reais do Claude, e acabou entrando para o time de Vagner.

## Citações com contexto

> "Comece devagar, comece enviando para 10, 20 pessoas por dia com um timer ali, com uma diferença de tempo, de minutos. Porque se você usar isso daqui, o S-Zap, que é a ferramenta de disparo, e você enviar para muitas empresas de uma vez, vai cair o seu WhatsApp." **[00:59]**

Estabelece a regra operacional mais importante da ferramenta antes de qualquer explicação técnica: volume controlado é condição de sobrevivência do número, não uma sugestão opcional.

> "Testa diferentes abordagens, mandando oi, mandando... Quer ver? Eu vou até mostrar para você." **[02:17]**

Marca a transição da aula: de "isso aqui é para você chegar nesses leads" para o ensino do script de abordagem, deixando claro que a captação de leads (scraper) é só metade do trabalho, a outra metade é a mensagem em si.

> "Manda para 50 pessoas um script de um jeito. Depois muda a abertura. Depois muda tudo. Tenta textos maiores, textos menores. Tenta curiosidade. É teste. Não adianta." **[04:35]**

Reforça a tese central de que não existe script definitivo, o resultado vem de iteração (teste A/B manual) e não de copiar uma fórmula pronta.

> "Já teve pessoas aqui dentro da comunidade. Eu mandei, acho que menos de 10 pessoas usou isso daqui. [...] Já teve um moleque que mandou no grupo. Que já pegou dois clientes utilizando isso daqui. Em menos de, sei lá, em menos de 3 dias." **[04:35]**

Prova social usada para sustentar a promessa de resultado rápido; o "moleque" é depois identificado como o próprio Eric, que criará as próximas aulas do módulo.

> "Não adianta. Quem trabalha mais. Ganha mais dinheiro. [...] Hoje é jogo do Brasil. E eu vou estar aqui trabalhando." **[05:52]**

Fechamento motivacional que amarra o uso da ferramenta a um discurso de sacrifício/disciplina, coerente com o tom de outras aulas de abertura do curso (ex.: "Obrigado...", camada ouro já registrada).

## Conexões com as próximas 2 aulas do módulo

1. **"Como funciona a ferramenta Kaptar"**: destrincha tecnicamente o scraper de leads anunciado aqui, mostra a configuração da fonte de dados (Google Maps API gratuita com 5 mil requisições/mês, ou OpenStreetMap como alternativa sem cartão de crédito), como rodar buscas por categoria e região, e como gerenciar leads (qualificar, arquivar, limpar). Termina anunciando explicitamente a aula seguinte sobre o S-Zap.
2. **"Como fazer disparos com o S-Zap"**: ensina a parte de disparo mencionada nesta aula introdutória como o componente que "pode derrubar o WhatsApp" se usado sem cautela. Detalha a instalação do servidor local, conexão via QR Code, segmentação de campanhas por filtro de lead, variáveis personalizadas (nome, cidade) e o intervalo recomendado de 45 segundos entre mensagens, com limite seguro de 100 leads/dia, operacionalizando o alerta de risco de bloqueio já dado nesta aula.
