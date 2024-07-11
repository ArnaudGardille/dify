const translation = {
  api: {
    success: 'Succes',
    actionSuccess: 'Acțiune reușită',
    saved: 'Salvat',
    create: 'Creat',
    remove: 'Eliminat',
  },
  operation: {
    create: 'Creează',
    confirm: 'Confirmă',
    cancel: 'Anulează',
    clear: 'Șterge',
    save: 'Salvează',
    edit: 'Editează',
    add: 'Adaugă',
    added: 'Adăugat',
    refresh: 'Reîncarcă',
    reset: 'Resetează',
    search: 'Caută',
    change: 'Schimbă',
    remove: 'Elimină',
    send: 'Trimite',
    copy: 'Copiază',
    lineBreak: 'Linie nouă',
    sure: 'Sunt sigur',
    download: 'Descarcă',
    delete: 'Șterge',
    settings: 'Setări',
    setup: 'Configurare',
    getForFree: 'Obține gratuit',
    reload: 'Reîncarcă',
    ok: 'OK',
    log: 'Jurnal',
    learnMore: 'Află mai multe',
    params: 'Parametri',
    duplicate: 'Duplică',
    rename: 'Redenumește',
  },
  placeholder: {
    input: 'Vă rugăm să introduceți',
    select: 'Vă rugăm să selectați',
  },
  voice: {
    language: {
      zhHans: 'Chineză',
      zhHant: 'Chineză tradițională',
      enUS: 'Engleză',
      deDE: 'Germană',
      frFR: 'Franceză',
      esES: 'Spaniolă',
      itIT: 'Italiană',
      thTH: 'Thailandeză',
      idID: 'Indoneziană',
      jaJP: 'Japoneză',
      koKR: 'Coreeană',
      ptBR: 'Portugheză',
      ruRU: 'Rusă',
      ukUA: 'Ucraineană',
      viVN: 'Vietnameză',
    },
  },
  unit: {
    char: 'caractere',
  },
  actionMsg: {
    noModification: 'Nicio modificare în acest moment.',
    modifiedSuccessfully: 'Modificat cu succes',
    modifiedUnsuccessfully: 'Modificare eșuată',
    copySuccessfully: 'Copiat cu succes',
    paySucceeded: 'Plata a reușit',
    payCancelled: 'Plata a fost anulată',
    generatedSuccessfully: 'Generat cu succes',
    generatedUnsuccessfully: 'Generare eșuată',
  },
  model: {
    params: {
      temperature: 'Temperatură',
      temperatureTip:
        'Controlează aleatorietatea: Reducerea duce la mai puține completări aleatorii. Pe măsură ce temperatura se apropie de zero, modelul va deveni deterministic și repetitiv.',
      top_p: 'Top P',
      top_pTip:
        'Controlează diversitatea prin eșantionarea nucleului: 0,5 înseamnă că jumătate din toate opțiunile ponderate după probabilitate sunt luate în considerare.',
      presence_penalty: 'Penalizare prezență',
      presence_penaltyTip:
        'Cât de mult să se penalizeze noile jetoane în funcție de dacă apar sau nu în textul de până acum.\nCrește probabilitatea modelului de a vorbi despre subiecte noi.',
      frequency_penalty: 'Penalizare frecvență',
      frequency_penaltyTip:
        'Cât de mult să se penalizeze noile jetoane în funcție de frecvența lor existentă în textul de până acum.\nScade probabilitatea modelului de a repeta aceeași linie cuvânt cu cuvânt.',
      max_tokens: 'Jetoane maxime',
      max_tokensTip:
        'Folosit pentru a limita lungimea maximă a răspunsului, în jetoane.\nValori mai mari pot limita spațiul rămas pentru cuvintele promptului, jurnalele de chat și cunoștințe.\nSe recomandă să fie setat la mai puțin de două treimi\ngpt-4-1106-preview, gpt-4-vision-preview jetoane maxime (intrare 128k ieșire 4k)',
      maxTokenSettingTip: 'Setarea jetoanelor maxime este ridicată, limitând potențial spațiul pentru prompturi, interogări și date. Luați în considerare setarea acesteia la sub 2/3.',
      setToCurrentModelMaxTokenTip: 'Jetoanele maxime sunt actualizate la 80% din jetoanele maxime ale modelului curent {{maxToken}}.',
      stop_sequences: 'Secvențe de oprire',
      stop_sequencesTip: 'Până la patru secvențe în care API-ul va înceta să genereze mai multe jetoane. Textul returnat nu va conține secvența de oprire.',
      stop_sequencesPlaceholder: 'Introduceți secvența și apăsați Tab',
    },
    tone: {
      Creative: 'Creativ',
      Balanced: 'Echilibrat',
      Precise: 'Precis',
      Custom: 'Personalizat',
    },
    addMoreModel: 'Mergeți la setări pentru a adăuga mai multe modele',
  },
  menus: {
    status: 'beta',
    explore: 'Explorează',
    apps: 'Studio',
    plugins: 'Plugin-uri',
    pluginsTips: 'Integrați plugin-uri terțe părți sau creați AI-Plugin-uri compatibile cu ChatGPT.',
    datasets: 'Cunoștințe',
    datasetsTips: 'CURÂND DISPONIBIL: Importați-vă propriile date text sau scrieți date în timp real prin Webhook pentru îmbunătățirea contextului LLM.',
    newApp: 'Aplicație nouă',
    newDataset: 'Creează Cunoștințe',
    tools: 'Instrumente',
  },
  userProfile: {
    settings: 'Setări',
    workspace: 'Spațiu de lucru',
    createWorkspace: 'Creează Spațiu de lucru',
    helpCenter: 'Ajutor',
    roadmapAndFeedback: 'Feedback',
    community: 'Comunitate',
    about: 'Despre',
    logout: 'Deconectare',
  },
  settings: {
    accountGroup: 'CONT',
    workplaceGroup: 'SPAȚIU DE LUCRU',
    account: 'Contul meu',
    members: 'Membri',
    billing: 'Facturare',
    integrations: 'Integrări',
    language: 'Limbă',
    provider: 'Furnizor de modele',
    dataSource: 'Sursă de date',
    plugin: 'Plugin-uri',
    apiBasedExtension: 'Extensie API',
  },
  account: {
    avatar: 'Avatar',
    name: 'Nume',
    email: 'Email',
    password: 'Parolă',
    passwordTip: 'Puteți seta o parolă permanentă dacă nu doriți să utilizați coduri de conectare temporare',
    setPassword: 'Setează o parolă',
    resetPassword: 'Resetează parola',
    currentPassword: 'Parola curentă',
    newPassword: 'Parolă nouă',
    confirmPassword: 'Confirmă parola',
    notEqual: 'Cele două parole sunt diferite.',
    langGeniusAccount: 'Cont Dify',
    langGeniusAccountTip: 'Contul Vigie și datele de utilizator asociate.',
    editName: 'Editează Nume',
    showAppLength: 'Afișează {{length}} aplicații',
    delete: 'Șterge contul',
    deleteTip: 'Ștergerea contului vă va șterge definitiv toate datele și nu pot fi recuperate.',
    deleteConfirmTip: 'Pentru a confirma, trimiteți următoarele din e-mailul înregistrat la ',
  },
  members: {
    team: 'Echipă',
    invite: 'Adaugă',
    name: 'NUME',
    lastActive: 'ULTIMA ACTIVITATE',
    role: 'ROLURI',
    pending: 'În așteptare...',
    owner: 'Proprietar',
    admin: 'Administrator',
    adminTip: 'Poate construi aplicații și gestiona setările echipei',
    normal: 'Normal',
    normalTip: 'Poate doar utiliza aplicații, nu poate construi aplicații',
    editor: 'Editor',
    editorTip: 'Poate construi aplicații, dar nu poate gestiona setările echipei',
    inviteTeamMember: 'Adaugă membru în echipă',
    inviteTeamMemberTip: 'Pot accesa direct datele echipei dvs. după autentificare.',
    email: 'Email',
    emailInvalid: 'Format de email invalid',
    emailPlaceholder: 'Vă rugăm să introduceți emailuri',
    sendInvite: 'Trimite invitație',
    invitedAsRole: 'Invitat ca utilizator {{role}}',
    invitationSent: 'Invitație trimisă',
    invitationSentTip: 'Invitația a fost trimisă și pot să se autentifice în Vigie pentru a accesa datele echipei dvs.',
    invitationLink: 'Link de invitație',
    failedinvitationEmails: 'Următorii utilizatori nu au fost invitați cu succes',
    ok: 'OK',
    removeFromTeam: 'Elimină din echipă',
    removeFromTeamTip: 'Va elimina accesul la echipă',
    setAdmin: 'Setează ca administrator',
    setMember: 'Setează ca membru obișnuit',
    setEditor: 'Setează ca editor',
    disinvite: 'Anulează invitația',
    deleteMember: 'Șterge membru',
    you: '(Dvs.)',
  },
  integrations: {
    connected: 'Conectat',
    google: 'Google',
    googleAccount: 'Autentificare cu cont Google',
    github: 'GitHub',
    githubAccount: 'Autentificare cu cont GitHub',
    connect: 'Conectează',
  },
  language: {
    displayLanguage: 'Limbă de afișare',
    timezone: 'Fus orar',
  },
  provider: {
    apiKey: 'Cheie API',
    enterYourKey: 'Introduceți cheia API aici',
    invalidKey: 'Cheie API OpenAI nevalidă',
    validatedError: 'Validare eșuată: ',
    validating: 'Se validează cheia...',
    saveFailed: 'Salvarea cheii API a eșuat',
    apiKeyExceedBill: 'Această CHEIE API nu are cotă disponibilă, vă rugăm să citiți',
    addKey: 'Adaugă cheie',
    comingSoon: 'Curând disponibil',
    editKey: 'Editează',
    invalidApiKey: 'Cheie API nevalidă',
    azure: {
      apiBase: 'Bază API',
      apiBasePlaceholder: 'URL-ul de bază al API-ului pentru punctul final Azure OpenAI.',
      apiKey: 'Cheie API',
      apiKeyPlaceholder: 'Introduceți cheia API aici',
      helpTip: 'Aflați despre serviciul Azure OpenAI',
    },
    openaiHosted: {
      openaiHosted: 'OpenAI găzduit',
      onTrial: 'ÎN PROBĂ',
      exhausted: 'COTĂ EPUIZATĂ',
      desc: 'Serviciul de găzduire OpenAI furnizat de Vigie vă permite să utilizați modele precum GPT-3.5. Înainte ca cota de probă să fie epuizată, trebuie să configurați alți furnizori de modele.',
      callTimes: 'Apeluri',
      usedUp: 'Cota de probă a fost epuizată. Adăugați propriul furnizor de modele.',
      useYourModel: 'În prezent se utilizează propriul furnizor de modele.',
      close: 'Închide',
    },
    anthropicHosted: {
      anthropicHosted: 'Anthropic Claude',
      onTrial: 'ÎN PROBĂ',
      exhausted: 'COTĂ EPUIZATĂ',
      desc: 'Model puternic, care excelează într-o gamă largă de sarcini, de la dialog sofisticat și generare de conținut creativ, până la instrucțiuni detaliate.',
      callTimes: 'Apeluri',
      usedUp: 'Cota de probă a fost epuizată. Adăugați propriul furnizor de modele.',
      useYourModel: 'În prezent se utilizează propriul furnizor de modele.',
      close: 'Închide',
    },
    anthropic: {
      using: 'Capacitatea de încorporare utilizează',
      enableTip: 'Pentru a activa modelul Anthropic, trebuie să vă legați mai întâi la OpenAI sau la serviciul Azure OpenAI.',
      notEnabled: 'Nu este activat',
      keyFrom: 'Obțineți cheia API de la Anthropic',
    },
    encrypted: {
      front: 'Cheia dvs. API va fi criptată și stocată folosind',
      back: ' tehnologie.',
    },
  },
  modelProvider: {
    notConfigured: 'Modelul de sistem nu a fost încă configurat complet, iar unele funcții pot fi indisponibile.',
    systemModelSettings: 'Setări model de sistem',
    systemModelSettingsLink: 'De ce este necesar să se configureze un model de sistem?',
    selectModel: 'Selectați modelul dvs.',
    setupModelFirst: 'Vă rugăm să configurați mai întâi modelul',
    systemReasoningModel: {
      key: 'Model de raționament de sistem',
      tip: 'Setați modelul de inferență implicit care va fi utilizat pentru crearea aplicațiilor, precum și caracteristici precum generarea de nume pentru dialog și sugestia următoarei întrebări vor utiliza, de asemenea, modelul de inferență implicit.',
    },
    embeddingModel: {
      key: 'Model de încorporare',
      tip: 'Setați modelul implicit pentru procesarea încorporării documentelor a Cunoștințelor, atât pentru recuperare, cât și pentru importul Cunoștințelor, folosind acest model de încorporare pentru procesarea vectorizării. Comutarea va cauza inconsecvența dimensiunii vectorului între Cunoștințele importate și întrebarea, ceea ce va duce la eșecul recuperării. Pentru a evita eșecul recuperării, vă rugăm să nu comutați acest model la întâmplare.',
      required: 'Modelul de încorporare este obligatoriu',
    },
    speechToTextModel: {
      key: 'Model de conversie text-la-vorbire',
      tip: 'Setați modelul implicit pentru intrarea de conversie text-la-vorbire în conversație.',
    },
    ttsModel: {
      key: 'Model de conversie vorbire-la-text',
      tip: 'Setați modelul implicit pentru intrarea de conversie vorbire-la-text în conversație.',
    },
    rerankModel: {
      key: 'Model de reordonare',
      tip: 'Modelul de reordonare va reordona lista de documente candidate pe baza potrivirii semantice cu interogarea utilizatorului, îmbunătățind rezultatele clasificării semantice',
    },
    quota: 'Cotă',
    searchModel: 'Model de căutare',
    noModelFound: 'Nu a fost găsit niciun model pentru {{model}}',
    models: 'Modele',
    showMoreModelProvider: 'Arată mai multe furnizori de modele',
    selector: {
      tip: 'Acest model a fost eliminat. Vă rugăm să adăugați un model sau să selectați un alt model.',
      emptyTip: 'Nu există modele disponibile',
      emptySetting: 'Vă rugăm să mergeți la setări pentru a configura',
      rerankTip: 'Vă rugăm să configurați modelul de reordonare',
    },
    card: {
      quota: 'COTĂ',
      onTrial: 'În probă',
      paid: 'Plătit',
      quotaExhausted: 'Cotă epuizată',
      callTimes: 'Apeluri',
      tokens: 'Jetoane',
      buyQuota: 'Cumpără cotă',
      priorityUse: 'Utilizare prioritară',
      removeKey: 'Elimină cheia API',
      tip: 'Prioritate va fi acordată cotei plătite. Cota de probă va fi utilizată după epuizarea cotei plătite.',
    },
    item: {
      deleteDesc: '{{modelName}} sunt utilizate ca modele de raționare a sistemului. Unele funcții nu vor fi disponibile după eliminare. Vă rugăm să confirmați.',
      freeQuota: 'COTĂ GRATUITĂ',
    },
    addApiKey: 'Adăugați cheia dvs. API',
    invalidApiKey: 'Cheie API nevalidă',
    encrypted: {
      front: 'Cheia dvs. API va fi criptată și stocată folosind',
      back: ' tehnologie.',
    },
    freeQuota: {
      howToEarn: 'Cum să câștigați',
    },
    addMoreModelProvider: 'ADĂUGAȚI MAI MULȚI FURNIZORI DE MODELE',
    addModel: 'Adăugați model',
    modelsNum: '{{num}} Modele',
    showModels: 'Arată modele',
    showModelsNum: 'Arată {{num}} modele',
    collapse: 'Restrânge',
    config: 'Configurare',
    modelAndParameters: 'Model și parametri',
    model: 'Model',
    featureSupported: '{{feature}} acceptat',
    callTimes: 'Apeluri',
    credits: 'Credite mesaje',
    buyQuota: 'Cumpără cotă',
    getFreeTokens: 'Obțineți jetoane gratuite',
    priorityUsing: 'Prioritizează utilizarea',
    deprecated: 'Învechit',
    confirmDelete: 'confirmați ștergerea?',
    quotaTip: 'Jetoane gratuite disponibile rămase',
    loadPresets: 'Încarcă presetări',
    parameters: 'PARAMETRI',
  },
  dataSource: {
    add: 'Adăugați o sursă de date',
    connect: 'Conectați',
    notion: {
      title: 'Notion',
      description: 'Utilizarea Notion ca sursă de date pentru Cunoștințe.',
      connectedWorkspace: 'Spațiu de lucru conectat',
      addWorkspace: 'Adăugați spațiu de lucru',
      connected: 'Conectat',
      disconnected: 'Deconectat',
      changeAuthorizedPages: 'Schimbați paginile autorizate',
      pagesAuthorized: 'Pagini autorizate',
      sync: 'Sincronizare',
      remove: 'Elimină',
      selector: {
        pageSelected: 'Pagini selectate',
        searchPages: 'Căutați pagini...',
        noSearchResult: 'Niciun rezultat la căutare',
        addPages: 'Adăugați pagini',
        preview: 'PREVIZUALIZARE',
      },
    },
  },
  plugin: {
    serpapi: {
      apiKey: 'Cheie API',
      apiKeyPlaceholder: 'Introduceți cheia dvs. API',
      keyFrom: 'Obțineți cheia dvs. SerpAPI din pagina contului SerpAPI',
    },
  },
  apiBasedExtension: {
    title: 'Extensiile bazate pe API oferă o gestionare centralizată a API-urilor, simplificând configurația pentru o utilizare ușoară în aplicațiile Dify.',
    link: 'Aflați cum să dezvoltați propria extensie bazată pe API.',
    linkUrl: 'https://docs.dify.ai/features/extension/api_based_extension',
    add: 'Adăugați extensie API',
    selector: {
      title: 'Extensie API',
      placeholder: 'Vă rugăm să selectați extensia API',
      manage: 'Gestionați extensia API',
    },
    modal: {
      title: 'Adăugați extensie API',
      editTitle: 'Editați extensia API',
      name: {
        title: 'Nume',
        placeholder: 'Vă rugăm să introduceți numele',
      },
      apiEndpoint: {
        title: 'Endpoint API',
        placeholder: 'Vă rugăm să introduceți endpoint-ul API',
      },
      apiKey: {
        title: 'Cheie API',
        placeholder: 'Vă rugăm să introduceți cheia API',
        lengthError: 'Lungimea cheii API nu poate fi mai mică de 5 caractere',
      },
    },
    type: 'Tip',
  },
  about: {
    changeLog: 'Jurnal modificări',
    updateNow: 'Actualizați acum',
    nowAvailable: 'Dify {{version}} este acum disponibil.',
    latestAvailable: 'Dify {{version}} este ultima versiune disponibilă.',
  },
  appMenus: {
    overview: 'Prezentare generală',
    promptEng: 'Orchestrare',
    apiAccess: 'Acces API',
    logAndAnn: 'Jurnale și Ann.',
    logs: 'Jurnale',
  },
  environment: {
    testing: 'TESTARE',
    development: 'DEZVOLTARE',
  },
  appModes: {
    completionApp: 'Generator de text',
    chatApp: 'Aplicație de chat',
  },
  datasetMenus: {
    documents: 'Documente',
    hitTesting: 'Testare recuperare',
    settings: 'Setări',
    emptyTip: 'Cunoștințele nu au fost asociate, vă rugăm să mergeți la aplicație sau la plug-in pentru a finaliza asocierea.',
    viewDoc: 'Vizualizați documentația',
    relatedApp: 'aplicații asociate',
  },
  voiceInput: {
    speaking: 'Vorbiți acum...',
    converting: 'Se convertește la text...',
    notAllow: 'microfonul nu este autorizat',
  },
  modelName: {
    'gpt-3.5-turbo': 'GPT-3.5-Turbo',
    'gpt-3.5-turbo-16k': 'GPT-3.5-Turbo-16K',
    'gpt-4': 'GPT-4',
    'gpt-4-32k': 'GPT-4-32K',
    'text-davinci-003': 'Text-Davinci-003',
    'text-embedding-ada-002': 'Text-Embedding-Ada-002',
    'whisper-1': 'Whisper-1',
    'claude-instant-1': 'Claude-Instant',
    'claude-2': 'Claude-2',
  },
  chat: {
    renameConversation: 'Redenumește conversația',
    conversationName: 'Nume conversație',
    conversationNamePlaceholder: 'Vă rugăm să introduceți numele conversației',
    conversationNameCanNotEmpty: 'Numele conversației este obligatoriu',
    citation: {
      title: 'CITĂRI',
      linkToDataset: 'Legătură la Cunoștințe',
      characters: 'Caractere:',
      hitCount: 'Număr de recuperări:',
      vectorHash: 'Hash vector:',
      hitScore: 'Scor de recuperare:',
    },
  },
  promptEditor: {
    placeholder: 'Scrieți aici prompt-ul, introduceți \'{}\' pentru a insera o variabilă, introduceți \'/\' pentru a insera un bloc de conținut prompt',
    context: {
      item: {
        title: 'Context',
        desc: 'Inserați șablon de context',
      },
      modal: {
        title: '{{num}} Cunoștințe în context',
        add: 'Adăugați context ',
        footer: 'Puteți gestiona contextele în secțiunea Context de mai jos.',
      },
    },
    history: {
      item: {
        title: 'Istoric conversație',
        desc: 'Inserați șablon de mesaj istoric',
      },
      modal: {
        title: 'EXEMPLU',
        user: 'Salut',
        assistant: 'Salut! Cum vă pot ajuta astăzi?',
        edit: 'Editați numele rolurilor de conversație',
      },
    },
    variable: {
      item: {
        title: 'Variabile și instrumente externe',
        desc: 'Inserați variabile și instrumente externe',
      },
      outputToolDisabledItem: {
        title: 'Variabile',
        desc: 'Inserați variabile',
      },
      modal: {
        add: 'Nouă variabilă',
        addTool: 'Nou instrument',
      },
    },
    query: {
      item: {
        title: 'Interogare',
        desc: 'Inserați șablon de interogare utilizator',
      },
    },
    existed: 'Există deja în prompt',
  },
  imageUploader: {
    uploadFromComputer: 'Încărcați de pe computer',
    uploadFromComputerReadError: 'Citirea imaginii a eșuat, vă rugăm încercați din nou.',
    uploadFromComputerUploadError: 'Încărcarea imaginii a eșuat, vă rugăm încărcați din nou.',
    uploadFromComputerLimit: 'Imaginile încărcate nu pot depăși {{size}} MB',
    pasteImageLink: 'Inserați link-ul imaginii',
    pasteImageLinkInputPlaceholder: 'Inserați link-ul imaginii aici',
    pasteImageLinkInvalid: 'Link-ul imaginii este nevalid',
    imageUpload: 'Încărcare imagine',
  },
  tag: {
    placeholder: 'Toate etichetele',
    addNew: 'Adăugați o etichetă nouă',
    noTag: 'Nicio etichetă',
    noTagYet: 'Încă nu există etichete',
    addTag: 'Adăugați etichete',
    editTag: 'Editați etichete',
    manageTags: 'Gestionați etichete',
    selectorPlaceholder: 'Tastați pentru a căuta sau crea',
    create: 'Creați',
    delete: 'Ștergeți eticheta',
    deleteTip: 'Eticheta este utilizată, ștergeți-o?',
    created: 'Etichetă creată cu succes',
    failed: 'Crearea etichetei a eșuat',
  },
}

export default translation
