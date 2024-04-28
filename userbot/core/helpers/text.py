from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from userbot.config import LOGS_MAKER_UBOT, OWNER_ID
from userbot import bot, ubot
from userbot.core.database import get_expired_date

class MSG:
    def DEAK(X):
        return f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ telah berhasil di hapus dari telegram</b>
"""
            
    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ masa aktif telah habis</b>
"""

    
    def START(message):
        return f"""
<b>👻 sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>

🤖 sᴀʏᴀ ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ

🤖 sᴀʏᴀ ᴍᴇɴʏᴇᴅɪᴀᴋᴀɴ ʙᴀɴʏᴀᴋ ᴍᴏᴅᴜʟᴇ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴀɴᴅᴀ ʟᴇʙɪʜ ɢᴀᴍᴘᴀɴɢ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴀᴋᴛɪғɪᴛᴀs ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ

🗨 sᴇᴘᴇʀᴛɪ ʙʀᴏᴀᴅᴄᴀsᴛ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴜᴘ ᴅᴀɴ ʟᴀɪɴ ʟᴀɪɴ

🗨 sᴇʟᴇʙɪʜɴʏᴀ sɪʟᴀʜᴋᴀɴ ᴄᴇᴋ ᴍᴏᴅᴜʟᴇ

👤 ᴛᴇʀɪᴍᴀ ᴋᴀsɪʜ sᴜᴅᴀʜ sᴛᴀʀᴛ ʙᴏᴛ ɪɴɪ

"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
Silakan Lakukan Pembayaran Terlebih Dahulu

Harga Perbulan: {harga}.000

💳 Metode Pembayaran:
 ├──• DANA
 ├─• xxxxxxxxxxxx


🔖 Total Harga: Rp {total}.000
🗓️ Total Bulan: {bulan}

✅ Klik Tombol Di Bawah Ini Untuk Mengirimkan Bukti Pembayaran
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ userbot ke</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ akun:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ id:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ expired</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""

    def POLICY():
        return """
Kebijakan Pengembalian:

Setelah melakukan pembayaran, jika anda belum menerima manfaat dari pembelian, 
anda berhak untuk mengajukan pengembalian dalam waktu 2 hari setelah pembelian. 
Namun, jika anda telah menggunakan atau menerima salah satu manfaat dari pembelian, 
termasuk akses ke fitur pembuatan userbot, maka anda tidak lagi memenuhi syarat untuk pengembalian dana.

Dukungan:

Untuk mendapatkan bantuan atau dukungan, 
anda dapat menghubungi admin di bawah ini atau mengirim pesan ke @AnonymousX888 di Telegram. 
Harap diingat, jangan menghubungi Dukungan Telegram atau 
Dukungan Bot untuk masalah terkait pembayaran yang dilakukan di bot ini.

Tombol Lanjutkan:

Klik tombol "Lanjutkan" untuk mengkonfirmasi 
bahwa anda telah membaca dan menerima ketentuan ini dan 
melanjutkan proses pembelian. Jika tidak, klik tombol "Kembali".
"""


async def sending_user(user_id):
    try:
        if bot and bot.me and bot.me.username:
            await bot.send_message(
                user_id,
                "💬 silahkan buat ulang userbot anda",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💠 buat userbot 💠",
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
➡️ yang merasa memiliki id: {user_id}

✅ silahkan buat ulang userbot nya di: @{bot.me.username}
        """,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "📁 cek masa aktif 📁",
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
        # Lakukan penanganan kesalahan sesuai kebutuhan anda
