# Observabilidade e lineage

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: cadeia autorizada na Etapa 3.

**sensor → state → history → context → anomaly → decision → action → evidence**.

| Elo | Vínculo estrutural necessário |
| --- | --- |
| sensor | Origem do sinal e identificação da captura. |
| state | Estado derivado, com referência ao sinal e transformação. |
| history | Sequência temporal e versões dos estados, preservando origem. |
| context | Contexto utilizado, proveniência e limites. |
| anomaly | Desvio identificado, critério e dados que sustentam a interpretação. |
| decision | Autoridade, justificativa e referências à anomalia e ao contexto. |
| action | Ação autorizada, alvo e registro da execução efetiva. |
| evidence | Registro que permite verificar a execução e suas consequências delimitadas. |

Preservar identidade, ordem temporal, referências entre elos e transformações.
Lacunas e eventos ausentes devem ser explícitos; uma decisão não prova que houve ação.
Correlacionar contribuição de IA com decisão e execução conforme o gate AI→Execution Lineage.

Lineage permite reconstruir o caminho; verificação compara esse caminho e o resultado
com critérios explícitos. Ter uma cadeia documentada não comprova correção do resultado.
Dashboards, renders e diagramas são representações, não prova automática de estado real.

Sensores, armazenamento, mecanismos, owners e critérios históricos: RECOVERY_REQUIRED.
Implementação e funcionamento da cadeia: NOT_VERIFIED. Não se define esquema físico aqui.
