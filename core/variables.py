# Словарь: имя_переменной → русский ярлык для формы
VARIABLE_LABELS: dict[str, str] = {
    # ── Реквизиты договора ────────────────────────────────────────────────
    "nomer_dogovora":             "Номер договора",
    "gorod":                      "Город",
    "den":                        "День (число)",
    "mesyac":                     "Месяц",
    "god":                        "Год",

    # ── Сторона 1 / Продавец ─────────────────────────────────────────────
    "suf_prodavec":               "Гражданин / Гражданка (Продавец)",
    "fio_prodavec":               "ФИО Продавца",
    "den_rozhd_prodavec":         "День рождения Продавца",
    "mesyac_rozhd_prodavec":      "Месяц рождения Продавца",
    "god_rozhd_prodavec":         "Год рождения Продавца",
    "mesto_rozhd_prodavec":       "Место рождения Продавца",
    "pol_prodavec":               "Пол Продавца (М / Ж)",
    "pasport_seriya_prodavec":    "Серия паспорта Продавца",
    "pasport_nomer_prodavec":     "Номер паспорта Продавца",
    "pasport_vidan_prodavec":     "Кем выдан паспорт Продавца",
    "pasport_kod_prodavec":       "Код подразделения (Продавец)",
    "okonch_prodavec":            "Зарегистрирован/а (Продавец, -а/-)",
    "adres_prodavec":             "Адрес регистрации Продавца",
    "okonch_im_prodavec":         "Именуем/ая (Продавец, -ый/-ая)",

    # ── Сторона 2 / Покупатель ───────────────────────────────────────────
    "pol_pokupatel":              "Гражданин/ка (Покупатель, ин/ка)",
    "fio_pokupatel":              "ФИО Покупателя",
    "den_rozhd_pokupatel":        "День рождения Покупателя",
    "mesyac_rozhd_pokupatel":     "Месяц рождения Покупателя",
    "god_rozhd_pokupatel":        "Год рождения Покупателя",
    "mesto_rozhd_pokupatel":      "Место рождения Покупателя",
    "pol_pokupatel_pol":          "Пол Покупателя (М / Ж)",
    "pasport_seriya_pokupatel":   "Серия паспорта Покупателя",
    "pasport_nomer_pokupatel":    "Номер паспорта Покупателя",
    "pasport_vidan_pokupatel":    "Кем выдан паспорт Покупателя",
    "pasport_kod_pokupatel":      "Код подразделения (Покупатель)",
    "okonch_pokupatel":           "Зарегистрирован/а (Покупатель, -а/-)",
    "adres_pokupatel":            "Адрес регистрации Покупателя",
    "okonch_im_pokupatel":        "Именуем/ая (Покупатель, -ый/-ая)",

    # ── Сторона 1 мены ───────────────────────────────────────────────────
    "fio_storona1":               "ФИО Стороны 1",
    "adres_storona1":             "Адрес Стороны 1",
    "adres_storona1_dop":         "Адрес Стороны 1 (продолжение)",
    "pasport_seriya_storona1":    "Серия паспорта Стороны 1",
    "pasport_nomer_storona1":     "Номер паспорта Стороны 1",
    "pasport_vidan_storona1":     "Кем выдан паспорт Стороны 1",
    "telefon_storona1":           "Телефон Стороны 1",
    "email_storona1":             "Email Стороны 1",
    "schet_storona1":             "Расчётный счёт Стороны 1",

    # ── Сторона 2 мены ───────────────────────────────────────────────────
    "fio_storona2":               "ФИО Стороны 2",
    "adres_storona2":             "Адрес Стороны 2",
    "adres_storona2_dop":         "Адрес Стороны 2 (продолжение)",
    "pasport_seriya_storona2":    "Серия паспорта Стороны 2",
    "pasport_nomer_storona2":     "Номер паспорта Стороны 2",
    "pasport_vidan_storona2":     "Кем выдан паспорт Стороны 2",
    "telefon_storona2":           "Телефон Стороны 2",
    "email_storona2":             "Email Стороны 2",
    "schet_storona2":             "Расчётный счёт Стороны 2",

    # ── Наймодатель ──────────────────────────────────────────────────────
    "fio_namodatel":              "ФИО Наймодателя",
    "den_rozhd_namodatel":        "День рождения Наймодателя",
    "mesyac_rozhd_namodatel":     "Месяц рождения Наймодателя",
    "god_rozhd_namodatel":        "Год рождения Наймодателя",
    "mesto_rozhd_namodatel":      "Место рождения Наймодателя",
    "pol_namodatel":              "Пол Наймодателя (ин/ка)",
    "pasport_seriya_namodatel":   "Серия паспорта Наймодателя",
    "pasport_nomer_namodatel":    "Номер паспорта Наймодателя",
    "pasport_vidan_namodatel":    "Кем выдан паспорт Наймодателя",
    "pasport_kod_namodatel":      "Код подразделения (Наймодатель)",
    "okonch_namodatel":           "Зарегистрирован/а (Наймодатель)",
    "adres_namodatel":            "Адрес регистрации Наймодателя",
    "polnomochie_namodatel":      "Полномочие Наймодателя (реквизиты документа)",
    "osnovanie_prava_namodatel":  "Основание права Наймодателя",

    # ── Наниматель ───────────────────────────────────────────────────────
    "fio_nanimatel":              "ФИО Нанимателя",
    "den_rozhd_nanimatel":        "День рождения Нанимателя",
    "mesyac_rozhd_nanimatel":     "Месяц рождения Нанимателя",
    "god_rozhd_nanimatel":        "Год рождения Нанимателя",
    "mesto_rozhd_nanimatel":      "Место рождения Нанимателя",
    "pol_nanimatel":              "Пол Нанимателя (ин/ка)",
    "pasport_seriya_nanimatel":   "Серия паспорта Нанимателя",
    "pasport_nomer_nanimatel":    "Номер паспорта Нанимателя",
    "pasport_vidan_nanimatel":    "Кем выдан паспорт Нанимателя",
    "pasport_kod_nanimatel":      "Код подразделения (Наниматель)",
    "okonch_nanimatel":           "Зарегистрирован/а (Наниматель)",
    "adres_nanimatel":            "Адрес регистрации Нанимателя",

    # ── Ссудодатель / Ссудополучатель (безвозмездное) ────────────────────
    "fio_ssudodatel":             "ФИО Ссудодателя",
    "den_rozhd_ssudodatel":       "День рождения Ссудодателя",
    "mesyac_rozhd_ssudodatel":    "Месяц рождения Ссудодателя",
    "god_rozhd_ssudodatel":       "Год рождения Ссудодателя",
    "mesto_rozhd_ssudodatel":     "Место рождения Ссудодателя",
    "pol_ssudodatel":             "Пол Ссудодателя (ин/ка)",
    "pasport_seriya_ssudodatel":  "Серия паспорта Ссудодателя",
    "pasport_nomer_ssudodatel":   "Номер паспорта Ссудодателя",
    "pasport_vidan_ssudodatel":   "Кем выдан паспорт Ссудодателя",
    "pasport_kod_ssudodatel":     "Код подразделения (Ссудодатель)",
    "okonch_ssudodatel":          "Зарегистрирован/а (Ссудодатель)",
    "adres_ssudodatel":           "Адрес регистрации Ссудодателя",
    "fio_ssudopoluchatel":        "ФИО Ссудополучателя",
    "den_rozhd_ssudopoluchatel":  "День рождения Ссудополучателя",
    "mesyac_rozhd_ssudopoluchatel": "Месяц рождения Ссудополучателя",
    "god_rozhd_ssudopoluchatel":  "Год рождения Ссудополучателя",
    "mesto_rozhd_ssudopoluchatel": "Место рождения Ссудополучателя",
    "pol_ssudopoluchatel":        "Пол Ссудополучателя (ин/ка)",
    "pasport_seriya_ssudopoluchatel": "Серия паспорта Ссудополучателя",
    "pasport_nomer_ssudopoluchatel": "Номер паспорта Ссудополучателя",
    "pasport_vidan_ssudopoluchatel": "Кем выдан паспорт Ссудополучателя",
    "pasport_kod_ssudopoluchatel": "Код подразделения (Ссудополучатель)",
    "okonch_ssudopoluchatel":     "Зарегистрирован/а (Ссудополучатель)",
    "adres_ssudopoluchatel":      "Адрес регистрации Ссудополучателя",

    # ── Объект: квартира / помещение ─────────────────────────────────────
    "tip_pomeshheniya":           "Тип помещения (квартира/дом/часть)",
    "etazh":                      "Этаж",
    "adres_kvartiry":             "Адрес квартиры / помещения",
    "obshaya_ploshhad":           "Общая площадь (кв. м)",
    "zhilaya_ploshhad":           "Жилая площадь (кв. м)",
    "kolichestvo_komnat":         "Количество комнат",
    "kadastrovyj_nomer":          "Кадастровый номер",
    "kadastrovyj_uslovnyj_nomer": "Кадастровый/условный номер (прилож.)",
    "nomer_pril_kv":              "Номер приложения (план квартиры)",

    # Квартира 1 мены
    "etazh_kv1":                  "Этаж (Квартира 1)",
    "adres_kv1":                  "Адрес Квартиры 1",
    "obshaya_ploshhad_kv1":       "Общая площадь Квартиры 1 (кв. м)",
    "zhilaya_ploshhad_kv1":       "Жилая площадь Квартиры 1 (кв. м)",
    "kolichestvo_komnat_kv1":     "Количество комнат (Квартира 1)",
    "kadastrovyj_nomer_kv1":      "Кадастровый номер Квартиры 1",
    "nomer_pril_kv1":             "Номер приложения (план Кв. 1)",

    # Квартира 2 мены
    "etazh_kv2":                  "Этаж (Квартира 2)",
    "adres_kv2":                  "Адрес Квартиры 2",
    "obshaya_ploshhad_kv2":       "Общая площадь Квартиры 2 (кв. м)",
    "zhilaya_ploshhad_kv2":       "Жилая площадь Квартиры 2 (кв. м)",
    "kolichestvo_komnat_kv2":     "Количество комнат (Квартира 2)",
    "kadastrovyj_nomer_kv2":      "Кадастровый номер Квартиры 2",
    "nomer_pril_kv2":             "Номер приложения (план Кв. 2)",

    # ── Право собственности ──────────────────────────────────────────────
    "osnovanie_prava":            "Основание права собственности",
    "data_osnovaniya":            "Дата документа-основания",
    "svid_seriya":                "Серия свидетельства о регистрации",
    "svid_nomer":                 "Номер свидетельства о регистрации",
    "svid_data":                  "Дата свидетельства о регистрации",
    "rosreestr_region":           "Регион Росреестра (напр. Москве)",
    "data_zapisi":                "Дата записи в ЕГРН",
    "nomer_zapisi":               "Номер записи регистрации",
    "data_vydachi_svid":          "Дата выдачи свидетельства",

    # Право собственности — Сторона 1 мены
    "osnovanie_prava_storona1":   "Основание права Стороны 1",
    "data_osnovaniya_storona1":   "Дата документа-основания (Ст. 1)",
    "svid_nomer_storona1":        "Номер свидетельства (Ст. 1)",
    "svid_data_storona1":         "Дата свидетельства (Ст. 1)",
    "data_zapisi_storona1":       "Дата записи ЕГРН (Ст. 1)",
    "nomer_zapisi_storona1":      "Номер записи ЕГРН (Ст. 1)",

    # Право собственности — Сторона 2 мены
    "osnovanie_prava_storona2":   "Основание права Стороны 2",
    "data_osnovaniya_storona2":   "Дата документа-основания (Ст. 2)",
    "svid_nomer_storona2":        "Номер свидетельства (Ст. 2)",
    "svid_data_storona2":         "Дата свидетельства (Ст. 2)",
    "data_zapisi_storona2":       "Дата записи ЕГРН (Ст. 2)",
    "nomer_zapisi_storona2":      "Номер записи ЕГРН (Ст. 2)",

    # ЕГРН для найма
    "den_zapisi":                 "День записи ЕГРН",
    "mesyac_zapisi":              "Месяц записи ЕГРН",
    "god_zapisi":                 "Год записи ЕГРН",
    "den_vyposki":                "День выписки ЕГРН",
    "mesyac_vyposki":             "Месяц выписки ЕГРН",
    "god_vyposki":                "Год выписки ЕГРН",
    "nomer_vyposki":              "Номер выписки ЕГРН",
    "nomer_pril_vypiska":         "Номер приложения (выписка ЕГРН)",

    # ── Цена и расчёты ───────────────────────────────────────────────────
    "cena_cifr":                  "Цена в цифрах (руб.)",
    "cena_prop":                  "Цена прописью (руб.)",
    "srok_oplaty_cifr":           "Срок оплаты (цифра, дней)",
    "srok_oplaty_prop":           "Срок оплаты (прописью)",
    "srok_oplaty_data":           "Крайняя дата оплаты",
    "data_ispolneniya_oplaty":    "Дата исполнения оплаты",
    "stoimost_nayma":             "Стоимость найма (руб./мес.)",
    "stoimost_nayma_prop":        "Стоимость найма прописью",
    "poryadok_oplaty":            "Способ и сроки оплаты",
    "poryadok_perechisleniya":    "Порядок перечисления",
    "kommunalnye_uslugi":         "Перечень коммунальных услуг",
    "srok_kommunalnyh":           "Порядок и сроки оплаты коммунальных",
    "razmer_obespecheniya":       "Размер обеспечительного платежа (руб.)",
    "srok_obespecheniya":         "Срок внесения обеспечительного платежа",
    "usloviya_uderzhaniya":       "Условия удержания обеспечительного",

    # ── Сроки и условия ──────────────────────────────────────────────────
    "srok_nayma":                 "Срок найма (менее 1 года)",
    "nomer_pril_akt":             "Номер приложения (Акт передачи)",
    "srok_peredachi_cifr":        "Срок передачи (цифра)",
    "srok_peredachi_edinitsa":    "Единица срока (дней/рабочих)",
    "srok_peredachi_pomeshheniya": "Срок передачи помещения",
    "sostoyanie_kvartiry":        "Состояние квартиры при передаче",
    "imushhestvo_ostaetsya":      "Имущество, остающееся в квартире",
    "zaregistrirovannye_lica":    "Зарегистрированные лица (Кв. 1 / Продавца)",
    "zaregistrirovannye_lica_kv2": "Зарегистрированные лица (Кв. 2)",
    "srok_remonta":               "Сроки ремонта",
    "tekushij_remont_opredelenie": "Определение текущего ремонта",
    "kapitalnyj_remont_opredelenie": "Определение капитального ремонта",
    "iznos_procent":              "Нормальный износ (%)",
    "srok_vozvrata_pomeshheniya": "Срок возврата помещения",
    "chastota_proverki":          "Частота проверок помещения",
    "obremeneniya":               "Сведения об обременениях",

    # ── Ответственность ──────────────────────────────────────────────────
    "peni_procent":               "Размер пени (% в день/год)",
    "peni_cifr":                  "Пени в цифрах (руб.)",
    "peni_prop":                  "Пени прописью (руб.)",
    "peni_peredacha":             "Пени за несвоевременную передачу (%)",
    "srok_ustraneniya_nedostatkov": "Срок устранения недостатков",
    "srok_ustranenia_nedostatkov": "Срок устранения недостатков",
    "moment_nachala_sroka":       "Момент начала срока устранения",
    "srok_ustranen":              "Срок устранения просрочки",
    "srok_peredachi_narusheniya": "Срок передачи при нарушении",

    # ── Регистрация ──────────────────────────────────────────────────────
    "nazvanie_organa_registracii": "Название органа регистрации прав",

    # ── Дополнительные поля (купли-продажа, мены, найм) ──────────────────
    "telefon_prodavec":           "Телефон Продавца",
    "email_prodavec":             "Email Продавца",
    "telefon_pokupatel":          "Телефон Покупателя",
    "email_pokupatel":            "Email Покупателя",

    "peni_pokupatel":             "Пени Покупателя (руб.)",
    "peni_prodavec_nedostatki":   "Пени Продавца за недостатки (руб.)",
    "peni_prodavec_peredacha":    "Пени Продавца за несвоевременную передачу",

    "nomer_doma":                 "Номер дома",
    "korpus":                     "Корпус / строение",
    "nomer_kvartiry":             "Номер квартиры",
    "tip_doma":                   "Тип дома (кирпичный, панельный и т.д.)",
    "tip_sobstvennosti":          "Вид собственности (общая долевая и т.д.)",
    "kadastrovyj_nomer_zemli":    "Кадастровый номер земельного участка",

    "stoimost_cifr":              "Стоимость в цифрах (руб.)",
    "stoimost_prop":              "Стоимость прописью (руб.)",
    "oplata_cifr":                "Оплата в цифрах (руб.)",
    "oplata_prop":                "Оплата прописью (руб.)",
    "doplata_cifr":               "Доплата в цифрах (руб.)",
    "doplata_prop":               "Доплата прописью (руб.)",
    "stoimost_kv1_cifr":          "Стоимость Квартиры 1 в цифрах (руб.)",
    "stoimost_kv1_prop":          "Стоимость Квартиры 1 прописью (руб.)",
    "stoimost_kv2_cifr":          "Стоимость Квартиры 2 в цифрах (руб.)",
    "stoimost_kv2_prop":          "Стоимость Квартиры 2 прописью (руб.)",
    "sposob_oplaty":              "Способ оплаты (наличные/безналичные)",
    "kto_platit_rashody":         "Кто несёт расходы по регистрации",

    "nomer_osnovaniya":           "Номер документа-основания",
    "den_osnovaniya":             "День документа-основания",
    "mesyac_osnovaniya":          "Месяц документа-основания",
    "nomer_resheniya":            "Номер решения суда / органа",
    "den_resheniya":              "День решения суда",
    "mesyac_resheniya":           "Месяц решения суда",
    "god_resheniya":              "Год решения суда",
    "nomer_vypisi":               "Номер выписки из реестра",
    "data_vypisi":                "Дата выписки из реестра",
    "nomer_pril_priemka":         "Номер приложения (Акт приёмки)",
    "nomer_pril_vozvrat":         "Номер приложения (Акт возврата)",
    "dop_prilozhenie":            "Дополнительное приложение",
    "dokumenty_prinadlezhnosti":  "Документы принадлежности",

    "sobstvennik":                "Собственник (ФИО)",
    "sobstvennik_dop":            "Собственник (дополнительно)",
    "osnovanie_polnom":           "Основание полномочий представителя",
    "nazvanie_organa":            "Название органа (сокращённо)",

    "moment_peredachi_riska":     "Момент перехода риска случайной гибели",
    "srok_forsmazhor":            "Срок уведомления о форс-мажоре",

    # Члены семьи / жильцы
    "zhilec_1":                   "Жилец 1 (ФИО и дата рождения)",
    "zhilec_2":                   "Жилец 2 (ФИО и дата рождения)",
    "zhilec_3":                   "Жилец 3 (ФИО и дата рождения)",
    "chlen_semi_1":               "Член семьи 1 (ФИО)",
    "chlen_semi_2":               "Член семьи 2 (ФИО)",
    "chlen_semi_3":               "Член семьи 3 (ФИО)",

    # Сторона 1/2 дополнительные поля (мены)
    "pol_storona1":               "Пол Стороны 1 (ин/ка)",
    "pol_storona2":               "Пол Стороны 2 (ин/ка)",
    "den_rozhd_storona1":         "День рождения Стороны 1",
    "mesyac_rozhd_storona1":      "Месяц рождения Стороны 1",
    "god_rozhd_storona1":         "Год рождения Стороны 1",
    "mesto_rozhd_storona1":       "Место рождения Стороны 1",
    "den_rozhd_storona2":         "День рождения Стороны 2",
    "mesyac_rozhd_storona2":      "Месяц рождения Стороны 2",
    "god_rozhd_storona2":         "Год рождения Стороны 2",
    "mesto_rozhd_storona2":       "Место рождения Стороны 2",
    "pasport_kod_storona1":       "Код подразделения (Сторона 1)",
    "pasport_kod_storona2":       "Код подразделения (Сторона 2)",
    "okonch_im_storona1":         "Именуем/ая (Сторона 1, -ый/-ая)",
    "okonch_im_storona2":         "Именуем/ая (Сторона 2, -ый/-ая)",

    # Сроки окончания
    "den_okonch":                 "День окончания срока",
    "mesyac_okonch":              "Месяц окончания срока",
    "god_okonch":                 "Год окончания срока",

    # Паспортные данные найма (полная дата выдачи)
    "pasport_data_vid_namodatel": "Дата выдачи паспорта Наймодателя",
    "pasport_data_vid_nanimatel": "Дата выдачи паспорта Нанимателя",

    # ── Метки из «таблицы разметки» юриста (договоры по отчуждению) ─────
    "adres_cedent":                "Адрес цедента",
    "adres_cedent_dop":            "Адрес цедента",
    "adres_cessionarij":           "Адрес цессионария",
    "adres_daritel":               "Адрес дарителя",
    "adres_doma":                  "Адрес многоквартирного дома",
    "adres_platelschik_renty":     "Адрес плательщика ренты",
    "adres_prozhivaniya_prodavec": "Адрес проживания продавца на момент акта",
    "bank_cedent":                 "Банк цедента",
    "bank_cessionarij":            "Банк цессионария",
    "bik_cedent":                  "БИК цедента",
    "bik_cessionarij":             "БИК цессионария",
    "data_dogovora":               "Дата договора",
    "data_egrn":                   "Дата выписки ЕГРН",
    "data_soglasiya_supruga":      "Дата согласия супруга",
    "data_vydachi":                "Дата выдачи",
    "ddu_den":                     "День заключения ДДУ",
    "ddu_god":                     "Год заключения ДДУ",
    "ddu_mesyac":                  "Месяц заключения ДДУ",
    "ddu_nomer":                   "Номер ДДУ",
    "den_akta":                    "День подписания акта (число)",
    "den_rozhd_daritel":           "День рождения дарителя",
    "den_rozhd_platelschik_renty": "День рождения плательщика ренты",
    "den_rozhd_zaregistrirovannykh_lits": "День рождения зарегестрированного лица",
    "email_cedent":                "E-mail цедента",
    "email_cessionarij":           "E-mail цессионария",
    "email_platelschik_renty":     "E-mail плательщика ренты",
    "email_poluchatel_renty":      "E-mail получателя ренты",
    "fio_cedent":                  "Ф.И.О. цедента",
    "fio_cessionarij":             "Ф.И.О. цессионария",
    "fio_daritel":                 "Фио дарителя",
    "fio_notariusa":               "Ф.И.О. нотариуса",
    "fio_platelschik_renty":       "Ф.И.О. плательщика ренты",
    "fio_poluchatel_renty":        "Ф.И.О. получателя ренты",
    "fio_zaregistrirovannykh_lits": "Ф.И.О. зарегестрированного лица",
    "god_akta":                    "Год подписания акта",
    "god_rozhd_daritel":           "Год рождения дарителя",
    "god_rozhd_platelschik_renty": "Год рождения плательщика ренты",
    "god_rozhd_zaregistrirovannykh_lits": "Год рождения зарегестрированного лица",
    "inn_cedent":                  "ИНН цедента",
    "inn_cessionarij":             "ИНН цессионария",
    "inye_dokumenty":              "Иные передаваемые документы",
    "kadastrovyj_nomer_uchastka":  "Кадастровый номер земельного участка",
    "kolichestvo_etazhey":         "Количество этажей",
    "kpp_cedent":                  "КПП цедента",
    "kpp_cessionarij":             "КПП цессионария",
    "ks_cedent":                   "Корреспондентский счёт цедента",
    "ks_cessionarij":              "Корреспондентский счёт цессионария",
    "mesto_rozhd_daritel":         "Место рождения дарителя",
    "mesto_rozhd_platelschik_renty": "Место рождения плательщика ренты",
    "mesyac_akta":                 "Месяц подписания акта",
    "mesyac_rozhd_daritel":        "Месяц рождения дарителя",
    "mesyac_rozhd_platelschik_renty": "Месяц рождения плательщика ренты",
    "mesyac_rozhd_zaregistrirovannykh_lits": "Месяц рождения зарегестрированного лица",
    "naimenovanie_cedent":         "Наименование / Ф.И.О. цедента",
    "naimenovanie_cessionarij":    "Наименование / Ф.И.О. цессионария",
    "naimenovanie_i_rekvizity_pravoustanavlivayushchego_dokumenta": "Наименование и реквизиты правоустанавливающего документа",
    "naimenovanie_organa_registratsii_prav": "Наименование органа регистрации прав",
    "naimenovanie_vydavshego_organa": "Наименование выдавшего органа",
    "naimenovanie_zastrojshhik":   "Наименование застройщика",
    "naselennyj_punkt":            "Населённый пункт",
    "nomer_akt_app":               "Номер приложения (акт приёма-передачи)",
    "nomer_pril_akt_priema":       "Номер приложения — акт приёма-передачи",
    "nomer_pril_akt_raschet":      "Номер приложения — акт о взаиморасчётах",
    "oblast":                      "Область",
    "obshaya_ploshhad_prop":       "Общая площадь (прописью)",
    "ogrn_cedent":                 "ОГРН/ОГРНИП цедента",
    "ogrn_cessionarij":            "ОГРН/ОГРНИП цессионария",
    "okonch_act_cessionarij":      "Окончание в «действующий» для цессионария",
    "okonch_daritel":              "Окончание (зарегистрирован / зарегистрирована)",
    "okonch_im_cessionarij":       "Окончание в «именуемый» для цессионария",
    "okonch_im_daritel":           "Окончание в именовании дарителя",
    "okonch_im_zastrojshhik":      "Окончание в «именуемый» для застройщика",
    "okonch_platelschik_renty":    "Окончание в именовании плательщика ренты",
    "okpo_cedent":                 "ОКПО цедента",
    "okpo_cessionarij":            "ОКПО цессионария",
    "organ_registracii":           "Наименование органа регистрации прав",
    "osnovanie_polnomochij_cedent": "Основание полномочий цедента",
    "osnovanie_polnomochij_cessionarij": "Основание полномочий цессионария",
    "osnovanie_stroitelstva":      "Основание строительства",
    "pasport_cedent":              "Паспортные данные цедента",
    "pasport_cedent_dop":          "Паспортные данные цедента (доп. строка)",
    "pasport_cessionarij":         "Паспортные данные цессионария",
    "pasport_cessionarij_dop":     "Паспортные данные цессионария",
    "pasport_kod_platelschik_renty": "Код подразделения плательщика ренты",
    "pasport_kod_prodavets":       "Код подразделения (Продавец)",
    "pasport_nomer_daritel":       "Номер паспорта дарителя",
    "pasport_nomer_platelschik_renty": "Номер паспорта плательщика ренты",
    "pasport_seriya_daritel":      "Серия паспорта дарителя",
    "pasport_seriya_platelschik_renty": "Серия паспорта плательщика ренты",
    "pasport_vidan_daritel":       "Когда паспорт выдан",
    "pasport_vidan_platelschik_renty": "Выдан паспорт плательщика ренты",
    "pasport_vydan_data_pokupatel": "Дата выдачи паспорта покупателя",
    "pasport_vydan_data_prodavec": "Дата выдачи паспорта продавца",
    "pasport_vydan_kem_pokupatel": "Кем выдан паспорт покупателя",
    "pasport_vydan_kem_prodavec":  "Кем выдан паспорт продавца",
    "platezh_den":                 "День платежа (число)",
    "platezh_god":                 "Год платежа",
    "platezh_mesyac":              "Месяц платежа",
    "platezhka_den":               "День платёжного поручения (число)",
    "platezhka_god":               "Год платёжного поручения",
    "platezhka_mesyac":            "Месяц платёжного поручения",
    "platezhka_nomer":             "Номер платёжного поручения",
    "ploshhad_uchastka":           "Площадь земельного участка",
    "podpis_cedent":               "Подпись цедента",
    "podpis_cessionarij":          "Подпись цессионария",
    "podpis_platelschika_renty":   "Подпись плательщика ренты",
    "podpis_pokupatel":            "Подпись покупателя",
    "podpis_poluchatelya_renty":   "Подпись получателя ренты",
    "podpis_prodavec":             "Подпись продавца",
    "pol_daritel":                 "Пол ( где гражданин / гражданка) дарителя",
    "pol_platelschik_renty":       "Пол ( где гражданин / гражданка) плательщика ренты",
    "pol_poluchatel_renty":        "Пол ( где гражданин / гражданка) получатель ренты",
    "pol_zaregistrirovannykh_lits": "Пол ( где гражданин / гражданка) зарегестрированное лицо",
    "pravoustanavlivayushhij_dokument": "Правоустанавливающий документ",
    "predstavitel_cedent":         "Должность, Ф.И.О. представителя цедента",
    "predstavitel_cessionarij":    "Должность, Ф.И.О. представителя цессионария",
    "punkt_ddu_peredacha":         "Пункт ДДУ о передаче объекта",
    "punkt_ddu_uvedomlenie":       "Пункт ДДУ об уведомлении застройщика",
    "registracionnyj_nomer_egrn":  "Регистрационный номер ЕГРН",
    "rs_cedent":                   "Расчётный счёт цедента",
    "rs_cessionarij":              "Расчётный счёт цессионария",
    "rs_platelschik_renty":        "Счет плательщика ренты",
    "rs_poluchatel_renty":         "Счет получателя ренты",
    "schet_cedent":                "Счёт цедента",
    "schet_cessionarij":           "Счёт цессионария",
    "srok_oplaty_den":             "День срока оплаты",
    "srok_oplaty_dnej":            "Срок оплаты, дней (цифрой)",
    "srok_oplaty_dnej_prop":       "Срок оплаты, дней (прописью)",
    "srok_oplaty_god":             "Год срока оплаты",
    "srok_oplaty_mesyac":          "Месяц срока оплаты",
    "srok_peredachi_dokumentov":   "Срок передачи документов",
    "srok_registracii":            "Срок регистрации договора",
    "srok_uvedomleniya":           "Срок уведомления застройщика",
    "storona_registracii":         "Сторона, осуществляющая регистрацию",
    "telefon_cedent":              "Телефон цедента",
    "telefon_cessionarij":         "Телефон цессионария",
    "telefon_platelschik_renty":   "Телефон плательщика ренты",
    "telefon_poluchatel_renty":    "Телефон получателя ренты",
    "udostoveritelnaya_nadpis_notariusa": "Удостоверительная надпись нотариуса",
    "ulica":                       "Улица",
    "zhilaya_ploshhad_prop":       "Жилая площадь (прописью)",
}


# Автосборка меток: префикс поля + роль стороны (родительный падеж).
# Покрывает переменные вида fio_prodavets, pasport_kod_odaryaemyj и т.п.
# без ручного перечисления — новые шаблоны подхватываются автоматически.
_LABEL_PREFIXES: list[tuple[str, str]] = [
    ("pasport_data_vid", "Дата выдачи паспорта"),
    ("pasport_seriya",   "Серия паспорта"),
    ("pasport_nomer",    "Номер паспорта"),
    ("pasport_vidan",    "Кем выдан паспорт"),
    ("pasport_vydan_data", "Дата выдачи паспорта"),
    ("pasport_vydan_kem", "Кем выдан паспорт"),
    ("pasport_kod",      "Код подразделения"),
    ("pasport",          "Паспортные данные"),
    ("den_rozhd",        "День рождения"),
    ("mesyac_rozhd",     "Месяц рождения"),
    ("god_rozhd",        "Год рождения"),
    ("mesto_rozhd",      "Место рождения"),
    ("okonch_im",        "Именуем-ый/-ая:"),
    ("okonch_act",       "Действующ-его/-ей:"),
    ("okonch_zaregistrirovan", "Зарегистрирован/-а:"),
    ("okonch",           "Окончание (-/-а):"),
    ("pol",              "Гражданин/Гражданка:"),
    ("suf",              "Гражданин/Гражданка:"),
    ("fio_podpis",       "ФИО в подписи"),
    ("fio",              "ФИО"),
    ("adres_registracii", "Адрес регистрации"),
    ("adres_prozhivaniya", "Адрес проживания"),
    ("adres",            "Адрес"),
    ("telefon",          "Телефон"),
    ("email",            "Email"),
    ("schet",            "Счёт"),
    ("rs",               "Расчётный счёт"),
    ("ks",               "Корр. счёт"),
    ("bank",             "Банк"),
    ("bik",              "БИК"),
    ("inn",              "ИНН"),
    ("kpp",              "КПП"),
    ("ogrn",             "ОГРН/ОГРНИП"),
    ("okpo",             "ОКПО"),
    ("podpis",           "Подпись"),
    ("naimenovanie",     "Наименование / ФИО"),
    ("predstavitel",     "Представитель"),
    ("osnovanie_polnomochij", "Основание полномочий"),
]

_LABEL_ROLES: dict[str, str] = {
    "prodavets": "Продавца",
    "prodavec": "Продавца",
    "prodavca": "Продавца",
    "pokupatel": "Покупателя",
    "pokupatelja": "Покупателя",
    "daritel": "Дарителя",
    "odaryaemyj": "Одаряемого",
    "storona1": "Стороны 1",
    "storona2": "Стороны 2",
    "poluchatel_renty": "Получателя ренты",
    "poluchatelya_renty": "Получателя ренты",
    "platelschik_renty": "Плательщика ренты",
    "platelschika_renty": "Плательщика ренты",
    "cedent": "Цедента",
    "cessionarij": "Цессионария",
    "zastrojshhik": "Застройщика",
    "namodatel": "Наймодателя",
    "nanimatel": "Нанимателя",
    "ssudodatel": "Ссудодателя",
    "ssudopoluchatel": "Ссудополучателя",
    "zaregistrirovannykh_lits": "зарегистрированных лиц",
}


def get_label(var_name: str) -> str:
    """Возвращает русский ярлык для переменной или красивое имя по умолчанию."""
    if var_name in VARIABLE_LABELS:
        return VARIABLE_LABELS[var_name]
    # Автосборка: префикс + роль (fio_prodavets → «ФИО Продавца»)
    v = var_name.lower()
    for prefix, prefix_label in _LABEL_PREFIXES:
        if v.startswith(prefix + "_"):
            role = v[len(prefix) + 1:]
            if role in _LABEL_ROLES:
                return f"{prefix_label} {_LABEL_ROLES[role]}"
    # Fallback: превращаем snake_case в читаемую строку
    return var_name.replace('_', ' ').capitalize()


# ── Типы полей для спец-рендеринга ───────────────────────────────────────────
# Тип определяется по префиксу имени переменной — новые шаблоны подхватываются
# автоматически, без правки кода.

# Тип поля → (display_label, docx_value)[]
FIELD_OPTIONS: dict[str, list[tuple[str, str]]] = {
    'gender_ink':  [('Мужской', 'ин'),         ('Женский', 'ка')],
    'suffix':      [('Гражданин', 'Гражданин'), ('Гражданка', 'Гражданка')],
    'okonch_im':   [('Мужской (-ый)', 'ый'),   ('Женский (-ая)', 'ая')],
    'okonch_act':  [('Мужской (-его)', 'его'), ('Женский (-ей)', 'ей')],
    'okonch':      [('Мужской (-)', ''),        ('Женский (-а)', 'а')],
}


def get_field_type(var_name: str) -> str:
    """Возвращает тип поля: 'text' | 'gender_ink' | 'suffix' | 'okonch_im' | 'okonch_act' | 'okonch'."""
    v = var_name.lower()
    # pol_* → «Граждан-ин/-ка»
    if v.startswith('pol_'):
        return 'gender_ink'
    # suf_* → «Гражданин» / «Гражданка» (слово целиком)
    if v.startswith('suf_'):
        return 'suffix'
    # okonch_im_* → «именуем-ый/-ая»
    if v.startswith('okonch_im_'):
        return 'okonch_im'
    # okonch_act_* → «действующ-его/-ей»
    if v.startswith('okonch_act_'):
        return 'okonch_act'
    # okonch_* → «зарегистрирован-/-а»
    if v.startswith('okonch_'):
        return 'okonch'
    return 'text'


# Порядок секций для формы
_SECTION_ORDER = [
    "Реквизиты договора",
    "Продавец / Наймодатель / Ссудодатель / Сторона 1",
    "Покупатель / Наниматель / Ссудополучатель / Сторона 2",
    "Объект: Квартира 1",
    "Объект: Квартира 2 (договор мены)",
    "Объект: квартира / помещение",
    "Право собственности",
    "Цена и порядок оплаты",
    "Сроки и условия",
    "Ответственность",
    "Регистрация прав",
    "Прочее",
]


def _classify(var: str) -> str:
    v = var.lower()

    # Реквизиты договора
    if v in ("nomer_dogovora", "gorod", "den", "mesyac", "god"):
        return "Реквизиты договора"

    # Стороны 1 (продавец / даритель / получатель ренты / цедент / наймодатель / …)
    if any(k in v for k in (
        "_prodavec", "_prodavets", "_prodavca", "_storona1", "_namodatel",
        "_ssudodatel", "_daritel", "_poluchatel_renty", "_poluchatelya_renty", "_cedent",
    )):
        return "Продавец / Наймодатель / Ссудодатель / Сторона 1"

    # Стороны 2 (покупатель / одаряемый / плательщик ренты / цессионарий / …)
    if any(k in v for k in (
        "_pokupatel", "_storona2", "_nanimatel", "_ssudopoluchatel",
        "_odaryaemyj", "_platelschik_renty", "_platelschika_renty", "_cessionarij",
    )):
        return "Покупатель / Наниматель / Ссудополучатель / Сторона 2"

    # Квартира 1 мены
    if v.endswith("_kv1") or v.startswith("etazh_kv1") or v.startswith("adres_kv1"):
        return "Объект: Квартира 1"

    # Квартира 2 мены
    if v.endswith("_kv2") or v.startswith("etazh_kv2") or v.startswith("adres_kv2"):
        return "Объект: Квартира 2 (договор мены)"

    # Общий объект
    if any(k in v for k in (
        "tip_pomeshh", "etazh", "adres_kvartiry", "ploshhad",
        "komnat", "kadastrov", "pomeshh", "nomer_pril_kv",
    )):
        return "Объект: квартира / помещение"

    # Право собственности
    if any(k in v for k in (
        "osnovanie_prava", "svid_", "rosreestr", "data_zapisi",
        "nomer_zapisi", "data_vydachi", "den_zapisi", "mesyac_zapisi",
        "god_zapisi", "den_vyposki", "mesyac_vyposki", "god_vyposki",
        "nomer_vyposki", "nomer_pril_vyp", "egrn", "data_osnovaniya",
        "nomer_pril_k",
    )):
        return "Право собственности"

    # Цена и оплата
    if any(k in v for k in (
        "cena", "stoimost", "oplat", "poryadok", "schet",
        "kommunaln", "obespecheni", "uderzh", "razmer_",
    )):
        return "Цена и порядок оплаты"

    # Сроки и условия
    if any(k in v for k in (
        "srok", "peredach", "vozvrat", "remont", "iznos",
        "sostoyanie", "imushhestvo", "zaregistr", "obremenen",
        "chastota", "opredelenie",
    )):
        return "Сроки и условия"

    # Ответственность
    if any(k in v for k in (
        "peni", "neust", "ustran", "moment_", "narushen",
    )):
        return "Ответственность"

    # Регистрация
    if any(k in v for k in ("registrac", "organ", "nazvanie_")):
        return "Регистрация прав"

    return "Прочее"


def group_variables(
    variables: list[str],
    post_data: dict | None = None,
    var_order: list[str] | None = None,
) -> list[tuple[str, list[dict]]]:
    """
    Возвращает список (название_секции, [поля]).
    Каждое поле: {'name', 'label', 'value', 'field_type', 'options'}.
    Если передан var_order — поля внутри секций сортируются
    по порядку первого появления в документе.
    """
    post_data = post_data or {}
    sections: dict[str, list[dict]] = {k: [] for k in _SECTION_ORDER}

    for var in variables:
        section = _classify(var)
        if section not in sections:
            section = "Прочее"
        ftype = get_field_type(var)
        sections[section].append({
            "name": var,
            "label": get_label(var),
            "value": post_data.get(var, ""),
            "field_type": ftype,
            "options": FIELD_OPTIONS.get(ftype, []),
        })

    # Сортировка внутри секций по порядку появления в документе
    if var_order:
        order_index = {v: i for i, v in enumerate(var_order)}
        for fields in sections.values():
            fields.sort(key=lambda f: order_index.get(f["name"], 9999))

    # Убираем пустые секции и возвращаем в нужном порядке
    return [(name, fields) for name, fields in sections.items() if fields]
