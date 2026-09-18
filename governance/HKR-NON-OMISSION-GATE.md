# HKR — gate de não omissão

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: autorização da Etapa 3 indicada no README.
Historical Knowledge Recovery ainda requer fontes históricas: RECOVERY_REQUIRED.

## Cadeia obrigatória

**SOURCE → CLAIM → EVIDENCE → PROVENANCE → INTERPRETATION → MATERIALITY → OWNER →
DELTA → DECISION → TARGET → IMPLEMENTATION → VERIFICATION → CLOSURE**.

| Elo | Registro necessário |
| --- | --- |
| SOURCE | Identificador, origem, versão/data e localização recuperável da fonte. |
| CLAIM | Afirmação delimitada, separada de opinião ou hipótese. |
| EVIDENCE | Evidência que sustenta/refuta a afirmação e seus limites. |
| PROVENANCE | Autor/origem, contexto, cadeia de obtenção e transformações. |
| INTERPRETATION | Leitura proposta e alternativas, sem convertê-las em fatos. |
| MATERIALITY | Impacto semântico, técnico ou de governança e justificativa. |
| OWNER | Responsável e autoridade sobre o assunto; desconhecidos bloqueiam promoção. |
| DELTA | Diferença contra baseline identificado, inclusive inclusões e remoções. |
| DECISION | Decisão humana, autoridade, data, escopo e condições. |
| TARGET | Artefato/versão ou alvo da mudança com identidade única. |
| IMPLEMENTATION | O que foi efetivamente alterado, onde e sob qual autorização. |
| VERIFICATION | Critérios, método, evidência, resultado, executor e limitações. |
| CLOSURE | Reconciliação dos elos e disposição verificável das pendências. |

### Persistência e vínculo da cadeia HKR

`HKR-INVENTORY.csv` é um índice controlado de fontes históricas, contexto de
recuperação e estado de tratamento da fonte.

Uma linha em `HKR-INVENTORY.csv` NÃO constitui, isoladamente, evidência de que
a cadeia HKR foi completada.

Em particular, uma linha de inventário NÃO prova por si só:

- que todos os claims materiais da fonte foram extraídos;
- que evidência suficiente foi avaliada;
- que a proveniência foi considerada adequada para o claim;
- que a interpretação foi reconciliada;
- que materialidade e owner foram confirmados;
- que um delta foi aprovado;
- que uma decisão competente ocorreu;
- que o target foi alterado;
- que a implementação ocorreu;
- que a implementação foi verificada;
- que o conhecimento foi encerrado sem dívida residual.

A cadeia obrigatória

SOURCE → CLAIM → EVIDENCE → PROVENANCE → INTERPRETATION → MATERIALITY →
OWNER → DELTA → DECISION → TARGET → IMPLEMENTATION → VERIFICATION → CLOSURE

DEVE permanecer reconstruível por referências controladas entre a fonte
inventariada e os registros ou artefatos aplicáveis.

Um elo pode ser marcado como não aplicável somente quando sua inaplicabilidade
for explicitamente justificada no contexto do claim e revisada conforme a
governança aplicável.

Nenhum campo `*_status` do inventário pode substituir o registro material do
evento, decisão, execução ou verificação a que se refere.

Esta regra NÃO cria novo domínio, registry, owner, engine ou fonte de verdade.
Também NÃO exige adicionar novas colunas ao `HKR-INVENTORY.csv`.

## Execução do gate

Inventariar fontes em `registry/HKR-INVENTORY.csv`, mantendo vínculos para registros
complementares quando necessários. O cabeçalho não contém toda a cadeia e seu simples
preenchimento não fecha o gate. Novos arquivos exigem escopo autorizado próprio.

Para cada candidato, buscar explicitamente conflitos, supersession, duplicações,
aliases e omissões. Registrar universo consultado, estratégia de busca, resultados
positivos e negativos, fontes inacessíveis e lacunas. “Não encontrado” não prova inexistência.
Comparar fontes entre si e com a versão aceita, se houver, sem eleger a mais recente
como autoridade automaticamente. Encaminhar divergências materiais à decisão humana.

Detalhe histórico ausente: RECOVERY_REQUIRED. Afirmação sem verificação: NOT_VERIFIED.
Elo inaplicável exige justificativa revisada; não pode ser omitido silenciosamente.
Ausência de dados, autoridade ou evidência necessária bloqueia o fechamento.

Só declarar recuperação completa após delimitar o universo histórico, reconciliar
todas as fontes e candidatos, resolver conflitos e omissões, registrar disposições
e obter revisão humana do fechamento verificável. Fontes ainda indisponíveis impedem
declaração de completude sobre seu conteúdo. Este bootstrap não executou esse processo.
