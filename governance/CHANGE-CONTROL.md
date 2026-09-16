# Controle de mudança

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: autorização da Etapa 3 indicada no README.

Fluxo: **branch → change → evidence → tests → diff → review → PR → merge**.

1. Confirmar repositório, branch de trabalho, HEAD e working tree baseline conhecido.
2. Preparar mudança delimitada fora de `main`, com origem, owner, identidade e destino.
3. Vincular evidência sanitizada ao delta e às afirmações materiais.
4. Executar verificações aplicáveis e registrar falhas, limites e resultados.
5. Revisar diff completo, incluindo arquivos novos, omissões e segredos.
6. Obter revisão e decisão humana competente, registrando escopo e versão aprovados.
7. Preparar PR e merge somente quando houver autorização específica para essas ações.

Nenhuma mudança material diretamente em `main`. Nesta Etapa 3, o fluxo termina na
preparação e inspeção local: commit, push, PR e merge não estão autorizados.

## Eventos distintos

- Aprovação: decisão que autoriza um escopo; não comprova execução.
- Implementação: alteração efetivamente realizada no alvo, com referência e evidência.
- Verificação: comparação do resultado com critérios explícitos, registrando método e limites.
- Closure: fechamento que reconcilia decisão, alvo, implementação, verificação e pendências.

Não fechar mudança por aprovação isolada nem transformar teste de documentação em
prova de funcionamento. Falta de evidência implica NOT_VERIFIED e bloqueio da promoção.

## Mudança semântica e identidade

Comparar significado anterior e proposto, registrar motivo, materialidade, impactos,
fontes, conflitos, owner e decisão. Preservar o significado vigente até revisão e
promoção explícitas; não substituir silenciosamente termos, IDs, fronteiras ou taxonomias.
Versões substituídas devem apontar para a sucessora e a decisão de supersession.
Se o significado histórico não foi recuperado, marcar RECOVERY_REQUIRED e bloquear
qualquer alegação de preservação semântica já verificada.
