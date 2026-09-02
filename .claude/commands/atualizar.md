---
description: Busca aulas novas do MazyOS na Kirvano e atualiza bronze/prata/ouro, indice, site e o GitHub
---

Atualize a base de conhecimento deste repo com as aulas novas do curso MazyOS. Siga o fluxo abaixo, na ordem. Os caminhos sao relativos a raiz do repo (mazyos-brain).

## 1. Descobrir aulas novas

Rode `bronze/pipeline/.venv/bin/python bronze/pipeline/check_new.py` (crie o venv com websocket-client se nao existir). Ele sobe o Chrome do pipeline (perfil `~/.chrome-edj`, que guarda a sessao logada da Kirvano), abre `https://app.kirvano.com/lessons/<course_uuid>` e compara a lista de aulas com `bronze/catalogo/lessons.json`.

- Exit 0: nada novo. Diga isso ao usuario e pare.
- Exit 2: sessao expirada ou layout mudou. Nao tente logar; peca ao usuario pra fazer login no Chrome do pipeline e pare.
- Exit 1: ha aulas novas. Continue.

## 2. Capturar video_id das aulas novas

Para cada aula nova em video, e preciso do `video_id` da Bunny CDN. Com o Chrome do pipeline aberto na area de membros (via CDP na porta 9222): clique na aula (evento de mouse confiavel via `Input.dispatchMouseEvent`; clicks sinteticos de JS nao funcionam nos accordions) e leia em `performance.getEntriesByType('resource')` a URL `https://<cdn_host>/<video_id>/playlist.m3u8`. O `cdn_host` esta no catalogo.

Adicione as aulas novas em `bronze/catalogo/lessons.json` no modulo certo (crie o modulo `N-slug` se for modulo novo, mantendo a numeracao existente; nunca renumere modulos antigos). Aulas so-texto entram sem `video_id` e nao passam pelo pipeline de audio.

## 3. Pipeline bronze → prata

De dentro de `bronze/pipeline/`:

1. `python3 download.py --module <n>` para cada modulo com aula nova (baixa mp3 via ffmpeg, precisa do header Referer, ja embutido).
2. `python3 transcribe.py --module <n>` (whisper-cli local, modelo em `models/ggml-large-v3-turbo.bin`; ~10-20 min por hora de audio).
3. `python3 gen_prata.py` (gera as notas prata deterministicamente).

## 4. Camada ouro

Para cada aula nova, leia a transcricao prata completa (`prata/<modulo>/<aula>.md`) e escreva a nota ouro em `ouro/aulas/<modulo>/<aula>.md`, no mesmo padrao das notas existentes: frontmatter igual, tese central, frameworks passo a passo, exemplos concretos, numeros, citacoes com contexto e conexoes com outras aulas. Leia 1-2 notas ouro existentes antes, pra manter o padrao. Se houver mais de uma aula nova, use agentes em paralelo (um por aula, cada um lendo a transcricao inteira).

## 5. Indice, README e site

- Atualize `INDICE.md` com as aulas/modulos novos.
- Atualize a tabela de modulos e o Status no `README.md` (contagens de aulas).
- Rode `python3 build_site.py` na raiz.

## 6. Publicar

`git add -A`, commit descrevendo as aulas adicionadas, `git push origin main`. Os mp3 e transcricoes ficam fora do git (gitignore); confira com `git status` que nada pesado entrou.
