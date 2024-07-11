const translation = {
  list: {
    title: 'Tài liệu',
    desc: 'Tất cả các tệp của Kiến thức được hiển thị ở đây, và toàn bộ Kiến thức có thể được liên kết với trích dẫn của Vigie hoặc được lập chỉ mục thông qua plugin Chat.',
    addFile: 'Thêm tệp',
    addPages: 'Thêm Trang',
    table: {
      header: {
        fileName: 'TÊN TỆP',
        words: 'TỪ',
        hitCount: 'SỐ LẦN TRUY VẤN',
        uploadTime: 'THỜI GIAN TẢI LÊN',
        status: 'TRẠNG THÁI',
        action: 'HÀNH ĐỘNG',
      },
    },
    action: {
      uploadFile: 'Tải lên tệp mới',
      settings: 'Cài đặt phân đoạn',
      addButton: 'Thêm đoạn',
      add: 'Thêm một đoạn',
      batchAdd: 'Thêm hàng loạt',
      archive: 'Lưu trữ',
      unarchive: 'Khôi phục',
      delete: 'Xóa',
      enableWarning: 'Tệp được lưu trữ không thể được kích hoạt',
      sync: 'Đồng bộ',
    },
    index: {
      enable: 'Kích hoạt',
      disable: 'Vô hiệu hóa',
      all: 'Tất cả',
      enableTip: 'Tệp có thể được lập chỉ mục',
      disableTip: 'Tệp không thể được lập chỉ mục',
    },
    status: {
      queuing: 'Đang chờ',
      indexing: 'Đang lập chỉ mục',
      paused: 'Tạm dừng',
      error: 'Lỗi',
      available: 'Có sẵn',
      enabled: 'Đã kích hoạt',
      disabled: 'Đã vô hiệu hóa',
      archived: 'Đã lưu trữ',
    },
    empty: {
      title: 'Chưa có tài liệu',
      upload: {
        tip: 'Bạn có thể tải lên tệp, đồng bộ từ trang web, hoặc từ ứng dụng web như Notion, GitHub, v.v.',
      },
      sync: {
        tip: 'Dify sẽ định kỳ tải xuống tệp từ Notion của bạn và hoàn tất xử lý.',
      },
    },
    delete: {
      title: 'Bạn có chắc chắn muốn xóa?',
      content: 'Nếu bạn cần tiếp tục xử lý sau này, bạn sẽ tiếp tục từ vị trí bạn đã dừng lại',
    },
    batchModal: {
      title: 'Thêm đoạn hàng loạt',
      csvUploadTitle: 'Kéo và thả tệp CSV của bạn vào đây, hoặc ',
      browse: 'duyệt',
      tip: 'Tệp CSV phải tuân thủ cấu trúc sau:',
      question: 'câu hỏi',
      answer: 'trả lời',
      contentTitle: 'nội dung đoạn',
      content: 'nội dung',
      template: 'Tải mẫu ở đây',
      cancel: 'Hủy bỏ',
      run: 'Chạy Hàng loạt',
      runError: 'Chạy hàng loạt thất bại',
      processing: 'Đang xử lý hàng loạt',
      completed: 'Nhập đã hoàn thành',
      error: 'Lỗi nhập',
      ok: 'OK',
    },
  },
  metadata: {
    title: 'Siêu dữ liệu',
    desc: 'Gắn nhãn siêu dữ liệu cho các tài liệu cho phép trí tuệ nhân tạo truy cập chúng một cách kịp thời và tiết lộ nguồn của các tài liệu tham chiếu cho người dùng.',
    dateTimeFormat: 'D MMMM, YYYY hh:mm A',
    docTypeSelectTitle: 'Vui lòng chọn loại tài liệu',
    docTypeChangeTitle: 'Thay đổi loại tài liệu',
    docTypeSelectWarning:
      'Nếu thay đổi loại tài liệu, các siêu dữ liệu hiện tại sẽ không được bảo toàn nữa',
    firstMetaAction: 'Bắt đầu',
    placeholder: {
      add: 'Thêm ',
      select: 'Chọn ',
    },
    source: {
      upload_file: 'Tải lên Tệp',
      notion: 'Đồng bộ từ Notion',
      github: 'Đồng bộ từ Github',
    },
    type: {
      book: 'Sách',
      webPage: 'Trang Web',
      paper: 'Bài báo',
      socialMediaPost: 'Bài viết trên Mạng xã hội',
      personalDocument: 'Tài liệu cá nhân',
      businessDocument: 'Tài liệu doanh nghiệp',
      IMChat: 'Trò chuyện qua tin nhắn',
      wikipediaEntry: 'Bài viết Wikipedia',
      notion: 'Đồng bộ từ Notion',
      github: 'Đồng bộ từ Github',
      technicalParameters: 'Tham số kỹ thuật',
    },
    field: {
      processRule: {
        processDoc: 'Xử lý Tài liệu',
        segmentRule: 'Quy tắc phân đoạn',
        segmentLength: 'Chiều dài các đoạn',
        processClean: 'Quy tắc làm sạch Văn bản',
      },
      book: {
        title: 'Tiêu đề',
        language: 'Ngôn ngữ',
        author: 'Tác giả',
        publisher: 'Nhà xuất bản',
        publicationDate: 'Ngày xuất bản',
        ISBN: 'ISBN',
        category: 'Danh mục',
      },
      webPage: {
        title: 'Tiêu đề',
        url: 'URL',
        language: 'Ngôn ngữ',
        authorPublisher: 'Tác giả/Nhà xuất bản',
        publishDate: 'Ngày xuất bản',
        topicsKeywords: 'Chủ đề/Từ khóa',
        description: 'Mô tả',
      },
      paper: {
        title: 'Tiêu đề',
        language: 'Ngôn ngữ',
        author: 'Tác giả',
        publishDate: 'Ngày xuất bản',
        journalConferenceName: 'Tên tạp chí/Hội nghị',
        volumeIssuePage: 'Số/Trang',
        DOI: 'DOI',
        topicsKeywords: 'Chủ đề/Từ khóa',
        abstract: 'Tóm tắt',
      },
      socialMediaPost: {
        platform: 'Nền tảng',
        authorUsername: 'Tác giả/Tên người dùng',
        publishDate: 'Ngày đăng',
        postURL: 'URL Bài viết',
        topicsTags: 'Chủ đề/Thẻ',
      },
      personalDocument: {
        title: 'Tiêu đề',
        author: 'Tác giả',
        creationDate: 'Ngày tạo',
        lastModifiedDate: 'Ngày sửa đổi cuối cùng',
        documentType: 'Loại tài liệu',
        tagsCategory: 'Thẻ/Danh mục',
      },
      businessDocument: {
        title: 'Tiêu đề',
        author: 'Tác giả',
        creationDate: 'Ngày tạo',
        lastModifiedDate: 'Ngày sửa đổi cuối cùng',
        documentType: 'Loại tài liệu',
        departmentTeam: 'Phòng ban/Nhóm',
      },
      IMChat: {
        chatPlatform: 'Nền tảng Trò chuyện',
        chatPartiesGroupName: 'Đối tác Trò chuyện/Tên nhóm',
        participants: 'Tham gia viên',
        startDate: 'Ngày bắt đầu',
        endDate: 'Ngày kết thúc',
        topicsKeywords: 'Chủ đề/Từ khóa',
        fileType: 'Loại tệp',
      },
      wikipediaEntry: {
        title: 'Tiêu đề',
        language: 'Ngôn ngữ',
        webpageURL: 'URL trang web',
        editorContributor: 'Biên tập viên/Đóng góp viên',
        lastEditDate: 'Ngày chỉnh sửa cuối cùng',
        summaryIntroduction: 'Tóm tắt/Giới thiệu',
      },
      notion: {
        title: 'Tiêu đề',
        language: 'Ngôn ngữ',
        author: 'Tác giả',
        createdTime: 'Thời gian tạo',
        lastModifiedTime: 'Thời gian chỉnh sửa cuối cùng',
        url: 'URL',
        tag: 'Thẻ',
        description: 'Mô tả',
      },
      github: {
        repoName: 'Tên kho lưu trữ',
        repoDesc: 'Mô tả kho lưu trữ',
        repoOwner: 'Chủ sở hữu kho lưu trữ',
        fileName: 'Tên tệp',
        filePath: 'Đường dẫn tệp',
        programmingLang: 'Ngôn ngữ lập trình',
        url: 'URL',
        license: 'Giấy phép',
        lastCommitTime: 'Thời gian commit cuối cùng',
        lastCommitAuthor: 'Tác giả commit cuối cùng',
      },
      originInfo: {
        originalFilename: 'Tên tệp gốc',
        originalFileSize: 'Kích thước tệp gốc',
        uploadDate: 'Ngày tải lên',
        lastUpdateDate: 'Ngày cập nhật cuối cùng',
        source: 'Nguồn',
      },
      technicalParameters: {
        segmentSpecification: 'Đặc tả các đoạn',
        segmentLength: 'Chiều dài các đoạn',
        avgParagraphLength: 'Độ dài trung bình của đoạn',
        paragraphs: 'Các đoạn',
        hitCount: 'Số lần truy vấn',
        embeddingTime: 'Thời gian nhúng',
        embeddedSpend: 'Chi phí nhúng',
      },
    },
    languageMap: {
      zh: 'Tiếng Trung',
      en: 'Tiếng Anh',
      es: 'Tiếng Tây Ban Nha',
      fr: 'Tiếng Pháp',
      de: 'Tiếng Đức',
      ja: 'Tiếng Nhật',
      ko: 'Tiếng Hàn',
      ru: 'Tiếng Nga',
      ar: 'Tiếng Ả Rập',
      pt: 'Tiếng Bồ Đào Nha',
      it: 'Tiếng Ý',
      nl: 'Tiếng Hà Lan',
      pl: 'Tiếng Ba Lan',
      sv: 'Tiếng Thụy Điển',
      tr: 'Tiếng Thổ Nhĩ Kỳ',
      he: 'Tiếng Do Thái',
      hi: 'Tiếng Hindi',
      da: 'Tiếng Đan Mạch',
      fi: 'Tiếng Phần Lan',
      no: 'Tiếng Na Uy',
      hu: 'Tiếng Hungary',
      el: 'Tiếng Hy Lạp',
      cs: 'Tiếng Séc',
      th: 'Tiếng Thái',
      id: 'Tiếng Indonesia',
    },
    categoryMap: {
      book: {
        fiction: 'Hư cấu',
        biography: 'Tiểu sử',
        history: 'Lịch sử',
        science: 'Khoa học',
        technology: 'Công nghệ',
        education: 'Giáo dục',
        philosophy: 'Triết học',
        religion: 'Tôn giáo',
        socialSciences: 'Khoa học xã hội',
        art: 'Nghệ thuật',
        travel: 'Du lịch',
        health: 'Sức khỏe',
        selfHelp: 'Tự giúp bản thân',
        businessEconomics: 'Kinh doanh và kinh tế',
        cooking: 'Nấu ăn',
        childrenYoungAdults: 'Trẻ em và thanh thiếu niên',
        comicsGraphicNovels: 'Truyện tranh và tiểu thuyết đồ họa',
        poetry: 'Thơ',
        drama: 'Kịch',
        other: 'Khác',
      },
      personalDoc: {
        notes: 'Ghi chú',
        blogDraft: 'Nháp Blog',
        diary: 'Nhật ký',
        researchReport: 'Báo cáo nghiên cứu',
        bookExcerpt: 'Trích đoạn sách',
        schedule: 'Lịch trình',
        list: 'Danh sách',
        projectOverview: 'Tổng quan dự án',
        photoCollection: 'Bộ sưu tập ảnh',
        creativeWriting: 'Viết sáng tạo',
        codeSnippet: 'Đoạn mã',
        designDraft: 'Bản dựng thiết kế',
        personalResume: 'Sơ yếu lý lịch cá nhân',
        other: 'Khác',
      },
      businessDoc: {
        meetingMinutes: 'Biên bản cuộc họp',
        researchReport: 'Báo cáo nghiên cứu',
        proposal: 'Đề xuất',
        employeeHandbook: 'Sổ tay nhân viên',
        trainingMaterials: 'Tài liệu đào tạo',
        requirementsDocument: 'Tài liệu yêu cầu',
        designDocument: 'Tài liệu thiết kế',
        productSpecification: 'Thông số sản phẩm',
        financialReport: 'Báo cáo tài chính',
        marketAnalysis: 'Phân tích thị trường',
        projectPlan: 'Kế hoạch dự án',
        teamStructure: 'Cấu trúc nhóm',
        policiesProcedures: 'Chính sách và quy trình',
        contractsAgreements: 'Hợp đồng và thoả thuận',
        emailCorrespondence: 'Thư tín',
        other: 'Khác',
      },
    },
  },
  embedding: {
    processing: 'Đang nhúng...',
    paused: 'Đã tạm dừng việc nhúng',
    completed: 'Hoàn tất việc nhúng',
    error: 'Lỗi khi nhúng',
    docName: 'Đang xử lý văn bản',
    mode: 'Quy tắc phân đoạn',
    segmentLength: 'Chiều dài các đoạn',
    textCleaning: 'Định nghĩa và làm sạch Văn bản',
    segments: 'Đoạn',
    highQuality: 'Chế độ chất lượng cao',
    economy: 'Chế độ tiết kiệm',
    estimate: 'Ước lượng tiêu thụ',
    stop: 'Dừng xử lý',
    resume: 'Tiếp tục xử lý',
    automatic: 'Tự động',
    custom: 'Tùy chỉnh',
    previewTip: 'Xem trước đoạn sẽ có sẵn sau khi việc nhúng hoàn tất',
  },
  segment: {
    paragraphs: 'Đoạn',
    keywords: 'Từ khóa',
    addKeyWord: 'Thêm từ khóa',
    keywordError: 'Độ dài tối đa của từ khóa là 20',
    characters: 'ký tự',
    hitCount: 'Số lần truy vấn',
    vectorHash: 'Băm vector: ',
    questionPlaceholder: 'thêm câu hỏi ở đây',
    questionEmpty: 'Câu hỏi không thể trống',
    answerPlaceholder: 'thêm câu trả lời ở đây',
    answerEmpty: 'Câu trả lời không thể trống',
    contentPlaceholder: 'thêm nội dung ở đây',
    contentEmpty: 'Nội dung không thể trống',
    newTextSegment: 'Đoạn văn mới',
    newQaSegment: 'Đoạn câu hỏi & trả lời mới',
    delete: 'Xóa đoạn này?',
  },
}

export default translation
