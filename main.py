# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
TOKEN = "8155567969:AAF4X57d0J7N6WSiHZDD9gfwWz8sHvLbPHE"

TEXTS = {
    "ru": {
        "choose_language": "Выберите язык:",
        "main_menu": "Главное меню:",
        "about_stai": "О STAI",
        "about_booking": "О бронировании",
        "house_rules": "Правила проживания",
        "payment_refunds": "Оплата и возвраты",
        "legal_docs": "Документы / Правила",
        "contact_operator": "Связаться с оператором",
        "back": "Назад",
        "operator_text": "Пока что связь с оператором ещё не подключена. Скоро здесь появится возможность написать оператору.",
        "description" : "Официальный Телеграм бот STAI  \nЕсть вопросы? Напишите нам, и наша команда ответит вам в течении 24 часов!\n -> support@stai.uz",
        "description_title" : "Описание",
        "unknown_action": "Не удалось обработать действие.",
        "welcome": "Добро пожаловать в STAI bot!",
        "website": "Наш официальный сайт: www.stai.uz",
        "sections": {
            "about_stai": {
                "title": "Раздел: О STAI",
                "questions": {
                    "what_users_can_do": {
                        "q": "Что можно делать прямо в Telegram?",
                        "a": (
                            "В Telegram-боте STAI вы можете:\n"
                            "• Найти свободные номера, дома и виллы\n"
                            "• Проверить цены и доступность\n"
                            "• Получить актуальную информацию о правилах бронирования"
                        ),
                    },
                    "what_makes_better": {
                        "q": "Почему STAI лучше других?",
                        "a": (
                            "STAI — первая платформа в Узбекистане, созданная с нуля с учётом потребностей местного рынка.\n\n"
                            "Мы предлагаем:\n"
                            "• Моментальное бронирование без звонков\n"
                            "• Прозрачные цены без скрытых комиссий\n"
                            "• Проверенных владельцев\n"
                            "• Поддержку на русском и узбекском языках\n"
                            "• Удобные инструменты для гостей и отелей\n"
                            "• Простую и быструю работу через Telegram или сайт"
                        ),
                    },
                    "what_is_stai": {
                        "q": "Что такое STAI?",
                        "a": (
                            "STAI — это современная платформа для бронирования отелей, домов отдыха и квартир по всему Узбекистану.\n\n"
                            "Мы делаем процесс поиска и бронирования быстрым, удобным и безопасным как для гостей, так и для владельцев."
                        ),
                    },
                    "why_trustworthy": {
                        "q": "Почему STAI заслуживает доверия?",
                        "a": (
                            "STAI использует:\n"
                            "• Защищённые платежи и защиту данных\n"
                            "• Только проверенных и подтверждённых владельцев\n"
                            "• Прозрачные правила отмены\n"
                            "• Подтверждение бронирования в течение нескольких секунд\n"
                            "• Систему отзывов и рейтингов\n\n"
                            "Мы стремимся стать самой надёжной платформой в Узбекистане."
                        ),
                    },
                    "website_link": {
                        "q": "Ссылка на сайт",
                        "a": "Наш официальный сайт: www.stai.uz",
                    },
                },
            },
            "about_booking": {
                "title": "Раздел: О бронировании",
                "questions": {
                    "find_room": {
                        "q": "Как найти номер?",
                        "a": (
                            "На официальном сайте:\n"
                            "• Выберите нужную локацию\n"
                            "• Укажите даты и количество гостей\n"
                            "• Вам будут показаны доступные варианты\n"
                            "• Выберите понравившийся объект и перейдите к этапу бронирования"
                        ),
                    },
                    "price_calculated": {
                        "q": "Как рассчитывается цена?",
                        "a": (
                            "Цена складывается из:\n"
                            "• Базовой стоимости за ночь\n"
                            "• Дополнительных услуг (если выбраны)\n"
                            "• Налогов и сборов (если применяются)\n"
                            "• Скидок по акциям и промокодам\n"
                            "• Правил цены на конкретные даты (праздники / высокий сезон)"
                        ),
                    },
                    "promo_codes": {
                        "q": "Как работают промокоды?",
                        "a": (
                            "• Промокод вводится при бронировании\n"
                            "• Скидка применяется автоматически\n"
                            "• У каждого промокода есть срок действия и условия\n"
                            "• Некоторые промокоды действуют только для новых пользователей"
                        ),
                    },
                    "edit_cancel": {
                        "q": "Можно ли изменить или отменить бронь?",
                        "a": (
                            "Да, если это разрешено правилами объекта.\n\n"
                            "Вы можете:\n"
                            "• Изменить даты (при наличии свободных мест)\n"
                            "• Отменить бронь\n"
                            "• Получить автоматический расчёт возврата по политике отмены"
                        ),
                    },
                },
            },

            "house_rules": {
                "title": "Раздел: Правила проживания",
                "questions": {
                    "checkin_checkout": {
                        "q": "Правила заезда / выезда",
                        "a": (
                            "Заезд: обычно после 14:00\n"
                            "Выезд: обычно до 12:00\n\n"
                            "(Конкретное время всегда указано в карточке объекта)"
                        ),
                    },
                    "guest_limits": {
                        "q": "Лимит гостей",
                        "a": (
                            "У каждого объекта есть своё максимальное количество гостей.\n"
                            "Если вы превышаете лимит, объект может отказать в размещении."
                        ),
                    },
                    "damage_deposit": {
                        "q": "Залог за повреждения",
                        "a": (
                            "Некоторые владельцы могут требовать залог за возможные повреждения.\n"
                            "Сумма залога указывается заранее.\n"
                            "Залог возвращается после выезда, если всё в порядке."
                        ),
                    },
                },
            },
            "payment_refunds": {
                "title": "Раздел: Оплата и возвраты",
                "questions": {
                    "supported_payments": {
                        "q": "Поддерживаемые способы оплаты",
                        "a": (
                            "STAI поддерживает:\n"
                            "• Карты Uzcard и Humo\n"
                            "• Международные карты (Visa/MasterCard) — после запуска\n"
                            "• Удобные локальные способы оплаты"
                        ),
                    },
                    "when_payment_captured": {
                        "q": "Когда списывается оплата?",
                        "a": "Оплата списывается в момент подтверждения бронирования.",
                    },
                    "refund_policy": {
                        "q": "Политика возврата",
                        "a": (
                            "Возврат зависит от выбранной политики отмены:\n"
                            "• Бесплатная отмена (за 7 дней до заселения) — полный возврат\n"
                            "• При отмене за 3–6 дней до заселения — возврат 50%\n"
                            "• При отмене менее чем за 48 часов — возврат 0%"
                        ),
                    },
                    "host_denies_entry": {
                        "q": "Что делать, если хозяин не пускает?",
                        "a": (
                            "Это крайне редкая ситуация, но если она случится:\n"
                            "• Вы имеете право на полный возврат денег\n"
                            "• STAI может найти альтернативный вариант\n"
                            "• Хозяин может получить штраф и быть удалён с платформы\n\n"
                            "Мы всегда защищаем наших гостей."
                        ),
                    },
                },
            },
            "legal_docs": {
                "title": "Раздел: Документы / Правила",
                "questions": {
                    "passport_id": {
                        "q": "Нужен ли паспорт или ID?",
                        "a": (
                            "Да, при заселении необходимо предъявить паспорт или ID-карту.\n"
                            "Это обязательное требование законодательства Узбекистана."
                        ),
                    },
                    "official_invoices": {
                        "q": "Предоставляет ли STAI официальные документы?",
                        "a": (
                            "Да, по запросу мы можем предоставить:\n"
                            "• Электронный чек\n"
                            "• Официальный документ для отчётности"
                        ),
                    },
                    "foreigners_registration": {
                        "q": "Правила регистрации для иностранцев",
                        "a": (
                            "Согласно правилам Узбекистана:\n"
                            "• Иностранные граждане должны быть зарегистрированы по месту проживания\n"
                            "• Регистрацию обычно оформляет сам объект размещения\n"
                            "• Гость должен предъявить паспорт при заселении"
                        ),
                    },
                },
            },
        },
    },
    "uz": {
        "choose_language": "Tilni tanlang:",
        "main_menu": "Asosiy menyu:",
        "about_stai": "STAI haqida",
        "about_booking": "Bron qilish haqida",
        "house_rules": "Yashash qoidalari",
        "payment_refunds": "To‘lov va qaytarish",
        "legal_docs": "Hujjatlar / Qoidalar",
        "contact_operator": "Operator bilan bog‘lanish",
        "back": "Orqaga",
        "operator_text": "Hozircha operator bilan bog‘lanish funksiyasi ulanmagan. Tez orada bu yerda operatorga yozish imkoniyati paydo bo‘ladi.",
        "unknown_action": "Amalni bajarib bo‘lmadi.",
        "description" : "STAI'ni rasmiy Telegram bot\nSavollaringiz bormi? Biz bilan bog'laning, jamoamiz 24 soat ichida javob beradi!\n -> support@stai.uz",
        "description_title" : "Bot haqida ma’lumot",
        "welcome": "STAI botiga xush kelibsiz!",
        "website": "Bizning rasmiy veb-saytimiz: www.stai.uz",
        "sections": {
            "about_stai": {
                "title": "Bo‘lim: STAI haqida",
                "questions": {
                    "what_users_can_do": {
                        "q": "Telegram orqali nimalarni qilish mumkin?",
                        "a": (
                            "STAI Telegram boti orqali siz quyidagilarni qilishingiz mumkin:\n"
                            "• Bo‘sh xonalar, uylar va villalarni topish\n"
                            "• Narxlar va mavjudlikni tekshirish\n"
                            "• Bron qilish qoidalari haqida eng so‘nggi ma’lumotlarni olish"
                        ),
                    },
                    "what_makes_better": {
                        "q": "Nega STAI boshqalardan yaxshiroq?",
                        "a": (
                            "STAI — O‘zbekistonda mahalliy bozor ehtiyojlari uchun noldan yaratilgan birinchi platforma.\n\n"
                            "Biz quyidagilarni taklif qilamiz:\n"
                            "• Qo‘ng‘iroqlarsiz tezkor bron qilish\n"
                            "• Yashirin to‘lovlarsiz shaffof narxlar\n"
                            "• Tasdiqlangan egalar\n"
                            "• Rus va o‘zbek tillarida qo‘llab-quvvatlash\n"
                            "• Mehmonlar va mehmonxonalar uchun qulay vositalar\n"
                            "• Telegram yoki veb-sayt orqali oddiy va tezkor foydalanish"
                        ),
                    },
                    "what_is_stai": {
                        "q": "STAI nima?",
                        "a": (
                            "STAI — bu O‘zbekiston bo‘ylab mehmonxonalar, dam olish uylari va kvartiralarni bron qilish uchun zamonaviy platforma.\n\n"
                            "Biz qidiruv va bron qilish jarayonini mehmonlar va egalar uchun tez, qulay va xavfsiz qilamiz."
                        ),
                    },
                    "why_trustworthy": {
                        "q": "Nega STAI ishonchli?",
                        "a": (
                            "STAI quyidagilarni ta’minlaydi:\n"
                            "• Xavfsiz to‘lovlar va ma’lumotlarni himoya qilish\n"
                            "• Faqat tasdiqlangan egalar\n"
                            "• Shaffof bekor qilish qoidalari\n"
                            "• Bir necha soniya ichida bronni tasdiqlash\n"
                            "• Sharhlar va reyting tizimi\n\n"
                            "Biz O‘zbekistondagi eng ishonchli platformaga aylanishga intilamiz."
                        ),
                    },
                    "website_link": {
                        "q": "Sayt havolasi",
                        "a": "Bizning rasmiy veb-saytimiz: www.stai.uz",
                    },
                },
            },
            "about_booking": {
                "title": "Bo‘lim: Bron qilish haqida",
                "questions": {
                    "find_room": {
                        "q": "Xonani qanday topish mumkin?",
                        "a": (
                            "Rasmiy veb-saytda:\n"
                            "• Kerakli joylashuvni tanlang\n"
                            "• Sanalar va mehmonlar sonini kiriting\n"
                            "• Sizga mavjud variantlar ko‘rsatiladi\n"
                            "• Yoqtirgan obyektni tanlab, bron qilish bosqichiga o‘ting"
                        ),
                    },
                    "price_calculated": {
                        "q": "Narx qanday hisoblanadi?",
                        "a": (
                            "Narx quyidagilardan iborat:\n"
                            "• Bir kecha uchun asosiy narx\n"
                            "• Qo‘shimcha xizmatlar (agar tanlangan bo‘lsa)\n"
                            "• Soliqlar va yig‘imlar (agar qo‘llansa)\n"
                            "• Aksiya va promo-kodlar bo‘yicha chegirmalar\n"
                            "• Muayyan sanalar uchun narx qoidalari (bayramlar / yuqori mavsum)"
                        ),
                    },
                    "promo_codes": {
                        "q": "Promo-kodlar qanday ishlaydi?",
                        "a": (
                            "• Promo-kod bron qilish vaqtida kiritiladi\n"
                            "• Chegirma avtomatik ravishda qo‘llaniladi\n"
                            "• Har bir promo-kodning amal qilish muddati va shartlari mavjud\n"
                            "• Ba’zi promo-kodlar faqat yangi foydalanuvchilar uchun amal qiladi"
                        ),
                    },
                    "edit_cancel": {
                        "q": "Bronni o‘zgartirish yoki bekor qilish mumkinmi?",
                        "a": (
                            "Ha, agar obyekt qoidalari bunga ruxsat bersa.\n\n"
                            "Siz quyidagilarni qilishingiz mumkin:\n"
                            "• Sanalarni o‘zgartirish (mavjud joylarga qarab)\n"
                            "• Bronni bekor qilish\n"
                            "• Bekor qilish siyosatiga asosan avtomatik qaytarish hisobini olish"
                        ),
                    },
                },
            },
            "house_rules": {
                "title": "Bo‘lim: Yashash qoidalari",
                "questions": {
                    "checkin_checkout": {
                        "q": "Kirish / chiqish qoidalari",
                        "a": (
                            "Kirish: odatda 14:00 dan keyin\n"
                            "Chiqish: odatda 12:00 gacha\n\n"
                            "(Aniq vaqt har doim obyekt sahifasida ko‘rsatiladi)"
                        ),
                    },
                    "guest_limits": {
                        "q": "Mehmonlar limiti",
                        "a": (
                            "Har bir obyektning maksimal mehmonlar soni mavjud.\n"
                            "Agar siz belgilangan limitdan oshsangiz, obyekt joylashtirishni rad etishi mumkin."
                        ),
                    },
                    "damage_deposit": {
                        "q": "Zarar uchun garov puli",
                        "a": (
                            "Ba’zi egalar mumkin bo‘lgan zararlar uchun garov puli talab qilishlari mumkin.\n"
                            "Garov summasi oldindan ko‘rsatiladi.\n"
                            "Agar hammasi joyida bo‘lsa, garov puli chiqishdan keyin qaytariladi."
                        ),
                    },
                },
            },
            "payment_refunds": {
                "title": "Bo‘lim: To‘lov va qaytarish",
                "questions": {
                    "supported_payments": {
                        "q": "Qo‘llab-quvvatlanadigan to‘lov turlari",
                        "a": (
                            "STAI quyidagilarni qo‘llab-quvvatlaydi:\n"
                            "• Uzcard va Humo kartalari\n"
                            "• Xalqaro kartalar (Visa/MasterCard) — ishga tushirilgandan so‘ng\n"
                            "• Qulay mahalliy to‘lov usullari"
                        ),
                    },
                    "when_payment_captured": {
                        "q": "To‘lov qachon yechib olinadi?",
                        "a": "To‘lov bron tasdiqlanganda yechib olinadi.",
                    },
                    "refund_policy": {
                        "q": "Qaytarish siyosati",
                        "a": (
                            "Qaytarish tanlangan bekor qilish siyosatiga bog‘liq:\n"
                            "• Bepul bekor qilish (kirishdan 7 kun oldin) — to‘liq qaytarish\n"
                            "• Kirishdan 3–6 kun oldin bekor qilish — 50% qaytarish\n"
                            "• Kirishdan 48 soatdan kam vaqt oldin bekor qilish — 0% qaytarish"
                        ),
                    },
                    "host_denies_entry": {
                        "q": "Agar mezbon kiritmasa nima bo‘ladi?",
                        "a": (
                            "Bu juda kam uchraydigan holat, ammo shunday bo‘lsa:\n"
                            "• Siz to‘liq pulni qaytarib olish huquqiga egasiz\n"
                            "• STAI sizga muqobil variant topib berishi mumkin\n"
                            "• Mezbon jarimaga tortilishi va platformadan chiqarilishi mumkin\n\n"
                            "Biz har doim mehmonlarimizni himoya qilamiz."
                        ),
                    },
                },
            },
            "legal_docs": {
                "title": "Bo‘lim: Hujjatlar / Qoidalar",
                "questions": {
                    "passport_id": {
                        "q": "Pasport yoki ID kerakmi?",
                        "a": (
                            "Ha, ro‘yxatdan o‘tishda pasport yoki ID-kartani ko‘rsatish kerak.\n"
                            "Bu O‘zbekiston qonunchiligiga muvofiq majburiy talabdir."
                        ),
                    },
                    "official_invoices": {
                        "q": "STAI rasmiy hujjatlar beradimi?",
                        "a": (
                            "Ha, so‘rov bo‘yicha biz quyidagilarni taqdim eta olamiz:\n"
                            "• Elektron чек\n"
                            "• Hisobot uchun rasmiy hujjat"
                        ),
                    },
                    "foreigners_registration": {
                        "q": "Chet elliklar uchun ro‘yxatdan o‘tish qoidalari",
                        "a": (
                            "O‘zbekiston qoidalariga ko‘ra:\n"
                            "• Chet el fuqarolari yashash joyida ro‘yxatdan o‘tishlari kerak\n"
                            "• Ro‘yxatdan o‘tkazishni odatda turar joy egasi amalga oshiradi\n"
                            "• Mehmon ro‘yxatdan o‘tishda pasportni ko‘rsatishi kerak"
                        ),
                    },
                },
            },
        },
    },
}


def get_language(context: ContextTypes.DEFAULT_TYPE) -> str:
    return context.user_data.get("lang", "ru")


def language_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Русский", callback_data="lang:ru"),
            InlineKeyboardButton("O‘zbekcha", callback_data="lang:uz"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    keyboard = [
        [InlineKeyboardButton(t["about_stai"], callback_data="section:about_stai")],
        [InlineKeyboardButton(t["about_booking"], callback_data="section:about_booking")],
        [InlineKeyboardButton(t["house_rules"], callback_data="section:house_rules")],
        [InlineKeyboardButton(t["payment_refunds"], callback_data="section:payment_refunds")],
        [InlineKeyboardButton(t["legal_docs"], callback_data="section:legal_docs")],
        [InlineKeyboardButton(t["contact_operator"], callback_data="operator")],
        [InlineKeyboardButton(t["description_title"], callback_data="description")],
    ]
    return InlineKeyboardMarkup(keyboard)


def section_keyboard(lang: str, section_key: str) -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    questions = t["sections"][section_key]["questions"]

    keyboard = []
    for question_key, question_data in questions.items():
        keyboard.append([
            InlineKeyboardButton(
                question_data["q"],
                callback_data=f"question:{section_key}:{question_key}"
            )
        ])

    keyboard.append([InlineKeyboardButton(t["back"], callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)


def answer_keyboard(lang: str, section_key: str) -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    keyboard = [
        [InlineKeyboardButton(t["back"], callback_data=f"section:{section_key}")],
        [InlineKeyboardButton(t["main_menu"], callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "STAI bot\n\nChoose language / Выберите язык / Tilni tanlang:",
        reply_markup=language_keyboard()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("lang:"):
        lang = data.split(":")[1]
        context.user_data["lang"] = lang
        t = TEXTS[lang]

        await query.edit_message_text(
            text=f"{t['welcome']}\n\n{t['main_menu']}",
            reply_markup=main_menu_keyboard(lang)
        )
        return

    lang = get_language(context)
    t = TEXTS[lang]

    if data == "main_menu":
        await query.edit_message_text(
            text=t["main_menu"],
            reply_markup=main_menu_keyboard(lang)
        )
        return

    if data == "operator":
        await query.edit_message_text(
            text=t["operator_text"],
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(t["back"], callback_data="main_menu")]]
            )
        )
        return
    if data == "description":
        await query.edit_message_text(
            text = t["description"],
            reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton(t["back"], callback_data="main_menu")]])
        )
        return
    if data.startswith("section:"):
        section_key = data.split(":")[1]
        section_title = t["sections"][section_key]["title"]

        await query.edit_message_text(
            text=section_title,
            reply_markup=section_keyboard(lang, section_key)
        )
        return

    if data.startswith("question:"):
        _, section_key, question_key = data.split(":")
        answer_text = t["sections"][section_key]["questions"][question_key]["a"]

        await query.edit_message_text(
            text=answer_text,
            reply_markup=answer_keyboard(lang, section_key)
        )
        return

    await query.edit_message_text(
        text=t["unknown_action"],
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(t["back"], callback_data="main_menu")]]
        )
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()