# Segurança

Escopo: FOUNDATION / BOOTSTRAP V0.1. Fonte: autorização da Etapa 3 indicada no README.

Senhas, PATs, tokens, API keys, private keys e outras credenciais nunca devem entrar
no repositório, inclusive em evidências, logs, exemplos, diffs ou histórico.
Quando uma integração futura precisar de autenticação, use variáveis de ambiente
ou secret stores apropriados, com acesso mínimo; documente apenas o mecanismo e
a referência não sensível. Nenhum segredo real deve ser usado como exemplo.

Não ingira dados pessoais desnecessários de clientes. Minimize e remova informações
sensíveis antes de revisar qualquer fonte. Restrinja acesso a materiais que exijam
proteção; o fato de o repositório ser privado não autoriza armazenar segredos.

## Exposição acidental

1. Interromper a ingestão/publicação e não reproduzir o valor em mensagens ou issues.
2. Avisar o responsável humano por canal restrito, descrevendo alcance sem revelar o segredo.
3. Solicitar ao responsável autorizado revogação/rotação e análise de acessos e impacto.
4. Preparar remoção do conteúdo e avaliar o histórico, clones e cópias; apagar um arquivo não revoga a credencial.
5. Qualquer reescrita de histórico ou ação externa exige autoridade explícita própria.
6. Registrar evidência sanitizada da correção e sua verificação antes de fechar o incidente.

Responsáveis e canais específicos: RECOVERY_REQUIRED. A eficácia dos controles
operacionais permanece NOT_VERIFIED. `.gitignore` auxilia prevenção, mas não detecta
segredos e não remove arquivos já rastreados.
