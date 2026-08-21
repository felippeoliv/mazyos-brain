---
titulo: "PREPARANDO O TERRENO PARA O MAZYOS"
curso: MazyOS
modulo: LETS GO! Tudo na prática
modulo_slug: 1-lets-go
camada: ouro
fonte_prata: prata/1-lets-go/PREPARANDO O TERRENO PARA O MAZYOS.md
tags: [mazyos, setup, vscode, cloud-code, whisper-flow, ambiente]
---

# PREPARANDO O TERRENO PARA O MAZYOS

> [!info] Camada ouro: conhecimento destilado a partir da transcrição em prata/1-lets-go/PREPARANDO O TERRENO PARA O MAZYOS.md

## Tese central

Antes de instalar o MazyOS, existe um "terreno" fixo e obrigatório: VS Code + extensão Cloud Code (Claude Code) conectada a um plano pago da Anthropic. Tudo o resto (tema, ícones, ditado por voz) é estético ou opcional. Vagner é explícito sobre o que é essencial versus o que é gosto pessoal: "A gente precisa do VS Code e... o que mais a gente pensar? Mais nada." A aula é curta (07:31) de propósito, ela existe para eliminar qualquer dúvida de setup antes da aula de instalação propriamente dita, e serve também como filtro de entrada: quem não consegue seguir este passo a passo básico não está pronto para o restante do curso ("se você caiu de paraquedas e não sabe nada disso, só segue o passo a passo").

## Framework / passo a passo (ordem exata mencionada na aula)

1. **Baixar o VS Code** — pesquisar "Download VS Code" no Google, clicar no primeiro resultado (é da Microsoft), baixar a versão do seu sistema (Windows/Linux/Mac). Instalação padrão: "só clicar em avançar aqui, avançar, avançar, instalar."
2. **Escolher o editor de IA a conectar** — o curso usa Claude Code, mas Vagner reconhece alternativas: "Você pode conectar com o Codex, com Antigravity, cursor, aí você escolhe." Recomendação dele é Claude Code, mas deixa livre.
3. **Fazer login no VS Code** — via GitHub ou Google (ele usou Google, recebeu código no Gmail).
4. **Escolher o tema visual** — etapa cosmética, "Tanto faz."
5. **Instalar extensões** (aba Extensões do VS Code), na ordem em que ele baixou:
   - **Dracula** — tema de cores do código, puramente estético.
   - **Cloud Code (Claude Code)** — a extensão principal e obrigatória: "Muito importante. Você precisa do Cloud Code." Ele remete a um vídeo anterior no YouTube explicando Claude Code do zero para quem nunca usou.
   - **Material Icon Theme** — ícones de pasta, também estético ("fica com as pastinhas bem bonitinhas").
6. **(Opcional) Instalar o Whisper Flow** — ferramenta de ditado por voz para gravar prompts. Ele explica o motivo de usar: dá para gravar o áudio do prompt enquanto navega em outras abas, e o resultado sai "enxuto" (economiza token) e "categorizado". É paga, mas tem trial: "acho que uns 15 dias de batas aí." Há um vídeo extra só sobre o Whisper Flow na seção Extras do curso.
7. **Conectar a conta do Claude Code dentro do VS Code** — abrir a extensão Cloud Code, clicar em "Open", autorizar a conexão (fluxo OAuth no navegador), confirmar.
8. **Escolher e contratar um plano da Anthropic**, pois o plano gratuito não dá acesso ao Claude Code:
   - **Plano Free**: sem acesso ao Claude Code.
   - **Plano Pro**: ~US$ 20/mês, dá acesso ao Claude Code. Recomendado para quem está começando.
   - **Plano Max**: ~R$ 500/mês, usado pelo próprio Vagner. Mais poderoso, limites duram muito mais, permite atender todos os clientes dele só com esse plano.
9. **Abrir a pasta do projeto** — "Open Folder", selecionar o diretório do cliente/projeto em que vai trabalhar (ele usa como exemplo o projeto "Tubalir").

Ao final desses passos o ambiente de trabalho está pronto: VS Code + Claude Code conectado, aguardando a instalação do MazyOS propriamente dito.

## Exemplos concretos e números citados

- **Duração da aula**: 07:31.
- **Preço do plano Pro**: "20 dólares por mês", convertido por ele para "cerca de cento e poucos reais".
- **Preço do plano Max**: "uns 500 reais por mês" — o que ele mesmo usa hoje para atender todos os clientes.
- **Trial do Whisper Flow**: "acho que uns 15 dias de batas aí" (grátis antes de cobrar).
- **Extensões instaladas, em ordem**: Dracula (tema), Cloud Code / Claude Code (obrigatória), Material Icon Theme (ícones).
- **Projeto de exemplo usado para testar o "Open Folder"**: cliente chamado "Tubalir".
- **Preparação prévia do computador**: ele formatou a máquina e só tinha instalado "papel de parede" (wallpaper), Discord e Loom (ferramenta usada para gravar as próprias aulas) antes de começar o setup do MazyOS — ou seja, o setup descrito parte de uma máquina praticamente limpa.

## Citações relevantes com contexto

> "A gente precisa do VS Code e... o que mais a gente pensar? Mais nada." [00:39]
Contexto: resposta direta à pergunta implícita "o que é realmente necessário". Reforça que tudo depois disso (tema, ícones) é opcional.

> "No caso aqui, eu prefiro esse daqui, que é o Visual Studio, mas você usa o que você preferir. Se quiser seguir a minha recomendação, siga." [00:39]
Contexto: ao escolher entre Claude Code, Codex, Antigravity e Cursor, ele deixa claro que o curso não impõe ferramenta, apenas recomenda a que ele usa.

> "Muito importante. Você precisa do Cloud Code." [02:10]
Contexto: única extensão, entre as quatro instaladas na aula, que ele marca explicitamente como não-opcional (Dracula e Material Icon Theme são estética; Whisper Flow é declarado opcional à parte).

> "Eu prefiro ele porque você consegue gravar o áudio ali, o prompt. Enquanto você está navegando em outras abas. Você consegue enxugar seu prompt para economizar mais token." [04:01]
Contexto: justificativa de uso do Whisper Flow. Note a lógica de custo: prompts mais "enxutos" e organizados por voz economizam tokens no Claude Code, ligando uma ferramenta de terceiros diretamente ao custo operacional do MazyOS.

> "Hoje eu utilizo esse plano Max, que é uns 500 reais por mês, tá? Mas ele é muito mais poderoso que esse plano Pro. Dura muito mais. Eu consigo cuidar de todos os meus clientes só com ele." [05:27]
Contexto: ele descreve a própria trajetória de upgrade (começou no Pro, foi para o Max conforme ganhou clientes), e recomenda o mesmo caminho: "Se você está começando, começa pelo Pro (...) Quando começar a chegar muito rápido no limite dele, aí você vai para o Max."

> "E se você caiu de paraquedas e não sabe nada disso, só segue o passo a passo. Instala o VS Code, pega um plano no Cloud Code, conecta ali." [06:38]
Contexto: fechamento da aula, resumindo o mínimo indispensável em três verbos (instalar, pegar plano, conectar) para quem é totalmente iniciante.

## Conexões com outras aulas

- Esta é a primeira aula do módulo "LETS GO! Tudo na prática" (módulo 1), focada exclusivamente em preparar o ambiente (VS Code + Claude Code + extensões) antes de qualquer instalação do produto.
- **A próxima aula do módulo ensina a instalar o MazyOS propriamente dito** — o próprio Vagner fecha a aula direcionando para ela: "você vai ter bonitinho aqui para você ir para a próxima aula que é ensinando a instalar o MasiOS."
- Referência cruzada externa: ele cita um vídeo seu no YouTube que explica o Claude Code "do zero", recomendado para quem nunca usou a ferramenta antes de prosseguir no curso.
- Referência cruzada interna: existe um vídeo na seção "Extras" do curso dedicado só ao Whisper Flow, para quem quiser detalhes sobre a ferramenta de ditado opcional.
- O tema de planos (Free/Pro/Max da Anthropic) introduzido aqui provavelmente reaparece em aulas futuras sobre custo operacional/precificação de serviços para clientes, já que ele liga diretamente o plano escolhido à capacidade de atender múltiplos clientes.
