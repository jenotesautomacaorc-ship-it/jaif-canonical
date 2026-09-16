# Política de ingestão

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: autorização da Etapa 3 indicada no README.

Pode entrar conteúdo autorizado, pertinente ao escopo, sanitizado, com origem e
direitos de uso compatíveis: fontes históricas, propostas, contratos e evidências
delimitadas. Não podem entrar segredos, credenciais, dados pessoais desnecessários,
conteúdo sem autorização de uso ou afirmações inventadas apresentadas como fatos.

## Classes e proveniência

- SOURCE: material de origem; preservar autoria/origem, data ou versão, contexto e localização.
- EVIDENCE: registro que sustenta/refuta claim específico; incluir método de obtenção, escopo e limites.
- CANONICAL: conteúdo que passou pelos gates aplicáveis, recebeu decisão competente favorável de aceitação e possui identidade canônica controlada, com versão e estado explícitos. Submissão aos gates não confere essa classificação.

Classe não substitui estado de governança. Uma fonte pode dar origem a evidência sem
se tornar canônica. SOURCE não é CANONICAL; EVIDENCE não é automaticamente CANONICAL.
PROPOSED não é CANONICAL vigente; REJECTED nunca é CANONICAL vigente. ACCEPTED registra
a aceitação; CURRENT exige também vigência autorizada pela autoridade humana competente.
Aprovação isolada não confere CURRENT. SUPERSEDED preserva identidade e histórico
canônico de conteúdo anteriormente vigente. Aplicam-se os nove estados da governança,
sem nova máquina de estados. Sem evidência ou autoridade suficientes, bloquear promoção.
Registrar quem recuperou, transformações/redações e vínculo ao
original permitido, sem copiar segredos. Proveniência desconhecida deve ser marcada
RECOVERY_REQUIRED e impede promoção material; evidência não validada é NOT_VERIFIED.

## Tratamento por origem

| Origem | Tratamento |
| --- | --- |
| Benchmark | Referência comparativa externa, com versão, condições e limitações; não prova arquitetura ou desempenho da JAIF. |
| Documentação externa | Fonte sobre o produto/versão descritos; não demonstra implementação local. |
| Conversa histórica | Recuperar participantes/autoridade, data e contexto, distinguindo discussão, proposta e decisão. |
| Arquivo enviado | Registrar origem, versão, contexto de envio e sanitização; envio não equivale a aprovação do conteúdo. |
| Memória/inferência de IA | Pode orientar busca ou hipótese explicitamente identificada; não basta como fonte canônica. |

Buscar conflitos, supersession, duplicações e omissões antes de reconciliar candidatos.
Não criar IDs concorrentes, domínios ou ativos por conveniência. O ASSET-REGISTRY registra
somente BOOTSTRAP-AUTHORIZATION-001; o HKR-INVENTORY permanece somente com cabeçalho.
Esse registro de autorização não equivale à fonte histórica recuperada nem representa
inventário completo; a recuperação da fonte permanece RECOVERY_REQUIRED / NOT_VERIFIED.
É proibida promoção automática por ingestão, resumo, formatação, teste ou presença em `main`.
Aplicar o gate HKR e obter decisão humana quando exigida para promoção.
