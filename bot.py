import os
import discord
from discord.ext import commands
from discord.ui import View, Button
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
ALERT_CHANNEL_ID = int(os.getenv("ALERT_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

class AlertView(View):
    def __init__(self, alert_channel_id, allowed_user_id):
        super().__init__()
        self.alert_channel_id = alert_channel_id
        self.allowed_user_id = allowed_user_id

    @discord.ui.button(label="🚨 Тривога", style=discord.ButtonStyle.danger)
    async def alarm(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id != self.allowed_user_id:
            await interaction.response.send_message("⛔ У вас немає прав для цього!", ephemeral=True)
            return

        channel = interaction.client.get_channel(self.alert_channel_id)
        await channel.send("@everyone 🚨 **ПОВІТРЯНА ТРИВОГА!**", allowed_mentions=discord.AllowedMentions(everyone=True))
        await interaction.response.send_message("✅ Повідомлення надіслано!", ephemeral=True)

    @discord.ui.button(label="✅ Відбій", style=discord.ButtonStyle.success)
    async def safe(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id != self.allowed_user_id:
            await interaction.response.send_message("⛔ У вас немає прав для цього!", ephemeral=True)
            return

        channel = interaction.client.get_channel(self.alert_channel_id)
        await channel.send("@everyone ✅ **ВІДБІЙ!**", allowed_mentions=discord.AllowedMentions(everyone=True))
        await interaction.response.send_message("✅ Повідомлення надіслано!", ephemeral=True)

@bot.event
async def on_ready():
    owner = await bot.fetch_user(OWNER_ID)
    view = AlertView(ALERT_CHANNEL_ID, OWNER_ID)
    await owner.send("🔧 Панель керування тривогами:", view=view)
    print(f"✅ Бот запущено як {bot.user}")

bot.run(TOKEN)
import os
import discord
from discord.ext import commands
from discord.ui import View, Button
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
ALERT_CHANNEL_ID = int(os.getenv("ALERT_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)



class AlertView(View):
    def __init__(self, alert_channel_id, allowed_user_id):
        super().__init__()
        self.alert_channel_id = alert_channel_id
        self.allowed_user_id = allowed_user_id



    @discord.ui.button(label="🚨 Тривога", style=discord.ButtonStyle.danger)
    async def alarm(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id != self.allowed_user_id:
            await interaction.response.send_message("⛔ У вас немає прав для цього!", ephemeral=True)
            return
        channel = interaction.client.get_channel(self.alert_channel_id)
        await channel.send("@everyone 🚨 **ПОВІТРЯНА ТРИВОГА!**", allowed_mentions=discord.AllowedMentions(everyone=True))
        await interaction.response.send_message("✅ Повідомлення надіслано!", ephemeral=True)



    @discord.ui.button(label="✅ Відбій", style=discord.ButtonStyle.success)
    async def safe(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id != self.allowed_user_id:
            await interaction.response.send_message("⛔ У вас немає прав для цього!", ephemeral=True)
            return


        channel = interaction.client.get_channel(self.alert_channel_id)
        await channel.send("@everyone ✅ **ВІДБІЙ!**", allowed_mentions=discord.AllowedMentions(everyone=True))
        await interaction.response.send_message("✅ Повідомлення надіслано!", ephemeral=True)



@bot.event
async def on_ready():
    owner = await bot.fetch_user(OWNER_ID)
    view = AlertView(ALERT_CHANNEL_ID, OWNER_ID)
    await owner.send("🔧 Панель керування тривогами:", view=view)
    print(f"✅ Бот запущено як {bot.user}")

bot.run(TOKEN)
