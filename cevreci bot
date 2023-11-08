import discord
import random
from discord.ext import commands

imza_kampanya=['https://www.change.org/p/santraller-yatırımları-tamamlamadan-tekrar-havamızı-kirletmeye-başladı-izinvermeyin-temizhavahaktır-csbgovtr-murat-kurum','https://www.change.org/p/cop28-e-kadar-türkiye-2030-a-kadar-emisyonları-yüzde-35-azaltmalı-tbmmresmi-csbgovtr-2030iklimhedefi']
oneriler=['Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve ayaklarınızı (mümkün olduğunda) kullanmaya çalışın.','Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın. Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.','Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın.','Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.','Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.','Bunu niye koyduğumu bikmiyorum, tekrar dene :D','Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin.','Eski eşyaları çöpe atmak yerine geri dönüştürün','Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben size çevre konusunda yardımcı olacak bir botum.')

@bot.command()
async def oneri(ctx):

    await ctx.send(random.choice(oneriler))

@bot.command()
async def imza_kampanyalari(ctx):
    await ctx.send(random.choice(imza_kampanya))

@bot.command()
async def bye(ctx):
    await ctx.send(f'Görüşürüz!')

@bot.command()
async def yardim(ctx):
    yardim_mesaji="""$hello - Size selam verir.
$bye - Sizi yollar.
$on_ready - Bot girişini yazar.
$oneri - Size çevre ile ilgili öneriler verir.
$imza_kampanyalari - Size çevre ile ilgili imza kampanyaları verir."""
    await ctx.send(yardim_mesaji)

bot.run(PUT YOUR TOKEN HERE)
