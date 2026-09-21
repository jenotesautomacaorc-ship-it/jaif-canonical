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

## Admissibilidade no HKR-INVENTORY e referências complementares

Clarificação proposta neste CHANGE, vinculada à [evidência da análise](../evidence/HKR-INVENTORY-ENCODING-CHANGE.md).
Não concede ACCEPTED ou CURRENT nem autoriza ingestão por si só.

1. **Row admission.** HKR-INVENTORY é índice de fontes históricas, não backlog
   genérico de assuntos ou knowledge debt. Cada linha representa uma fonte
   histórica suficientemente identificada para ser distinguida de outras fontes.
   Subject conhecido, memória de existência, documento contemporâneo semelhante,
   recovery disposition, successor candidate ou evidência de ausência não bastam.
2. **Source identity.** source_id identifica a fonte inventariada segundo política
   de identidade controlada. Historical object/subject ≠ identified source instance.
   Enquanto a identidade distintiva não estiver sustentada, não inventar source_id.
   Não usar como substitutos por conveniência: nome de assunto, ID de sucessor,
   canonical_id, nome/locator de arquivo evidence, disposition id, RECOVERY_REQUIRED,
   PERMANENTLY_UNAVAILABLE ou hash arbitrário sem política aprovada. Esta seção não
   define algoritmo de geração de IDs nem atribui identificadores.
3. **Objeto histórico não identificado como fonte.** Quando existe evidência de
   objeto histórico, mas não de fonte histórica identificável, manter o objeto em
   registro complementar de evidência/recovery autorizado. Não criar linha artificial
   nem transformar esse evidence record na fonte histórica que falta. Isso não
   significa inexistência, rejeição, recuperação, supersession ou closure.
4. **Referência complementar.** provenance pode referenciar registro complementar
   SOMENTE quando o conteúdo referido for provenance da fonte/claim: autor/origem,
   contexto, cadeia de obtenção, transformações e locators/evidence pertinentes.
   PROVENANCE != GENERIC LINK BAG. Decision, authority, conflict, recovery disposition
   e candidate relationship não são codificados em provenance por falta de coluna;
   permanecem em registros complementares semanticamente próprios.
   Para linha válida e source_id sustentado, o registro complementar pode referenciar
   a source instance pelo source_id. A reconstruibilidade HKR pode usar esse sentido
   de referência, desde que inequívoco, recuperável e auditável. Não duplicar a ligação
   artificialmente no CSV se nenhum campo tiver semântica compatível.
   Usar locator estável disponível
   e recuperável, preferencialmente caminho relativo à raiz do repositório para
   artefato interno; identificar seção e versão/commit quando necessários para
   distinguir o registro referido. Não fabricar locator ausente: NOT_VERIFIED.
   A referência deve explicitar sua relação com a fonte e o claim; lacuna material
   bloqueia o uso dependente. Não confere autoridade/status nem substitui identidade
   da fonte, decisão, autoridade, recovery event ou verification. A cadeia HKR
   integral permanece exigida; o link não prova sua conclusão. Complementary record
   != provenance field. Não cria generic reference field, coluna, registry,
   identidade ou máquina de estados.
5. **candidate_artifact.** Indica somente artefato candidato relacionado à análise.
   Não é source_id, confirmação de sucessão, identidade canônica nem prova de
   equivalência histórica. SOURCE ≠ SUCCESSOR.
6. **Campos de status.** conflict_status, recovery_status, decision_status,
   implementation_status e verification_status são índices/resumos, nunca
   substitutos dos registros materiais dos eventos aplicáveis. PERMANENTLY UNAVAILABLE
   é disposição de recuperação, não source_id, governance state ou recovery_status
   automático; não introduzir silenciosamente esse valor nesta mudança.
   RECOVERY_REQUIRED e NOT_VERIFIED continuam marcadores, não identidades ou estados.
7. **Consequência para a Wave 01.** AIF/EVAL histórico original, JAIF-VIC-001
   histórico original e Automation Execution & Observability histórico original
   continuam sem identidade de fonte suficientemente recuperada. Não criar linhas
   nesta mudança. Preservar os registros evidence existentes e RECOVERY_REQUIRED /
   NOT_VERIFIED aplicáveis. Fonte autorizada identificável que surgir exigirá gate
   próprio, identidade sustentada e referências à evidência existente; não ingestão
   automática. A exclusão de linha sem identidade não autoriza omitir a dívida.
8. **Sem alteração de schema.** O schema atual NÃO é alterado neste CHANGE.
   A resolução proposta é semântica de admissibilidade e referência. Nova coluna
   somente poderá ser proposta em CHANGE posterior se caso real demonstrar
   necessidade irredutível após esta convenção. Não há novo registry, enum ou estado.
