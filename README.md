# MazyOS Brain — Base de Conhecimento (Arquitetura Medalhão)

Todo o conteúdo em vídeo do curso [MazyOS](https://app.kirvano.com) (23 aulas, ~10h) extraído, transcrito e organizado em três camadas, da mais crua à mais inteligente. Abra esta pasta como vault no Obsidian para navegar com links e busca.

MazyOS é um sistema de trabalho (skills + memória de projeto) que roda em cima do Claude Code para criar sites, carrosséis, propostas e automatizar prospecção/vendas para clientes de agência e serviços digitais.

## As três camadas

```
bronze/   dado cru e reproduzível
prata/    transcrição integral, legível e navegável
ouro/     conhecimento destilado (a camada de inteligência)
```

### 🥉 Bronze: o dado cru

- `bronze/<modulo>/audio/*.mp3`: áudio extraído do player (Bunny Stream / Kirvano) via ffmpeg.
- `bronze/<modulo>/transcripts/*.json`: saída bruta do whisper.cpp (`ggml-large-v3-turbo`, local, pt), com texto e segmentos com timestamp.
- `bronze/catalogo/lessons.json`: catálogo das aulas (módulo, título, video_id no Bunny CDN).
- `bronze/pipeline/`: scripts de extração (`download.py` baixa o áudio via ffmpeg com o header `Referer` exigido pela Bunny CDN; `transcribe.py` transcreve localmente com `whisper-cli`; `gen_prata.py` gera a camada prata). Requer o modelo `bronze/pipeline/models/ggml-large-v3-turbo.bin` (baixado do Hugging Face) e o binário `whisper-cli` (`brew install whisper-cpp`).

Diferente do pipeline original (que usava a API paga da OpenAI), aqui a transcrição roda 100% local via whisper.cpp com aceleração Metal — sem custo de API e sem enviar áudio pra fora da máquina.

### 🥈 Prata: a transcrição legível

Um markdown por aula em `prata/<modulo>/`, com:

- Frontmatter: título, curso, módulo, video_id, duração, ponteiro pro bronze
- Transcrição **integral e fiel ao áudio**, sem cortes, em blocos de ~75 segundos com timestamp

É a fonte da verdade legível: quem quiser conferir exatamente o que foi dito, vem aqui.

### 🥇 Ouro: o conhecimento destilado

- `ouro/aulas/<modulo>/`: uma nota estruturada por aula, processada com leitura completa da transcrição: tese central, frameworks passo a passo, exemplos concretos, números, citações com contexto e conexões com outras aulas. Não é resumo genérico de IA.

**Navegação: comece pelo [[INDICE]]** na raiz do vault.

## Estrutura de módulos (espelho da Kirvano)

| Pasta | Módulo na Kirvano | Aulas |
|---|---|---|
| `0-introducao` | Introdução (opcional) | 1 |
| `1-lets-go` | LETS GO! Tudo na prática | 8 |
| `2-kaptar` | KAPTAR: seus clientes no automático | 3 |
| `3-importante` | IMPORTANTE: detalhes que você tem que se atentar | 1 (+2 aulas em texto, sem vídeo) |
| `4-como-vender-infoprodutos` | Como vender infoprodutos com o MazyOS | 1 |
| `5-calls-gravadas` | Calls gravadas (ouro escondido) | 6 |
| `6-extras` | EXTRAS | 3 (+1 aula em texto, sem vídeo) |

23 aulas em vídeo no total. 3 aulas do curso são só texto (sem vídeo) e por isso não têm bronze/prata/ouro: "FAQ com as Dúvidas Frequentes", "MazyOS com Antigravity de Graça!" e "Pegue seu cargo de MazyOS Member no Discord".

## Status

| Camada | Estado |
|---|---|
| Bronze | ✅ 23 áudios baixados, 23 transcrições locais |
| Prata | ✅ 23 notas |
| Ouro por aula | ✅ 23/23 notas (paridade 1:1 com a prata) |
| Índice mestre | ✅ INDICE.md |

## Como foi feito

1. **Descoberta**: navegação manual pela Kirvano (via Claude in Chrome) pra mapear módulos, aulas e os `video_id` da Bunny CDN de cada uma, salvos em `bronze/catalogo/lessons.json`.
2. **Download**: `bronze/pipeline/download.py` monta a URL HLS (`https://<cdn_host>/<video_id>/playlist.m3u8`) e baixa o áudio com ffmpeg, passando o header `Referer: https://app.kirvano.com/` exigido pela proteção de hotlink da Bunny.
3. **Transcrição**: `bronze/pipeline/transcribe.py` roda `whisper-cli` localmente (modelo `ggml-large-v3-turbo`, português, aceleração Metal) sobre cada áudio.
4. **Prata**: geração determinística a partir dos JSONs (`bronze/pipeline/gen_prata.py`).
5. **Ouro**: leitura e destilação aula a aula com agentes de IA em paralelo, cada um lendo a transcrição completa da sua aula e escrevendo a nota estruturada.
