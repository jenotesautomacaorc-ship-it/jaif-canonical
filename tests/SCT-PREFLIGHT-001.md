# SCT-PREFLIGHT-001 — Semantic Conformance Test

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: autorização da Etapa 3 indicada no README.
Procedimento documental manual; não é código executável nem comprovação de execução.

Registrar repositório, branch, HEAD, momento, executor, universo de arquivos, evidências
e resultado de cada verificação. PASS exige evidência; FAIL indica violação demonstrada;
NOT_VERIFIED indica verificação ausente ou inconclusiva e bloqueia a promoção dependente.

## Aplicabilidade histórica e lotes posteriores

O SHA fixo e as expectativas de estado final de Foundation Bootstrap V0.1
permanecem requisitos históricos daquela execução. Não são baselines universais
para toda mudança posterior da JAIF. Cada lote controlado posterior deve declarar
seu SHA base esperado e o estado final esperado do repositório em seu registro
delimitado de mudança/evidência. A evidência histórica do bootstrap não é reescrita
retroativamente. As condições específicas da Etapa 3 abaixo permanecem preservadas.

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

## Governance M1/M2 — adversarial fixtures

Estes são casos de preflight documental/semântico. Materializar a definição de
um teste não comprova sua execução. Os valores de Test_ID identificam casos
internos deste SCT; não criam objetos canônicos de negócio, estados, owners ou
domínios. Aplicam-se os requisitos de registro de execução e evidência acima.
As regras de referência são os contratos CANONICAL-GOVERNANCE e HKR-NON-OMISSION-GATE;
esta tabela operacionaliza sua verificação sem substituí-los.

| Test_ID | Caso | Cenário / controle existente | Condição para PASS |
| --- | --- | --- | --- |
| M1-T01 | NEWEST_IS_NOT_CURRENT | A v1.0 é ACCEPTED/CURRENT; B v1.1 é mais nova, mas apenas PROPOSED. | B permanece NOT CURRENT. Recência ou versão, isoladamente, não concede CURRENT. |
| M1-T02 | DOMAIN_CURRENT_IS_NOT_GOVERNANCE_CURRENT | Uma configuração de domínio está operacionalmente/efetivamente vigente. | O documento/view que a representa não recebe automaticamente CURRENT de governança. |
| M1-T03 | DISCOVERED_SUBJECT_IS_EXPLICIT | A fonte histórica F foi localizada e o registro R referencia F. | DISCOVERED atribuído a F não classifica silenciosamente R, claim, evidência ou artefato candidato como aquela fonte histórica. |
| M1-T04 | LATEST_WINS_PROHIBITED | Duas versões estão em conflito. | Timestamp/versão mais recente, isoladamente, não determina autoridade, precedência, resolução do conflito ou CURRENT. |
| M2-T01 | INVENTORY_IS_NOT_CLOSURE | Uma fonte possui linha completamente preenchida no HKR-INVENTORY. | A linha, isoladamente, não comprova conclusão da cadeia HKR nem CLOSURE. |
| M2-T02 | STATUS_IS_NOT_EVENT | Um campo *_status aparenta resultado positivo. | O valor não substitui o registro material de decisão/evento, autoridade competente, escopo, execução ou evidência de verificação, quando aplicáveis. |
| M2-T03 | DOCUMENT_IS_NOT_IMPLEMENTATION | EXISTING_EQUIVALENT: controles “Implementação” e “Verificação” da tabela original são os requisitos regentes. Aplicá-los ao documento que afirma implementação e à evidência apresentada. | PASS exige satisfazer ambos os controles existentes: a declaração documental não prova implementação no alvo, e evidência de implementação não prova verificação. Este mapeamento não institui requisito normativo duplicado. |
| M2-T04 | MISSING_LINK_FAILS_CLOSED | Um claim material carece de Evidence, binding de Owner/autoridade ou Decision exigidos e aplicáveis. | Promoção/closure dependentes permanecem bloqueados. Nenhum elo ausente recebe PASS por inferência. |
| M2-T05 | NO_SCHEMA_PROLIFERATION | Uma clarificação de governança/HKR é proposta. | Não se cria registry, schema, owner, domínio, engine, estado ou coluna CSV sem evidência de necessidade irredutível. Este teste não autoriza criação: as restrições do lote continuam obrigatórias; a Phase 7B não permite nenhuma dessas criações. |
