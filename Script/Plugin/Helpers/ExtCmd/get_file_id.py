from pyrogram.types import Message


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "صوره",
            "متحركه",
            "اغنيه",
            "مستند",
            "فيديو",
            "فيديو_ملاحظه",
            "صوتيه",
            "الاتصال",
            "dice",
            "استصلاع",
            "الموقع",
            "موقع",
            "ملصقات",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj
