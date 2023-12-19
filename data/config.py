from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")

channel = (-1002123295643, "Uy ishi savdosi", "https://t.me/uy_ishi_chop")
