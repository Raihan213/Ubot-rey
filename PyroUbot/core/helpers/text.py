from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot.config import LOGS_MAKER_UBOT, OWNER_ID
from PyroUbot import bot, ubot
from PyroUbot.core.database import get_expired_date

class MSG:
    def DEAK(X):
        return f"""
<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs ᴅᴀʀɪ ᴛᴇʟᴇɢʀᴀᴍ</b>
"""
            
    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b>
"""

    
    def START(message):
        return f"""
<b>👋🏻 Hallo <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

Di bot ini, Anda bisa membeli userbot dengan mudah & simple 
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
Silakan Lakukan Pembayaran Terlebih Dahulu

Harga Perbulan: {harga}.000

💳 Metode Pembayaran:
 ├──• DANA
 ├─• 082231511518


🔖 Total Harga: Rp {total}.000
🗓️ Total Bulan: {bulan}

✅ Klik Tombol Di Bawah Ini Untuk Mengirimkan Bukti Pembayaran
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""

    def POLICY():
        return """
Kebijakan Pengembalian:

Setelah melakukan pembayaran, jika Anda belum menerima manfaat dari pembelian, 
Anda berhak untuk mengajukan pengembalian dalam waktu 2 hari setelah pembelian. 
Namun, jika Anda telah menggunakan atau menerima salah satu manfaat dari pembelian, 
termasuk akses ke fitur pembuatan userbot, maka Anda tidak lagi memenuhi syarat untuk pengembalian dana.

Dukungan:

Untuk mendapatkan bantuan atau dukungan, 
Anda dapat menghubungi admin di bawah ini atau mengirim pesan ke @swandisini di Telegram. 
Harap diingat, jangan menghubungi Dukungan Telegram atau 
Dukungan Bot untuk masalah terkait pembayaran yang dilakukan di bot ini.

Tombol Lanjutkan:

Klik tombol "Lanjutkan" untuk mengkonfirmasi 
bahwa Anda telah membaca dan menerima ketentuan ini dan 
melanjutkan proses pembelian. Jika tidak, klik tombol "Kembali".
"""


async def sending_user(user_id):
    try:
        if bot and bot.me and bot.me.username:
            await bot.send_message(
                user_id,
                "💬 sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ᴀɴᴅᴀ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥",
                                callback_data="bahan",
                            )
                        ],
                    ]
                ),
                disable_web_page_preview=True,
            )
            await bot.send_message(
                LOGS_MAKER_UBOT,
                f"""
➡️ ʏᴀɴɢ ᴍᴇʀᴀsᴀ ᴍᴇᴍɪʟɪᴋɪ ɪᴅ: {user_id}

✅ sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ɴʏᴀ ᴅɪ: @{bot.me.username}
        """,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                                callback_data=f"cek_masa_aktif {user_id}",
                            )
                        ],
                    ]
                ),
                disable_web_page_preview=True,
            )
        else:
            print("Bot belum diinisialisasi dengan benar atau atribut 'me' tidak tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        # Lakukan penanganan kesalahan sesuai kebutuhan Anda
