---
titulo: "SE SEU MAZYOS ESTA SEM SKILL ASSISTA"
curso: MazyOS
modulo: "IMPORTANTE: detalhes que você tem que se atentar"
camada: ouro
fonte_prata: prata/3-importante/SE SEU MAZYOS ESTA SEM SKILL ASSISTA.md
tags: [mazyos, troubleshooting, instalacao, skills, claude-code, estrutura-de-pastas]
---

# SE SEU MAZYOS ESTA SEM SKILL ASSISTA

## Tese central

Quando uma skill do MazyOS (ex.: `/atualizar`, `/carrossel`) não aparece ou não funciona, a causa quase sempre é estrutural, não uma falha da IA: a pasta MazyOS foi deixada **dentro** de outra pasta (ex. `Davidson/MazyOS` ou `LP Store/MazyOS`) em vez de ser aberta como a pasta raiz/principal do projeto na IDE. Como o Claude lê o `CLAUDE.md` (que ele chama de "cloud.md") a partir da pasta que está aberta, se essa pasta não for a própria MazyOS, o Claude Code está rodando "puro", sem nunca carregar as regras, memórias e skills do MazyOS, mesmo elas existindo fisicamente no disco.

## Diagnóstico: como identificar o problema

- Sintoma: `/atualizar` ou qualquer outra skill "não aparece, não está conseguindo".
- Causa raiz: a pasta que está aberta na IDE (Cursor/VS Code) não é a pasta MazyOS em si, e sim uma pasta-mãe que contém a pasta MazyOS dentro dela.
- Caso 1 (Davidson): estrutura era `Davidson/ → Masios/` (a pasta principal aberta era "Davidson", com "Masios" apenas como subpasta).
- Caso 2 (grupo de suporte): estrutura era `LP Store/ → Masios/` (mesmo problema, outro nome de pasta-mãe).
- Verificação: durante a própria instalação do MazyOS, em algum momento ele pergunta sobre isso ("chega uma hora que ele mesmo fala para você isso") — se você respondeu para achatar/tornar principal, provavelmente já está correto; se não lembra de ter respondido isso, vale checar a estrutura de pastas manualmente.

## Solução: passo a passo exato

Duas maneiras de corrigir, conforme citado na aula:

1. **Pedir para o próprio Claude resolver**: "você ou pede para o próprio Cloud transformar o Masios na sua pasta principal" — comando direto ao Claude para promover a pasta MazyOS a pasta raiz.
2. **Fazer manualmente quando já existem outros arquivos na pasta-mãe**:
   - Mover (jogar) todos os arquivos que estão fora da pasta MazyOS para **dentro** da pasta MazyOS.
   - Abrir a pasta MazyOS diretamente na IDE (não mais a pasta-mãe).
   - Opcional, por último: renomear a pasta MazyOS para o nome do seu projeto/cliente (ex. de "Masios" para "StarCard").

Exemplo aplicado (caso do grupo de suporte, `LP Store/Masios`): "ele jogou tudo para dentro da pasta (...) ele copiou tudo aqui e jogou dentro da pasta LP Store e pronto. Na verdade, ele tornou a pasta Masios a pasta principal dele e aqui resolveu." Resultado: agora ele abre a pasta MazyOS direto, e nela estão `memória`, `cloud`, e as outras pastas que ele tinha criado antes (ex. "marcas que trabalham").

Checklist de validação pós-correção:
- A pasta aberta na IDE deve conter diretamente `memória`, `cloud`, `dados`, `identidade`, `marketing` etc. (as pastas internas do MazyOS), e não estar um nível acima delas.
- Depois de corrigido, testar novamente a skill (`/atualizar` ou outra) — "agora, quando ele tentar usar alguma skill, ele vai conseguir usar."

## Citações relevantes com contexto

> "Se você está tentando usar skill barra atualizar ou qualquer outra skill e não está conseguindo, não aparece, é porque você não tornou o Masios a sua pasta principal." **[00:00]**
Contexto: abertura da aula, definição do sintoma e da causa raiz em uma frase.

> "Você ou pede para o próprio Cloud transformar o Masios na sua pasta principal, ou se já é alguma pasta que você já tem outros arquivos, você joga todos esses arquivos para dentro da pasta Masios e depois transforma essa pasta Masios como sua pasta principal e já abre direto ela. Depois você pode só renomear a pasta Masios." **[00:00]**
Contexto: enumeração das duas rotas de correção (pedir ao Claude vs. mover arquivos manualmente), seguida do passo final opcional de renomear.

> "Sempre que você pedir um prompt ou tentar usar uma skill, ele vai achar, porque ele vai ler o seu cloud.md dentro da pasta Masios." **[01:19]**
Contexto: explica o mecanismo técnico por trás do problema — o Claude só carrega o `CLAUDE.md` (que ele fala como "cloud.md") se a pasta MazyOS for a raiz aberta.

> "Você percebe que ele estava abrindo a pasta LP Store e dentro da pasta LP Store tem a pasta Masios. Está errado." **[01:59]**
Contexto: segundo exemplo real de aluno com o mesmo erro estrutural, usado para reforçar o diagnóstico.

> "Na verdade, ele tornou a pasta Masios a pasta principal dele e aqui resolveu. (...) Isso é muito importante você entender que, se não, você vai estar usando o cloud normal ao invés de estar usando o cloud com Masios. Você vai estar usando o cloud code achando que está usando o Masios e está usando da maneira errada." **[01:59]**
Contexto: consequência do erro não corrigido — o aluno segue conversando com o Claude Code "puro" (sem MazyOS) sem perceber, achando que está usando o sistema completo.

> "Você não está usando o Masios. O Masios é uma série de regras, skills e configurações que fazem tudo isso, que organizam. Então, você roda ali barra instalada, ele vai te entrevistar, vai fazer perguntas sobre..." **[03:15]**
Contexto: reforço conceitual do que é o MazyOS (regras + skills + configurações) e lembrete de que a instalação correta passa pela skill de entrevista (`/instalar`).

## Conexões com a aula de instalação

Esta aula de troubleshooting é a continuação direta de um ponto levantado ao final de **ACESSO AO MAZYOS + INSTALAÇÃO**: durante a instalação, depois que o Claude cria a pasta do projeto, ele pergunta explicitamente sobre a estrutura de pastas — no exemplo do StarCard: "O MasiOS está dentro da pasta StarCard. Deixar como está, funciona. Só ignora o nome. Ou achatar." **[17:15]**. Vagner responde escolhendo achatar ("Eu prefiro achatar (...) Quero uma pasta só chamada StarCard com tudo do MasiOS dentro"), que é exatamente o resultado final que esta aula de troubleshooting ensina a alcançar manualmente para quem pulou ou errou essa etapa.

Ou seja:
- Na instalação, essa decisão (achatar/tornar a pasta MazyOS principal) é feita **de forma guiada**, dentro do próprio fluxo de instalação.
- Nesta aula, o mesmo resultado é alcançado **corretivamente**, depois que o aluno já instalou errado e só percebeu o problema quando uma skill falhou.
- O fio condutor entre as duas aulas é o mesmo princípio técnico citado em ambas: o Claude só enxerga as regras/skills do MazyOS se a pasta MazyOS (com `memória`, `cloud` etc.) for a pasta raiz aberta na IDE — nunca uma subpasta dentro de outra pasta de projeto.
