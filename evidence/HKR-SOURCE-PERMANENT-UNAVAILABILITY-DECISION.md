# Decisão delimitada de indisponibilidade de fontes históricas

Scope: MAT-WAVE-01 — HKR Source Disposition & Controlled Contemporary Succession.
MAT-WAVE-01 é somente rótulo operacional; não é canonical_id, domínio, Engine,
owner, lifecycle, estado de governança ou taxonomia. Filename: locator de trabalho.
Canonical ID: NOT_ASSIGNED. Nenhum source_id é atribuído.
Baseline: 333d5892548a207ee099b2f8ab1a6fb1a059b490.
Branch: recovery/hkr-source-disposition-succession-v0.1.

## Decisão, provenance e universo considerado

Authority: decisão humana explícita desta execução, limitada à disposição das
fontes e à preparação documental de sucessão. Source type da autorização:
instrução humana fornecida na conversa de trabalho, por arquivo anexado.
Durable locator da autorização: NOT_VERIFIED. Não se atribui autoridade
empresarial genérica, semantic owner, Role_ID ou identidade pessoal por inferência.

Segundo a declaração humana autorizada, foram consideradas as superfícies de
recuperação já auditadas e eventuais backups, exports, repositórios e arquivos
offline conhecidos. Nomes, datas, logs e cobertura exata dessas buscas não foram
fornecidos nesta execução: NOT_VERIFIED. Não se alega nova busca nesses ambientes
nem prova independente de exaustão universal. O universo aqui registrado é o
universo conhecido declarado pelo humano, com esses limites explícitos.

| Objeto histórico exato | Disposição humana de recuperação |
| --- | --- |
| AIF/EVAL histórico original | PERMANENTLY UNAVAILABLE para recuperação/implementação, no universo declarado |
| JAIF-VIC-001 histórico original | PERMANENTLY UNAVAILABLE para recuperação/implementação, no universo declarado |
| Automation Execution & Observability histórico original | PERMANENTLY UNAVAILABLE para recuperação/implementação, no universo declarado |

Para cada um dos três objetos, registra-se somente a declaração humana:
"não existe neste momento fonte histórica autorizada e razoavelmente disponível
conhecida para recuperação/implementação", dentro do universo de busca registrado.

PERMANENTLY UNAVAILABLE é disposição de recuperação autorizada para esse universo,
não certeza ontológica sobre toda fonte possível ou garantia sobre descobertas
futuras. Não pressupor recuperação futura para implementar um original ausente.
Se surgir fonte autorizada, sua avaliação exige CHANGE e decisão próprios,
preservando esta decisão histórica; não há supersession automática.

## Reconciliação semântica e efeitos

- PERMANENTLY UNAVAILABLE ≠ GOVERNANCE STATE ≠ RECOVERED ≠ REJECTED ≠ SUPERSEDED
  ≠ CURRENT ≠ proof of non-existence. São distinções, não transições de estado.
- Historical original ≠ contemporary successor; SOURCE ≠ SUCCESSOR.
- Recovery disposition ≠ reconstruction; decision ≠ implementation.
- Preparation ≠ acceptance; PROPOSED ≠ ACCEPTED; ACCEPTED ≠ CURRENT.
- Git presence não concede CANONICAL, VERIFIED, ACCEPTED, CURRENT ou IMPLEMENTED.
- NOT_VERIFIED ≠ FAIL; absence of source ≠ proof source never existed.
- Memória de IA, resumos históricos ou conversa isolada não podem fabricar
  conteúdo dos originais. Nenhum dos três originais é declarado recuperado,
  conhecido, inexistente, rejeitado ou substituído formalmente por este registro.

A decisão desbloqueia somente a preparação contemporânea controlada por
[CHANGE-CONTROL](../governance/CHANGE-CONTROL.md), com a análise delimitada no
[registro de sucessão](HKR-CONTROLLED-CONTEMPORARY-SUCCESSION.md).
Não resolve a relação entre cada documento atual e um sucessor formal.
Semantic Freeze preservado: não alegar equivalência semântica com originais cujo
conteúdo é desconhecido; justificar qualquer proposta contemporânea por suas
fontes próprias, delta explícito, escopo e decisão humana.

Continuam RECOVERY_REQUIRED: conteúdo/identidade/versionamento históricos não
recuperados, contratos exatos aplicáveis, binding de owner, autoridade requerida
para promoção e targets necessários ainda não sustentados. A disposição não
converte essas lacunas em recuperação concluída nem obrigação de reconstruí-las.
Continuam NOT_VERIFIED: locators duráveis ausentes, cobertura independente das
buscas, equivalência histórica, relações formais de sucessão, implementação e
verificação operacional. Evidência da decisão não prova o conteúdo dos originais.

ACCEPTED: não concedido. Acceptance: NOT_GRANTED. CURRENT: NOT_GRANTED.
Esta wave não implementa sucessores, integração, DDL, migration, PostgreSQL, n8n,
Notion ou runtime; não autoriza publicação, merge, promoção ou closure global.
Fechamento M1/M2 e dívida residual permanecem delimitados e preservados.

## Rastreabilidade e limite do fechamento

SOURCE → CLAIM → EVIDENCE → PROVENANCE → INTERPRETATION → MATERIALITY → OWNER →
DELTA → DECISION → TARGET → IMPLEMENTATION → VERIFICATION → CLOSURE.

SOURCE/DECISION: instrução humana desta wave; CLAIM: disponibilidade conhecida
delimitada; EVIDENCE/PROVENANCE: declaração recebida, não originais recuperados;
INTERPRETATION: disposição de recuperação, não estado; MATERIALITY: bloqueia uso
de conteúdo histórico ausente; OWNER: binding não demonstrado, RECOVERY_REQUIRED;
DELTA/TARGET: somente estes dois documentos autorizados; IMPLEMENTATION: escrita
documental desta decisão, distinta da implementação de sucessores; VERIFICATION:
revisão documental não verifica objetos operacionais; CLOSURE: global não concedido.
Nenhum elo requerido ausente é omitido ou convertido em PASS.
