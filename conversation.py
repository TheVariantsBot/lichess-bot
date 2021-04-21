class Conversation:
    def __init__(self, game, engine, xhr, version, challenge_queue, hi):
        self.game = game
        self.engine = engine
        self.xhr = xhr
        self.version = version
        self.challengers = challenge_queue
        self.hi = hi

    command_prefix = "!"

    def react(self, line, game):
        print("*** {} [{}] {}: {}".format(self.game.url(), line.room, line.username, line.text.encode("utf-8")))
        if (line.text[0] == self.command_prefix):
            self.command(line, game, line.text[1:].lower())

    def command(self, line, game, cmd):
        if cmd == "commands" or cmd == "help":
            self.send_reply(line, "Supported commands: !name, !howto, !eval, !queue, !hi, !engine")
        elif cmd == "wait" and game.is_abortable():
            game.ping(60, 120)
            self.send_reply(line, "I'm waiting 60 Seconds...")
        elif cmd == "name":
            self.send_reply(line, "{} Lichess-Bot By @VahidBashirli! (v{})".format(self.engine.name(), self.version))
        elif cmd == "howto":
            self.send_reply(line, "How to run your own bot: Check out 'Lichess Bot API'")
        elif cmd == "eval" and line.room == "spectator":
            stats = self.engine.get_stats()
            self.send_reply(line, ", ".join(stats))
        elif cmd == "eval":
            self.send_reply(line, "No! I Can't Tell it to You! Don't Cry! :)")
        elif cmd == "queue":
            if self.challengers:
                challengers = ", ".join(["@" + challenger.challenger_name for challenger in reversed(self.challengers)])
                self.send_reply(line, "Challenge queue: {}".format(challengers))
            else:
                self.send_reply(line, "No challenges queued.")

    def send_reply(self, line, reply):
        self.xhr.chat(self.game.id, line.room, reply)
        elif cmd == "hi":
                self.send_reply(line, "Hello My Friend!")
        elif cmd == "engine":
                self.send_reply(line, "{} *_* (v{})".format(self.engine.name()")
       


class ChatLine:
    def __init__(self, json):
        self.room = json.get("room")
        self.username = json.get("username")
        self.text = json.get("text")
