# SCT-PREFLIGHT-001 — Semantic Conformance Test

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: autorização da Etapa 3 indicada no README.
Procedimento documental manual; não é código executável nem comprovação de execução.

Registrar repositório, branch, HEAD, momento, executor, universo de arquivos, evidências
e resultado de cada verificação. PASS exige evidência; FAIL indica violação demonstrada;
NOT_VERIFIED indica verificação ausente ou inconclusiva e bloqueia a promoção dependente.

| Verificação | Método e condição para PASS |
| --- | --- |
| Branch fora de main | Consultar branch ativa antes e depois; alteração ocorre somente na branch autorizada. |
| Baseline conhecido | Registrar HEAD e status anteriores; nesta etapa, exigir HEAD 664dd81a521337c49b887b4a30b3fe68736f83d1 e working tree inicialmente limpo. |
| Escopo dos arquivos | Comparar lista real, incluindo não rastreados, com lista autorizada; nenhuma adição inesperada. |
| Segredos conhecidos | Inspecionar todo conteúdo alterado/novo e padrões de credenciais; nenhum achado conhecido, sem expor valores. Não equivale a garantia absoluta. |
| Identidade | Conferir IDs técnicos quando aplicáveis e caminhos documentais; não há aliases ou identidades concorrentes. |
| Estados | Conferir estados com a governança; distinguir marcadores de bootstrap/lacuna de promoção canônica. |
| Proveniência material | Toda afirmação material tem fonte/contexto adequado ou está explicitamente bloqueada por lacuna. |
| Implementação | Nenhuma alegação de implementação real sem evidência vinculada ao alvo e à versão. |
| Verificação | Nenhuma alegação de verificação real sem método, critério, resultado e evidência. |
| Promoção | Nenhuma promoção automática para CURRENT ou aceitação inferida da escrita. |
| P01–P15 | Inspecionar cada princípio e seus reflexos nos contratos, registros e procedimentos. |
| Completude histórica | Nenhuma alegação de recuperação completa sem fechamento verificável do HKR. |

Executar `git status`, `git diff --stat` e `git diff`. Esses diffs não incluem arquivos
não rastreados: enumerá-los e inspecionar seu conteúdo integral sem staging.
Buscar IMPLEMENTED, VERIFIED, CURRENT, COMPLETE, production-ready e operacional;
avaliar contexto, pois definições, proibições e NOT_VERIFIED não são alegações positivas.

Este documento não registra resultados fictícios. A execução deve produzir relatório
na sessão ou em destino posteriormente autorizado. Um working tree modificado ao final
é esperado para este bootstrap sem commit, desde que contenha somente mudanças autorizadas.
