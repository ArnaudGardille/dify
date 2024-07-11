const translation = {
  apiServer: 'Servidor da API',
  apiKey: 'Chave da API',
  status: 'Status',
  disabled: 'Desativado',
  ok: 'Em Serviço',
  copy: 'Copiar',
  copied: 'Copiado',
  merMaind: {
    rerender: 'Refazer Rerender',
  },
  never: 'Nunca',
  apiKeyModal: {
    apiSecretKey: 'Chave Secreta da API',
    apiSecretKeyTips: 'Para evitar abuso da API, proteja sua Chave da API. Evite usá-la como texto simples no código front-end. :)',
    createNewSecretKey: 'Criar nova Chave Secreta',
    secretKey: 'Chave Secreta',
    created: 'CRIADA',
    lastUsed: 'ÚLTIMO USO',
    generateTips: 'Mantenha esta chave em um local seguro e acessível.',
  },
  actionMsg: {
    deleteConfirmTitle: 'Excluir esta chave secreta?',
    deleteConfirmTips: 'Esta ação não pode ser desfeita.',
    ok: 'OK',
  },
  completionMode: {
    title: 'Completar App API',
    info: 'Para geração de texto de alta qualidade, como artigos, resumos e traduções, use a API de mensagens de conclusão com entrada do usuário. A geração de texto depende dos parâmetros do modelo e dos modelos de prompt definidos no Vigie Prompt Engineering.',
    createCompletionApi: 'Criar Mensagem de Conclusão',
    createCompletionApiTip: 'Crie uma Mensagem de Conclusão para suportar o modo pergunta e resposta.',
    inputsTips: '(Opcional) Forneça campos de entrada do usuário como pares chave-valor, correspondendo a variáveis no Prompt Eng. A chave é o nome da variável, o valor é o valor do parâmetro. Se o tipo do campo for Select, o Valor enviado deve ser uma das opções predefinidas.',
    queryTips: 'Conteúdo de texto de entrada do usuário.',
    blocking: 'Tipo de bloqueio, aguardando a conclusão da execução e retornando os resultados. (As solicitações podem ser interrompidas se o processo for longo)',
    streaming: 'Retorno de streaming. Implementação de retorno de streaming com base em SSE (Server-Sent Events).',
    messageFeedbackApi: 'Feedback de mensagem (curtir)',
    messageFeedbackApiTip: 'Avalie as mensagens recebidas em nome dos usuários finais com curtidas ou descurtidas. Esses dados são visíveis na página de Logs e Anotações e são usados para ajustes futuros no modelo.',
    messageIDTip: 'ID da mensagem',
    ratingTip: 'curtir ou descurtir, null desfaz',
    parametersApi: 'Obter informações de parâmetros do aplicativo',
    parametersApiTip: 'Recupere os parâmetros de entrada configurados, incluindo nomes de variáveis, nomes de campos, tipos e valores padrão. Geralmente usado para exibir esses campos em um formulário ou preencher valores padrão após o carregamento do cliente.',
  },
  chatMode: {
    title: 'Chat App API',
    info: 'Para aplicativos de conversação versáteis usando um formato de pergunta e resposta, chame a API de mensagens de chat para iniciar o diálogo. Mantenha conversas em andamento passando o conversation_id retornado. Os parâmetros de resposta e modelos dependem das configurações do Vigie Prompt Eng.',
    createChatApi: 'Criar mensagem de chat',
    createChatApiTip: 'Crie uma nova mensagem de conversa ou continue um diálogo existente.',
    inputsTips: '(Opcional) Forneça campos de entrada do usuário como pares chave-valor, correspondendo a variáveis no Prompt Eng. A chave é o nome da variável, o valor é o valor do parâmetro. Se o tipo do campo for Select, o Valor enviado deve ser uma das opções predefinidas.',
    queryTips: 'Conteúdo de entrada/pergunta do usuário',
    blocking: 'Tipo de bloqueio, aguardando a conclusão da execução e retornando os resultados. (As solicitações podem ser interrompidas se o processo for longo)',
    streaming: 'Retorno de streaming. Implementação de retorno de streaming com base em SSE (Server-Sent Events).',
    conversationIdTip: '(Opcional) ID da conversa: deixe vazio para a primeira conversa; passe conversation_id do contexto para continuar o diálogo.',
    messageFeedbackApi: 'Feedback do usuário final da mensagem, curtir',
    messageFeedbackApiTip: 'Avalie as mensagens recebidas em nome dos usuários finais com curtidas ou descurtidas. Esses dados são visíveis na página de Logs e Anotações e são usados para ajustes futuros no modelo.',
    messageIDTip: 'ID da mensagem',
    ratingTip: 'curtir ou descurtir, null desfaz',
    chatMsgHistoryApi: 'Obter histórico de mensagens de chat',
    chatMsgHistoryApiTip: 'A primeira página retorna as últimas `limit` mensagens, em ordem reversa.',
    chatMsgHistoryConversationIdTip: 'ID da conversa',
    chatMsgHistoryFirstId: 'ID do primeiro registro de chat na página atual. O padrão é nenhum.',
    chatMsgHistoryLimit: 'Quantos chats são retornados em uma solicitação',
    conversationsListApi: 'Obter lista de conversas',
    conversationsListApiTip: 'Obtém a lista de sessões do usuário atual. Por padrão, as últimas 20 sessões são retornadas.',
    conversationsListFirstIdTip: 'O ID do último registro na página atual, padrão nenhum.',
    conversationsListLimitTip: 'Quantos chats são retornados em uma solicitação',
    conversationRenamingApi: 'Renomear conversa',
    conversationRenamingApiTip: 'Renomeie conversas; o nome é exibido nas interfaces de cliente com várias sessões.',
    conversationRenamingNameTip: 'Novo nome',
    parametersApi: 'Obter informações de parâmetros do aplicativo',
    parametersApiTip: 'Recupere os parâmetros de entrada configurados, incluindo nomes de variáveis, nomes de campos, tipos e valores padrão. Geralmente usado para exibir esses campos em um formulário ou preencher valores padrão após o carregamento do cliente.',
  },
  develop: {
    requestBody: 'Corpo da Solicitação',
    pathParams: 'Parâmetros de Caminho',
    query: 'Consulta',
  },
}

export default translation
