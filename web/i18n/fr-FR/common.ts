const translation = {
  api: {
    success: 'Succès',
    actionSuccess: 'Action réussie',
    saved: 'Sauvegardé',
    create: 'Créé',
    remove: 'Supprimé',
  },
  operation: {
    create: 'Créer',
    confirm: 'Confirmer',
    cancel: 'Annuler',
    clear: 'Effacer',
    save: 'Enregistrer',
    saveAndEnable: 'Enregistrer et Activer',
    edit: 'Modifier',
    add: 'Ajouter',
    added: 'Ajouté',
    refresh: 'Redémarrer',
    reset: 'Réinitialiser',
    search: 'Recherche',
    change: 'Changer',
    remove: 'Supprimer',
    send: 'Envoyer',
    copy: 'Copier',
    lineBreak: 'Saut de ligne',
    sure: 'Je suis sûr',
    download: 'Télécharger',
    delete: 'Supprimer',
    settings: 'Paramètres',
    setup: 'Configuration',
    getForFree: 'Obtenez gratuitement',
    reload: 'Recharger',
    ok: 'D\'accord',
    log: 'Journal',
    learnMore: 'En savoir plus',
    params: 'Paramètres',
    duplicate: 'Dupliquer',
    rename: 'Renommer',
  },
  placeholder: {
    input: 'Veuillez entrer',
    select: 'Veuillez sélectionner',
  },
  voice: {
    language: {
      zhHans: 'Chinois',
      zhHant: 'Chinois (traditionnel)',
      enUS: 'Anglais',
      deDE: 'Allemand',
      frFR: 'Français',
      esES: 'Espagnol',
      itIT: 'Italien',
      thTH: 'Thaï.',
      idID: 'Indonésien',
      jaJP: 'Japonais',
      koKR: 'Coréen',
      ptBR: 'Portugais',
      ruRU: 'Russe',
      ukUA: 'Ukrainien',
      viVN: 'Vietnamien',
      plPL: 'Polonais',
    },
  },
  unit: {
    char: 'caractères',
  },
  actionMsg: {
    noModification: 'Aucune modification pour le moment.',
    modifiedSuccessfully: 'Modifié avec succès',
    modifiedUnsuccessfully: 'Modifié sans succès',
    copySuccessfully: 'Copié avec succès',
    paySucceeded: 'Paiement réussi',
    payCancelled: 'Paiement annulé',
    generatedSuccessfully: 'Généré avec succès',
    generatedUnsuccessfully: 'Généré sans succès',
  },
  model: {
    params: {
      temperature: 'Température',
      temperatureTip:
        'Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.',
      top_p: 'Haut P',
      top_pTip:
        'Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.',
      presence_penalty: 'Pénalité de présence',
      presence_penaltyTip:
        'Combien pénaliser les nouveaux tokens en fonction de leur apparition dans le texte jusqu\'à présent. Augmente la probabilité du modèle de parler de nouveaux sujets.',
      frequency_penalty: 'Pénalité de fréquence',
      frequency_penaltyTip:
        'Combien pénaliser les nouveaux tokens en fonction de leur fréquence existante dans le texte jusqu\'à présent. Réduit la probabilité du modèle de répéter la même ligne mot pour mot.',
      max_tokens: 'Max jeton',
      max_tokensTip:
        'Utilisé pour limiter la longueur maximale de la réponse, en jetons. \nDes valeurs plus grandes peuvent limiter l\'espace restant pour les mots de prompt, les journaux de chat, et la Connaissance. \nIl est recommandé de le régler en dessous des',
      maxTokenSettingTip: 'Votre réglage de max token est élevé, limitant potentiellement l\'espace pour les prompts, les requêtes et les données. Envisagez de le définir en dessous de 2/3.',
      setToCurrentModelMaxTokenTip: 'Le max token est mis à jour à 80% du max token du modèle actuel {{maxToken}}.',
      stop_sequences: 'Séquences d\'arrêt',
      stop_sequencesTip: 'Jusqu\'à quatre séquences où l\'API arrêtera de générer d\'autres tokens. Le texte renvoyé ne contiendra pas la séquence d\'arrêt.',
      stop_sequencesPlaceholder: 'Entrez la séquence et appuyez sur Tab',
    },
    tone: {
      Creative: 'Créatif',
      Balanced: 'Équilibré',
      Precise: 'Précis',
      Custom: 'Personnalisé',
    },
    addMoreModel: 'Allez dans les paramètres pour ajouter plus de modèles',
  },
  menus: {
    status: 'bêta',
    explore: 'Explorer',
    apps: 'Studio',
    plugins: 'Plugins',
    pluginsTips: 'Intégrez des plugins tiers ou créez des AI-Plugins compatibles avec ChatGPT.',
    datasets: 'Connaissance',
    datasetsTips: 'COMING SOON: Import your own text data or write data in real-time via Webhook for LLM context enhancement.',
    newApp: 'Nouvelle Application',
    newDataset: 'Créer des Connaissances',
    tools: 'Outils',
  },
  userProfile: {
    settings: 'Paramètres',
    emailSupport: 'Support par courriel',
    workspace: 'Espace de travail',
    createWorkspace: 'Créer un Espace de Travail',
    helpCenter: 'Aide',
    roadmapAndFeedback: 'Retour d\'information',
    community: 'Communauté',
    about: 'À propos',
    logout: 'Se déconnecter',
  },
  settings: {
    accountGroup: 'COMPTE',
    workplaceGroup: 'ESPACE DE TRAVAIL',
    account: 'Mon compte',
    members: 'Membres',
    billing: 'Facturation',
    integrations: 'Intégrations',
    language: 'Langue',
    provider: 'Fournisseur de Modèle',
    dataSource: 'Source de Données',
    plugin: 'Plugins',
    apiBasedExtension: 'Extension API',
  },
  account: {
    avatar: 'Avatar',
    name: 'Nom',
    email: 'Courriel',
    password: 'Mot de passe',
    passwordTip: 'Vous pouvez définir un mot de passe permanent si vous ne souhaitez pas utiliser des codes de connexion temporaires.',
    setPassword: 'Définir un mot de passe',
    resetPassword: 'Réinitialiser le mot de passe',
    currentPassword: 'Mot de passe actuel',
    newPassword: 'Nouveau mot de passe',
    confirmPassword: 'Confirmer le mot de passe',
    notEqual: 'Les deux mots de passe sont différents.',
    langGeniusAccount: 'Compte Dify',
    langGeniusAccountTip: 'Votre compte Vigie et les données utilisateur associées.',
    editName: 'Modifier le nom',
    showAppLength: 'Afficher {{length}} applications',
    delete: 'Supprimer le compte',
    deleteTip: 'La suppression de votre compte effacera définitivement toutes vos données et elles ne pourront pas être récupérées.',
    deleteConfirmTip: 'Pour confirmer, veuillez envoyer ce qui suit depuis votre adresse e-mail enregistrée à ',
  },
  members: {
    team: 'Équipe',
    invite: 'Ajouter',
    name: 'NOM',
    lastActive: 'DERNIÈRE ACTIVITÉ',
    role: 'RÔLES',
    pending: 'En attente...',
    owner: 'Propriétaire',
    admin: 'Administrateur',
    adminTip: 'Peut construire des applications & gérer les paramètres de l\'équipe',
    normal: 'Normal',
    normalTip: 'Peut seulement utiliser des applications, ne peut pas construire des applications',
    editor: 'Éditeur',
    editorTip: 'Peut construire des applications, mais ne peut pas gérer les paramètres de l\'équipe',
    inviteTeamMember: 'Ajouter un membre de l\'équipe',
    inviteTeamMemberTip: 'Ils peuvent accéder directement à vos données d\'équipe après s\'être connectés.',
    email: 'Courrier électronique',
    emailInvalid: 'Format de courriel invalide',
    emailPlaceholder: 'Veuillez entrer des emails',
    sendInvite: 'Envoyer une invitation',
    invitedAsRole: 'Invité en tant qu\'utilisateur {{role}}',
    invitationSent: 'Invitation envoyée',
    invitationSentTip: 'Invitation envoyée, et ils peuvent se connecter à Vigie pour accéder aux données de votre équipe.',
    invitationLink: 'Lien d\'invitation',
    failedinvitationEmails: 'Les utilisateurs ci-dessous n\'ont pas été invités avec succès',
    ok: 'D\'accord',
    removeFromTeam: 'Retirer de l\'équipe',
    removeFromTeamTip: 'Supprimera l\'accès de l\'équipe',
    setAdmin: 'Définir comme administrateur',
    setMember: 'Définir en tant que membre ordinaire',
    setEditor: 'Définir en tant qu\'éditeur',
    disinvite: 'Annuler l\'invitation',
    deleteMember: 'Supprimer Membre',
    you: '(Vous)',
  },
  integrations: {
    connected: 'Connecté',
    google: 'Google',
    googleAccount: 'Connectez-vous avec un compte Google',
    github: 'GitHub',
    githubAccount: 'Connectez-vous avec un compte GitHub',
    connect: 'Connecter',
  },
  language: {
    displayLanguage: 'Langue d\'affichage',
    timezone: 'Fuseau horaire',
  },
  provider: {
    apiKey: 'Clé API',
    enterYourKey: 'Entrez votre clé API ici',
    invalidKey: 'Clé API OpenAI invalide',
    validatedError: 'Validation failed: ',
    validating: 'Validation de la clé...',
    saveFailed: 'La sauvegarde de la clé API a échoué',
    apiKeyExceedBill: 'Cette clé API n\'a pas de quota disponible, veuillez lire',
    addKey: 'Ajouter une clé',
    comingSoon: 'Bientôt disponible',
    editKey: 'Modifier',
    invalidApiKey: 'Clé API invalide',
    azure: {
      apiBase: 'Base de l\'API',
      apiBasePlaceholder: 'L\'URL de base de l\'API de votre point de terminaison Azure OpenAI.',
      apiKey: 'Clé API',
      apiKeyPlaceholder: 'Entrez votre clé API ici',
      helpTip: 'Apprenez le service OpenAI Azure',
    },
    openaiHosted: {
      openaiHosted: 'OpenAI Hébergé',
      onTrial: 'EN ESSAI',
      exhausted: 'QUOTA ÉPUISÉ',
      desc: 'Le service d\'hébergement OpenAI fourni par Vigie vous permet d\'utiliser des modèles tels que GPT-3.5. Avant que votre quota d\'essai ne soit épuisé, vous devez configurer d\'autres fournisseurs de modèles.',
      callTimes: 'Temps d\'appel',
      usedUp: 'Quota d\'essai épuisé. Ajoutez votre propre fournisseur de modèle.',
      useYourModel: 'Utilise actuellement son propre fournisseur de modèle.',
      close: 'Fermer',
    },
    anthropicHosted: {
      anthropicHosted: 'Anthropic Claude',
      onTrial: 'EN ESSAI',
      exhausted: 'QUOTA ÉPUISÉ',
      desc: 'Modèle puissant, qui excelle dans une large gamme de tâches allant du dialogue sophistiqué et de la génération de contenu créatif à l\'instruction détaillée.',
      callTimes: 'Temps d\'appel',
      usedUp: 'Quota d\'essai épuisé. Ajoutez votre propre fournisseur de modèle.',
      useYourModel: 'Utilise actuellement son propre fournisseur de modèle.',
      close: 'Fermer',
    },
    anthropic: {
      using: 'La capacité d\'embedding est utilisée',
      enableTip: 'Pour activer le modèle Anthropic, vous devez d\'abord vous lier à OpenAI ou au service Azure OpenAI.',
      notEnabled: 'Non activé',
      keyFrom: 'Obtenez votre clé API de chez Anthropic',
    },
    encrypted: {
      front: 'Votre clé API sera chiffrée et stockée en utilisant',
      back: 'technologie.',
    },
  },
  modelProvider: {
    notConfigured: 'Le modèle du système n\'a pas encore été entièrement configuré, et certaines fonctions peuvent être indisponibles.',
    systemModelSettings: 'Paramètres du Modèle Système',
    systemModelSettingsLink: 'Pourquoi est-il nécessaire de mettre en place un modèle de système ?',
    selectModel: 'Sélectionnez votre modèle',
    setupModelFirst: 'Veuillez d\'abord configurer votre modèle',
    systemReasoningModel: {
      key: 'Modèle de Raisonnement du Système',
      tip: 'Définissez le modèle d\'inférence par défaut à utiliser pour la création d\'applications, ainsi que des fonctionnalités telles que la génération de noms de dialogue et la suggestion de la prochaine question utiliseront également le modèle d\'inférence par défaut.',
    },
    embeddingModel: {
      key: 'Modèle d\'Embedding',
      tip: 'Définissez le modèle par défaut pour le traitement d\'incorporation de documents de la Connaissance, à la fois la récupération et l\'importation de la Connaissance utilisent ce modèle d\'Embedding pour le traitement de vectorisation. Si vous changez de modèle, la dimension du vecteur entre la connaissance importée et la question ne sera pas cohérente, ce qui entraînera un échec de la recherche. Pour éviter les échecs de recherche, veuillez ne pas changer de modèle à volonté.',
      required: 'Le modèle d\'embedding est requis',
    },
    speechToTextModel: {
      key: 'Modèle de Texte-à-Parole',
      tip: 'Définissez le modèle par défaut pour l\'entrée de texte par la parole dans la conversation.',
    },
    ttsModel: {
      key: 'Modèle de Texte-à-Parole',
      tip: 'Définissez le modèle par défaut pour l\'entrée de texte à la parole dans une conversation.',
    },
    rerankModel: {
      key: 'Modèle de Réorganisation',
      tip: 'Le modèle de réorganisation réorganisera la liste des documents candidats en fonction de la correspondance sémantique avec la requête de l\'utilisateur, améliorant ainsi les résultats du classement sémantique.',
    },
    quota: 'Quota',
    searchModel: 'Modèle de recherche',
    noModelFound: 'Aucun modèle trouvé pour {{model}}',
    models: 'Modèles',
    showMoreModelProvider: 'Montrer plus de fournisseur de modèle',
    selector: {
      tip: 'Ce modèle a été supprimé. Veuillez ajouter un modèle ou sélectionner un autre modèle.',
      emptyTip: 'Aucun modèle disponible',
      emptySetting: 'Veuillez aller dans les paramètres pour configurer',
      rerankTip: 'Veuillez configurer le modèle Rerank',
    },
    card: {
      quota: 'QUOTA',
      onTrial: 'En Essai',
      paid: 'Payé',
      quotaExhausted: 'Quota épuisé',
      callTimes: 'Temps d\'appel',
      tokens: 'Jetons',
      buyQuota: 'Acheter Quota',
      priorityUse: 'Utilisation prioritaire',
      removeKey: 'Supprimer la clé API',
      tip: 'La priorité sera donnée au quota payant. Le quota d\'essai sera utilisé après épuisement du quota payant.',
    },
    item: {
      deleteDesc: '{{modelName}} sont utilisés comme modèles de raisonnement système. Certaines fonctions ne seront pas disponibles après la suppression. Veuillez confirmer.',
      freeQuota: 'QUOTA GRATUIT',
    },
    addApiKey: 'Ajoutez votre clé API',
    invalidApiKey: 'Clé API invalide',
    encrypted: {
      front: 'Votre clé API sera cryptée et stockée en utilisant',
      back: 'technologie.',
    },
    freeQuota: {
      howToEarn: 'Comment gagner',
    },
    addMoreModelProvider: 'AJOUTER PLUS DE FOURNISSEUR DE MODÈLE',
    addModel: 'Ajouter un modèle',
    modelsNum: '{{num}} Modèles',
    showModels: 'Montrer les modèles',
    showModelsNum: 'Afficher {{num}} Modèles',
    collapse: 'Effondrer',
    config: 'Configuration',
    modelAndParameters: 'Modèle et Paramètres',
    model: 'Modèle',
    featureSupported: '{{feature}} pris en charge',
    callTimes: 'Temps d\'appel',
    credits: 'Crédits de Messages',
    buyQuota: 'Acheter Quota',
    getFreeTokens: 'Obtenez des Tokens gratuits',
    priorityUsing: 'Prioriser l\'utilisation',
    deprecated: 'Obsolète',
    confirmDelete: 'confirmer la suppression?',
    quotaTip: 'Tokens gratuits restants disponibles',
    loadPresets: 'Charger les Présents',
    parameters: 'PARAMÈTRES',
  },
  dataSource: {
    add: 'Ajouter une source de données',
    connect: 'Connecter',
    notion: {
      title: 'Notion',
      description: 'Utiliser Notion comme source de données pour la Connaissance.',
      connectedWorkspace: 'Espace de travail connecté',
      addWorkspace: 'Ajouter un espace de travail',
      connected: 'Connecté',
      disconnected: 'Déconnecté',
      changeAuthorizedPages: 'Modifier les pages autorisées',
      pagesAuthorized: 'Pages autorisées',
      sync: 'Synchronisation',
      remove: 'Supprimer',
      selector: {
        pageSelected: 'Pages Sélectionnées',
        searchPages: 'Rechercher des pages...',
        noSearchResult: 'Aucun résultat de recherche',
        addPages: 'Ajouter des pages',
        preview: 'APERÇU',
      },
    },
  },
  plugin: {
    serpapi: {
      apiKey: 'Clé API',
      apiKeyPlaceholder: 'Entrez votre clé API',
      keyFrom: 'Obtenez votre clé SerpAPI depuis la page de compte SerpAPI',
    },
  },
  apiBasedExtension: {
    title: 'Les extensions API fournissent une gestion centralisée des API, simplifiant la configuration pour une utilisation facile à travers les applications de Dify.',
    link: 'Apprenez comment développer votre propre Extension API.',
    linkUrl: 'https://docs.dify.ai/fonctionnalites/extension/extension_basee_sur_api',
    add: 'Ajouter l\'extension API',
    selector: {
      title: 'Extension de l\'API',
      placeholder: 'Veuillez sélectionner l\'extension API',
      manage: 'Gérer l\'extension API',
    },
    modal: {
      title: 'Ajouter une extension API',
      editTitle: 'Modifier l\'extension API',
      name: {
        title: 'Nom',
        placeholder: 'Veuillez entrer le nom',
      },
      apiEndpoint: {
        title: 'Point de terminaison API',
        placeholder: 'Veuillez entrer le point de terminaison de l\'API',
      },
      apiKey: {
        title: 'clé API',
        placeholder: 'Veuillez entrer la clé API',
        lengthError: 'La longueur de la clé API ne peut pas être inférieure à 5 caractères',
      },
    },
    type: 'Tapez',
  },
  about: {
    changeLog: 'Journal des modifications',
    updateNow: 'Mettre à jour maintenant',
    nowAvailable: 'Dify {{version}} est maintenant disponible.',
    latestAvailable: 'Dify {{version}} est la dernière version disponible.',
  },
  appMenus: {
    overview: 'Surveillance',
    promptEng: 'Orchestrer',
    apiAccess: 'Accès API',
    logAndAnn: 'Journaux & Annonces.',
    logs: 'Journaux',
  },
  environment: {
    testing: 'TESTER',
    development: 'DÉVELOPPEMENT',
  },
  appModes: {
    completionApp: 'Générateur de Texte',
    chatApp: 'Appli de Chat',
  },
  datasetMenus: {
    documents: 'Documents',
    hitTesting: 'Test de Récupération',
    settings: 'Paramètres',
    emptyTip: 'La Connaissance n\'a pas été associée, veuillez aller à l\'application ou au plug-in pour compléter l\'association.',
    viewDoc: 'Voir la documentation',
    relatedApp: 'applications liées',
  },
  voiceInput: {
    speaking: 'Parle maintenant...',
    converting: 'Conversion en texte...',
    notAllow: 'microphone non autorisé',
  },
  modelName: {
    'gpt-3.5-turbo': 'GPT-3.5-Turbo',
    'gpt-3.5-turbo-16k': 'GPT-3.5-Turbo-16K',
    'gpt-4': 'GPT-4',
    'gpt-4-32k': 'GPT-4-32K',
    'text-davinci-003': 'Texte-Davinci-003',
    'text-embedding-ada-002': 'Texte-Intégration-Ada-002',
    'whisper-1': 'Whisper-1',
    'claude-instant-1': 'Claude-Instant',
    'claude-2': 'Claude-2',
  },
  chat: {
    renameConversation: 'Renommer la conversation',
    conversationName: 'Nom de la conversation',
    conversationNamePlaceholder: 'Veuillez entrer le nom de la conversation',
    conversationNameCanNotEmpty: 'Nom de la conversation requis',
    citation: {
      title: 'CITATIONS',
      linkToDataset: 'Lien vers la Connaissance',
      characters: 'Personnages :',
      hitCount: 'Nombre de récupérations :',
      vectorHash: 'Hachage vectoriel:',
      hitScore: 'Score de Récupération:',
    },
  },
  promptEditor: {
    placeholder: 'Écrivez votre mot d\'invite ici, entrez \'{\' pour insérer une variable, entrez \'/\' pour insérer un bloc de contenu d\'invite',
    context: {
      item: {
        title: 'Contexte',
        desc: 'Insérez le modèle de contexte',
      },
      modal: {
        title: '{{num}} Connaissance en Contexte',
        add: 'Ajouter Contexte',
        footer: 'Vous pouvez gérer les contextes dans la section Contexte ci-dessous.',
      },
    },
    history: {
      item: {
        title: 'Historique des conversations',
        desc: 'Insérer le modèle de message historique',
      },
      modal: {
        title: 'EXEMPLE',
        user: 'Bonjour',
        assistant: 'Bonjour ! Comment puis-je vous aider aujourd\'hui ?',
        edit: 'Modifier les Noms des Rôles de Conversation',
      },
    },
    variable: {
      item: {
        title: 'Variables & Outils Externes',
        desc: 'Insérer des Variables & Outils Externes',
      },
      outputToolDisabledItem: {
        title: 'Variables',
        desc: 'Insérer Variables',
      },
      modal: {
        add: 'Nouvelle variable',
        addTool: 'Nouvel outil',
      },
    },
    query: {
      item: {
        title: 'Requête',
        desc: 'Insérez le modèle de requête utilisateur',
      },
    },
    existed: 'Existe déjà dans le prompt',
  },
  imageUploader: {
    uploadFromComputer: 'Télécharger depuis l\'ordinateur',
    uploadFromComputerReadError: 'La lecture de l\'image a échoué, veuillez réessayer.',
    uploadFromComputerUploadError: 'Le téléchargement de l\'image a échoué, veuillez télécharger à nouveau.',
    uploadFromComputerLimit: 'Le téléchargement d\'images ne peut pas dépasser {{size}} MB',
    pasteImageLink: 'Collez le lien de l\'image',
    pasteImageLinkInputPlaceholder: 'Collez le lien de l\'image ici',
    pasteImageLinkInvalid: 'Lien d\'image invalide',
    imageUpload: 'Téléchargement d\'image',
  },
  tag: {
    placeholder: 'Toutes les balises',
    addNew: 'Ajouter une nouvelle balise',
    noTag: 'Aucune balise',
    noTagYet: 'Aucune balise pour l\'instant',
    addTag: 'ajouter une balise',
    editTag: 'Modifier les balises',
    manageTags: 'Gérer les balises',
    selectorPlaceholder: 'Type de recherche ou de création',
    create: 'Créer',
    delete: 'Supprimer la balise',
    deleteTip: 'Le tag est utilisé, le supprimer ?',
    created: 'Tag créé avec succès',
    failed: 'La création de la balise a échoué',
  },
}

export default translation
