from loader import _


class MsgText:
    @property
    def WELCOME(self):
        return _("👋, <a href='tg://user?id={}'>{}</a>")

    @property
    def INFO(self):
        return _("Bot Info:")

    @property
    def INVITE_FRIENDS(self):
        return _(
            "Invited users: <b>{}</b>\n\nLink for friends:\n<code>https://t.me/{}?start={}</code>"
        )

    @property
    def ADMIN_WELCOME(self):
        return _("You're the administrator!")

    @property
    def CHANGE_LANG(self):
        return _("Select the language you want to switch to: 🌐")

    @property
    def DONE_CHANGE_LANG(self):
        return _("Your language has been successfully changed! ✅")


msg_text = MsgText()
