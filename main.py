import os, random, json
import discord
from discord import app_commands
from discord.ext import commands, tasks
from typing import Optional
from discord.app_commands import Choice, CommandTree,Group
import requests
from bs4 import BeautifulSoup as bs
from discord.ui import Button, Select, View
from discord import ui
from discord.ext.commands import has_permissions
#MissingPermissions
import time
import datetime
import asyncio
import pytube
from pytube import Channel, YouTube
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
#import youtube_dl
import yt_dlp as youtube_dl
import aiohttp
import aiofiles
from datetime import date
import requests
import re
from PIL import Image, ImageDraw, ImageOps, ImageFont
import speech_recognition as sr
# from onmessage import onmessage
from pydub import AudioSegment
# from jinja2 import Template
import ffmpeg
from aiset import chatai
recognizer = sr.Recognizer()
# from googletrans import Translator
from aiset import gen_image
# translator = Translator()

start_time = time.time()
useText = {}
tag = 0




print(os.path.dirname(os.path.abspath(__file__)))
with open('top.json', 'r', encoding='utf-8') as file:
        content = file.read()

#BUG處理
def saybugs(err, nam):
  embed = discord.Embed(title="我被臭蟲絆倒了")
  embed.add_field(name=nam, value=err, inline=True)
  return embed


#遷入產生氣
def embedMake(
  head,
  tt="",
  ttt="",
  tttt="",
  ttttt="",
  end="",
  us=""
):
  embed = discord.Embed(title=head,
                        url="https://bot.is-from.tw/",
                        color=0x2676f7)
  if tt!="":
      embed.add_field(name=tt, value=ttt, inline=False)
  if tttt!="":
      embed.add_field(name=tttt, value=ttttt, inline=False)
  #ch=["[教學](http://owo.freeserver.tw:20371/h2)","[支援中心](https://discord.gg/CaFUuFTUzQ)"]
  #ch2=["[運作贊助](https://divahosting.net)","[部分圖片提供](https://www.recraft.ai/)"]
  #embed.add_field(name=f"{random.choice(ch)}",value="", inline=False)
  if end=="":
      ch=["一切功能|皆為可能","讓discord變得更有趣","專門播迷因的機器"]
      end=random.choice(ch)  
  tex= "pokeegg" if us=="" else f"{us}"
  icon= us.avatar.url if us!="" else "https://images-ext-1.discordapp.net/external/ECzBfRz8aLmyNKOzuo5tUvliLPzejUNBWnG0b8fYsGA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1132079788140531872/7bf64313d0ca5a1461d1916a772d2b95.png?width=701&height=701"
  embed.set_footer(text=f"{tex}•{end}", icon_url=icon)
  return embed


#butt產生
def butt(n="沒有權限", l="https://discord.com/oauth2/authorize?client_id=1132079788140531872", e="💌"):
  button = Button(label=n, emoji=e, url=l, style=discord.ButtonStyle.link)
  view = View(timeout=0)
  view.add_item(button)
  return view



#開始指令

intents = discord.Intents.all()
intents.presences = False
bot = commands.Bot(command_prefix="-", intents=intents)


class setCog(commands.Cog):
  global useText
  def __init__(self, bot):
    self.set60.start()
    #self.set20.start()
    self.everyday.start()
    # self.everyd.start()
    self.bot=bot
  @tasks.loop(seconds=20)
  async def set20(self):
    if random.randint(0,1)==1:
      await self.bot.change_presence(activity=discord.Streaming(name=f"{len(self.bot.guilds)}個伺服器活動",url="https://discord.com/oauth2/authorize?client_id=1132079788140531872",platform="discord"))
    else:
      await self.bot.change_presence(activity=discord.Streaming(name="可以使用/客服 列出功能或與伺服器管理員聯繫",url="https://discord.com/oauth2/authorize?client_id=1132079788140531872",platform="help"))
  @tasks.loop(seconds=180)
  async def set60(self):
    global start_time, useText
    async with aiofiles.open('YT.json', 'r') as file:
            data = await file.read()
            daa = json.loads(data)

    for x in daa:
      await asyncio.sleep(1)
      連結 = daa[x][1]
      通知 = daa[x][2]
      try:
        videos = scrapetube.get_channel(channel_url=連結, limit=1)
        for video in videos:
          if video['title']['runs'][0]['text'] != daa[x][3]:
            embed = discord.Embed(
                            title="<a:YT:1135838936892186675>" + video['title']['runs'][0]['text'],
                            url=f"https://www.youtube.com/watch?v={video['videoId']}",
                            color=0xd03a20
                        )
            embed.set_image(url=video['thumbnail']['thumbnails'][0]['url'])
            print(f"https://www.youtube.com/watch?v={video['videoId']}")  # video id
            print(video['title']['runs'][0]['text'])  # video title
            daa[x][3] = video['title']['runs'][0]['text']

            async with aiofiles.open("YT.json", "w") as file:
              await file.write(json.dumps(daa, indent=4))
              頻道 = bot.get_channel(daa[x][0])          
              await 頻道.send(
                            通知.replace('@n', video['title']['runs'][0]['text']),
                            embed=embed,
                            view=butt("打開連結", f"https://www.youtube.com/watch?v={video['videoId']}", "<a:YT:1135838936892186675>")
                        )
      except Exception as e:
                print(e)
        # 臺灣時區 UTC+8

  tz = datetime.timezone(datetime.timedelta(hours=8))
  # 設定每日十二點執行一次函式
  everyday_time = datetime.time(hour=7, minute=30, tzinfo=tz)
  everydayt = datetime.time(hour=10, minute=10, tzinfo=tz)
  # @tasks.loop(time=everydayt)
  # async def everyd(self):
  #       try:
  #           await bot.get_channel(1139426870740385863).send(embed=embedMake("別氣餒，我永遠是每日第一", "不過，\n> [可以投票](https://discordservers.tw/servers/1062288200187510904)\n可以置頂:</bump:936267730636660786>"))
  #       except:
  #           pass
        
            
  @tasks.loop(time=everyday_time)
  async def everyday(self):
    with open("AI.json", "r", encoding='utf-8') as file:
      daate = json.load(file)
    daate = {}
    daate["date"] = str(date.today())
    daate["today"] = 0
    a = []
    async for message in bot.get_channel(1127466764792508566).history(
        limit=1, oldest_first=False):
      a.append(message)
    a = eval(a[0].content)
    a = a[random.randint(0, len(a) - 1)]
    with open("AI.json", "w") as file:
      json.dump(daate, file, indent=4)
    dic={}
    with open("dds.json", "w") as file:
        json.dump(dic, file, indent=4)
    # for g in bot.guilds:
      #for c in g.channels:
        #if c.name.startswith("本日總發言字數✨"):
          #try:
          #  await c.edit(name=f"本日總發言字數✨0")
         # except:
         #   pass
    taiwan_tz = pytz.timezone('Asia/Taipei')
    current_time_taiwan = datetime.datetime.now(taiwan_tz)
    print(current_time_taiwan.month)
    if current_time_taiwan.month == 1 and current_time_taiwan.day == 27:
        for g in bot.guilds:
            for c in g.channels:
                try:
                        await c.send('''預測今年紅包可以拿多少?
                                     用` /紅包 `看看!
                                     -# 祝大家拿到的都是紅的。
                                     ''')
                    
                except:
                    pass
                else:
                    print('+1')
                    break
    
        
class set300cog(commands.Cog):
  
  def __init__(self, bot):
    self.set300.start()
  @tasks.loop(seconds=300)
  async def set300(self):
    with open("music.json" ,"r") as file:
        dic=json.load(file)
    for gid,lis in dic.items():
      guild=bot.get_guild(int(gid))
      if guild== None:
            continue
      vc= guild.voice_client
      if vc:
        vcs= [channel for channel in guild.voice_channels if channel.guild.me in channel.members]
        if len(vc.channel.members)<1 :
            us=bot.get_user(dic[str(guild.id)]["u"])
            embed=discord.Embed(title=f"已結束在<#{vcs[0].id}>的音樂")
            embed.set_author(icon_url=us.avatar.url,name=us.global_name if us.global_name else us.name)
            await vc.disconnect()
            ch=bot.get_channel(int(dic[str(guild.id)]["c"]))
            lis=["語音頻道沒人=我可以偷懶","沒人聽歌 我先溜嘍","囂喧妓坊歌滿樓 轉眼人去光熄 只留餘歌繞樑 默默隨餘音歸去","歌播完 我走嘍"]
            embed.set_footer(text=random.choice(lis))
            os.remove(f'downloads/audio{guild.id}.mp3')
            try:
                s=await ch.fetch_message(dic[str(guild.id)]["s"])
                await s.edit(content="",embed=embed,view=None)
            except:
                pass
                
class set10cog(commands.Cog):
  global tag

  def __init__(self, bot):
    #self.set10.start()
    self.clock = 0

  @tasks.loop(seconds=100)
  async def set10(self):
    self.clock += 1
    tag = 0
    for g in bot.guilds:
      for c in g.channels:
        if c.name.startswith("總人數✨"):
          try:
            await c.edit(name=f"總人數✨{len(g.members)}")
          except:
            pass
        
      await asyncio.sleep(2)



@bot.event
async def on_ready():
  await bot.load_extension('fast')
  # try:
  #   slash = await bot.tree.sync()
  #   for i in slash:
  #       print(f"</{i.name}:{i.id}>",end="|")
  # except Exception as bug:
  #   print(f"\n\n\ngg by\n\n{bug}")
  #   del bug
  if '蟲洞使者' not in bot.cogs:
    await bot.add_cog(MyCog(bot))
  await bot.add_cog(setCog(bot))
  await bot.add_cog(set10cog(bot))
  await bot.add_cog(set300cog(bot))
  
 # print(bot.get_emoji(1138322474782691389).url)
  
  
    
  


@bot.event
async def on_message(ctx):
  global start_time, useText, tag
  if ctx.author.bot:
    return
###
  if ctx.author==None:
        return
  with open("top.json", "r", encoding='utf-8') as file:
      data = json.load(file)
  
  with open("top.json", "r", encoding='utf-8') as file:
      data = json.load(file)
  if ctx.guild:
    with open("d.json", "r", encoding='utf-8') as file:
        data3 = json.load(file)
    if str(ctx.guild.id) in data3:
        if "CS" in data3[str(ctx.guild.id)]:
            xp=data3[str(ctx.guild.id)]["CS"]
            
            cc=xpcont(ctx.guild,ctx.author.id,xp=xp)
            if cc[1]:
              with open("xp.json", "r", encoding='utf-8') as file:
                data3 = json.load(file)
              await ctx.channel.send(f"恭喜!{ctx.author.name}的羈絆來到{data3[str(ctx.guild.id)][str(ctx.author.id)][1]}\n> 升至等級{cc[0]}",delete_after=20,mention_author=False,reference=ctx)
        with open("d.json", "r", encoding='utf-8') as file:
          data3 = json.load(file)
        if "ST" in data3[str(ctx.guild.id)]:
            xp=data3[str(ctx.guild.id)]["ST"]*len(ctx.content)
            with open("xp.json", "r", encoding='utf-8') as file:
                data3 = json.load(file)
            cc=xpcont(ctx.guild,ctx.author.id,xp=xp)
            if cc[1]:
              with open("xp.json", "r", encoding='utf-8') as file:
                data3 = json.load(file)
              await ctx.channel.send(f"恭喜!{ctx.author.name}的羈絆來到{data3[str(ctx.guild.id)][str(ctx.author.id)][1]}\n> 升至等級{cc[0]}",delete_after=20,mention_author=False,reference=ctx)
            del data3
    with open("AI.json", "r", encoding='utf-8') as file:
      daate = json.load(file)
    if str(ctx.guild.id) not in daate:
      daate[str(ctx.guild.id)] = []
    if ctx.author.id not in daate[str(ctx.guild.id)]:
      daate[str(ctx.guild.id)].append(ctx.author.id)
      with open("AI.json", "w") as file:
        json.dump(daate, file, indent=4)
      with open("US.json", "r", encoding='utf-8') as file:
        money = json.load(file)
      if str(ctx.author.id) not in money:
        money[str(ctx.author.id)] = [0]
        money[str(ctx.author.id)][0] += 50
        with open("US.json", "w") as file:
            json.dump(money, file, indent=4)
        view=View(timeout=0)
        bu1=discord.ui.Button(style=discord.ButtonStyle.danger, label="刪除訊息")
        bu1.callback=deldaytn
        bu2=discord.ui.Button(style=discord.ButtonStyle.danger, label="永不顯示")
        bu2.callback=stopsend
        view.add_item(bu1)
        select=helpchi()
        view.add_item(select)
        embed=EM('歡迎使用AI萬能機器!','不論是管理員還是成員都能盡情使用，按下底下選單查看功能').set_footer(text=f'$+50•將在20秒後自動隱藏')
        await ctx.channel.send(embed=embed,delete_after=20,mention_author=False,reference=ctx,view=view)
        return
      money[str(ctx.author.id)][0] += 50
      with open("US.json", "w") as file:
        json.dump(money, file, indent=4)
      a=[]#a=["每日一話，醫生失業","日一言，勝潛十年水","日行一善不如日發一言","日吐一話，健康久久","一日之計在於發言","常發言，不發炎",'有些簽到訊息可以增加智慧，有些則無，例如這句。']
      #a=['新年快樂，在/計算 輸入 新年快樂會發生什麼是呢?']
      with open("dayt.json", "r", encoding='utf-8') as file:
        ss = json.load(file)
      if str(ctx.guild.id) in ss:
        a=ss[str(ctx.guild.id)]
      with open("stop.json", "r", encoding='utf-8') as file:
        data3 = json.load(file)
      if a !=[]:
          if ctx.author.id in data3["stop"]:
              return
          view=View(timeout=0)
          bu1=discord.ui.Button(style=discord.ButtonStyle.danger, label="刪除訊息")
          bu1.callback=deldaytn
          bu2=discord.ui.Button(style=discord.ButtonStyle.danger, label="永不顯示")
          bu2.callback=stopsend
          view.add_item(bu1)
          embed=EM('<a:okk:1277864492163928166>簽到成功',random.choice(a)).set_author(icon_url=ctx.author.avatar.url,name=ctx.author.global_name if ctx.author.global_name else ctx.author.name).set_footer(text=f'$+50，目前:{money[str(ctx.author.id)][0]}•將在10秒後自動隱藏')
          await ctx.channel.send(embed=embed,delete_after=10,mention_author=False,reference=ctx,view=view)
      
      del money,daate,ss
      with open("d.json", "r", encoding='utf-8') as file:
        data3 = json.load(file)
      if str(ctx.guild.id) in data3:
        if "CS" in data3[str(ctx.guild.id)]:
            xp=data3[str(ctx.guild.id)]["CS"]
            
            cc=xpcont(ctx.guild,ctx.author.id,xp=xp)
            if cc[1]:
              await ctx.channel.send(f"恭喜!{ctx.author.name}的羈絆來到{data3[str(ctx.guild.id)][str(ctx.author.id)][1]}\n> 升至等級{cc[0]}",delete_after=20,mention_author=True,reference=ctx)
            
            del data3

  ####
  if ctx.guild :
    for c in ctx.guild.channels:
        if c.name.startswith("本日總發言字數✨"):
          try:
            r=int(c.name.split("✨")[1])
            await c.edit(name=f"本日總發言字數✨{r+len(ctx.content)}")
          except Exception as bug:
            print(bug)
    

  ####
    if type(ctx.content) == str and str(
        ctx.guild.id) in data and data[str(ctx.guild.id)] != False:
      if ctx.guild.id not in useText:
        useText[ctx.guild.id] = {}
      if ctx.author.id not in useText[ctx.guild.id]:
        useText[ctx.guild.id][ctx.author.id] = 0
      if useText[ctx.guild.id][ctx.author.id] > data[str(ctx.guild.id)]:
        duration = datetime.timedelta(seconds=0, minutes=10)
        try:
          await ctx.author.timeout(duration, reason="超過字數上限")
          await ctx.channel.send(
            embed=embedMake("糟糕!!", f"{ctx.author.name}過度發『炎』先休息以確保您的健康。"),reference=ctx,mention_author=True,silent=True)
          useText[ctx.guild.id][ctx.author.id]=0
        except Exception as bug:
          pass
      else:
        useText[ctx.guild.id][ctx.author.id] += len(ctx.content)
        if useText[ctx.guild.id][ctx.author.id] > data[str(ctx.guild.id)]:
          try:
            duration = datetime.timedelta(seconds=5, )
            await ctx.author.timeout(duration, reason="超過字數上限")
            useText[ctx.guild.id][ctx.author.id]=0
          except Exception as bug:
            pass
          await ctx.channel.send(embed=embedMake(
            "注意!",
            f"{ctx.author.name}，您已達本分鐘淦話字數上限{data[str(ctx.guild.id)]}請睡個60秒後再講話","不滿可以用</客服 開始:1136503115059830858>開啟一場有趣的客服!",
            end="這是伺服器管理員設定的"),reference=ctx,mention_author=True,silent=True)
  # print(ctx.content, end=" X ")
  
  if "<@1132079788140531872>" in ctx.content :
      if ctx.attachments:
            if any(ctx.attachments[0].filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
                await ctx.channel.typing()
                tim=time.time()
                async with aiohttp.ClientSession() as session:
                    async with session.get(ctx.attachments[0].url) as resp:
                        if resp.status == 200:
                            image_data=await resp.read()
                            txt=await gen_image(image_data, ctx.author.name+'說了:'+ctx.content)
                            em=EM( ctx.content if len(ctx.content)<255 else ctx.content[:250]+'...','',{f'這是經過{time.time()-tim}秒努力思考的結果:':txt})
                            await ctx.channel.send(embed=em,reference=ctx)
                            return
            if  any(ctx.attachments[0].filename.lower().endswith(ext) for ext in ['.txt', '.js', '.py', '.json', '.css','.html','.htm']):
                t=await ctx.attachments[0].read()
                t=ctx.content+t.decode('utf-8')
                await predict_reply(t.replace("<@1132079788140531872>",""),ctx)
                return
   # try:
      await predict_reply(ctx.content.replace("<@1132079788140531872>",""),ctx)
#    except Exception as bug:
 #     print(bug)
  #    await ctx.channel.send(f"可以用</help:1132088808012271686>來看看我的指令")
      return
  with open("cog/setai.json", "r", encoding='utf-8') as file:
        data = json.load(file)
  if ctx.guild:
    if str(ctx.guild.id) in data:
        if ctx.channel.id ==data[str(ctx.guild.id)]:
            await predict_reply(ctx.content,ctx)
            return
  mentions = re.findall(r"<@(\d+)>", ctx.content)
  m = re.findall(r"<@&(\d+)>", ctx.content)
  if mentions or m or "@her" in ctx.content or "@ever" in ctx.content:
    if mentions==ctx.author.id:
      return
    if tag == ctx.author.id:
      try:
        await ctx.author.timeout(duration, reason="過度@人")
        await ctx.channel.send(embed=embedMake("請不要過度@人"))
        await ctx.add_reaction('💢')
        return
      except:
        pass
    tag = ctx.author.id
    
    return
  if ctx.content.startswith("..."):
      await ctx.channel.send(".....")
      return
  if "嗨"== ctx.content or "早"== ctx.content or "hi"== ctx.content:
    await ctx.channel.send("沒錯!，\n可以用</2:1132088808368775195>等**快捷發言**來跟大家說早!")
    return
  if ctx.reference:
    print("11",end='')
    if len(ctx.content)>1 and ctx.content[0] in'+-/*':
      try:
        int(ctx.content[1:])
      except:
        pass
      else:
        ad = await ctx.channel.fetch_message(ctx.reference.message_id)
        ad=ad.content
        if ad!="":
          ad=list(ad+ctx.content)
        for i in ad:
          if i in "Xx。∙•∗⊛⊙⊚⋅⋆⋇*":
            ad[ad.index(i)] = "*"
        for i in ad:
            if i not in ".0123456789+-/*()[]{}%":
              return
        try:
          await ctx.channel.send(eval("".join(ad)))
        except:
          pass
        return
    if ctx.guild:
        with open("d.json", "r", encoding='utf-8') as file:
            data3 = json.load(file)
        if str(ctx.guild.id) in data3:
            if "RM" in data3[str(ctx.guild.id)]:
                xp=data3[str(ctx.guild.id)]["RM"]
                del data3
                cc=xpcont(ctx.guild,ctx.author.id,xp=xp)
                if cc[1]:
                  await ctx.channel.send(f"恭喜!{ctx.author.name}的羈絆來到{data3[str(ctx.guild.id)][str(ctx.author.id)][1]}\n> 升至等級{cc[0]}",delete_after=20,mention_author=True,reference=ctx)
                
  if random.randint(0, 100) < 15 and ctx.guild:
      with open('t.json', 'r') as file:
        d = json.load(file)
      if str(ctx.guild.id) in d:
        try:
          if ctx.channel.topic != None:
            await ctx.channel.send(embed=discord.Embed(
              title=ctx.channel.name,description=ctx.channel.topic, color=0x5f3ffd))
        except:
          pass
  if ctx.type==discord.MessageType.chat_input_command:
    if ctx.guild:
        with open("d.json", "r", encoding='utf-8') as file:
            data3 = json.load(file)
        if str(ctx.guild.id) in data3:
            if "SS" in data3[str(ctx.guild.id)]:
                xp=data3[str(ctx.guild.id)]["SS"]
                del data3
                cc=xpcont(ctx.guild,ctx.author.id,xp=xp)
                if cc[1]:
                  await ctx.channel.send(f"恭喜!{ctx.author.name}的羈絆來到{data3[str(ctx.guild.id)][str(ctx.author.id)][1]}\n> 升至等級{cc[0]}",delete_after=20,mention_author=True,reference=ctx)
  if re.search(r'\[(.*?)\]\((https?://.*?)\)', ctx.content):
        view=View(timeout=0)
        matches = re.findall(r'\[(.*?)\]\((https?://.*?)\)', ctx.content)
        urs=[]
        for match in matches:
            name = match[0]
            url = match[1]
            print(name)
            try:
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, label=name, url=url))
                urs.append(url)
            except:
                pass
        await sendlink(ctx.channel,urs,view)
  if re.search(r'\((.*/)+\)', ctx.content):
      view=View(timeout=0)
      matches = re.findall(r'\((.*/)+\)', ctx.content)
      matches=matches[0].split('/')[:-1]
      if len(matches)<1:
            return
      em={}
      con=0
      for match in matches:
            name = match
            em[name]=''
            if name.replace(' ','')=='':
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, label='其他',custom_id=f'concon'))
            else:
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, label=name,custom_id=f'con{con}'))
            con+=1
      await ctx.channel.send(view=view,embed=EM('接龍表達式','',em).set_author(name=ctx.author.global_name if ctx.author.global_name else ctx.author.name,icon_url =ctx.author.avatar.url))
  
  if ctx.content[0:2] in ['&p','&P','.p','.P','-p','-P']:
    


    try:
        YouTube(ctx.content[2:].replace(' ',''))
        await playm(ctxx,url,'c')
    except Exception:
        await ctx.channel.typing()
        options=[]
        c=0
        url=ctx.content[2:].replace(' ','')
        videos = scrapetube.get_search(query=ctx.content[2:].replace(' ','').replace("	",""),limit=24,results_type="video")
        for video in videos:
            options.append(discord.SelectOption(label=video['title']['runs'][0]['text'],value="p&https://www.youtube.com/watch?v="+video['videoId'],emoji="<a:YT:1135838936892186675>"))
            c+=1
        embed=discord.Embed(title="<a:YT:1135838936892186675>"+url if len("<a:YT:1135838936892186675>"+url)<200 else "<a:YT:1135838936892186675>"+url[:150], url=f"https://www.youtube.com/results?search_query={url}",color=0xf50000,description="點選以下選項開始播放")
        if c==0:
            options.append(discord.SelectOption(label="DISCORD看我建造一個機器人伺服器",value="p&https://www.youtube.com/watch?v=dne5kKtz2lA",emoji="<:me:1122364224103006300>"))
        select = Select(placeholder=f"找到{c}項結果", options=options)
        view = View(timeout=0)
        view.add_item(select)
        await ctx.channel.send(embed=embed,view=view,reference=ctx)
  if ctx.content.startswith('!(') and ctx.content.endswith(')'):
    t=ctx.content
    for i,v in {'大':'小','遠':'近','進':'出','平':'凸','長':'短','高':'矮','胖':'瘦','吃':'拉','快':'慢','肥':'瘦','正':'歪','直':'彎','良':'惡','低':'高','東':'西','南':'北','男':'女','你':'我'}.items():
        if i in ctx.content:
            t=t.replace(i,v)
        elif v in ctx.content:
            t=t.replace(v,i)
    await ctx.channel.send(t[2:-1])
  pattern = r'https://discord\.com/channels/(\d+)/(\d+)/(\d+)'
  match = re.match(pattern, ctx.content)
  if match:
        guild_id, chennal_id, message_id = map(int, match.groups())
        if ctx.guild.id==guild_id:
            message=bot.get_channel(chennal_id)
            message=await message.fetch_message(message_id)
            if message.author.bot==False:
                d={f'<t:{int(message.created_at.timestamp())}:F>':message.content}
                if message.reference.cached_message:
                    d[f"回覆<@{message.reference.cached_message.author.id}>"]=message.reference.cached_message.content
                await ctx.channel.send(f"自動分析訊息{' '.join([i.url for i in message.attachments])}",reference=ctx,embed=EM("",f"<@{message.author.id}>",d),mention_author=False)
   
async def sendlink(ch,ls,v):
    return
    ll={}
    for l in ls:
        if l.startswith("https://"): continue
        try:
            response = requests.get(l)
            soup = bs(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else "無法取得標題"
            og_title = soup.find('meta', property='og:title')['content'] if soup.find('meta', property='og:title') else "沒有說明"
            ll[l] = title + '\n' + og_title
        except Exception as e:
            print(e)
    await ch.send(embed=EM('AI萬能機器自動分析連結','以下為各連結的預覽',ll),view=v)
   
async def stopsend(it):
    with open("stop.json", "r", encoding='utf-8') as file:
        data3 = json.load(file)
    if it.user.id not in data3["stop"]:
        data3["stop"].append(it.user.id)
    
    with open("stop.json", "w") as file:
      json.dump(data3, file, indent=4)
    await it.response.send_message("已阻擋",ephemeral=True)
async def deldaytn(it):
    await it.response.send_message("已刪除",ephemeral=True)
    await it.message.delete()
            
def helpchi():
  select = Select(placeholder="選想查的功能",
                  options=[
                    discord.SelectOption(label="快捷發言",
                                         value="help1",
                                         emoji="💬",
                                         description="懶得打字就用它!"),
                    discord.SelectOption(label="遊戲與娛樂",
                                         value="help2",
                                         emoji="🎮",
                                         description="簡單小遊戲"),
                  discord.SelectOption(label="AI",
                                         value="help9",
                                         description="!就是AI"),
                    discord.SelectOption(label="音樂播放與改變音調",
                                         value="help3",
                                         emoji="🎵",
                                         description="萬能機器-讓機器人成為Discord聽音樂首選!"),                     
                    discord.SelectOption(label="管理與設定",
                                         value="help4",
                                         emoji="🚥",
                                         description="辦事真輕鬆"),
                    discord.SelectOption(label="文字改造工具!҉꧔ꦿ'้้้้้",
                                         value="help5",
                                         emoji="🆎",
                                         description="華麗!҉꧔ꦿ'้้้้้้無上限"),
                    discord.SelectOption(label="查詢與生成",
                                         value="help6",
                                         emoji="🔍",
                                         description="搜尋網路及寶可夢圖鑑"),
                    discord.SelectOption(label="開發者工具",
                                         value="help7",
                                         emoji="🧿",
                                         description="!"),
                    discord.SelectOption(label="列出所有指令",
                                         value="help8",
                                         emoji="🈯",
                                         description="列出全部"),
                  ])
  return select

#HELP

@bot.tree.command(name="help", description="如何使用")
@app_commands.allowed_installs(guilds=True, users=True)
async def hl(ctx, ):
  select=helpchi()

  button = Button(
    label="報修單",
    emoji="🛠",
    url=
    "https://docs.google.com/forms/d/e/1FAIpQLSePDj_iVFkeKHlC1sEFWF9vvj06055ELuI-C9EpuYcNKRgq_g/viewform?usp=sf_link",
    style=discord.ButtonStyle.link)
  butt2 = Button(
    label=
    "官้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้網้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้",
    emoji="<a:okk:1277864492163928166>",
    url="http://owo.freeserver.tw:20371/",
    style=discord.ButtonStyle.link)
  butt3 = Button(
    label="把我抓進你的伺服器",
    emoji="<a:cc:1147777573074522172>",
    url=
    "https://discord.com/oauth2/authorize?client_id=1132079788140531872",
    style=discord.ButtonStyle.link)
  butt4 = Button(label="訂閱我",
                 emoji="🎉",
                 url="https://www.youtube.com/@xHSK",
                 style=discord.ButtonStyle.link)
  embed = None

  

  view = View(timeout=0)
  view.add_item(select)
  # view.add_item(button)
  view.add_item(butt2)
  view.add_item(butt3)
  view.add_item(butt4)
  embed = discord.Embed(title="客服",
                        url="https://bot.is-from.tw")
  embed.add_field(
    name="選則底下的功能來詢問",
    value=
    "嗨嗨，你發現了酷東西!使用我來讓你的discord更棒!!想要了解某個類別請使用下方的選單，如要查看特定的指令請使用</help:1106476433875927102> 或`/客服`你也可以到**官網**https://bot.is-from.tw/ 有教學\n\n在輸入欄打/來看有哪些斜線命令\n\n||如果真的有問題請按《開始客服》||",
    inline=False)
  await ctx.response.send_message(embed=embed, view=view)





import scrapetube


@bot.tree.command(name="設定yt發片通知", description="有新片時自動通知")
@commands.has_permissions(administrator=True)
@app_commands.describe(
  連結=
  "你的YT頻道連結，例如:https://www.youtube.com/channel/UCNBQ9IWXzUv81rcKZkvXP7A 錯誤:https://www.youtube.com/@xHSK",
  通知="要說甚麼，(@n代表影片名稱)例如:不是人發片瞜!@n",
  頻道="發通知到哪?")
async def set_yt(ctx, 連結: str, 頻道: discord.TextChannel, 通知: str):
  if ctx.user.guild_permissions.administrator:
    # try:
    if True:
      
      with open("YT.json", "r") as file:
        data = json.load(file)
      try:
      
        videos = scrapetube.get_channel(channel_url=連結, limit=1)

        for video in videos:
          embed = discord.Embed(
            title="<a:YT:1135838936892186675>"+video['title']['runs'][0]['text'],
            url=f"https://www.youtube.com/watch?v={video['videoId']}",
            color=0xd03a20)
          embed.set_image(url=video['thumbnail']['thumbnails'][0]['url'])
          # embed.set_author(name=video['longBylineText']['runs'][0]['text'], url="https://youtube.com"+video['longBylineText']['runs'][0]['navigationEndpoint']['browseEndpoint']['canonicalBaseUrl'], icon_url=video['channelThumbnailSupportedRenderers']['channelThumbnailWithLinkRenderer']['thumbnail']['thumbnails'][0]['url'])
          print(
            f"https://www.youtube.com/watch?v={video['videoId']}")  # video id
          print(video['title']['runs'][0]['text'])  # video title
          await 頻道.send(通知.replace('@n',video['title']['runs'][0]['text']), embed=embed)
          if len(通知) < 5000:
            data[str(ctx.guild.id)] = [
              頻道.id, 連結, 通知, video['title']['runs'][0]['text']
            ]
            await ctx.response.send_message("<a:okk:1277864492163928166>資料更新成功"
                                            )
          else:
            await ctx.response.send_message(
              "<a:okk:1277864492163928166>資料太長，已自動刪去")
            data[str(ctx.guild.id)] = [
              頻道.id, 連結, "".join(list(通知)[:21]),
              video['title']['runs'][0]['text']
            ]
      except Exception as bug:
         await ctx.response.send_message("私人頻道或連結錯誤"+str(bug))

      with open("YT.json", "w") as file:
        json.dump(data, file, indent=4)

    # except Exception as bug:
    #   await ctx.response.send_message(bug)
    #   print(bug)
  else:
    await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限還想怎樣?", "把我家到你的伺服器才有用")
    )





class aremo(discord.ui.Modal,title="回報"):
  def __init__(self, title):
        super().__init__(timeout=60.0)
        self.title = title
  answer = discord.ui.TextInput (label = "讓機器人有更好的回答", style = discord.TextStyle.short, placeholder="", default="", required = True, max_length= 50)
 
  async def on_submit(self, ctx: discord.Interaction):
    with open("aii.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    data["index"].append({"input":self.title, "output": [str(self.answer)]})
    with open("aii.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    await ctx.response.edit_message(view=butt("已收到您的回覆","https://discord.com/oauth2/authorize?client_id=1132079788140531872","✨"))



import aiohttp
from itertools import cycle
from aiset import gen_image
from discord.app_commands import Choice, CommandTree,Group,command


@bot.tree.context_menu(name="問問ai")
async def saai(ctx, s: discord.Message):
    await predict_reply(s.content,ctx,'i')
    await bot.change_presence(activity=discord.Streaming(name="訓練/ai",platform="YouTube",url="https://www.youtube.com/watch?v=wbS6IK-4Qe0"))
#AI
@bot.tree.command(name="ai", description="與AI對話")
@app_commands.describe(問題="你想講什麼?")
async def ai(ctx: discord.Interaction, 問題: str,檔案:Optional[discord.Attachment]):
  attachments=檔案
  if attachments:
      if any(attachments.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
                await ctx.response.defer()
                tim=time.time()
                async with aiohttp.ClientSession() as session:
                    async with session.get(attachments.url) as resp:
                        if resp.status == 200:
                            image_data=await resp.read()
                            txt=await gen_image(image_data, ctx.user.name+'說了:'+問題)
                            em=EM( 問題 if len(問題)<255 else 問題[:250]+'...','',{f'這是經過{time.time()-tim}秒努力思考的結果:':txt})
                            await ctx.followup.send(embed=em)
                            return
      if  any(attachments.filename.lower().endswith(ext) for ext in ['.txt', '.js', '.py', '.json', '.css','.html','.htm']):
                t=await attachments.read()
                t=問題+t.decode('utf-8')
                await predict_reply(t.replace("<@1132079788140531872>",""),ctx,'i')
                return  
  await predict_reply(問題,ctx,'i')
  await bot.change_presence(activity=discord.Streaming(name="訓練/ai",platform="YouTube",url="https://www.youtube.com/watch?v=wbS6IK-4Qe0"))

@bot.tree.command(name="ai拔除頻道",description="拔除AI頻道")
async def subsnd(ctx):
      if ctx.user.guild_permissions.administrator!=True:
            await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你不是擁有者",
                      "把我加到你的伺服器才有用"),
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ),ephemeral=True)
            return
      with open('cog/setai.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
      if str(ctx.guild.id) in data:
        del data[str(ctx.guild.id)]
      with open(" cog/setai.json", "w") as outfile:
            json.dump(data, outfile)
      await ctx.response.send_message('完成!<a:yes:1293857715013025792>')

@bot.tree.command(name="ai設定頻道",description="設為AI頻道")
async def subsubcommd2(ctx):
      if ctx.user.guild_permissions.administrator!=True:
            await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你不是擁有者",
                      "把我加到你的伺服器才有用"),
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ),ephemeral=True)
            return
      with open('cog/setai.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
      data[str(ctx.guild.id)]=ctx.channel.id
      with open("cog/setai.json", "w") as outfile:
            json.dump(data, outfile)
      await ctx.response.send_message('完成!<a:yes:1293857715013025792>')    
    
async def cccc(ctx):
    await ctx.response.send_modal(aremo(title=ctx.message.embeds[0].title))
  # try:
  #   with open("AI.json", "r", encoding='utf-8') as file:
  #     data = json.load(file)
  #   answer = "今天次數已達上限"
  #   if data["today"] < 6:
  #     data["today"] += 1
  #     with open("AI.json", "w") as file:
  #       json.dump(data, file)
  #     answer = chatgtp_response(thing_to_say)
  #   await interaction.channel.send(embed=discord.Embed(
  #     title="".join(list(answer)[:1001])))
  #   print(answer)
  # except Exception as bug:
  #   await interaction.channel.send(f"恩~說的對，『{bug}』永遠是對的")
  # del answer
async def predict_reply(input_text,ctx,typ="c"):
    with open('aic.json') as user_file:
        jso = json.load(user_file)
    # 讀取訓練資料
    for i in ['music','音樂','播放','YT',"youtube"]:
        if i in input_text:
            try:
                YouTube(input_text.replace(' ',''))
                await playm(ctx,url,'c')
            except Exception:
                await ctx.channel.typing()
                options=[]
                c=0
                url=input_text[2:].replace(' ','').replace(i,'')
                videos = scrapetube.get_search(query=input_text[2:].replace(' ','').replace("	",""),limit=24,results_type="video")
                for video in videos:
                    options.append(discord.SelectOption(label=video['title']['runs'][0]['text'],value="p&https://www.youtube.com/watch?v="+video['videoId'],emoji="<a:YT:1135838936892186675>"))
                    c+=1
                embed=discord.Embed(title="<a:YT:1135838936892186675>"+url if len("<a:YT:1135838936892186675>"+url)<200 else "<a:YT:1135838936892186675>"+url[:150], url=f"https://www.youtube.com/results?search_query={url}",color=0xf50000,description="點選以下選項開始播放")
                if c==0:
                    options.append(discord.SelectOption(label="DISCORD看我建造一個機器人伺服器",value="p&https://www.youtube.com/watch?v=dne5kKtz2lA",emoji="<:me:1122364224103006300>"))
                select = Select(placeholder=f"找到{c}項結果", options=options)
                view = View(timeout=0)
                view.add_item(select)
                if typ=='c':
                    await ctx.channel.send(embed=embed,view=view,reference=ctx)
                else:
                    await ctx.response.send_message(embed=embed,view=view)
                return
    if input_text:
        await ctx.channel.send("<a:yes:1293857715013025792>分析成功!使用AI 4.5回答\n> 這可能需要10秒的時間")
        if typ=='c':
            await ctx.channel.typing()
            em=await initiate_conversation(message=input_text,ii=ctx.guild.id,us=ctx.author.name)
            await ctx.channel.send(embed=em,reference=ctx)
        else:
            await ctx.response.defer()
            em=await initiate_conversation(message=input_text,ii=ctx.guild.id,us=ctx.user.name)
            await ctx.followup.send(embed=em)
        return
            
    for i in ["幹白癡","雞掰","死","爛","廢","智障","低能兒","你媽","你娘"]:
      if i in input_text:
        em=EM(input_text,f"你才{input_text[1:50]}！🙄")
        if typ=='c':
            await ctx.channel.send(content="<a:yes:1293857715013025792>分析成功!使用AI 1.0回答",embed=em,reference=ctx)
        else:
            await ctx.response.send_message("<a:yes:1293857715013025792>分析成功!使用AI 1.0回答",embed=em)
        return
    with open("aii.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 提取訓練資料的輸入和輸出
    #X_train = [item["input"] for item in data["index"]]
    #y_train = [random.choice(item["output"]) for item in data["index"]]

    # 建立模型
    #model = make_pipeline(TfidfVectorizer(), MultinomialNB())

    # 訓練模型
    #model.fit(X_train, y_train)

    # 使用模型進行預測
    predicted_output ='???' #model.predict([input_text])
    if len(predicted_output) >3 :
        predicted_output=predicted_output[:3]
    elif len(predicted_output) <1:
        predicted_output=["不好意思，我不太明白你的問題。"]
    em=EM(input_text,random.choice(predicted_output))
    if typ=='c':
        await ctx.channel.send(content="<a:yes:1293857715013025792>分析成功!使用AI 3.0回答\n#### 這可能需要2秒的時間",embed=em,reference=ctx)
    else:
        b=discord.ui.Button(style=discord.ButtonStyle.green, label="有更好的說法?", emoji="✨")
        view=View().add_item(b)
        b.callback=cccc
        await ctx.response.send_message("<a:yes:1293857715013025792>分析成功!使用AI 3.0回答\n#### 這可能需要2秒的時間",embed=em,view=view)
    return
  
async def initiate_conversation(message,ii,us):
    tim=time.time()
    with open('aic.json') as user_file:
        jso = json.load(user_file)
    ii=str(ii)
    if ii in jso:
        data = {'message': message, 'chat_id':jso[ii][1]}
    else:
        jso[ii]=[0,0]
        data = {'message': message}
    jso[ii][0]+=1
    if jso[ii][0]<10:
        msg=us+"說:"+message
        with open('cog/aichannel.json', 'r', encoding='utf-8') as file:
          data = json.load(file)  #開啟json檔
        if ii not in data:
            data[ii]=[]
        data[ii].append(msg)
        content= await chatai(msg)
        data[ii].append(content)
        content=content if len(content)<1000 else content[:1000]
        em=EM( message if len(message)<255 else message[:250]+'...','',{f'這是經過{time.time()-tim}秒努力思考的結果:':content})
        #with open(" a/aic.json", "w") as outfile:
          #  json.dump(jso, outfile)
        #with open(" a/cog/aichannel.json", "w") as outfile:
         #  json.dump(data, outfile)
        return em
    base_url = f'https://api.oneai.com/agent/v1/agents/-14858/chat'
    headers = {
        'Content-Type': 'application/json',
        'api-key': "28c08626-7ecd-4dd7-afbe-aba98328f334"
    }
    

    response = requests.post(base_url, headers=headers, json=data)
    
    print(response.content.decode('utf-8'))
    lines = response.content.decode('utf-8').split('\n')
    
    content_lines = [line.split(': ', 1)[1].strip() for line in lines if line.startswith('data:')]
    if len(content_lines)<2:
        data = {'message': message}
        response = requests.post(base_url, headers=headers, json=data)
        lines = response.content.decode('utf-8').split('\n')
        content_lines = [line.split(': ', 1)[1].strip() for line in lines if line.startswith('data:')]    
    jso[ii][1]=content_lines[-2]
    with open("aic.json", "w") as outfile:
        json.dump(jso, outfile)
    # 將內容連結成字串
    content = ''
    for i in content_lines[:-2]:
        if i[-1] in 'QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp':
            content+=i+' '
        else:
            content+=i
    
    content=content.replace('OneAgent','One能AI')
    if 'a' not in content:
        content=content.replace("`",'```')
    content=content if len(content)<1000 else content[:1000]
    if 'only answer relevant questions'in content :
        content='作為One能AI你只能問我AI萬能機器的指令用法或discordpy'
    em=EM( message if len(message)<255 else message[:250]+'...','',{f'這是經過{time.time()-tim}秒努力思考的結果:':content})
    return em
        


@bot.tree.command(name="大量建立身分組", description="用於草創期與破壞修復")
@app_commands.choices(權限類別=[
  Choice(name='無設定', value=0),
  Choice(name='可說話', value=4915593582656),
  Choice(name='長老', value=58822328055876),
  Choice(name='管理員', value=70368744177527),
])
async def makes(ctx, 數量: int, 權限類別: Choice[int]):
  if ctx.user.guild_permissions.administrator:
    guild = ctx.guild
    try:
      for i in range(數量):
        await guild.create_role(
          name=f"自動建立{i+1}",
          permissions=discord.Permissions(permissions=權限類別.value))
        await asyncio.sleep(1)
    except:
      await ctx.response.send_message(
        embed=saybugs("把我權限拉高", "<a:XX:1120631053921566861>沒改名權限"),
        view=butt(
          "增加權限",
          "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
        ))
    try:
      await ctx.response.send_message(
        embed=embedMake("<a:yes:1293857715013025792>完成!"))
    except:
      await ctx.channel.send(embed=embedMake("<a:yes:1293857715013025792>完成!"))
  else:
    await ctx.response.send_message(
      embed=saybugs("你不是伺服器用有者", "<a:XX:1120631053921566861您沒權限"),
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ),ephemeral=True)


@bot.tree.command(name="嵌入產生", description="產生嵌入")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.describe(標題="標題", 副標題="副標", 內文="比較小的字", 第二副標="比較中的字", 第二內文="小字")
async def eee(interaction: discord.Interaction,
              標題: str,
              副標題: Optional[str] = "",
              內文: Optional[str] = "",
              第二副標: Optional[str] = "",
              第二內文: Optional[str] = ""):
  await interaction.response.send_message(
    embed=embedMake(標題, 副標題, 內文, 第二副標, 第二內文))


@bot.tree.command(name="kick", description="笑他然後踢爆他")
@commands.has_permissions(manage_roles=True, ban_members=True)
async def _kick(ctx, member: discord.Member, 如何笑他: str):
  if ctx.user.guild_permissions.kick_members:
    try:
      if member.id != 1132079788140531872:
        button = Button(label="改去別的伺服器逛逛",
                        emoji="🥚",
                        url="https://discord.gg/CaFUuFTUzQ",
                        style=discord.ButtonStyle.link)
        view = View()
        view.add_item(button)
        user = await bot.fetch_user(member.id)
        await user.send(embed=embedMake("你被踢出了伺服器",
                                        如何笑他,
                                        end=f"BY {ctx.guild}"),
                        view=view)
        await member.kick()
        await ctx.response.send_message(embed=embedMake("YA!她被我踢了", 如何笑他))
      else:
        await ctx.response.send_message(embed=embedMake(
          "幹你踢我幹嘛?", "", "<a:gan:1072391347383849002> 要踢先踢YEE式鐵廢龍，他的伺服器的管理員很壞")
                                        )
    except Exception as bug:
      button = Button(
        label="重設我的權限",
        emoji="💌",
        url=
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872",
        style=discord.ButtonStyle.link)
      view = View()
      view.add_item(button)
      await ctx.response.send_message(embed=embedMake(
        "太硬 踢到鐵板了", f"可以試著把我重新加入伺服器確保權限足夠{bug}", "請確保我有踢人權限"),
                                      view=view)
  else:
    await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限還想怎樣?", "把我加到你的伺服器才有用")
    )


@bot.tree.command(name="計算", description="進行國小程度的四則運算")
@app_commands.describe(算式="例如:1+1")
async def ee(interaction: discord.Interaction, 算式: str):
  await bot.get_channel(1138271198929768498).send(f"{interaction.user}({interaction.user.id})使用了{算式}",allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
  if "interaction" in 算式:
    await interaction.channel.send("<discord.interactions.Interaction object at 0503asksxmz>",allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
    return
  if "\"" in 算式:
    await interaction.response.send_message(算式.split("\"")[1],allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
    return
  if "'" in 算式:
    await interaction.response.send_message(算式.split("'")[1],allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
    return
  if "除夕" in 算式:
    await interaction.response.send_message(embed=EM('除夕','2月9日星期五',{'現在時間:':f"<t:{int(time.time())}:R>","祝您愉快":"https://www.google.com/search?q=%E9%99%A4%E5%A4%95 "}),allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
    return
  if "新年" in 算式 or "春節" in 算式:
    await interaction.response.send_message(embed=EM('新年快樂','2月10日星期六',{'現在時間:':f"<t:{int(time.time())}:R>","祝您愉快":"https://www.google.com/search?q=%E6%98%A5%E7%AF%80"}),allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
    return
  
  w = list(算式)
  for i in w:
    if i in "Xx。∙•∗⊛⊙⊚⋅⋆⋇*":
      w[w.index(i)] = "*"
  for i in w:
    if i not in ".0123456789+-/*()[]{}%":
      await interaction.response.send_message(
        embed=saybugs("SyntaxError:(U+FF0C)", "你的題目難到本蛋算不出來"))
      return
  await interaction.response.defer()
  try:
    aa = eval("".join(w))
    if int(aa) in [1225,37,125]:
        pass
        embed = discord.Embed(title=aa,
                          url="https://sites.google.com/view/pokeegg",color=0x0053fa)
        lis=[['聖誕節','聖誕節，又稱耶誕節[註 1]，是基督教紀念耶穌降生的節日，西方社會定於12月25日，但東方教會的國家稱其主顯節，則大致定於1月7日。其為基督教禮儀年曆的重要節日，部分教派會透過將臨期及聖誕夜來準備，並以八日慶典與禮儀節期延續慶祝。聖誕節也是許多國家和地區、尤其是西方國家等以基督教文化為主流之地區的公共假日；在教會以外的場合，聖誕節已轉化成一種民俗節日，並常與日期相近的公曆新年合稱「聖誕及新年季」。由於耶穌的誕生日期無法確定，聖經上也無相關記載，所以在學術上認為聖誕節是以聖母領報（3月25日）的日期來推估，或是在基督教發展初期將古羅馬的農神節（羅馬多神信仰）轉化而來，當時社會上（如古羅馬的冬至）以該節日慶祝日照時間由短變長。西方教會在發展初期至4世紀前中期開始將聖誕節定在12月25日，東方正教會稍晚以儒略曆定於1月7日，亞美尼亞教會則定在1月6日或1月19日。在現代聖誕節同時兼具宗教節日與文化節慶的雙重功能，除了參與教會儀式與活動外，家戶、行號與街頭上也可見相關佈置，更是重要的商業活動時令；而過聖誕節的習慣，亦隨著近代西方國家的影響力而擴展到全世界。但在基督教並非主流宗教的地區（如東亞），除了當地的教會團體外，聖誕節經常被當作消費活動的名目，這種沒有宗教意義的商業民俗活動，不需要接受西方文化者也能自由的參與，且如同西方國家的「聖誕及新年季」與公曆新年結合，過節時間拉長到數週，成為全年重要的購物和消費季之一。宗教上一脈相承的伊斯蘭教國家則更為特殊，雖然聖誕節在伊斯蘭教文化也是有意義的，並承認耶穌是先知，但視聖誕節為歪曲產物，不允許過聖誕有關的宗教活動，不過鑒於西方聖誕民俗活動多數已經失去宗教色彩，穆斯林則可以給予對方祝福、適當參加團聚活動亦可[1]。猶太教的以色列也沒有這個節日[2][3]。','https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Nativity_tree.jpg/250px-Nativity_tree.jpg','維基百科','https://zh.wikipedia.org/zh-tw/%E5%9C%A3%E8%AF%9E%E8%8A%82'],['12月25日','聖誕節\n太陽神密特拉的誕辰\n 中華民國：\n雲南起義紀念日\n行憲紀念日\n巴基斯坦：領袖誕辰','https://google.com','維基百科','https://zh.wikipedia.org/zh-tw/12%E6%9C%8825%E6%97%A5'],['行憲紀念日','行憲紀念日為中華民國法定節日，定於每年12月25日，是紀念制憲國民大會代表於1946年（民國35年）12月25日三讀通過《中華民國憲法》而設立。1963年（民國52年）行政院將行憲紀念日定為國定假日[1]；直至2000年（民國89年）取消的這段期間，每年12月25日均放假一天。2001年（民國90年）起公務人員實施周休二日，行憲紀念日不再放假。目前12月25日因為這天也是基督教的聖誕節，部份企業與基督新教、天主教會學校仍會宣佈放假。','https://zh.wikipedia.org/wiki/File:%E6%B6%B5%E7%A2%A7%E6%A8%93%E7%B4%80%E5%BF%B5%E9%A4%A8%E6%96%87%E7%89%A9%E5%B1%95%E8%A6%96-07.2023-10-13.jpg','維基百科','https://zh.wikipedia.org/wiki/%E8%A1%8C%E6%86%B2%E7%B4%80%E5%BF%B5%E6%97%A5']]
        lis=random.choice(lis)
        embed.add_field(name=lis[0], value=lis[1], inline=False)
        embed.set_image(url=lis[2])
        button = Button(label=lis[3], url=lis[4], style=discord.ButtonStyle.link)
        view = View(timeout=0)
        view.add_item(button)
        await interaction.followup.send(embed=embed,view=view)
        return
    if int(aa) in [10,20,100,101,1010]:
        embed = discord.Embed(title=aa,
                          url="https://sites.google.com/view/pokeegg",color=0x0053fa)
        lis=[["國慶日","中華民國的國慶日，定為1911年武昌起義的發動日——10月10日，亦稱雙十節、雙十國慶、雙十慶典。武昌起義是辛亥革命的開端，起事後兩個月內中國各地革命行動陸續成功，最終成功推翻清朝，並於1912年1月1日成立中華民國（中華民國開國紀念日），成為東亞第一個獲普遍承認的共和國。該日亦為中華民國的國定紀念日之一。\n> 維基百科","https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Double-tenth-symbol.svg/450px-Double-tenth-symbol.svg.png","打開維基百科","https://zh.wikipedia.org/zh-tw/%E5%9C%8B%E6%85%B6%E6%97%A5_(%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B)"],["武昌起事","武昌起義，或作武昌起事，是1911年10月10日（清宣統三年八月十九）清朝新軍等力量在中國武漢武昌發動的兵變，旨在推翻清朝統治，是辛亥革命的開端。武昌起義的成功，使中國各地陸續響應革命黨人推翻清朝的訴求，最終使清帝在1912年2月12日退位，結束了中國長達兩千年的帝制政體，建立中國史上第一個共和國，即中華民國，是中國走向民主共和的開端，在中國歷史中具有重要里程碑意義。\n> 維基百科","https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Hubei_Military_Government.jpg/330px-Hubei_Military_Government.jpg","打開維基百科","https://zh.wikipedia.org/zh-tw/%E6%AD%A6%E6%98%8C%E8%B5%B7%E4%B9%89"],
              ["雙十節","每年雙十節google都有彩蛋!","https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Double-tenth-symbol.svg/450px-Double-tenth-symbol.svg.png","打開google","https://www.google.com/search?q=%E9%9B%99%E5%8D%81%E7%AF%80&sca_esv=570946894"]]
        lis=random.choice(lis)
        embed.add_field(name=lis[0], value=lis[1], inline=False)
        embed.set_image(url=lis[2])
        button = Button(label=lis[3], url=lis[4], style=discord.ButtonStyle.link)
        view = View(timeout=0)
        view.add_item(button)
        await interaction.followup.send(embed=embed,view=view)
        return
    embed = discord.Embed(title=aa,
                          url="https://sites.google.com/view/pokeegg",color=0x0053fa)
    await interaction.followup.send(embed=embed)
  except ZeroDivisionError as er:
    await interaction.followup.send(embed=saybugs(er, "除數不能為零"))
  except Exception as er2:
    await interaction.followup.send(embed=saybugs(er2, "你的題目難到本蛋算不出來"))

class lonaddm(discord.ui.Modal,title="自訂選項"):
  def __init__(self):
        super().__init__(timeout=60.0)
        self.bot=bot
  titt=discord.ui.TextInput (label = "自訂選項", style = discord.TextStyle.short, placeholder="新增投票選項", default="", required = True, max_length= 5)
  
  async def on_submit(self, ctx: discord. Interaction):  
    view=View(timeout=0)
    em=ctx.message.embeds[0].to_dict()
    for i in range(len(em['fields'])):
      if em['fields'][i]['name']!='':
        view.add_item(Button(style=discord.ButtonStyle.green, label=str(em['fields'][i]['name']),custom_id=f'con{i}'))
    em=ctx.message.embeds[0].add_field(name=self.titt.value, value=f'<@{ctx.user.id}>')
    view.add_item(Button(style=discord.ButtonStyle.gray, label=str(self.titt.value), custom_id=f'con{len(ctx.message.embeds[0].fields)}'))
    view.add_item(Button(style=discord.ButtonStyle.green, label='其他',custom_id=f'concon'))
    await ctx.response.edit_message(embed=em)
    await ctx.message.edit(view=view)
    
@bot.tree.command(name="更改狀態",description="更改機器人狀態")
@app_commands.describe(狀態="自訂機器人狀態")
async def tolltoll(ctx,狀態:str): 
    if ctx.guild and ctx.guild.id==1062288200187510904:
        await bot.change_presence(activity=discord.Streaming(name=狀態,platform="YouTube",url="https://youtu.be/r5vCYxm-ZN0?si=ZClrV-Bvo-dJ2azh"))
        await ctx.response.send_message(embed=EM('<a:yes:1293857715013025792>更改成功'))
    else:
        await ctx.response.send_message(embed=EM('失敗，此指令只能在支援群使用','https://discord.gg/CaFUuFTUzQ'))
        
@bot.tree.command(name="調查活動",description="建立一個公開調查活動")
@app_commands.describe(選項="投票選項，用/分開")
async def tolltoll(ctx,主題:str,選項:str):
  t=選項
  matches=選項.split('/')
  em={}
  con=0
  view=View(timeout=0)
  for match in matches:
            name = match
            em[name]=''
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, label=name if name!='' else '其他',custom_id=f'con{con}' if name!='' else 'concon'))
            con+=1  
  await ctx.response.send_message(view=view,embed=EM(主題,'',em).set_author(name=ctx.user.global_name if ctx.user.global_name else ctx.user.name,icon_url =ctx.user.avatar.url))

@bot.tree.command(name="大家的邀請",description="檢查大家創建的邀請邀請到的人")
async def intvinec(ctx):
    invites = await ctx.guild.invites()
    invite_counts = {}
    for invite in invites:
        if invite.inviter in invite_counts:
            invite_counts[invite.inviter] += invite.uses
        else:
            invite_counts[invite.inviter] = invite.uses
    sorted_invites = sorted(invite_counts.items(), key=lambda x: x[1], reverse=True)
    embed = discord.Embed(title='邀请連結使用次数排名', color=0x00ff00)
    c=0
    for i, (user, uses) in enumerate(sorted_invites, start=1):
        embed.add_field(name=f'第{i}名：{user.name}', value=f'使用次数: {uses}', inline=False)
        c+=1
        if c>10:
            break

    await ctx.response.send_message(embed=embed)
    
#####蟲洞工廠
@bot.tree.command(name="設定頻道蟲洞", description="啟動後將能與其他有頻道蟲洞的人對話")
async def chat(ctx):
  if ctx.user.guild_permissions.administrator:
    try:
      with open("chat.json", "r") as file:
        data = json.load(file)
      if str(ctx.guild.id) in data:
        try:
          wb = data[str(ctx.guild.id)][1]
          wb = discord.Webhook.from_url(wb, session=aiohttp.ClientSession())
          await wb.send(embed=embedMake("將結束頻道蟲洞"), username="蟲洞使者")
          wb.delete
        except:
          pass
      wb = await ctx.channel.create_webhook(name="蟲洞使者")
      data[str(ctx.guild.id)] = [ctx.channel.id, wb.url]
      with open("chat.json", "w") as file:
        json.dump(data, file, indent=4)
      await ctx.response.send_message(
        embed=embedMake("💫這裡成了頻道蟲洞!", "在這講話別的頻道會看到，請小心"))
    except :
      await ctx.response.send_message(
      "<a:XX:1120631053921566861>我沒權限",
      view=butt(
        "增加權限",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ))
  else:
    await ctx.response.send_message(
      "<a:XX:1120631053921566861>您沒權限",
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ),ephemeral=True)


class MyCog(commands.Cog, name="蟲洞使者"):

  def __init__(self, bot):
    self.bot = bot
    with open("chat.json", "r") as file:
      self.data3 = json.load(file)
    self.wait = 0

  @tasks.loop(seconds=60)
  async def set60(self):
    with open("chat.json", "r") as file:
      self.data3 = json.load(file)

  @commands.Cog.listener()
  @commands.max_concurrency(5)
  async def on_message(self, ctx):
    if "來҉自҉" in str(ctx.author):
      return
    if ctx.author.bot and ctx.author.id!=1132079788140531872:
      return

    async def send_webhook_message(webhook_url, username, content, he, f, r,aa):
      async with aiohttp.ClientSession() as session:
        try:
          webhook = discord.Webhook.from_url(webhook_url, session=session)
          if r is not None:
            u = await ctx.channel.fetch_message(r.message_id)
            r = discord.Embed(color=0x00cc6d)
            r.set_author(name=u.author, icon_url=u.author.avatar.url)
            r.add_field(name="", value=u.content)
          else:
            r = None
          isa=discord.AllowedMentions(everyone=False, users=aa, roles=False, replied_user=False)
          if f!= 0:
            file=f
            await webhook.send(content,
                               username=username,
                               avatar_url=he,
                               files=[await i.to_file() for i in file],
                               embed=r,allowed_mentions=isa)
          else:
            await webhook.send(content,
                               username=username,
                               avatar_url=he,
                               embed=r,allowed_mentions=isa)
        except Exception as bug:
          print(str(bug))

    if ctx.guild and str(ctx.guild.id) in self.data3:
      if self.data3[str(ctx.guild.id)][0] == ctx.channel.id:
        ad = 0
        if len(ctx.attachments) > 0:
          ad=ctx.attachments
          
        await self.bot.change_presence(activity=discord.Streaming(name="當蟲洞",platform="YouTube",url="https://www.youtube.com/watch?v=wbS6IK-4Qe0"))
        mentioned_users = ctx.mentions
        aa=False
        
        # 檢查被提及的使用者是否在群組中
        aa=True
        for x in self.data3:
          if ctx.guild.id != int(x):
            await asyncio.sleep(self.wait)
            self.wait=0
            # target_channel = bot.get_channel(self.data3[x][0])
            user = ctx.author
            if str(user).endswith("#0"):
              user = ctx.author.name
            user=f"{user}來҉自҉{ctx.guild}"
            if ctx.author.id==1132079788140531872:
                async with aiohttp.ClientSession() as session:
                    try:
                      webhook = discord.Webhook.from_url(webhook_url, session=session)
                      webhook.channel.send(replace_mentions(ctx.content),embeds=ctx.embeds)
                    except:
                        pass
            else:    
                await send_webhook_message(self.data3[x][1],
                                       user if len(user)<80  else user[:79],
                                       replace_mentions(ctx.content),
                                       ctx.author.avatar.url,
                                       f=ad,
                                       r=ctx.reference,
            aa=aa)
            self.wait += 2
        #await ctx.add_reaction('💫')

def replace_mentions(text):
    # 將 "@everyone" 取代為 "@everybody"
    text = text.replace("@everyone", "@everybody")
    
    # 將 "@here" 取代為 "@there"
    text = text.replace("@here", "@there")
    
    return text

#開發者
ccgroup=Group(name="開發者",description="取得資訊")
@ccgroup.command(name="關於機器", description="about_this_bot")
async def ccapi(ctx):
  await ctx.response.defer()
  embed = discord.Embed(
    title="開發者模式",
    url=
    "https://discord.com/oauth2/authorize?client_id=1132079788140531872",
    color=0x5956f0)
  embed.add_field(name="正在住的伺服器",
                  value=len(bot.guilds),
                  inline=False)
  slash = await bot.tree.sync()
  embed.set_image(url=ctx.user.avatar.url)
  embed.add_field(name="提供的斜線指令數", value=len(slash), inline=True)
  embed.add_field(name="支援服宣傳文", value="# 想找個地方開趴卻怕被ban?想認識更多人卻不敢講話?\n> 可以邀請各種奇葩人士組織邪教\n\n> 自由開趴自由發言\n\n> 公平法治的管理\n\n\n## **小小伺服等大人需要你的小指頭**\n\n# 宣傳文看飽了?趕快加入:\n[discord/gg:pokeegg](https://discord.gg/CaFUuFTUzQ)", inline=False)
  await ctx.followup.send(embed=embed,view=View(timeout=0).add_item(helpchi()))

import pytz

@ccgroup.command(name="關於我", description="所有自己的狀態")
async def ccuser(ctx):
    us=ctx.user
    embed=discord.Embed(title=us.global_name if us.global_name else us.name, description=f"{us}", color=us.color)
    embed.add_field(name="使用者ID", value=us.id, inline=True)
    vi=None
    if us.avatar:
      embed.set_image(url=us.avatar.url)
      vi=butt("頭像連結",us.avatar.url)
    embed.add_field(name="成為成員時間", value=us.joined_at.astimezone(pytz.timezone('Asia/Taipei')), inline=True)
    embed.add_field(name="加入DC時間", value=us.created_at.astimezone(pytz.timezone('Asia/Taipei')), inline=True)    
    embed.add_field(name="暱稱", value=us.nick, inline=False)
    roles = [str(role.id) for role in us.roles] 
    embed.add_field(name="有的身分", value=f"<@&{'><@&'.join(roles)}>", inline=False)
    await ctx.response.send_message(embed=embed,view=vi)
  
@ccgroup.command(name="使用者", description="get_a_user's")
async def ccauser(ctx,從使用者:discord.User):
    us=從使用者
    embed=discord.Embed(title=us.global_name if us.global_name else us.name, description=f"{us}", color=us.color)
    embed.add_field(name="使用者ID", value=us.id, inline=True)
    embed.add_field(name="加入DC時間", value=us.created_at.astimezone(pytz.timezone('Asia/Taipei')), inline=True)                                 
    vi=None
    if us.avatar:
      embed.set_image(url=us.avatar.url)
      vi=butt("頭像連結",us.avatar.url)
    await ctx.response.send_message(embed=embed,view=vi)
    
    
@ccgroup.command(name="這個伺服器", description="get_this_guild")
async def ccagui(ctx):
    gu=ctx.guild
    embed=discord.Embed(title=gu.name, description=f"{gu.approximate_presence_count}位上線/{gu.approximate_member_count}位成員", color=0x0036b3)
    embed.add_field(name="伺服器ID", value=gu.id, inline=True)
    embed.add_field(name="成立時間", value=gu.created_at.astimezone(pytz.timezone('Asia/Taipei')), inline=True)                                 
    vi=None
    if gu.icon:
      embed.set_thumbnail(url=gu.icon.url)
      vi=butt("圖像連結",gu.icon.url)
    if gu.banner:
      embed.set_image(url=gu.banner.url)
      vi=butt("圖像連結",gu.icon.url)
    await ctx.response.send_message(embed=embed,view=vi)

@ccgroup.command(name="伺服器", description="get_guild")
async def ccaguild(ctx,id:str):
    gu=bot.get_guild(int(id))
    embed=discord.Embed(title=gu.name, description=f"{gu.approximate_presence_count}位上線/{gu.approximate_member_count}位成員", color=0x0036b3)
    embed.add_field(name="伺服器ID", value=gu.id, inline=True)
    embed.add_field(name="成立時間", value=gu.created_at.astimezone(pytz.timezone('Asia/Taipei')), inline=True)                                 
    vi=None
    if gu.icon:
      embed.set_thumbnail(url=gu.icon.url)
      vi=butt("圖像連結",gu.icon.url)
    if gu.banner:
      embed.set_image(url=gu.banner.url)
      vi=butt("圖像連結",gu.icon.url)
    await ctx.response.send_message(embed=embed,view=vi)

bot.tree.add_command(ccgroup)  

buttc=Group(name="按鈕",description="建立按鈕")

@buttc.command(name="發放一個身份組", description="give_a_role_to_clicker")
async def giverole(ctx,身分組:discord.Role,按鈕名稱:Optional[str],嵌入標題:Optional[str],嵌入說明:Optional[str],數量限制:Optional[int]):
    if ctx.user.guild_permissions.manage_roles and 身分組.position<ctx.user.roles[-1].position:
      embed=discord.Embed(title=嵌入標題 if 嵌入標題 else "按底下按鈕來獲得身份",description=嵌入說明)
      view=View(timeout=0)
      view.add_item(Button(label=f"{按鈕名稱 if 按鈕名稱 else 身分組.name}剩{數量限制 if 數量限制 else '無限'}次",custom_id=f"身分{身分組.id}&{數量限制 if 數量限制 else '-1'}",style=discord.ButtonStyle.green))
      await ctx.response.send_message(embed=embed,view=view)
    else:
        await ctx.response.send_message("無法拼出足夠的權限大餅",view=butt('帶我回家'),ephemeral=True)

@buttc.command(name="空投訊息", description="let_member_can_click_this_button_to_send_a_message")
async def giverole(ctx,投到頻道:discord.TextChannel,按鈕名稱:str,嵌入標題:Optional[str],嵌入說明:Optional[str],等級必須達到:Optional[int],邀請人數必須達到:Optional[int]):
    ch=投到頻道
    if ch.permissions_for(ctx.user).send_messages:
      embed=discord.Embed(title=嵌入標題 if 嵌入標題 else f"按底下按鈕空投訊息至{ch.name}",description=嵌入說明)
      view=View(timeout=0)
      view.add_item(Button(label=f"{按鈕名稱 if 按鈕名稱 else 身分組.name}",custom_id=f"空投{ch.id}&{等級必須達到 if 等級必須達到 else '0'}&{邀請人數必須達到 if 邀請人數必須達到 else '0'}"))
      await ctx.response.send_message(embed=embed,view=view)      
    else:
        await ctx.response.send_message("無法拼出足夠的權限大餅",view=butt('帶我回家'),ephemeral=True)    
@buttc.command(name="客服", description="建立一個按鈕可以開始客服(請先用</客服 管理>設定")
async def giverole(ctx,按鈕名稱:Optional[str],嵌入標題:Optional[str],嵌入說明:Optional[str]):
    if ctx.user.guild_permissions.manage_guild:
      embed=discord.Embed(title=嵌入標題 if 嵌入標題 else f"按底下按鈕開始客服",description=嵌入說明)
      view=View(timeout=0)
      view.add_item(Button(label=f"{按鈕名稱 if 按鈕名稱 else '開始客服'}",custom_id="客服"))
      await ctx.response.send_message(embed=embed,view=view)      
    else:
        await ctx.response.send_message("無法拼出足夠的權限大餅",view=butt('帶我回家'),ephemeral=True)

from itertools import zip_longest
@buttc.command(name="多個個身份組", description="give_some_roles_to_clicker")  
@app_commands.describe(身分組們="例如:@某身分@某身分@身分",按鈕們="每個按鈕名稱,用減號-隔開,例如:身分ㄧ-按我啊-按我得到某身分")
async def butttoroles(ctx,身分組們:str,按鈕們:Optional[str],嵌入標題:Optional[str],嵌入說明:Optional[str]):
    if ctx.user.guild_permissions.administrator:
        pass
    else:
        await ctx.response.send_message(embed=embedMake('雙方無法組合出足夠的權限'),view=butt('添加'))
        return
    try:
        身分組們=身分組們.replace(" ",'')
        rol=身分組們[3:-1].split('><@&')
        bun=(按鈕們.split("-") if len(按鈕們.split('-'))<=len(rol) else 按鈕們.split('-')[len(rol)-1]) if 按鈕們 else []
        view= View(timeout=0)
        for r,b in list(zip_longest(rol,bun, fillvalue=None)):
            view.add_item(Button(label=f"{b if b else ctx.guild.get_role(int(r))}",custom_id=f"身分{r}&-1",style=discord.ButtonStyle.green))
        embed=discord.Embed(title=嵌入標題 if 嵌入標題 else f"按底下按鈕獲得身分",description=嵌入說明 if 嵌入說明 else 身分組們)
        await ctx.channel.send(embed=embed,view=view)
        await ctx.response.send_message('完成!現在你可以刪除這則訊息')
    except Exception as bug:
        await ctx.response.send_message(embed=embedMake('發生錯誤',f'{bug}'),view=butt('添加權限'),ephemeral=True)
        
      
bot.tree.add_command(buttc) 


#@bot.tree.command(name="圖轉點字",description="turn_a_image_to:.:.")
async def imagetod(ctx,圖片:discord.Attachment):
    if 圖片.size>5000000:
        await ctx.response.send_message(embed=EM("檔案太大無法讀取"))
        return
    if len(set(圖片.content_type)&set("pngjif"))<3:
        await ctx.response.send_message(embed=EM("檔案格式不符"))
        return          
    pas=圖片.content_type.split("/")[1]
    await 圖片.save(f"aimg.{pas}")  
    image = Image.open(f"aimg.{pas}")  
    if image.size[0]>50:
        image=image.resize((50, int(image.size[1]*50/image.size[1])), Image.LANCZOS)
    words=[]
    aa=""
    wi,hi=image.size
    dic={"..":"⡆"," .":"⡀",". ":"⠐","  ":" "}
    #dic={"...":"⡆",".. ":"⠿", ".  ":"˙", ". .":"⡁", "  .":"⡀", " ..":"⢠","   ":" "," . ":"⠐"}
    for i in range(hi//4+1):
        words.append("")   
    for w in range(wi//2):
        for h in range(hi//2):
            try:
                r, g, b, a = image.getpixel((w*2, h*2))
            except :
                r, g, b = image.getpixel((w*2, h*2))
                a=0
            aa+="." if (r+g+b-a)<380 else " " 
            if len(aa)==2:
               words[h//4]+=dic[aa]
               aa=""
    await ctx.response.send_message('完成前:'+"\n"+圖片.proxy_url)
    w="\n".join(words)
    await ctx.channel.send('\n完成後:\n'+w[:1900])
    os.remove(f"aimg.{pas}") 


@bot.tree.command(name="列出文字",description="printUTF8")
@app_commands.allowed_installs(guilds=True, users=True) 
async def imagetod(ctx,字元碼:int):
    w="```"
    for i in range(字元碼,字元碼+1900):
        w+=chr(i)
    await ctx.response.send_message(w+"```")
    
@bot.tree.command(name="封殺身分組", description="他將只能欣賞頻道")
@app_commands.choices(
  能發言嗎=[Choice(name='開', value=1),
        Choice(name='關', value=0)])
@app_commands.choices(
  能用討論串嗎=[Choice(name='開', value=1),
          Choice(name='關', value=0)])
async def on(ctx, 身分組: discord.Role, 能發言嗎: Choice[int], 能用討論串嗎: Choice[int]):
  if 身分組 not in ctx.guild.me.roles and ctx.user.guild_permissions.administrator:
    await ctx.response.send_message("<a:ing:1138322474782691389>正在開始...")

    await 身分組.edit(permissions=discord.Permissions(permissions=0))
    a = 0
    for channel in ctx.guild.channels:
      a += 1
      try:
        await channel.set_permissions(
          身分組,
          send_messages=bool(能發言嗎.value),
          send_messages_in_threads=bool(能用討論串嗎.value),
          create_public_threads=bool(能用討論串嗎.value),
          create_private_threads=bool(能用討論串嗎.value))
        if a / len(ctx.guild.channels) * 100 % 25 == 0:
          await ctx.channel.send(
            f"<a:ing:1138322474782691389>完成{a/len(ctx.guild.channels)*100}%")
      except Exception as bug:
        await ctx.channel.send(
          f"<a:XX:1120631053921566861>我沒權限{bug}",
          view=butt(
            "增加權限或拉高位階",
            "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
          ))
    await ctx.channel.purge(limit=4)
    await ctx.channel.send(f"已關閉 {身分組} 在所有頻道的權限。")

  else:
    await ctx.response.send_message(
      "<a:XX:1120631053921566861>您沒權限",
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ),ephemeral=True)

class rep(discord.ui.Modal,title="回覆訊息"):
  def __init__(self,mid):
        super().__init__(timeout=60.0)
        self.bot=bot
        self.m=mid
  titt=discord.ui.TextInput (label = "想說什麼", style = discord.TextStyle.short, placeholder="", default="", required = True, max_length= 1000)
  
  async def on_submit(self, ctx: discord. Interaction): 
    try:
        m=await ctx.channel.fetch_message(self.m)
        await m.reply(content=self.titt,allowed_mentions=discord.AllowedMentions(everyone=False,roles=False))
    except Exception as bug:
        print(bug)
        await ctx.response.send_message("沒有權限[，增加](https://discord.com/oauth2/authorize?client_id=1132079788140531872)",ephemeral=True)
    else:
      await ctx.response.send_message("祝你愉快",ephemeral=True)
    await bot.get_channel(1144191411101638716).send(f"{ctx.user.name}&id={ctx.user.id}\n對{m.author.name}&id={m.author.id}\n的訊息{m.content}\n說了:{self.titt}",allowed_mentions=discord.AllowedMentions(everyone=False,roles=False))
    
@bot.tree.context_menu(name="幫我回覆他")
async def opn(ctx, m: discord.Message):  
    await ctx.response.send_modal(rep(m.id))
    

@bot.tree.context_menu(name="與他開房")
async def opn(ctx, 對象: discord.User):
  guild = ctx.guild
  try:

    overwrites = {
      guild.default_role: discord.PermissionOverwrite(read_messages=False),
      ctx.user: discord.PermissionOverwrite(read_messages=True),
      對象: discord.PermissionOverwrite(read_messages=True),
      bot.user: discord.PermissionOverwrite(read_messages=True),
    }
    channel = await guild.create_text_channel('私訊小房間', overwrites=overwrites)
    await channel.send(
      embed=embedMake("<a:yes:1293857715013025792>成功開房", f"<@{ctx.user.id}>與<@{對象.id}>一起來聊天!只須遵守法律"))
    try:
      await ctx.response.send_message(embed=embedMake(
        "<a:yes:1293857715013025792>成功!", f"到<#{channel.id}>看看"))
    except:
      await ctx.channel.send(embed=embedMake("<a:yes:1293857715013025792>成功!",
                                             f"到<#{channel.id}>看看"))
  except Exception as bug:
    try:
      await ctx.response.send_message(f"<a:XX:1120631053921566861>{bug}")
    except:
      await ctx.channel.send(f"<a:XX:1120631053921566861>{bug}")


@bot.tree.command(name="開房", description="開語音小房聊天")
async def on(ctx, 對象: discord.User, 用身分組: Optional[discord.Role]):
  guild = ctx.guild
  try:
    if 用身分組:
      overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.user: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
        對象: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
        bot.user: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
        guild.get_role(用身分組.id):
        discord.PermissionOverwrite(read_messages=True, manage_channels=True)
      }
    else:
      overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.user: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
        對象: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
        bot.user: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
      }
    channel = await guild.create_voice_channel('私訊小房間', overwrites=overwrites)
    await channel.send(
      embed=embedMake("<a:yes:1293857715013025792>成功開房", f"<@{ctx.user.id}>與<@{對象.id}>{用身分組}一起來聊天!只須遵守法律")
    )
    try:
      await ctx.response.send_message(embed=embedMake(
        "<a:okk:1277864492163928166>成功!", f"到<#{channel.id}>看看"))
    except:
      await ctx.channel.send(embed=embedMake("<a:okk:1277864492163928166>成功!",
                                             f"到<#{channel.id}>看看"))
  except Exception as bug:
    try:
      await ctx.response.send_message(f"<a:XX:1120631053921566861>{bug}")
    except:
      await ctx.channel.send(f"<a:XX:1120631053921566861>{bug}")


@bot.tree.command(name="建立狀態頻道", description="建立上線狀態文字頻道")
async def on(ctx):
  if ctx.user.guild_permissions.administrator and ctx.guild :
    try:
      頻=0
      for c in ctx.guild.channels:
        if "🟢"in  c.name and "🔘"in c.name:
          頻=c
          break
      if 頻==0:
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True),}
        頻= await ctx.guild.create_text_channel('🟢-💤-⛔-🔘-', overwrites=overwrites)
        
      with open("online.json", "r") as file:
        data = json.load(file)
      data[str(ctx.guild.id)] = 頻.id
      with open("online.json", "w") as file:
        json.dump(data, file, indent=4)
      guild = data[str(ctx.guild.id)]
      online_count = 0
      idle_count = 0
      dnd_count = 0
      lev = 0
      for member in ctx.guild.members:
          if member.status == discord.Status.online:
            online_count += 1
          elif member.status == discord.Status.idle:
            idle_count += 1
          elif member.status == discord.Status.dnd:
            dnd_count += 1
          else:
            lev += 1
      new_name = f"🟢:{online_count}💤:{idle_count}⛔:{dnd_count}🔘:{lev}"
      await 頻.edit(name=new_name)
      await ctx.response.send_message("<a:okk:1277864492163928166>資料更新成功")
    except Exception as bug:
      await ctx.response.send_message(bug)
      print(bug)
  else:
    await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限還想怎樣?",
                      "把我家到你的伺服器才有用"),
      view=butt(
        "加到伺服器",
        "https://discord.com/api/oauth2/authorize?client_id=1132079788140531872&permissions=27826959412343&scope=bot"
      ))
    
class xpm(discord.ui.Modal,title=""):
  def __init__(self,title):
        super().__init__(timeout=60.0)
        self.bot=bot
        self.title=title
  titt=discord.ui.TextInput (label = "輸入將獲得的羈絆數值", style = discord.TextStyle.short, placeholder="", default="30", required = True, max_length= 3)

  
  async def on_submit(self, ctx: discord. Interaction):
    b={"發送訊息":"CS","字數兌換":"ST","使用投幣":"CC","每日一句":"DY","邀請別人":"SS","回覆訊息獎勵":"RM"}
    try:
      t=float(self.titt.value)
    except Exception as bug:
      print(bug)
      await ctx.response.edit_message(content=f"# 發生錯誤，必須是數字")
      return
    with open("d.json", "r") as file:
        data = json.load(file)
    c=bot.get_channel(data[str(ctx.guild.id)]["i"])
    data[str(ctx.guild.id)][b[self.title]]=t
    with open("d.json", "w") as file:
        json.dump(data, file, indent=4)
    await c.send(f"{ctx.user}:修改{self.title}的羈絆值成:\n{self.titt.value}",silent=True)
    await ctx.response.edit_message(content=f"已修改{self.title}")
    d={}
    b={"CS": "發送訊息", "ST": "字數兌換", "CC": "使用投幣", "DY": "每日一句", "SS": "使用指令", "RM": "回覆訊息獎勵"}
    for i in data[str(ctx.guild.id)]:
      if i=="i":
        pass
      else:
        d[b[i]]=data[str(ctx.guild.id)][i]
    await c.send(embed=EM("羈絆獎勵更新了","以下是行為與獲得的羈絆值\n羈絆計畫是能讓成員與伺服器更緊密的小活動",d),silent=True)

class Butts(View):
  @discord.ui.button(style=discord.ButtonStyle.green,label="成員發言時的獎勵",emoji="🗨️")
  async def button_callback1(self, interaction, button):
    await interaction.response.send_modal(xpm(title="發送訊息"))
  @discord.ui.button(style=discord.ButtonStyle.green,label="成員發言\"字數\"獎勵",emoji="💬")
  async def button_callback2(self, interaction, button):
    await interaction.response.send_modal(xpm(title="字數兌換"))
  @discord.ui.button(style=discord.ButtonStyle.green,label="使用投幣獎勵",emoji="💰")
  async def button_callback3(self, interaction, button):
    await interaction.response.send_modal(xpm(title="使用投幣"))
  @discord.ui.button(style=discord.ButtonStyle.green,label="每日第一句獎勵",emoji="🗯️")
  async def button_callback4(self, interaction, button):
    await interaction.response.send_modal(xpm(title="每日一句"))
  @discord.ui.button(style=discord.ButtonStyle.green,label="邀請成員獎勵",emoji="➕")
  async def button_callback5(self, interaction, button):
    await interaction.response.send_modal(xpm(title="邀請別人"))
  @discord.ui.button(style=discord.ButtonStyle.green,label="回覆訊息獎勵",emoji="🪃")
  async def button_callback5(self, interaction, button):
    await interaction.response.send_modal(xpm(title="回覆訊息獎勵"))

levg=Group(name='等級', description='自訂伺服器升級系統')

@levg.command(name="給予", description="給予一些經驗")
async def give(ctx,誰:discord.User,數量:int):
  if ctx.guild==None:
    await ctx.response.send_message(embed=embedMake("請在自己的群組執行"))
    return
  with open("xp.json", "r", encoding='utf-8') as file:
    data3 = json.load(file)
  if str(ctx.guild.id) not in data3:
      data3[str(ctx.guild.id)]={}
  if str(誰.id) not in data3[str(ctx.guild.id)]:
      data3[str(guild.id)][str(id)]=[1,xp]
  with open("xp.json", "w") as file:
    json.dump(data3, file, indent=4)
    
  if ctx.user.guild_permissions.administrator:
      cc=xpcont(ctx.guild,誰.id,xp=數量)
      await ctx.response.send_message(embed=embedMake("<a:okk:1277864492163928166>成功!",f"<@{誰.id}>升級至{cc[0]}"),ephemeral=True)
  else:
    await ctx.response.send_message(embed=embedMake("您沒權限"),view=butt("加到自己的","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)

@levg.command(name="設定", description="管理自訂伺服器升級系統")
async def couf(ctx):
  if ctx.guild==None:
    await ctx.response.send_message(embed=embedMake("請在自己的群組執行"))
    return
  c=0
  if ctx.user.guild_permissions.administrator:
    with open("d.json", "r") as file:
        data = json.load(file)
    if str(ctx.guild.id) not in data:
      overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True),
    }
      c= await ctx.guild.create_text_channel('等級計畫', overwrites=overwrites)
      data[str(ctx.guild.id)] = {"i":c.id}
      with open("d.json", "w") as file:
        json.dump(data, file, indent=4)
      with open("xp.json", "r") as file:
        data = json.load(file)
      data[str(ctx.guild.id)] = {}
      with open("xp.json", "w") as file:
        json.dump(data, file, indent=4)
    view = Butts()
    await ctx.response.send_message(embed=embedMake("按下各個按鈕設定成員行為與對應的獎勵"),ephemeral=True,view=view)
  else:
    await ctx.response.send_message(embed=embedMake("您沒權限"),view=butt("加到自己的","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)
    
@levg.command(name="難度", description="修改升級系統升級公式")
@app_commands.describe(l2="升級難度指數成長率，設為發一言可獲得的身分組尤佳",l1='每升一級必備羈絆，可為零',l0='升至1級所需羈絆可為零')
@discord.app_commands.rename(l2="指數成長率",l1='每級羈絆',l0='初始羈絆')
async def levlev(ctx, l2: int, l1: int, l0: int):
  if ctx.guild==None:
    await ctx.response.send_message(embed=embedMake("請在自己的群組執行"))
    return
  if ctx.user.guild_permissions.administrator:
     pass
  else:
     return
  with open("d.json", "r") as file:
    data = json.load(file)
  if str(ctx.guild.id) not in data:
    await ctx.response.send_message('請先用</等級 設定:1172836165389398128>創建',ephemeral=True)
    return
  data[str(ctx.guild.id)]["lv"]=[l2,l1,l0]
  with open("d.json", "w") as file:
    json.dump(data, file, indent=4)
  await ctx.response.send_message(embed=embedMake('完成!'),ephemeral=True)
  bg = Image.open("lvu.jpg")
  hxp=(20*l2)**2+20*l1+l0
  for i in range(10):
    draw = ImageDraw.Draw(bg)
    draw.text((30,125+i*30),str(int(hxp/10*(10-i))),font=ImageFont.truetype("TT.ttf",size=20))
  hxp=300/hxp
  w=39
  for i in range(20):
    nxp=((i+1)*l2)**2+(i+1)*l1+l0
    x,y=(30+w*(i+1),410-hxp*nxp)
    draw.ellipse((x+w/2-3,y-3,x+w/2+3,y+3),fill=(255, 237, 135))
    draw.text((x,y-6),str(nxp),font=ImageFont.truetype("TT.ttf",size=20))
  bg.save("llll.jpg", encoding='utf-8')
  file = discord.File('llll.jpg')
  await ctx.channel.send('# 新的升級難度表!!',file=file)
      
  

bot.tree.add_command(levg)

@bot.tree.command(name="管理伺服器快捷發言", description="自訂伺服器快捷發言，將會創建一個狀態頻道以供處存資料")
@app_commands.choices(請同意=[
  Choice(name='必須創建一個上線狀態文字頻道',
         value='c')
])
async def couf(ctx,請同意: Choice[str]):
  if ctx.guild==None:
    await ctx.response.send_message(embed=embedMake("請在自己的群組執行"))
    return
  c=0
  if ctx.user.guild_permissions.administrator:
    for channel in ctx.guild.channels:
      if "🟢"in  channel.name and "🔘"in channel.name:
        c=channel
    if c==0:
      overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True),
    }
      c= await ctx.guild.create_text_channel('🟢-💤-⛔-🔘-', overwrites=overwrites)

    with open("online.json", "r") as file:
        data = json.load(file)
    data[str(ctx.guild.id)] = c.id
    with open("online.json", "w") as file:
        json.dump(data, file, indent=4)
    a=c.topic
    
    if a:
      a=a.split(">|<")
    else:
      a=[]
    #   message.channel.edit(topic=new_description)
    options=[]
    co=0
    for i in a:
      co+=1
      if co<6:
        options.append(discord.SelectOption(label=f"編輯快捷發言{co-1}({i[:-3]})",value=co-1,emoji="<:me:1122364224103006300>"))
    
    
    
    async def coub(ctx):
        bu1 = Button(style=discord.ButtonStyle.green,
               label=f"編輯快捷發言",
               emoji="<:gr:1127209538966261780>")
        bu2 = Button(style=discord.ButtonStyle.danger,
               label="刪除快捷發言",
               emoji="<a:XX:1120631053921566861>", custom_id=selects.values[0])
        async def ba(ctx):
          await ctx.response.send_modal(fchang(title=ctx.message.embeds[0].title))
        async def ba2(ctx):
          for channel in ctx.guild.channels:
            if "🟢"in  channel.name and "🔘"in channel.name:
              c=channel
          sliced_parts = c.topic.split(">|<")
          del sliced_parts[int(bu2.custom_id)]
          t=str(">|<".join(sliced_parts))
          await c.edit(topic=t)
          await c.send(f"{ctx.user}:刪除了步驟{bu2.custom_id}")
          await ctx.response.edit_message(content="已刪除",embed=None,view=None)
        bu1.callback=ba
        bu2.callback=ba2
        view = View(timeout=30)
        view.add_item(bu1).add_item(bu2)
        await ctx.response.send_message(embed=embedMake(f"編輯快捷發言:{selects.values[0]}"),view=view,ephemeral=True)
    view = View(timeout=300)
    if len(options)>1:
      selects = Select(placeholder=f"編輯快捷發言", options=options[1:])
      selects.callback = coub
      view.add_item(selects)
    but=Button(style=discord.ButtonStyle.green,
               label="新增快捷發言",
               emoji="<a:okk:1277864492163928166>")
    but.callback = fastback
    view.add_item(but)
    await ctx.response.send_message(embed=embedMake("按下『新建步驟』來建立一個快捷發言","按下編輯快捷發言(1、2、3)即可編輯快捷發言","當使用者使用"),ephemeral=True,view=view)
  else:
    await ctx.response.send_message(embed=embedMake("您沒權限"),view=butt("加到自己的","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)

class finput(discord.ui.Modal,title="請輸入快捷發言，支援MD打法"):
  def __init__(self):
        super().__init__(timeout=60.0)
        self.bot=bot
  titt=discord.ui.TextInput (label = "快捷發言代號", style = discord.TextStyle.short, placeholder="以短、好記為優先", default="", required = True, max_length= 5)
  answer = discord.ui.TextInput (label = "新增一個快捷發言", style = discord.TextStyle.paragraph, placeholder="", default="大家早阿", required = True, max_length= 200)
  
  async def on_submit(self, ctx: discord. Interaction):
    with open("online.json", "r") as file:
        data = json.load(file)
    c=bot.get_channel(data[str(ctx.guild.id)])
    a=c.topic
    if a:
      await c.edit(topic=f"{a}>|<{self.titt}|{self.answer}")
    else:
      await c.edit(topic=f">|<{self.titt}|{self.answer}")
    await c.send(f"{ctx.user}:新增了一個快捷發言:{self.titt}\n> {self.answer}",silent=True)
    await ctx.response.edit_message(content="已新增")

class fchang(discord.ui.Modal,title="修改快捷發言"):
  def __init__(self, title):
        super().__init__(timeout=60.0)
        self.title = int(title[-1])
  titt=discord.ui.TextInput (label = "新的快捷發言代號", style = discord.TextStyle.short, placeholder="以短、好記為優先", default="", required = True, max_length= 5)
  answer = discord.ui.TextInput (label = "修改一個快捷發言", style = discord.TextStyle.paragraph, placeholder="", default="大家晚安", required = True, max_length= 200)
 
  async def on_submit(self, ctx: discord.Interaction):
    with open("online.json", "r") as file:
        data = json.load(file)
    c=bot.get_channel(data[str(ctx.guild.id)])
    sliced_parts = c.topic.split(">|<")
    sliced_parts[self.title]=f"{self.titt}|{self.answer}"
    await c.edit(topic= ">|<".join(sliced_parts))
    await c.send(f"{ctx.user}:更新快捷發言:{self.title}:成:{self.titt}\n> {self.answer}",silent=True)
    await ctx.response.edit_message(content="已更新",embed=None,view=None)

async def fastback(ctx):
      await ctx.response.send_modal(finput())

@bot.tree.command(name="新增伺服器快捷發言", description="自訂伺服器快捷發言，將會創建一個狀態頻道以供處存資料")
@app_commands.choices(請同意=[
  Choice(name='必須創建一個上線狀態文字頻道',
         value='c')
])
async def couf(ctx,請同意: Choice[str],快捷發言代號:str,快捷發言內容:str):
  if ctx.guild==None:
    await ctx.response.send_message(embed=embedMake("請在自己的群組執行"))
    return
  c=0
  if ctx.user.guild_permissions.administrator:
    for channel in ctx.guild.channels:
      if "🟢"in  channel.name and "🔘"in channel.name:
        c=channel
    if c==0:
      overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True),
    }
      c= await ctx.guild.create_text_channel('🟢-💤-⛔-🔘-', overwrites=overwrites)

    with open("online.json", "r") as file:
        data = json.load(file)
    data[str(ctx.guild.id)] = c.id
    with open("online.json", "w") as file:
        json.dump(data, file, indent=4)
    a=c.topic
    if a:
      await c.edit(topic=f"{a}>|<{快捷發言代號}|{快捷發言內容}")
    else:
      await c.edit(topic=f">|<{快捷發言代號}|{快捷發言內容}")
    await c.send(f"{ctx.user}:新增了一個快捷發言:{快捷發言代號}\n> {快捷發言內容}",silent=True)
    await ctx.response.send_message(content="已新增",ephemeral=True)  
def repltxt(guild,mem,txt)->str:
   '''@$(UM),加入者的顯示名稱:$(UN)
   ,群組名稱:$(GN)
   ,群組人數:$(GC)
   ,加入者的加友代號:$(UF)'''
   t=txt.replace('$(UM)',f'<@{mem.id}>')
   t=t.replace('$(UN)',mem.global_name if mem.global_name else mem.name)
   t=t.replace('$(GN)',guild.name if guild else '私訊')
   t=t.replace('$(GC)',str(guild.member_count if guild else '2'))
   t=t.replace('$(UF)',f'{mem}')
   return t

def bstostr(bs:list):
  t=''
  for i in bs:
    t+=i[0].replace(',','&cmd').replace(':','&to')+':'+i[1].replace(',','&cmd').replace(':','&to')+','
  return t
def bstolist(bs:str):
  t=[]
  for i in bs.split(','):
    if ':' in i:
      t.append([i.split(':')[0].replace('&cmd',',').replace('&to',':'),i.split(':')[1].replace('&cmd',',').replace('&to',':')])
  return t

@bot.tree.command(name="0", description="使用自訂快捷發言")
@app_commands.allowed_installs(guilds=True, users=True)
async def couf(ctx,代號:str):
  await ctx.response.defer()
  with open('fastda.json','r') as file:
    data=json.load(file)
  if str(ctx.user.id) not in data:
    data[str(ctx.user.id)]={}
  if 代號 not in data[str(ctx.user.id)]:
    await ctx.followup.send("找不到此代號 使用` /快捷 新增 ` 來建立",ephemeral=True)
    return
  da=data[str(ctx.user.id)][代號]
  content,embedt,embedc,ment,bus=da
  view=View(timeout=0)
  bugs=[]
  fd=[]
  for b in bstolist(bus):
    try:
      if b[1]=='私':
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, custom_id=f'快私我{ctx.user.id}', label=b[0]))
      elif b[1].startswith('http'):
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url=b[1], label=b[0]))
      elif b[1]=='N':
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.gray,disabled=True, label=b[0]))
      else :
        fd.append(b)
    except Exception as bug:
      bugs.append(str(bug))
  em=None
  if embedt or embedc:
    em=EM(repltxt(ctx.guild,ctx.user,embedt),repltxt(ctx.guild,ctx.user,embedc),{},ctx.user)
    for b in fd:
      em.add_field(name=b[0],value=b[1],inline=False)
  try:
    await ctx.followup.send(content=repltxt(ctx.guild,ctx.user,content),embeds=em,allowed_mentions=discord.AllowedMentions(everyone=False,users=ment,roles=False),view=view)
  except Exception as bug:
    bugs.append(str(bug))
    await ctx.followup.send(content="*".join(bugs),embeds=[EM('發生錯誤')],allowed_mentions=discord.AllowedMentions(everyone=False,users=ment,roles=False),ephemeral=True)
  return
  with open("online.json", "r") as file:
      data = json.load(file)
  if ctx.guild==None:
    await ctx.response.send_message(content="本伺服器未設定",ephemeral=True) 
    return
  if str(ctx.guild.id) not in data:
    await ctx.response.send_message(content="本伺服器未設定",ephemeral=True) 
    return
  else:
    c=bot.get_channel(data[str(ctx.guild.id)]).topic
    c=c.split(">|<")
    embed=discord.Embed(title="找不到對應的快捷發言", description="以下是本服提供的快捷發言>代號:內容")
    for i in c[1:]:
      i=i.split("|")
      if i[0]==代號:
        await ctx.response.send_message(i[1])
        return
      embed.add_field(name=i[0], value=i[1], inline=False)
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name="自動提醒頻道", description="對所有有說明文的頻道啟用自動提醒頻道說明文")
@app_commands.choices(
  開關=[Choice(name='開', value=1),
      Choice(name='關', value=0)])
@app_commands.describe(開關="是否啟動")
async def on(ctx, 開關: Choice[int]):
  if ctx.user.guild_permissions.administrator:
    with open("t.json", "r") as file:
      data = json.load(file)
    data[str(ctx.guild.id)] = bool(開關.value)
    with open("t.json", "w") as file:
      json.dump(data, file, indent=4)
    await ctx.response.send_message("<a:okk:1277864492163928166>資料更新成功")
  else:
    await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限還想怎樣?",
                      "把我家到你的伺服器才有用"),
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ))


# @bot.tree.command(name = "發放身分組", description = "在私人頻道發放身分")
# async def rg(ctx,身分組:discord.Role):
#   if ctx.user.guild_permissions.administrator:
#     button = Button(style=discord.ButtonStyle.green, label=str(身分組),emoji="🪪")
#     async def grb(ctx):
#       try:
#         await ctx.user.add_roles(身分組)
#         await ctx.response.send_message(f"已給予你身分組")

#       except Exception as bug:
#         print(bug)
#     button.callback=grb
#     view = View()
#     view.add_item(button)
#     await ctx.response.send_message(embed=embedMake("免費身分組!",str(身分組)),view=view)
#   else:
#     await ctx.response.send_message(embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限還想怎樣?","把我家到你的伺服器才有用"),view=butt("加到伺服器","https://discord.com/oauth2/authorize?client_id=1064461042756878416&permissions=8&scope=bot"))


@bot.tree.command(name="一元二次方程式計算", description="進行.X²+.x+...的計算")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.describe(二次項="?x²", 一次項="?x", 常數項="數值")
async def eex(interaction: discord.Interaction, 二次項: float, 一次項: float,
              常數項: float):
  try:
    s2 = float(二次項)
    s1 = float(一次項)
    s0 = float(常數項)
    s0 = (s1**2) + (-4 * s2 * 常數項)
    if s2==0:
      await interaction.response.send_message(embed=embedMake("你該不會連一次方程式都不會吧?"))
      return
    if s0 < 0:
      await interaction.response.send_message(embed=saybugs('無解', "吳姊"))
    elif s0 == 0:
      await interaction.response.send_message(
        embed=saybugs('重根', -s1 / (2 * s2)))
    else:
      ans1 = (-s1 + (s0**0.5)) / (s2 * 2)
      ans2 = (-s1 - (s0**0.5)) / (s2 * 2)
      embed = discord.Embed(title=F"結果出爐{s2}X²+{s1}x+{常數項}")
      embed.add_field(name=F"{ans1}或{ans2}",
                      value=F"```{s1}∓√{s0}\n−−−−−−−−−−−−\n{s2/2}```",
                      inline=False)
      await interaction.response.send_message(embed=embed)
  except Exception as e:
    await interaction.response.send_message(
      embed=saybugs('二次項為零', "一元一次方程式你應該國小就算得出來了!!" + e))


@bot.tree.command(name="de", description="大量刪除訊息")
@commands.has_permissions(administrator=True)
async def de(ctx, 刪除數量: int):
  if ctx.user.guild_permissions.administrator:
    await ctx.response.defer(ephemeral=True, thinking=True)
    channel = ctx.channel
    try:
      deleted = await channel.purge(limit=刪除數量 + 1)
    except:
      deleted="沒有權限"
    try:
      await ctx.followup.send(f'已刪除 {len(deleted) - 1}個.')
    except:
      await ctx.channel.send(f'已刪除 {len(deleted) - 1}個.')


@bot.tree.command(name="1", description="快捷發言:說謝謝")
@app_commands.allowed_installs(guilds=True, users=True)
async def f1(interaction: discord.Interaction):
  c=["謝謝❤️💕!","謝謝你","太感謝了"]
  await interaction.response.send_message(random.choice(c))


@bot.tree.command(name="2", description="快捷發言:說早安")
@app_commands.allowed_installs(guilds=True, users=True)
async def f2(interaction: discord.Interaction):
  await interaction.response.send_message("早安!我會記得天天傳早安圖的!")


@bot.tree.command(name="3", description="快捷發言:問誰有空")
@app_commands.allowed_installs(guilds=True, users=True)
async def f3(interaction: discord.Interaction):
  await interaction.response.send_message("@here 誰現在~~~有~~~`空`",allowed_mentions=discord.AllowedMentions( everyone=False, replied_user=False))


@bot.tree.command(name="4", description="快捷發言:找人玩")
@app_commands.allowed_installs(guilds=True, users=True)
async def f4(interaction: discord.Interaction):
  await interaction.response.send_message("@here 誰想和我**玩??**")


@bot.tree.command(name="5", description="快捷發言:等一下")
@app_commands.allowed_installs(guilds=True, users=True)
async def f5(interaction: discord.Interaction):
  await interaction.response.send_message('等我一\"*夏\"*')


@bot.tree.command(name="6", description="快捷發言:集合大家")
async def f6(interaction: discord.Interaction, 集合地點: discord.TextChannel):
  集合地點 = 集合地點.name
  await interaction.response.send_message(F"@here🎌到**{集合地點}**集合!!",allowed_mentions=discord.AllowedMentions(everyone=False))


@bot.tree.command(name="7", description="快捷發言:炫耀一個東西")
@app_commands.allowed_installs(guilds=True, users=True)
async def f7(interaction: discord.Interaction):
  await interaction.response.send_message("__**看!**__這是我的傑作")


@bot.tree.command(name="8", description="叫大家看 釘選/群規/私訊/討論串")
@app_commands.describe(地點="觀看地點")
@app_commands.choices(地點=[
  Choice(name='釘選', value='釘選'),
  Choice(name='群規', value='群規'),
  Choice(name='私訊', value='私訊'),
  Choice(name='討論串', value='討論串')
])
async def f8(interaction: discord.Interaction, 地點: Choice[str]):
  await interaction.response.send_message(F"請看{地點.value}")


@bot.tree.command(name="tag", description="猛a人")
async def a(interaction: discord.Interaction, 對象: discord.User, 層數: int):
  global tag 
  tag=interaction.user.id
  a = ""
  if 層數 < 10:
    for i in range(層數):
      a += ('<@' + str(對象.id) + '>') * i
      a += "\n"
    await interaction.response.send_message(a,allowed_mentions=discord.AllowedMentions( everyone=False, users=False, roles=False, replied_user=False))
  else:
    await interaction.response.send_message(
      embed=saybugs("<a:XX:1120631053921566861>沒騙你，真的卡住了", "太多層會卡住"))


@bot.tree.command(name="文字山", description="文字金字塔只能20層以下")
@app_commands.describe(文字="要甚麼文字山")
async def a(interaction: discord.Interaction, 文字: str, 層數: int):
  a = ""
  if 層數 < 21 and len(文字) < 50:
    for i in range(層數):
      a += (文字) * (i + 1)
      a += "\n"
    await interaction.response.send_message(a,allowed_mentions=discord.AllowedMentions( everyone=False, users=False, roles=False, replied_user=False))
  else:
    await interaction.response.send_message(
      embed=saybugs("<a:XX:1120631053921566861>沒騙你，真的卡住了", "太多層會卡住 建議20以下"))


@bot.tree.command(name="建議伺服器", description="列出有我的伺服器")
async def prs(interaction: discord.Interaction):
  try:
    # print(bot.guilds)
    st1 = bot.guilds#).split("name=")
    st2 = ""
    for i in st1:
      # if i % 2 == 1:
      #   st2 += str(st1[i]).split(" shard_id")[0]
      #   st2 += "\n" * 2
      st2+=i.name+"\n"

    await interaction.response.send_message(f"{len(st1)}個:\n{st2}")
  except Exception as bug:
    await interaction.response.send_message(
      embed=saybugs(bug, f"有{len(bot.guilds)}個，但不知是哪{len(bot.guilds)}個"))

@bot.tree.context_menu(name="回報客服")
async def sa(ctx, s: discord.Message):
  c=0
  for channel in ctx.guild.channels:
    if channel.name=="客服資料":
      c=channel
  if c==0:
    await bot.get_channel(1135850441981300846).send(s.content,embed=s.embeds)
    await ctx.response.send_message("這個伺服器沒有『客服資料』請用</自訂客服:1135794437780418591>來建立客服功能",ephemeral=True)
  else:
    embed=discord.Embed(title=f"{ctx.user}回報了一個訊息")
    embed.set_author(name=s.author, url="https://discord.gg/CaFUuFTUzQ",icon_url=s.author.avatar.url)
    embed.add_field(name=s.content, value="", inline=False)
    await c.send(embed=embed)
    await ctx.response.send_message("<a:okk:1277864492163928166>完成!",ephemeral=True)
  
# from py_chinese_pronounce import Pronounce2Word

def replace_keys_in_string(dictionary, input_string):
    for key, value in dictionary.items():
        input_string = input_string.replace(key, value)
    return input_string

@bot.tree.context_menu(name="忘了按Shift?")
async def sa(ctx, s: discord.Message):
  a = list("ㄅㄉˇˋㄓˊ˙ㄚㄞㄢㄦㄆㄊㄍㄐㄔㄗㄧㄛㄟㄣㄇㄋㄎㄑㄕㄘㄨㄜㄠㄤㄈㄌㄏㄒㄖㄙㄩㄝㄡㄥ")
  b = list('1234567890-qwertyuiopasdfghjkl;zxcvbnm,./')
  c = []
  for i in list(s.content):
    try:
      c.append(a[b.index(i)])
    except:
      c.append(i)
  # a = []
  # for r in ''.join(c):
  #   a.append(Pronounce2Word.chewin2word(r)[0])
  d={'ㄅㄧ': '逼 ', 'ㄅㄧˊ': '鼻 ', 'ㄅㄧˇ': '比 ', 'ㄅㄧˋ': '必 ', 'ㄅㄨ': '補 ', 'ㄅㄨˋ': '不 ', 'ㄅㄧㄝ ': '鱉 ', 'ㄅㄧㄝˊ': '別 ', 'ㄅㄧㄝˇ': '癟 ', 'ㄅㄧㄝˋ': '彆 ', 'ㄅㄧㄠ': '標 ', 'ㄅㄧㄠˇ': '表 ', 'ㄅㄧㄠˋ': '表 ', 'ㄅㄧㄠ˙': '鰾 ', 'ㄅㄧㄢ ': '邊 ', 'ㄅㄧㄢˇ': '扁 ', 'ㄅㄧㄢˋ': '便 ', 'ㄅㄧㄣ ': '斌 ', 'ㄅㄧㄣˋ': '殯 ', 'ㄅㄧㄥ ': '冰 ', 'ㄅㄧㄥˇ': '炳 ', 'ㄅㄧㄥˋ': '並 ', 'ㄅㄚ ': '吧 ', 'ㄅㄚˊ': '拔 ', 'ㄅㄚˋ': '把 ', 'ㄅㄚ˙': '爸 ', 'ㄅㄛ ': '播 ', 'ㄅㄛˊ': '博 ', 'ㄅㄞ': '掰 ', 'ㄅㄞˊ': '白 ', 'ㄅㄞˇ': '百 ', 'ㄅㄞˋ': '敗 ', 'ㄅㄟ ': '杯 ', 'ㄅㄟˇ': '北 ', 'ㄅㄟˋ': '被 ', 'ㄅㄠ ': '包 ', 'ㄅㄠˊ': '薄 ', 'ㄅㄠˋ': '寶 ', 'ㄅㄠ˙': '爆 ', 'ㄅㄢ ': '班 ', 'ㄅㄢˇ': '版 ', 'ㄅㄢˋ': '半 ', 'ㄅㄣ ': '奔 ', 'ㄅㄣˇ': '本 ', 'ㄅㄣˋ': '笨 ', 'ㄅㄤ ': '幫 ', 'ㄅㄤˇ': '綁 ', 'ㄅㄤˋ': '棒 ', 'ㄅㄥ ': '琫 ', 'ㄅㄥˋ': '蹦 ', 'ㄆㄧ ': '匹 ', 'ㄆㄧˋ': '闢 ', 'ㄆㄨ ': '鋪 ', 'ㄆㄨˊ': '樸 ', 'ㄆㄨˇ': '普 ', 'ㄆㄨˋ': '鋪 ', 'ㄆㄧㄝ ': '撇 ', 'ㄆㄧㄠ ': '瞟 ', 'ㄆㄧㄠˇ': '票 ', 'ㄆㄧㄢˋ': '騙 ', 'ㄆㄧㄢˇ': '拚 ', 'ㄆㄧㄣˇ': '品 ', 'ㄆㄧㄥˋ': '聘 ', 'ㄆㄚˊ': '爬 ', 'ㄆㄚˋ': '怕 ','ㄆㄠˋ': '泡 ', 'ㄆㄠˊ': '袍 ', 'ㄅㄠˇ': '寶 ', 'ㄆㄡˇ': '剖 ', 'ㄆㄢ ': '潘 ', 'ㄆㄢˊ': '盤 ', 'ㄆㄢˋ': '盼 ', 'ㄆㄣ ': '噴 ', 'ㄆㄤ ': '乓 ', 'ㄆㄤˊ': '旁 ', 'ㄆㄤˋ': '胖 ', 'ㄆㄥ ': '烹 ', 'ㄆㄥˊ': '捧 ', 'ㄆㄥˋ': '碰 ', 'ㄇㄧ ': '米 ', 'ㄇㄧˋ': '密 ', 'ㄇㄨˇ': '母 ', 'ㄇㄨˋ': '墓 ', 'ㄇㄝ ': '咩 ', 'ㄇㄧㄝˋ': '滅 ', 'ㄇㄧ ㄠ ': '喵 ', 'ㄇㄧㄠˊ': '苗 ', 'ㄇㄧㄠˇ': '秒 ', 'ㄇㄧㄠˋ': '妙 ', 'ㄇㄧㄡˋ': '謬 ', 'ㄇㄧㄢˊ': '棉 ', 'ㄇㄧㄢˇ': '免 ', 'ㄇㄧㄢˋ': '面 ', 'ㄇㄧㄣ': '民 ', 'ㄇㄧㄣˇ': '敏 ', 'ㄇㄧㄥ': '明 ', 'ㄇㄧㄥˋ': '命 ', 'ㄇㄚ': '嗎 ', 'ㄇㄚˊ': '麻 ', 'ㄇㄚˇ': '馬 ', 'ㄇㄛ': '抹 ', 'ㄇㄛˋ': '末 ', 'ㄇㄛˊ': '麼 ', 'ㄇㄞˊ': '埋 ', ' ㄇㄞˇ': '買 ', 'ㄇㄞˋ': '賣 ', 'ㄇㄟˊ': '沒 ', 'ㄇㄟˇ': '美 ', 'ㄇㄟˋ': '妹 ', 'ㄇㄠ': '貓 ', 'ㄇㄠˊ': '毛 ', 'ㄇㄠˇ': '卯 ', 'ㄇㄠˋ': '茂 ', 'ㄇㄡˊ': '謀 ', ' ㄇㄡ': '某 ', 'ㄇㄢ': '鰻 ', 'ㄇㄢˇ': '滿 ', 'ㄇㄢˋ': '慢 '}
  c=replace_keys_in_string(d,''.join(c))
  await ctx.response.send_message(f">>> 你是不是想表達```{c}```?")

if False:
    #@bot.tree.context_menu(name="語音轉成文字並刪除")
    async def safdfgf(ctx, s: discord.Message):
      if s.attachments:
        if s.attachments[0].filename.endswith(('.mp3', '.wav', '.ogg')):
          await s.attachments[0].save(s.attachments[0].filename)
          print(s.attachments[0].filename)
          with sr.AudioFile(s.attachments[0].filename) as source:
            audio = recognizer.record(source)
            try:
              text = recognizer.recognize_google(audio, language='zh-TW')
              text = recognizer.recognize_google(audio, language='zh-TW')
              embed = discord.Embed(title="你是不是想表達:", color=0x2676f7)
              embed.set_author(name=ctx.user, icon_url=ctx.user.avatar.url)
              embed.add_field(name=text, value="?", inline=False)
              await ctx.response.send_message(embed=embed)
              await s.delete()
            except sr.UnknownValueError:
              print('失')
      else:
        await ctx.response.send_message(embed=embedMake("哪來的語音?"))

@bot.tree.command(name="主持一場遊戲", description="遊戲需要找人?用這看看")
@app_commands.choices(請同意=[
  Choice(name='必須創建一個討論串與建立頻道邀請',
         value='c')
])
async def zzz(ctx,請同意:Choice[str],遊戲名稱:str,模式:str,你的遊戲帳號名稱:Optional[str],你的遊戲帳號id:Optional[str],你的遊戲連結或大廳id:Optional[str]):
  if 你的遊戲帳號名稱:
    na=你的遊戲帳號名稱
  else:
    na=ctx.user.global_name
    if na==None:
      na=ctx.user
  button=Button(style=discord.ButtonStyle.green,
               label="確認主持",
               emoji="<a:okk:1277864492163928166>")
  button.callback=zcbbb
  view=View(timeout=30)
  view.add_item(button)
  if 你的遊戲連結或大廳id==None:
    你的遊戲連結或大廳id=""
  await ctx.response.send_message(embed=embedMake(遊戲名稱,模式,na,你的遊戲連結或大廳id).set_author(name=ctx.user, icon_url=ctx.user.avatar.url),view=view)
  
async def zcbbb(ctx):
    m=ctx.message.embeds[0]
    遊戲名稱=m.title
    f=m.fields
    模式=f[0].name
    na=f[0].value
    c=await ctx.channel.create_invite()
    t=await ctx.message.create_thread(name=f"{遊戲名稱}-{模式}@{na}",auto_archive_duration=60,slowmode_delay=5,reason=f"幫{na}主持{遊戲名稱}-{模式}")
    await bot.change_presence(activity=discord.Streaming(platform="Discord",name=f"幫{na}主持{模式}",game=遊戲名稱,url=c))
    await ctx.response.edit_message(content="<a:okk:1277864492163928166>成功啟動!!")    
    await t.send(embed=embeddMake(f"{遊戲名稱}-{模式}"))
# 
# v=scrapetube.get_search(query="DC",limit=1,results_type="playlist")
# for video in v:
#   print(video)
#   for vv in (video):

#     print(vv)
#del v
#0001
@bot.tree.command(name="搜尋yt", description="找>影片|頻道|播放清單")
@app_commands.choices(類型=[
    Choice(name='影片', value=0),
    Choice(name='頻道', value=1),
    Choice(name='播放清單', value=2),
])
async def syt(ctx, 關鍵字: str, 類型: Choice[int]):
  await ctx.response.defer( ephemeral=False, thinking=False)
  r=["video","channel","playlist"]
  videos = scrapetube.get_search(query=關鍵字,limit=24,results_type=r[類型.value])
  options=[]
  c=0
  關鍵字=關鍵字.replace(" ","_")
  for video in videos:
    
    if 類型.value==0:
      options.append(discord.SelectOption(label=video['title']['runs'][0]['text'],value="https://www.youtube.com/watch?v="+video['videoId'],emoji="<a:YT:1135838936892186675>"))
      if c==0:
        c+=1
        embed=discord.Embed(title="<a:YT:1135838936892186675>"+關鍵字, url=f"https://www.youtube.com/results?search_query={關鍵字}",color=0xf50000,description=類型.name)
    elif  類型.value==1:
        options.append(
        discord.SelectOption(label=video['title']['simpleText'],value="https://www.youtube.com/channel/"+video['channelId'],emoji="<a:YT:1135838936892186675>"))
        if c==0:
          c+=1
          embed=discord.Embed(title="<a:YT:1135838936892186675>"+關鍵字, url=f"https://www.youtube.com/results?search_query={關鍵字}",color=0xf50000,description=類型.name)
    elif  類型.value==2:
        options.append(
        discord.SelectOption(label=video['title']['simpleText'],value="https://www.youtube.com/playlist?list="+video['playlistId'],emoji="<a:YT:1135838936892186675>"))
        if c==0:
          c+=1
          embed=discord.Embed(title="<a:YT:1135838936892186675>"+關鍵字, url=f"https://www.youtube.com/results?search_query={關鍵字}&sp=EgIQAw%253D%253D",color=0xf50000,description=類型.name)
  if len(options)<1:
    options.append(discord.SelectOption(label="DISCORD看我建造一個機器人伺服器",value="https://www.youtube.com/watch?v=dne5kKtz2lA",emoji="<:me:1122364224103006300>"))
    embed=discord.Embed(title="<a:YT:1135838936892186675>"+關鍵字, url=f"https://www.youtube.com/results?search_query={關鍵字}&sp=CAASAhAC",color=0xf50000,description=類型.name)
  select = Select(placeholder=f"{len(options)}項結果", options=options)
  view = View(timeout=0)
  view.add_item(select)
  await ctx.followup.send(embed=embed,view=view)#,ephemeral=True

async def ytback(ctx):
    await playm(ctx,ctx.message.embeds[0].url,True)


async def playm(ctx,url,istr):
    with open("c.json" ,"r") as file:
        dic=json.load(file)
    vc= [channel for channel in ctx.guild.voice_channels if channel.guild.me in channel.members]
    if str(ctx.guild.id) not in dic:
        dic[str(ctx.guild.id)]={}
    if ctx.guild.voice_client:
        if len(ctx.guild.voice_client.channel.members)>1 and "m" in dic[str(ctx.guild.id)]:
            us=bot.get_user(dic[str(ctx.guild.id)]["u"])
            embed=discord.Embed(title=f"正在<#{vc[0].id}>播放音樂 請稍後", color=0x102e76)
            embed.set_author(icon_url=ctx.user.avatar.url,name=us.global_name if us.global_name else us.name)
            view=View(timeout=0)
            b=Button(style=discord.ButtonStyle.red,
               label="仍要繼續")    
            view.add_item(b) 
            if istr:
                try:
                  await ctx.response.edit_message(embed=embed,view=view)
                except:
                    await ctx.message.edit(embed=embed,view=view)
            else:
                try:
                  await ctx.response.send_message(embed=embed,view=view)
                except:
                    await ctx.channel.send(embed=embed,view=view)
            return
    if  ctx.user.voice:
        if ctx.guild.voice_client:
            vc=await ctx.guild.voice_client.move_to(ctx.user.voice.channel)
        else:
          vc=await ctx.user.voice.channel.connect()
        vc=ctx.guild.voice_client
        us=ctx.user
        embed=discord.Embed(title=f"已經加入<#{vc.channel.id if vc else 0}>", color=0x102e76)
        embed.set_author(icon_url=ctx.user.avatar.url,name=us.global_name if us.global_name else us.name)
        embed.set_footer( text="別急!正在載入音樂")
        if istr:
            if istr=='c':
                await ctx.channel.send(embed=embed)
            else:
                try:
                  await ctx.response.edit_message(embed=embed,view=None)  
                except:
                    await ctx.message.edit(embed=embed,view=None)
        else:
            await ctx.response.send_message(embed=embed,view=None)
    elif ctx.guild.voice_client :
        vc=ctx.guild.voice_client
        us=ctx.user
        embed=discord.Embed(title=f"繼續於<#{vc.channel.id}>播放新的影片", color=0x102e76)
        embed.set_author(icon_url=ctx.user.avatar.url,name=us.global_name if us.global_name else us.name)
        embed.set_footer( text="正在載入音樂，大約十秒鐘")
        if istr:
            if istr =='c':
                await ctx.channel.send(embed,view=None)
            else:
                try:
                  await ctx.response.edit_message(embed=embed,view=None)
                except:
                    await ctx.message.edit(embed=embed,view=None)
        else:
            await ctx.response.send_message(embed=embed,view=None)
    else:
        ops=[]  
        view=View(timeout=None)
        options=[]
        for ch in ctx.guild.voice_channels:
            if ch.permissions_for(ctx.user).connect:
              options.append(discord.SelectOption(label=ch.name,value=str(ch.id),emoji='<:VC:1176732439616426004>'))
        for ch in ctx.guild.stage_channels:
            if ch.permissions_for(ctx.user).connect:
                options.append(discord.SelectOption(label=ch.name,value=str(ch.id),emoji='<:ST:1176732441159925812>'))
        select=Select(placeholder=f"選擇頻道", options=options,custom_id="chvvch")
        select.callback=vcback
        view.add_item(select)
        us=ctx.user
        embed=discord.Embed(title=f"請選擇要在哪裡播放", color=0x102e76,url=url)
        embed.set_author(icon_url=ctx.user.avatar.url,name=us.global_name if us.global_name else us.name)
        embed.set_footer( text="選完後要記得加入!別讓我在那獨自念經")
        if istr:
            if istr=='c':
                await ctx.channel.send(embed=embed,view=view)
            else:
                try:
                  await ctx.response.edit_message(embed=embed,view=view)
                except:
                    await ctx.message.edit(embed=embed,view=view)
        else:
            await ctx.response.send_message(embed=embed,view=view,ephemeral=True)  
        return
    def playa(er):
        awa= playafter(ctx)
        fut = asyncio.run_coroutine_threadsafe(awa, bot.loop)
        try:
            fut.result()
        except:
        
            pass
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'downloads/audio{ctx.guild.id}',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ratelimit': 10000000,
            }
        def ydl_down(url,ydl_opts):
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, ydl_down, url,ydl_opts)
        
    except Exception as e:
        await ctx.channel.send(embed=discord.Embed(title=f"發生讀取問題{e}", color=0x102e76,url=url))
        return
    try:
        source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3')
        vs=discord.PCMVolumeTransformer(source,volume=0.5)
        vc.play(vs, after=playa)  
    except Exception as bug:
        embed=discord.Embed(title=f"發生問題，已中斷播放", color=0x102e76,url=url)
        embed.set_author(icon_url=ctx.user.avatar.url,name=us.global_name if us.global_name else us.name)
        embed.set_footer( text=f"可能是影片不支援聲音或是不允許嵌入{bug}")
        await ctx.channel.send(embed=embed)
        await vc.disconnect()
        return
    view=View(timeout=None)
    b=discord.ui.Button(style=discord.ButtonStyle.grey,emoji="<:bb:1157929365187858463>", label="後退5秒",custom_id="<<<")
    b.callback=goback
    view.add_item(b)
    s=discord.ui.Button(style=discord.ButtonStyle.green,emoji="<:stop:1157928550222004354>", label="暫停",custom_id="|||")
    s.callback=stopm
    view.add_item(s)
    n=discord.ui.Button(style=discord.ButtonStyle.grey,emoji="<:nn:1157929368153227285>", label="前進5秒",custom_id=">>>")
    n.callback=gonext
    view.add_item(n)
    s=discord.ui.Button(style=discord.ButtonStyle.red, label="🟥結束", custom_id="stopmusic")
    s.callback=byem
    view.add_item(s)
    select = Select(placeholder=f"調整播放速度", options=[
        discord.SelectOption(label="0.500",value="sp0.5"),
        discord.SelectOption(label="0.625",value="sp0.625"),
        discord.SelectOption(label="0.750",value="sp0.75"),
        discord.SelectOption(label="正常1.000",value="sp1"),
        discord.SelectOption(label="1.125",value="sp1.125"),
        discord.SelectOption(label="1.250",value="sp1.25"),
        discord.SelectOption(label="1.500",value="sp1.5"),
        discord.SelectOption(label="1.750",value="sp1.75"),
        discord.SelectOption(label="2.000",value="sp2"),
        discord.SelectOption(label="3.000",value="sp3"),
        discord.SelectOption(label="5.000",value="sp5"),
        discord.SelectOption(label="10.00",value="sp10"),
        ])
    sel = Select(placeholder=f"調整音調", options=[
        discord.SelectOption(label="移調0.5倍",value="inc0.5"),
        discord.SelectOption(label="移調0.75倍",value="inc0.75"),
        discord.SelectOption(label="恢復音調",value="inc1"),
        discord.SelectOption(label="移調x1.25",value="inc1.25"),
        discord.SelectOption(label="移調x1.5",value="inc1.5"),
        discord.SelectOption(label="雙倍",value="inc2"),
    ])
    view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, label="時間軸", custom_id="time"))
    bot.add_view(view)
    view.add_item(select)
    view.add_item(sel)
    s=await ctx.channel.send(f"## 正在播放{url} \nx1\nx1\n<t:{int(time.time())}:R>",view=view) 
    dic[str(ctx.guild.id)]={
        "m":url,
        "c":ctx.channel.id,
        "s":s.id,
        "u":ctx.user.id,
        'cu':False
    }
    with open("music.json", "w") as file:
        json.dump(dic, file, indent=4)
        
async def playafter(ctx) :
    try:
        def playa(ctx):
            awa= playafter(ctx)
            fut = asyncio.run_coroutine_threadsafe(awa, bot.loop)
            try:
                fut.result()
            except:
                pass  
        await asyncio.sleep(1)
        vc=bot.get_guild(ctx.guild.id).voice_client
        if vc.is_playing():
            return
        source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3')
        vs=discord.PCMVolumeTransformer(source,volume=0.5)
        vc.play(vs, after=playa())  
    except Exception as bug:
        voice_client = ctx.guild.voice_client
        with open("music.json", "r") as json_file:
          dic = json.load(json_file)
        try:
            await voice_client.disconnect()
            vc= [channel for channel in ctx.guild.voice_channels if channel.guild.me in channel.members]
            embed=discord.Embed(title=f"{ctx.user}結束了在<#{vc[0].id}>播放的影片", color=0x102e76).set_author(icon_url=ctx.user.avatar.url,name=ctx.user.global_name if ctx.user.global_name else ctx.user.name)
            await ctx.message.edit(content=None,embed=embed,view=None)
            with open("music.json", "r") as json_file:
              dic = json.load(json_file)
            del dic[str(ctx.guild.id)]
            with open("music.json", "w") as file:
              json.dump(dic, file)
            os.remove(f'downloads/audio{ctx.guild.id}.mp3')
        except:
            pass
        
    
async def vcback(ctx):
    ch=ctx.data['values'][0]
    print("@"+ch)
    ch=bot.get_channel(int(ch))
    await ch.connect()
    await playm(ctx,ctx.message.embeds[0].url,True)

async def goback(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        def playa(ctx):
            awa= playafter(ctx)
            fut = asyncio.run_coroutine_threadsafe(awa, bot.loop)
            try:
                fut.result()
            except:
                pass    
        with open("music.json", "r") as json_file:
          dic = json.load(json_file)
        if ctx.user.guild_permissions.move_members or dic[str(ctx.guild.id)]["u"]==ctx.user.id:
            try:
                voice_client.stop()
                ct=int(ctx.message.content.split('\n')[-1][3:-3])+5
                t=int(time.time())-ct
                print(t)
                options = '-filter:a "atempo='+ctx.message.content.split("\n")[1][1:]+'","asetrate='+str(float(ctx.message.content.split("\n")[2][1:])*44100)+'"'
                source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3',before_options=f'-ss {t}')
                vs=discord.PCMVolumeTransformer(source,volume=0.5) 
                voice_client.play(vs, after=playa)
                await ctx.response.edit_message(content=f"倒退五秒"+ctx.message.content[4:-16]+f'<t:{ct}:R>')
                with open("music.json", "w") as file:
                    json.dump(dic, file, indent=4)
            except Exception as bug:
                print(bug)
        else:
            await ctx.response.send_message("噓!別人正在聽",ephemeral=True)

async def gonext(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        with open("music.json", "r") as json_file:
          dic = json.load(json_file)
        if ctx.user.guild_permissions.move_members or dic[str(ctx.guild.id)]["u"]==ctx.user.id:
            def playa(ctx):
                awa =playafter(ctx)
                fut = asyncio.run_coroutine_threadsafe(awa, bot.loop)
                try:
                    fut.result()
                except:
                    pass   
            voice_client.stop()
            ct=int(ctx.message.content.split('\n')[-1][3:-3])-5
            t=int(time.time())-ct
            source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3',before_options=f'-ss {t}',options=f'-filter:a "atempo='+ctx.message.content.split("\n")[1][1:]+'","asetrate='+str(float(ctx.message.content.split("\n")[2][1:])*44100)+'"')
            vs=discord.PCMVolumeTransformer(source,volume=0.5) 
            voice_client.play(vs, after=playa)
            await ctx.response.edit_message(content=f"前進五秒"+ctx.message.content[4:-16]+f'<t:{ct}:R>')
        else:
            await ctx.response.send_message("噓!別人正在聽",ephemeral=True)        
async def stopm(ctx):
    voice_client = ctx.guild.voice_client
    with open("music.json", "r") as json_file: 
          dic = json.load(json_file)
    if ctx.user.guild_permissions.move_members or dic[str(ctx.guild.id)]["u"]==ctx.user.id:
        if voice_client and voice_client.is_playing():
            voice_client.pause()
            view=View(timeout=None)
            s=discord.ui.Button(style=discord.ButtonStyle.green,emoji="<:play:1157928913977225216>" ,label="繼續",custom_id="__")
            s.callback=stopm
            view.add_item(s)
            s=discord.ui.Button(style=discord.ButtonStyle.red, label="🟥結束", custom_id="stopmusic")
            s.callback=byem
            view.add_item(s)
        elif voice_client:
            voice_client.resume()
            view=View(timeout=None)
            b=discord.ui.Button(style=discord.ButtonStyle.grey,emoji="<:bb:1157929365187858463>", label="後退5秒",custom_id="<<<")
            b.callback=goback
            view.add_item(b)
            s=discord.ui.Button(style=discord.ButtonStyle.green,emoji="<:stop:1157928550222004354>", label="暫停",custom_id="|||")
            s.callback=stopm
            view.add_item(s)
            n=discord.ui.Button(style=discord.ButtonStyle.grey,emoji="<:nn:1157929368153227285>", label="前進5秒",custom_id=">>>")
            n.callback=gonext
            view.add_item(n)
            s=discord.ui.Button(style=discord.ButtonStyle.red,emoji="🟥", label="結束", custom_id="stopmusic")
            s.callback=byem
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, label="時間軸", custom_id="time"))
            view.add_item(s)
            bot.add_view(view)
            select = Select(placeholder=f"調整播放速度", options=[
            discord.SelectOption(label="0.500",value="sp0.5"),
            discord.SelectOption(label="0.625",value="sp0.625"),
            discord.SelectOption(label="0.750",value="sp0.75"),
            discord.SelectOption(label="1.000",value="sp1"),
            discord.SelectOption(label="1.125",value="sp1.125"),
            discord.SelectOption(label="1.250",value="sp1.25"),
            discord.SelectOption(label="1.500",value="sp1.5"),
            discord.SelectOption(label="1.750",value="sp1.75"),
            discord.SelectOption(label="2.000",value="sp2"),
            discord.SelectOption(label="3.000",value="sp3"),
            discord.SelectOption(label="5.000",value="sp5"),
            discord.SelectOption(label="10.00",value="sp10"),
            ])
            sel = Select(placeholder=f"調整音調", options=[
            discord.SelectOption(label="移調0.5倍",value="inc0.5"),
            discord.SelectOption(label="移調0.75倍",value="inc0.75"),
            discord.SelectOption(label="恢復音調",value="inc1"),
            discord.SelectOption(label="移調x1.25",value="inc1.25"),
            discord.SelectOption(label="移調x1.5",value="inc1.5"),
            discord.SelectOption(label="雙倍",value="inc2"),
            ])
            view.add_item(select)
            view.add_item(sel)

        await ctx.response.edit_message(view=view) 
    else:
        await ctx.response.send_message("噓!別人正在聽",ephemeral=True)    
async def byem(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client :   
        with open("music.json", "r") as json_file:
          dic = json.load(json_file)
        if ctx.user.guild_permissions.move_members or dic[str(ctx.guild.id)]["u"]==ctx.user.id:
            await ctx.response.defer()
            vc=await voice_client.disconnect()
            embed=discord.Embed(title=f"{ctx.user}結束了在<#{vc[0].id}>播放的影片", color=0x102e76).set_author(icon_url=ctx.user.avatar.url,name=ctx.user.global_name if ctx.user.global_name else ctx.user.name)
            await ctx.followup.send(content=None,embed=embed,view=None)
            with open("music.json", "r") as json_file:
              dic = json.load(json_file)
            del dic[str(ctx.guild.id)]
            with open("music.json", "w") as file:
              json.dump(dic, file)
            os.remove(f'downloads/audio{ctx.guild.id}.mp3')
            await ctx.message.delet()
    else:
            await ctx.response.send_message("噓!別人正在聽",ephemeral=True)
            
@bot.event
async def on_interaction(ctx: discord.Interaction):
    op = ctx.data
    if 'values'in op:
        op=op['values'][0]
    else:
        if "custom_id" in op:
          op=op["custom_id"]
        else:
            return
        if op=="re真心":
            await ctx.response.send_modal(inp())
        elif op=="檢舉真心":
            await bot.get_channel(1135850441981300846).send("新的檢舉",embed=ctx.message.embeds[0])
            await ctx.response.send_message("已收到你的檢舉",ephemeral=True)
        elif op=="客服":
            await cought(ctx)
        elif op=="time":
            with open("music.json", "r") as json_file:
              dic = json.load(json_file)
            if ctx.user.guild_permissions.move_members or dic[str(ctx.guild.id)]["u"]==ctx.user.id:
                await ctx.response.send_modal(playmod())
            else:
              await ctx.response.send_message("噓!別人正在聽",ephemeral=True)
        elif op.startswith("con"):    
            if op=='concon':
                await ctx.response.send_modal(lonaddm())
                return
            con=int(op[3:])
            em=ctx.message.embeds[0].to_dict()
            text=em['fields'][con]['value']
            
            if f'<@{ctx.user.id}>' in text:
                text=text.replace(f'<@{ctx.user.id}>','')
            else:
                text+=f'<@{ctx.user.id}>'
            em=ctx.message.embeds[0].set_field_at(index=con,name=em['fields'][con]['name'],value=text)
            await ctx.response.edit_message(embed=em)
            return
            
            
        elif op.startswith("身分"):
            tx=op.split("&")
            if tx[1]!="0":
                ro=ctx.guild.get_role(int(tx[0][2:]))
                if ro:
                    try:
                        if ro in ctx.user.roles:
                            await ctx.user.remove_roles(ro,reason=f"透過{ctx.channel.name}的按鈕取消給予身份")
                            await ctx.response.send_message(f"成功拔除<@&{ro.id}>!",ephemeral=True)
                        else:
                            await ctx.user.add_roles(ro,reason=f"透過{ctx.channel.name}的按鈕給予身份")
                            await ctx.response.send_message(f"<a:okk:1277864492163928166>成功獲得<@&{ro.id}>!",ephemeral=True)
                            
                    except Exception as bug:
                        await ctx.response.send_message(f"我沒有給身份的權限{bug}",view=butt("添加權限","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)
                        return
                    await ctx.message.edit(embed=ctx.message.embeds[0])
                else:
                    await ctx.response.send_message("此身份已經不復在",ephemeral=True)
        elif op.startswith("空投"):
            if op.split("&")[1]!="0":
                try:
                  
                    lv=xpcont(ctx.guild,ctx.user.id,0)
                    if lv[0]<int(op.split("&")[1]):
                        await ctx.response.send_message(f"您的等級必須達到{op.split('&')[1]}方能使用", view=butt("帶我回家", "https://discord.com/oauth2/authorize?client_id=1132079788140531872"), ephemeral=True)
                        return
                except :
                    await ctx.response.send_message(f"您的等級必須達到{op.split('&')[1]}方能使用，但我沒有這裡的等級資料，使用</自訂等級系統:1144520740075491489>設定", view=butt("帶我回家", "https://discord.com/oauth2/authorize?client_id=1132079788140531872"), ephemeral=True)
                    return
            if op.split("&")[2]!="0":   
                try:
                    invites = await ctx.guild.invites()
                    invite_counts = {}
                    for invite in invites:
                        if invite.inviter in invite_counts:
                            invite_counts[invite.inviter] += invite.uses
                        else:
                            invite_counts[invite.inviter] = invite.uses
                    if   invite_counts[ctx.user]<int(op.split("&")[2]):
                        await ctx.response.send_message(f"您必須邀請{op.split('&')[2]}人方能使用", view=butt("帶我回家", "https://discord.com/oauth2/authorize?client_id=1132079788140531872"), ephemeral=True)
                        return
                except:
                    await ctx.response.send_message(f"您必須邀請{op.split('&')[2]}人方能使用，但我沒有您的資料", view=butt("帶我回家", "https://discord.com/oauth2/authorize?client_id=1132079788140531872"), ephemeral=True)
                    return
            await  ctx.response.send_modal(sendmeto(int(op[2:].split("&")[0])))
                
                 
            
    if  op.startswith("sp"):
      voice_client = ctx.guild.voice_client
      if voice_client:
        with open("music.json", "r") as json_file:
          dic = json.load(json_file)
        if ctx.user.guild_permissions.move_members or dic[str(ctx.guild.id)]["u"]==ctx.user.id:
            voice_client.stop()
            def playa(er):
                awa=playafter(ctx)
                fut = asyncio.run_coroutine_threadsafe(awa, bot.loop)
                try:
                    fut.result()
                except:
                    pass
            t=int(time.time())-int(ctx.message.content.split('\n')[3][3:-3])
            source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3',
                                           before_options=f'-ss {t} ',
                                           options=f'-filter:a "atempo={op[2:]}","asetrate='+str(float(ctx.message.content.split("\n")[2][1:])*44100)+'"')
            voice_client.play(source, after=playa)
            await ctx.response.edit_message(content=f"速度調整"+ctx.message.content[4:].split('\n')[0]+f"\nx{op[2:]}\n"+ctx.message.content[4:].split('\n')[2]+'\n'+ctx.message.content[4:].split("\n")[3])
        else:
            await ctx.response.send_message("噓!別人正在聽",ephemeral=True)
            
    elif op.startswith("inc"):
      voice_client = ctx.guild.voice_client
      if voice_client:
        with open("music.json", "r") as json_file:
          dic = json.load(json_file)
        if ctx.user.guild_permissions.move_members or dic[str(ctx.guild.id)]["u"]==ctx.user.id:
            voice_client.stop()
            def playa(er):
                awa= playafter(ctx)
                fut = asyncio.run_coroutine_threadsafe(awa, bot.loop)
                try:
                    fut.result()
                except:
                    pass
            t=int(time.time())-int(ctx.message.content.split('\n')[3][3:-3])
            source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3',before_options=f'-ss {t} ',options=f'-filter:a "atempo='+ctx.message.content.split("\n")[1][1:]+f'","asetrate={float(op[3:])*44100}"')
            voice_client.play(source, after=playa)
            await ctx.response.edit_message(content=f"頻率調整"+ctx.message.content[4:].split("\n")[0]+"\n"+ctx.message.content[4:].split("\n")[1]+f"\nx{op[3:]}"+'\n'+ctx.message.content[4:].split("\n")[3])
        else:
            await ctx.response.send_message("噓!別人正在聽",ephemeral=True)
    elif op.startswith("https://www.youtube"):
        await bot.change_presence(activity=discord.Streaming(name="搜尋YT",platform="YouTube",url=op))
        if op.startswith("https://www.youtube.com/w"):
          video_info = dlt.get_video_info(op)
          embed=discord.Embed(title=f"<a:YT:1135838936892186675>", url=op,color=0xf50000)
          embed.set_image(url=
    f"https://i.ytimg.com/vi/{op[32:]}/maxresdefault.jpg")
          view=View()
          b=Button(style=discord.ButtonStyle.green,label="播放")    
          b.callback=ytback
          view.add_item(b)
          await ctx.response.send_message(content=op,embed=embed,view=view)
          return
        elif op.startswith("https://www.youtube.com/c"):
          videos = scrapetube.get_search(query=op.split("/channel/")[1],limit=1,results_type="channel")
          for video in videos:
            embed=discord.Embed(title="<a:YT:1135838936892186675>"+video['title']['simpleText'], url=f"https://www.youtube.com/channel/{video['channelId']}",color=0xf50000)
            embed.set_thumbnail(url="https:"+video['thumbnail']['thumbnails'][0]['url']) 
        else :
          videos = scrapetube.get_search(query=op.split("list=")[1],limit=1,results_type="playlist")
          for video in videos:
            embed=discord.Embed(title="<a:YT:1135838936892186675>"+video['title']['simpleText'], url=op,color=0xf50000)
            embed.set_image(url=video['thumbnails'][0]['thumbnails'][0]['url'])
            embed.set_author(name=video['longBylineText']['runs'][0]['text'], url=f"https://www.youtube.com/channel/{video['longBylineText']['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']}")

        view=view=butt("去按讚",op,"👍")
        await ctx.response.send_message(embed=embed,view=view)
    elif op.startswith("p&"):
        await playm(ctx,op[2:],True)
    elif op == "help1":
      await ctx.response.send_message(
        embed=EM("快捷發言", "懶得打字就用它!", 
   {
       '/0': '使用自訂快捷發言。',
       "</1:1132088808368775194>":"說謝謝",
       "</2:1132088808368775195>":"說早安",
       "</3:1132088808368775196>":"問誰有空",
       "</4:1132088808368775197>": "快捷發言:找人玩",
       "</5:1132088808599470180>":"等一下",
       "</6:1132088808599470181>":"集合大家",
       "</7:1132088808599470182>":"炫耀一個東西",
       "快捷管理":"編輯預存發言","/快捷 發言":"填入代號即可送出預存發言" ,
"/快捷新增":"新增一個快捷發言,使用/0填入代號即可送出預存發言"
   })
                 )
    elif op  == "help2":
      await ctx.response.send_message(embed=EM(
        "遊戲與娛樂",
        {'遊戲相關':'''
/大刀石頭布 新的遊戲玩法。
/主持一場遊戲 用於找人參加遊戲。
/探險 寶可夢探索遊戲。''',
'趣味指令':'''
/真心話出題 隨機問大家問題。
/文字山 建立一個文字金字塔（20層以下）。
/情書產生 生成有趣的情書內容。
/淦文產生 創造有聲有色的淦文內容。'''}
      )
      )
    elif op  == "help3":
      await ctx.response.send_message(embed=EM(
        "音樂播放與改變音調",
        "萬能機器-讓機器人成為discord聽音樂首選!",
        {'':'''首先，在文字頻道使用< /播放 音樂 >並附上要播的yt音樂關鍵字或連結，然後按ENTER (其實，使用.p -p &p /播放 音樂皆可)
如果是輸入關鍵字的話，選一個搜尋結果...
如果你已經加入語音頻道則會自動進入那邊播放 若您未加入則會再原本的頻道播放或於指定頻道播放
提供豐富的播放功能:
調整速度(*0.25-20倍!*)、調整音調(可以很刺耳也可以很低沉)、調前五秒、暫停、調後五秒、結束、時間軸

跳時間
時間:可以是10或0:10或0:0:10 末節時間點(可不填):填了以後如果播至那裏會自動重播
         [網站有圖片可能比較懂<點我](http://owo.freeserver.tw:20371/h2)
         '''}
        ))
    elif op == "help4":
      await ctx.response.send_message(embed=EM(
        "管理與設定",
          "辦事真輕鬆",
          {
             '伺服器管理':'''
/等級 設定 設定自訂伺服器升級系統。
/設定伺服器前瞻 自訂伺服器的進入連結。
/封殺身分組 禁止特定成員互動。
/設自動提醒頻道 設定提醒頻道。''',
'成員相關':'''
/歡迎 新增身份組 成員加入時自動分配身分組。
/歡迎 新增訊息 自動發送加入訊息。
/簽到通知 管理 管理簽到通知。'''
          }
      ))
    elif op == "help5":
      await ctx.response.send_message(embed=EM(
        "文字改造工具!҉꧔ꦿ'้้้้", "華麗!҉꧔ꦿ'้้้้้้無上限",
        {"/花樣文字產生":"產生花樣文字 ้ۣۣ ้ۣۣ ้ۣۣ","/英文字體轉換 原文: 樣式:":"轉換多種字體𝒶𝒻𝒸𝒹𝒻𝒹𝒻𝒹ℊⒼⒽⒻⓉⒽ","/網名生成器":"產生網名"}
        ))
    elif op == "help6":
      await ctx.response.send_message(embed=EM(
        "實用工具", "網路功能或節省手動時間",
        {"開房":"看見路人想直接跟她開一個既能私訊、語音、視訊的萬能小房?\n</開房:1132088808368775188>直接開始!只想文字?在他頭上>按右鍵>按應用程式>按與他開房","計算":"心算不夠?想讓我幫你?\n</計算:1132088808012271692>或</一元二次方程式計算:1132088808368775192>開始!","主持一場遊戲":"玩遊戲想找人?\n</主持一場遊戲:1137271181821624340>提供了一個到位的功能","<a:YT:1135838936892186675>搜尋yt":"想找 不是人 的影片?\n</搜尋yt:1133380602423419022> 關鍵字:不是人 類型:影片","寶可圖鑑":"我是洛托姆，洛托!\n</pokedex:1132088809048260701>非必填: 關鍵字(例:歐) 或是 圖鑑編號 (382)，登登!蓋歐卡出現了","搜尋網路":"我是sxxx可以幫你用別的網站搜尋東西\n</搜尋網路:1132088809048260702>可以找到一些網站!"}))
    elif op=='help9':
       await ctx.response.send_message(embed=EM("AI",'''/ai
> 與AI對話
# AI頻道(只能一個)
/ai拔除頻道
> 拔除AI頻道
/ai設定頻道
> 設為AI頻道''',
          {"AI功能":"想玩AI?@我直接開始(注意不要@到我的身分組，我會無視)\n</ai:1132088808012271688>讓我們開啟一場AI對話!"}
       ))
    elif op == "help7":
         await ctx.response.send_message(embed=EM("開發者工具", "伺服器開發者專用", {
    '</開發者 伺服器:1152386177240936599>': '取得伺服器資訊。',
    '</開發者 使用者:1152386177240936599>': '透過 ID 取得使用者資訊。',
    '</開發者 這個伺服器:1152386177240936599>': '取得當前伺服器資訊。',
    '</開發者 關於機器:1152386177240936599>': '查看機器人的狀態與資訊。'
}))
        #{"新增自訂快捷發言":"</新增自訂快捷發言:1143437979512209500>","</1:1132088808368775194>":"說謝謝","</2:1132088808368775195>":"說早安","</3:1132088808368775196>":"問誰有空","</4:1132088808368775197>": "快捷發言:找人玩","</5:1132088808599470180>":"等一下","</6:1132088808599470181>":"集合大家","</7:1132088808599470182>":"炫耀一個東西"}))
    elif op == "help8":
      await ctx.response.send_message(
        "</help:1132088808012271686>|</設定yt發片通知:1132088808012271687>|</ai:1132088808012271688>|</大量建立身分組:1132088808012271689>|</嵌入產生:1132088808012271690>|</kick:1132088808012271691>|</計算:1132088808012271692>|</調查活動:1192977146021425283>|</大家的邀請:1157304672508452984>|</設定頻道蟲洞:1132088808012271693>|</開發者:1152386177240936599>||</列出文字:1152877065733935186>|</封殺身分組:1132088808012271695>|</開房:1132088808368775188>|</建立狀態頻道:1141989110358212609>|</等級:1172836165389398128>|</自訂快捷發言:1141989110358212610>|</新增自訂快捷發言:1143437979512209500>|</0:1143437979512209501>|</設自動提醒頻道:1132088808368775191>|</一元二次方程式計算:1132088808368775192>|</de:1132088808368775193>|</1:1132088808368775194>|</2:1132088808368775195>|</3:1132088808368775196>|</4:1132088808368775197>|</5:1132088808599470180>|</6:1132088808599470181>|</7:1132088808599470182>|</8:1132088808599470183>|</tag:1132088808599470184>|</文字山:1132088808599470185>|</建議伺服器:1175326925883977748>|</主持一場遊戲:1137271181821624340>|</搜尋yt:1133380602423419022>|</播放:1157304672508452985>|</大刀石頭布:1157304672508452986>|</設定伺服器前瞻:1134460626438201364>|</自訂客服:1135794437780418591>|</歡迎:1166680445820346441>|</s:1166678401092943894>|</英文字體轉換:1132088808599470188>|</花樣文字產生:1132088808599470189>|</發表名言:1136551582553604196>|</進階發表名言:1136884278714716170>|</全服羈絆排名:1147716566113329162>|</簽到通知:1182604265412382820>|</我:1174290072510660619>|</美圖:1171754690560663664>|</取得使用者:1132088808809177088>|</真心話大填空:1132088808809177089>|</真心話出題:1132088808809177090>|</投幣:1132088808809177091>|</網名生成器:1132088808809177092>|</設定成員每分鐘字數上限:1132088808809177093>|</機器人加入語音頻道:1132088808809177094>|</設定成員退出嘲笑通知:1132088808809177097>|</探險:1132088809048260699>|</寶可盒子:1144155497373650964>|</pokedex:1132088809048260701>|</搜尋網路:1132088809048260702>|</淦文產生:1132088809048260703>|</情書產生:1132088809048260704>|</大量生成電郵:1136503115059830857>|</客服:1137954229252800552>"
      )
    elif op.startswith("dd&stp"):
        with open("dds.json", "r") as json_file:
          dic = json.load(json_file)
        key=ctx.message.embeds[0].footer.text
        if dic[key][0]!="ev" and  dic[key][0]!=str(ctx.user.id):
            await ctx.response.send_message("等等!🤔是我搞錯回合順序了嗎?[回報問題](https://discord.gg/CaFUuFTUzQ)\n或開新的一場",ephemeral=True)
            return
        dic[key][-1].append(op[6:])
        view=View(timeout=0)
        if len( dic[key][-1])>1:
             dic[key].append(list())
             del  dic[key][1][1][ dic[key][1][1].index(op[6:])]
             
             nus=ctx.message.content.split(" VS ")[0][2:-1]
             dic[key][0]=nus
             print(nus)
             with open("s.json", "w") as file:
                 json.dump(dic, file, indent=4)
             dex={"dd":["d","bb","b"],"d":["b"],"ss":["s","dd","d"],"s":["d"],"bb":["ss","s","d"],"b":"s"}
             ass= dic[key][-2]
             print(ass[0],dex[ass[1]])
             a=int(ass[0] not in dex[ass[1]])
             b=int(ass[1] not in dex[ass[0]])
             em=ctx.message.embeds[0]
             if len(dic[key][1][1])<1:
                    em.set_field_at(index=len(em.fields)-1,name=f"第{len(em.fields)}回合", value=f"{a}:{b}", inline=False)
                    a=0
                    b=0
                    for i in ctx.message.embeds[0].fields:
                        aa,bb=i.value.split(":")
                        a+=int(aa)
                        b+=int(bb)
                    await ctx.response.edit_message(
         embed=discord.Embed(title=f"{a}:{b}由{ctx.message.content.split(' VS ')[0] if a>b else ctx.message.content.split(' VS ')[1] }獲勝!"),view=None)
                    del dic[key]
                    with open("dds.json", "w") as file:
                        json.dump(dic, file, indent=4)
             chh={"dd":discord.SelectOption(label="大刀",value="dd&stpdd",emoji="🔪"), "d":discord.SelectOption(label="剪刀",value="dd&stpd",emoji="✂️"), "bb":discord.SelectOption(label="衛生紙",value="dd&stpbb",emoji="🗞️"), "b":discord.SelectOption(label="布",value="dd&stpb",emoji="📰"),"ss":discord.SelectOption(label="巨石",value="dd&stpss",emoji="🪦"),"s":discord.SelectOption(label="石頭",value="dd&stps",emoji="🪨")}
             ops=[ ]
             for i in dic[key][1][0]:
                 ops.append(chh[i])
             view.add_item(Select(placeholder=f"輪到{bot.get_user(int(nus)) if len(nus)>5 else '任何人'}",options=ops))
                           
             await ctx.response.edit_message(embed=em.set_field_at(index=len(em.fields)-1,name=f"第{len(em.fields)}回合", value=f"{a}:{b}", inline=False),view=view)
        else:
            del  dic[key][1][0][dic[key][1][0].index(op[6:])]
            nus=ctx.message.content.split(" VS ")[1][2:-1]
            dic[key][0]=nus
            with open("dds.json", "w") as file:
                 json.dump(dic, file, indent=4)
            em=ctx.message.embeds[0]
            chh={"dd":discord.SelectOption(label="大刀",value="dd&stpdd",emoji="🔪"),"d":discord.SelectOption(label="剪刀",value="dd&stpd",emoji="✂️"),"bb":discord.SelectOption(label="衛生紙",value="dd&stpbb",emoji="🗞️"), "b":discord.SelectOption(label="布",value="dd&stpb",emoji="📰"),"ss":discord.SelectOption(label="巨石",value="dd&stpss",emoji="🪦"),"s":discord.SelectOption(label="石頭",value="dd&stps",emoji="🪨")}
            ops=[]
            for i in dic[key][1][1]:
                ops.append(chh[i])
            view.add_item(Select(placeholder=f"輪到{bot.get_user(int(nus)) if len(nus)>5 else '任何人'}", options=ops))
            await ctx.response.edit_message(embed=em.add_field(name=f"第{len(em.fields)+1}回合", value=f"輪到{bot.get_user(int(nus)) if len(nus)>5 else '任何人'}", inline=False),view=view)       
  
playg=Group(name="播放",description="播放音樂")
@playg.command(name="yt音樂", description="在語音頻道播放youtube音樂")   
async def ytolayerr(ctx,搜尋或輸入連結:str):
    url=搜尋或輸入連結
    ydl_opts = {
        'quiet': True,  
        'noplaylist': True  
        }
    try:
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)  
        if info_dict:
          await playm(ctx,url,False)
        else:
          raise "not yt url"
    except:
        await ctx.response.defer( ephemeral=False, thinking=False)
        options=[]
        c=0
        videos = scrapetube.get_search(query=url.replace(" ",""),limit=24,results_type="video")
        for video in videos:
            options.append(discord.SelectOption(label=video['title']['runs'][0]['text'],value="p&https://www.youtube.com/watch?v="+video['videoId'],emoji="<a:YT:1135838936892186675>"))
            c+=1
        embed=discord.Embed(title="<a:YT:1135838936892186675>"+url, url=f"https://www.youtube.com/results?search_query={url}",color=0xf50000,description="點選以下選項開始播放")
        if c==0:
            options.append(discord.SelectOption(label="DISCORD看我建造一個機器人伺服器",value="p&https://www.youtube.com/watch?v=dne5kKtz2lA",emoji="<:me:1122364224103006300>"))
        select = Select(placeholder=f"找到{c}項結果", options=options)
        view = View(timeout=0)
        view.add_item(select)
        await ctx.followup.send(embed=embed,view=view)

bot.tree.add_command(playg)          
        
@bot.tree.command(name="大刀石頭布", description="跳脫命運安排的新玩法")   
async def ddstb(ctx,遊玩對象:discord.User): 
     with open("dds.json", "r", encoding='utf-8') as json_file:
          dic = json.load(json_file)
     def mack():
        a=chr(random.randint(1,500))
        if a not in dic:
            return a
        else:
            return mack()
     gaid=mack()
     dic[gaid]=[str(ctx.user.id),[["dd","d","bb","b","ss","s"],["dd","d","bb","b","ss","s"]],[]]
     with open("json", "w") as file:
        json.dump(dic, file, indent=4)
     em=discord.Embed(title="大刀石頭布",).set_footer(text=gaid)
     view=View()
     view.add_item(Select(placeholder=f"輪到{ctx.user}", options=[
        discord.SelectOption(label="大刀",value="dd&stpdd",emoji="🔪"),
        discord.SelectOption(label="剪刀",value="dd&stpd",emoji="✂️"),
        discord.SelectOption(label="衛生紙",value="dd&stpbb",emoji="🗞️"),
        discord.SelectOption(label="布",value="dd&stpb",emoji="📰"),
        discord.SelectOption(label="巨石",value="dd&stpss",emoji="🪦"),
        discord.SelectOption(label="石頭",value="dd&stps",emoji="🪨"),
        ]))
     await ctx.response.send_message(f"<@{ctx.user.id}> VS <@{遊玩對象.id}>",embed=em,view=view)
      
    
class sendmeto(discord.ui.Modal,discord.Embed,title="請輸入訊息"):
  def __init__(self, channel):
        super().__init__(timeout=60.0)
        self.channel = int(channel)
  text = discord.ui.TextInput (label = "文字訊息", style = discord.TextStyle.long, placeholder="傳的訊息內容", default="", required = False, max_length= 1900)
  emh = discord.ui.TextInput (label = "嵌入方塊標題", style = discord.TextStyle.short, placeholder="", default="", required = False, max_length= 200)
  emd = discord.ui.TextInput (label = "嵌入方塊內文", style = discord.TextStyle.long, placeholder="", default="", required = False, max_length= 1900)
  linkn = discord.ui.TextInput (label = "連結按鈕名稱", style = discord.TextStyle.short, placeholder="", default="", required = False, max_length= 20)
  link = discord.ui.TextInput (label = "連結按鈕連結", style = discord.TextStyle.short, placeholder="", default="", required = False,min_length=13, max_length= 200)
  async def on_submit(self, ctx: discord.Interaction):
    try:
        c=bot.get_channel(self.channel)
        em=discord.Embed(title=self.emh.value, description=self.emd.value) if self.emd.value and self.emh.value else None
        await c.send(content=self.text.value,embed=em,view= butt(self.linkn.value,self.link.value) if self.linkn.value and self.link.value else None,allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
        await c.send(f"-by<@{ctx.user.id}>\n也想空投訊息?到 https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id} 試試")
        await ctx.response.send_message(f"<a:okk:1277864492163928166>成功傳至<#{c.id}>",ephemeral=True)
    except Exception as bug:
        await ctx.response.send_message(f"失敗，原因:{bug}",ephemeral=True)
    
    
class playmod(discord.ui.Modal,discord.Embed,title="跳至..."):
  def __init__(self):
        super().__init__(timeout=60.0)
  emh = discord.ui.TextInput (label = "時間", style = discord.TextStyle.short, placeholder="像是1:05或65", default="", required = True, max_length= 20)
  emd = discord.ui.TextInput (label = "末截時間點:非必填，填了後將可以剪輯影片，從上面的時間到末截時間點", style = discord.TextStyle.short, placeholder="像是2:05或125", default="", required = False, max_length= 20)
  async def on_submit(self, ctx: discord.Interaction):
        voice_client = ctx.guild.voice_client
        if voice_client:
            voice_client.stop()
            with open("music.json", "r") as json_file:
              dic = json.load(json_file)
                    
            
             
            try:
                t=0
                c=0
                for i in self.emh.value.split(':'):
                  t+=int(i)*(60**c)
                  t+=1
                  c+=1
                ct=int(ctx.message.content.split('\n')[-1][3:-3])
                ct-=t
            except:
                await ctx.response.send_message(content="無法辨識時間",ephemeral=True)
            if self.emd.value !='':
              try:
                t=0
                c=0
                for i in self.emh.value.split(':'):
                  t+=int(i)*(60**c)
                  t+=1
                  c+=1
                cc=int(ctx.message.content.split('\n')[-1][3:-3])
                cc-=t
                if cc-ct>5:
                  await ctx.response.send_message(content="剪輯間距太短或超越奇異博士",ephemeral=True)
                  return
                
             
             
                
                source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3',options=f'-filter:a "atempo='+ctx.message.content.split("\n")[1][1:]+'","asetrate='+str(float(ctx.message.content.split("\n")[2][1:])*44100)+'"')
                vs=discord.PCMVolumeTransformer(source,volume=0.5) 
                voice_client.play(vs)
                await ctx.response.edit_message(content=f"跳至{self.emh.value}"+ctx.message.content[4:-16]+f'<t:{ct}:R>')
                await asyncio.sleep(ct-cc)
                await voice_client.stop()
               
                return
              except:
                await ctx.response.send_message(content="無法辨識時間",ephemeral=True)
                return
            t=time.time()-ct
            source =discord.FFmpegPCMAudio(f'downloads/audio{ctx.guild.id}.mp3',before_options=f'-ss {t}',options=f'-filter:a "atempo='+ctx.message.content.split("\n")[1][1:]+'","asetrate='+str(float(ctx.message.content.split("\n")[2][1:])*44100)+'"')
            vs=discord.PCMVolumeTransformer(source,volume=0.5) 
            voice_client.play(vs)
            await ctx.response.edit_message(content=f"跳至{self.emh.value}"+ctx.message.content[4:-16]+f'<t:{ct}:R>')
            
       
    
 
#disconnect()
#
@bot.tree.command(name="設定伺服器前瞻", description="將能用自訂連結進入伺服器")
async def testurl(ctx,自訂連結:str):
  await ctx.response.send_message(embed=embedMake("請使用Guild Gate"),ephemeral=True,view=butt("開始使用","https://gg.is-from.tw/"))
  return
  if ctx.user.guild_permissions.administrator:
    try:
      i=str(ctx.guild.icon)
      c=""
      for ch in ctx.guild.channels:
        c = str(await ch.create_invite())
        if c != "":
          break
      if c=="":
        await ctx.response.send_message(embed=embedMake("我沒權限創建邀請"),ephemeral=True,view=butt("增加權限","https://discord.com/oauth2/authorize?client_id=1132079788140531872"))
        return
      print(c)
    except Exception as bug:
      await ctx.response.send_message(embed=embedMake("這裡不是伺服器或者我沒權限",bug),view=butt("增加權限","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)
      return
    with open("url.json", "r", encoding='utf-8') as json_file:
          data = json.load(json_file)
    if 自訂連結 in data:
      if data[自訂連結][0]!=ctx.guild.id:
        await ctx.response.send_message(embed=embedMake("此連結已有人使用"),ephemeral=True)
        return
    data[自訂連結]=[ctx.guild.id,c,ctx.guild.name,i]
    with open("url.json", "w", encoding='utf-8') as file:
      json.dump(data, file, indent=4)
    await ctx.response.send_message(embed=embedMake("<a:okk:1277864492163928166>完成",f"https://dai.bigpokemonunite.repl.co/+{自訂連結}"),view=butt("打開",f"https://dai.bigpokemonunite.repl.co/+{自訂連結}","🔗"))

  else:
    await ctx.response.send_message(embed=embedMake("你不是管理員"),view=butt("加到自己的伺服器","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)  
#####
class inot(discord.ui.Modal,title="請輸入題目"):
  def __init__(self, title):
        super().__init__(timeout=60.0)
        self.title = int(title[4])
  answer = discord.ui.TextInput (label = "修改一個客服題目", style = discord.TextStyle.short, placeholder="", default="請問有甚麼問題", required = True, max_length= 20)
 
  async def on_submit(self, ctx: discord.Interaction):
    for channel in ctx.guild.channels:
      if channel.name=="客服資料":
        c=channel
    sliced_parts = c.topic.split("|>")
    sliced_parts[self.title]=f"{self.answer}{sliced_parts[self.title][-3:]}"
    await c.edit(topic= "|>".join(sliced_parts))
    await c.send(f"{ctx.user}:更新步驟:{self.title}:成:{self.answer}",silent=True)
    await ctx.response.edit_message(content="已更新",embed=None,view=None)
    
####
class inco(discord.ui.Modal,title="請輸入題目"):
  def __init__(self, title):
        super().__init__(timeout=60.0)
        a={'必填簡答': '*QS', '必填長文': '*QL', '可填簡答': '-QS', '可填長文': '-QL',"要在頻道說什麼?":"*CC","給予的身分組名稱":"*GS"}

        self.bot=bot
        self.title = a[title]
  
  answer = discord.ui.TextInput (label = "新增一個客服題目", style = discord.TextStyle.short, placeholder="", default="請問有甚麼問題", required = True, max_length= 20)
  
  async def on_submit(self, ctx: discord. Interaction):
    for channel in ctx.guild.channels:
      if channel.name=="客服資料":
        c=channel
    a=c.topic
    if a:
      await c.edit(topic=f"{a}|>{self.answer}{self.title}")
    else:
      await c.edit(topic=f"|>{self.answer}{self.title}")
    await c.send(f"{ctx.user}:新增了一個步驟:{self.answer}，類別:{self.title}",silent=True)
    await ctx.response.edit_message(content="已更新")
    # embed=embedMake("按下『新建步驟』來建立一個智慧客服的執行步驟","按下選項『步驟(1、2、3)即可編輯步驟』","當使用者使用</客服:1132088809048260705>時將會按照步驟執行"))

coufg=Group(name="自訂客服",description="伺服器自訂客服功能")

@coufg.command(name="管理", description="自訂伺服器客服功能，將會創建一個名為:『客服資料』的頻道以供處存資料")
@app_commands.choices(請同意=[
  Choice(name='必須創建一個log資料庫,若原本已有名為『客服資料』的頻道可能會干擾',
         value='c')
])
async def couf(ctx,請同意: Choice[str]):
  if ctx.guild==None:
    await ctx.response.send_message(embed=embedMake("請在自己的群組執行"))
    return
  c=0
  if ctx.user.guild_permissions.manage_guild:
    for channel in ctx.guild.channels:
      if channel.name=="客服資料":
        c=channel
    if c==0:
      overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
      ctx.user: discord.PermissionOverwrite(read_messages=True),
      bot.user: discord.PermissionOverwrite(read_messages=True),
    }  
      try:
        c= await ctx.guild.create_text_channel('客服資料', overwrites=overwrites)
      except:
        await ctx.response.send_message(embed=embedMake("沒權限!"))
        return
    a=c.topic
    
    if a:
      a=a.split("|>")
    else:
      a=[]
    #   message.channel.edit(topic=new_description)
    options=[]
    co=0
    for i in a:
      co+=1
      if co<6:
        options.append(discord.SelectOption(label=f"編輯步驟{co-1}({i[:-3]})",value=co-1,emoji="<:me:1122364224103006300>"))
    
    select = Select(placeholder=f"新增一個步驟類型", options=[
        discord.SelectOption(label="必填簡答",value="*QS",emoji="🔤"),
        discord.SelectOption(label="必填長文",value="*QL",emoji="📃"),
        discord.SelectOption(label="可填簡答",value="-QS",emoji="🔡"),
        discord.SelectOption(label="可填長文",value="-QL",emoji="📜"),
        discord.SelectOption(label="自動建立頻道",value="*CC",emoji="🎫"),
        discord.SelectOption(label="自動給予身分",value="*GS",emoji="🪪"),
        ])
    async def couba(ctx):
      a={"*QS":"必填簡答","*QL":"必填長文","-QS":"可填簡答","-QL":"可填長文","*CC":"要在頻道說什麼?","*GS":"給予的身分組名稱"}
      await ctx.response.send_modal(inco(title=str(a[select.values[0]])))
        
    async def coub(ctx):
        bu1 = Button(style=discord.ButtonStyle.green,
               label=f"編輯題目",
               emoji="<:gr:1127209538966261780>")
        bu2 = Button(style=discord.ButtonStyle.danger,
               label="刪除題目",
               emoji="<a:XX:1120631053921566861>", custom_id=selects.values[0])
        async def ba(ctx):
          await ctx.response.send_modal(inot(title=ctx.message.embeds[0].title))
        async def ba2(ctx):
          for channel in ctx.guild.channels:
            if channel.name=="客服資料":
              c=channel
          sliced_parts = c.topic.split("|>")
          del sliced_parts[int(bu2.custom_id)]
          t=str("|>".join(sliced_parts))
          await c.edit(topic=t)
          await c.send(f"{ctx.user}:刪除了步驟{bu2.custom_id}")
          await ctx.response.edit_message(content="已刪除",embed=None,view=None)
        bu1.callback=ba
        bu2.callback=ba2
        view = View(timeout=180)
        view.add_item(bu1).add_item(bu2)
        await ctx.response.send_message(embed=embedMake(f"編輯題目{selects.values[0]}"),view=view,ephemeral=True)
    view = View(timeout=600)
    if len(options)>1:
      selects = Select(placeholder=f"編輯題目", options=options[1:])
      selects.callback = coub
      view.add_item(selects)
    select.callback = couba
    view.add_item(select)
    await ctx.response.send_message(embed=embedMake("按下『新建步驟』來建立一個智慧客服的執行步驟","按下選項『步驟(1、2、3)即可編輯步驟』","當使用者使用</客服:1132088809048260705>時將會按照步驟執行"),ephemeral=True,view=view)
  else:
    await ctx.response.send_message(embed=embedMake("您沒權限"),view=butt("加到自己的","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)

@coufg.command(name="開始", description="根此伺服器客服聯繫")
async def cougg(ctx):
    if ctx.guild==None:
      await ctx.response.send_message("這裡不是伺服器")
      return
    await cought(ctx)
async def cought(ctx):
    c=0
    for channel in ctx.guild.channels:
      if channel.name=="客服資料":
        c=channel
        break
    if c==0 or "|>" not in c.topic:
        await ctx.response.send_message(embed=embedMake("此伺服器並未提供，請洽管理員","請用</客服 管理:1135794437780418591>來設定"),ephemeral=True)
    if c :
      rc=c.topic.split("|>")[1:]
      modal = getcou(title="伺服器客服")
      for im in rc:
        if im.endswith("*CC")  :
          has_permission = any(c.permissions_for(ctx.user).send_messages for c in ctx.guild.text_channels if c.name == '客服頻道')
          if not has_permission:
            # Create a new "客服頻道" with only the user having send_messages permission
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }
            c=await ctx.guild.create_text_channel('客服頻道', overwrites=overwrites)
            await c.send(f"<@{ctx.user.id}>{im[:-3]}")
          else:
            for channel in ctx.guild.channels:
              if channel.name=="客服頻道":
                await channel.send(f"<@{ctx.user.id}>{im[:-3]}")
                break
        elif im.endswith("*GS"):
          try:
            role = discord.utils.get(ctx.guild.roles, name=im[:-3])
            if role:
              
                await ctx.user.add_roles(role)
                await ctx.user.send(f"獲得一個身分組:{role.name}。在:{ctx.guild}中")
              
            else:
                for c in ctx.guild.channels:
                  if c.name=="客服資料":
                    await c.send(f"一則設定錯誤，沒有名為```{im[:-3]}```的身分可供使用者使用")
                    break
          except:
              for c in ctx.guild.channels:
                if c.name=="客服資料":
                  await c.send(f"一則設定錯誤，我沒有給予身分的權限```{im[:-3]}```",view=butt("增加權限","https://discord.com/oauth2/authorize?client_id=1132079788140531872"))
                  break
        else:
          modal.add_question(q=im[:-3],type=im[-3:])
      await ctx.response.send_modal(modal)
    else:
      await ctx.response.send_message(embed=embedMake("此伺服器並未提供，請洽管理員","請用</客服 管理:1135794437780418591>來設定"),ephemeral=True)

bot.tree.add_command(coufg)

class jionmo(discord.ui.Modal,title="新增歡迎資料"):
  def __init__(self, title):
        super().__init__(timeout=60.0)
        self.questions = [] 
        a={ '替換名稱':'CN' , '添加戰符': 'AN'} 
        self.title=a[title]
    
  def add_question(self,q,type="s",d="嗨嗨!歡迎@u加入"):
      a={"s":discord.TextStyle.short,"l":discord.TextStyle.paragraph}
      question= discord.ui.TextInput(label = q, style = a[type], placeholder="", default=d, required =True , max_length= 150)
      self.add_item(question)
      self.questions.append(question)
  
  async def on_submit(self, ctx: discord. Interaction):
    for channel in ctx.guild.channels:
      if channel.name=="歡迎資料":
        c=channel
    a=c.topic
    print(self)
    if a==None:
      a=""
    for i in self.questions:
      a+=i.value
    await c.edit(topic=f"|>{a}{self.title}")
    await ctx.response.edit_message(content="完成!",embed=None,view=None)

welg=Group(name="歡迎",description="設定伺服器歡迎系統")

@welg.command(name="編輯", description="自訂成員加入時要做的事，將會創建一個名為:『歡迎資料』的頻道以供儲存資料")
@app_commands.choices(請同意=[
  Choice(name='必須創建一個log資料庫,若原本已有名為『歡迎資料』的頻道可能會干擾，刪除我建立的頻道將會中止系統',
         value='c')
])
async def couf(ctx,請同意: Choice[str]):
  if ctx.guild==None:
    await ctx.response.send_message(embed=embedMake("請在自己的群組執行"))
    return
  c=0
  if ctx.user.guild_permissions.administrator:
    for channel in ctx.guild.channels:
      if channel.name=="歡迎資料":
        c=channel
    if c==0:
      overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
      ctx.user: discord.PermissionOverwrite(read_messages=True),
      bot.user: discord.PermissionOverwrite(read_messages=True),
    }
      c= await ctx.guild.create_text_channel('歡迎資料', overwrites=overwrites)
    a=c.topic
    
    if a:
      a=a.split("|>")
    else:
      a=[]
    #   message.channel.edit(topic=new_description)
    options=[]
    co=0
    for i in a:
      co+=1
      if co<6:
        if i.endswith("CN"):
           txt=f'替換名稱-{"->".join(i[:-2].split("|"))}'
        elif i.endswith("AN"):
           txt=f'添加戰符-{i[:-2]}'
        elif i.endswith("CS"):
           txt=f'發送訊息-{i[:-2]}'
        else:
           txt='給予身分'
        txt = txt if len(txt)<50 else txt[:49]
        options.append(discord.SelectOption(label=f"編輯步驟{co-1}-{txt}",value=co-1,emoji="<:me:1122364224103006300>"))
    
    select = Select(placeholder=f"新增一個步驟類型(歡迎訊息、給予身分以移至/歡迎 新增訊息、/歡迎 新曾身份)", options=[
        discord.SelectOption(label="替換名稱",value="CN",emoji="📇"),
        discord.SelectOption(label="添加戰符",value="AN",emoji="🏷️"),
        ])
    async def couba(ctx):
      a={'CN': '替換名稱', 'AN': '添加戰符'} 
      b={ 'CN': '(要將成員名稱中的?)|(替換為?)', 'AN': '幫成員名字前端加上?'} 
      c={ 'CN': 'XX|歡迎', 'AN': 'H ้้้şĸ'} 
      modal = jionmo(title=str(a[select.values[0]]))
      modal.add_question(q=b[select.values[0]],type="s",d=c[select.values[0]])
      await ctx.response.send_modal(modal)
      return
      
    async def coub(ctx):
        bu2 = Button(style=discord.ButtonStyle.danger,
               label="刪除步驟",
               emoji="<a:XX:1120631053921566861>", custom_id=selects.values[0])
        async def ba2(ctx):
          for channel in ctx.guild.channels:
            if channel.name=="歡迎資料":
              c=channel
          sliced_parts = c.topic.split("|>")
          del sliced_parts[int(bu2.custom_id)]
          t=str("|>".join(sliced_parts))
          await c.edit(topic=t)
          await c.send(f"{ctx.user}:刪除了步驟{bu2.custom_id}")
          await ctx.response.edit_message(content="已刪除",embed=None,view=None)
        bu2.callback=ba2
        view = View(timeout=180)
        view.add_item(bu2)
        await ctx.response.send_message(embed=embedMake(f"編輯步驟{selects.values[0]}"),view=view,ephemeral=True)
    view = View(timeout=600)
    if len(options)>1:
      selects = Select(placeholder=f"編輯步驟", options=options[1:])
      selects.callback = coub
      view.add_item(selects)
    select.callback = couba
    view.add_item(select)
    await ctx.response.send_message(embed=embedMake("按下『新建步驟』來建立一個成員加入的執行步驟","按下選項『步驟(1、2、3)即可刪除步驟』","當使用者加入時將會按照步驟執行(歡迎訊息、給予身分以移至/歡迎 新增訊息、/歡迎 新曾身份)"),ephemeral=True,view=view)
  else:
    await ctx.response.send_message(embed=embedMake("您沒權限"),view=butt("加到自己的","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)

@welg.command(name="新增訊息", description="新增一個成員加入時的訊息，使用@u提及加入的人@un代表他的名子")
@app_commands.choices(請同意=[
  Choice(name='會將資料儲存在一個log資料庫,若原本已有名為『歡迎資料』的頻道可能會干擾',
         value='c')
])
async def addin(ctx,請同意: Choice[str],指定頻道:discord.TextChannel,訊息內容:Optional[str],嵌入標題:Optional[str],嵌入說明:Optional[str]):
  if ctx.user.guild_permissions.administrator:
    if 訊息內容==None:
      訊息內容=""
    if 嵌入標題==None:
      嵌入標題=""
    if 嵌入說明==None:
      嵌入說明=""
    c=0
    for channel in ctx.guild.channels:
      if channel.name=="歡迎資料":
        c=channel
    if c==0:
      overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
      ctx.user: discord.PermissionOverwrite(read_messages=True),
      bot.user: discord.PermissionOverwrite(read_messages=True),
    }
      c= await ctx.guild.create_text_channel('歡迎資料', overwrites=overwrites)
    a=c.topic
    if a==None:
          a=""
    try:
          await c.edit(topic=f"{a}|>{指定頻道.id}|{訊息內容}|{嵌入標題}|{嵌入說明}CS")
          await ctx.response.send_message(embed=embedMake("<a:okk:1122807844736090152>完成"),ephemeral=True)
    except:
          await ctx.response.send_message(embed=embedMake("我沒權限"),view=butt("增加權限","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)
  else:
    await ctx.response.send_message(embed=embedMake("您沒權限"),view=butt("加到自己的","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)

@welg.command(name="新增身份組", description="新增一個成員加入時給予的身分組")
@app_commands.choices(請同意=[
  Choice(name='會將資料儲存在一個log資料庫,若原本已有名為『歡迎資料』的頻道可能會干擾',
         value='c')
])
async def addin(ctx,請同意: Choice[str],給予身分:Optional[discord.Role],真人身分:Optional[discord.Role],機器身分:Optional[discord.Role]):
  if ctx.user.guild_permissions.administrator:
    c=0
    for channel in ctx.guild.channels:
      if channel.name=="歡迎資料":
        c=channel
    if c==0:
      overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
      ctx.user: discord.PermissionOverwrite(read_messages=True),
      bot.user: discord.PermissionOverwrite(read_messages=True),
    }
      c= await ctx.guild.create_text_channel('歡迎資料', overwrites=overwrites)
    a=c.topic
    n=""
    if a==None:
      a=""
    if 給予身分:
      n+=f"|>{給予身分.id}GS"
    if 真人身分:
      n+=f"|>{真人身分.id}AS"
    if 機器身分:
      n+=f"|>{真人身分.id}BS"
    
    try:
          await c.edit(topic=f"{a}{n}")
          await ctx.response.send_message(embed=embedMake("<a:okk:1122807844736090152>完成"),ephemeral=True)
    except:
          await ctx.response.send_message(embed=embedMake("我沒權限"),view=butt("增加權限","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)
  else:
    await ctx.response.send_message(embed=embedMake("您沒權限"),view=butt("加到自己的","https://discord.com/oauth2/authorize?client_id=1132079788140531872"),ephemeral=True)


@welg.command(name="設定嵌入", description="成員加入後會在指定頻道發送嵌入")
@commands.has_permissions(administrator=True)
@app_commands.describe(頻道="要在哪裡發通知??", 通知="說啥?")
async def set_welcome(ctx, 頻道: discord.TextChannel, 通知: str):
  if ctx.user.guild_permissions.administrator:
    try:
      with open("welcome.json", "r") as file:
        data = json.load(file)
      if len(通知) < 21:
        data[str(ctx.guild.id)] = [頻道.id, 通知]
      else:
        await ctx.response.send_message("<a:okk:1111792427464917044>資料太長，已自動刪去"
                                        )
        data[str(ctx.guild.id)] = [頻道.id, "".join(list(通知)[:21])]
      with open("welcome.json", "w") as file:
        json.dump(data, file, indent=4)
      await ctx.response.send_message("<:okk:1277864492163928166>資料更新成功")
    except Exception as bug:
      await ctx.response.send_message(bug)
      print(bug)
  else:
    await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限?",
                      "把我家到你的伺服"),
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ))


bot.tree.add_command(welg)

@bot.event
async def on_member_join(member):

  if member.id == 585697975003774979:
    await member.ban()
    return
  with open("welcome.json", "r", encoding='utf-8') as file:
    data = json.load(file)
  
  cout=Button(
    label="幫自己取綽號",
    emoji="🧨",
    style=discord.ButtonStyle.green)
  async def cback(interaction):
    try:
      
        r = nameMake()
        await interaction.response.send_message(
          f"🛹POKE機器蛋幫妳生了個網名```按右邊複製``` \n```{r}```如果不喜歡可再用一次，可用</花樣文字產生:1132088808599470189>修飾", view=NM())
    except Exception as bug:
      await interaction.response.send_message(
        f"<a:XX:1120631053921566861>失敗```{bug}```")
  cout.callback = cback
  view = View()
  view.add_item(cout)
  if str(member.guild.id) in data:
    channel = bot.get_channel(data[str(member.guild.id)][0])
    a = data[str(member.guild.id)][1]
    if "@u" in str(data[str(member.guild.id)][1]):
      a=a.replace("@u", str(member))
      try:
        await channel.send(embed=embedMake(f"歡迎{member}加入!",
                                           a,
                                           f"<@{member.id}>多虧了你的加入，伺服器出生率大幅提升!",
                                           "快用`/網名生成器`幫自己取個綽號").set_image(url=member.avatar.url),
                           view=view)
      except:
        pass
    else:
      await channel.send(embed=embedMake(f"歡迎{member}加入!", f"{a}",
                                         f"<@{member.id}>多虧了你的加入，伺服器出生率大幅提升!",
                                         "快用`/網名生成器`幫自己取個綽號").set_image(url=member.avatar.url),
                         view=view)
  c=[]
  for channel in member.guild.channels:
      if channel.name=="歡迎資料":
        c=channel.topic.split("|>")
  if len(c)>0:
    usn=member.global_name
    if usn==None:
      usn=member.name
    for i in c[1:]:
      if i.endswith("CN"):
        i=i[:-2].split("|")
        if i[0] in usn:
          try:
            await member.edit(nick=usn.replace(i[0],i[1]))
          except Exception as bug:
            await rebugTo(member,f"沒有替換的權限，可以式著[增加權限](https://discord.com/oauth2/authorize?client_id=1132079788140531872)\n或拿著錯誤名稱前往支援伺服器請求協助：{bug}\n[支援尋求協助](https://discord.gg/CaFUuFTUzQ)")
          
      elif i.endswith("AN"):
        try:
          await member.edit(nick=i[:-2]+usn)
        except:
          await rebugTo(member,"沒有添加戰符的權限，可以式著[增加權限](https://discord.com/oauth2/authorize?client_id=1132079788140531872)")
        
      elif i.endswith("CS"):
        i=i.replace("@un",usn)
        i=i.replace("@u",f"<@{member.id}>")
        i=i[:-2].split("|")
        try:
          embed=None
          if i[2]:
            embed=discord.Embed(title=i[2], description=i[3])
            embed.set_author(name=usn,icon_url=member.avatar.url if member.avatar else 'http://owo.freeserver.tw:20371/b')
          await bot.get_channel(int(i[0])).send(i[1],embed=embed)
        except Exception as bug:
          print(bug)
          await rebugTo(member,f"發生找不到頻道或沒有發送訊息的權限，可以式著到[支援尋求協助](https://discord.gg/CaFUuFTUzQ)\n或拿著錯誤名稱前往支援伺服器請求協助：{bug}\n[支援尋求協助](https://discord.gg/CaFUuFTUzQ)")
      elif i.endswith("GS") or i.endswith("BS") or i.endswith("AS"):
        if i.endswith("AS"):
          if member.bot==True:
            break
        elif i.endswith("BS"):
          if member.bot!=True:
            break
        role = discord.utils.get(member.guild.roles, id=int(i[:-2]))
        try:
          await member.add_roles(role)
        except:
          await rebugTo(member,"沒有給予身分權限或找不到身分組，可以式著到[支援尋求協助](https://discord.gg/CaFUuFTUzQ)")
  else:
    pass
async def rebugTo(ctx,bug):
  for channel in ctx.guild.channels:
    if channel.name=="歡迎資料":
      await channel.send(bug)
  
  # await ctx.response.send_message(replace_mentions(t))#_modal(eat())

#發言


@bot.tree.command(name="s", description="讓我幫你發訊息")
@app_commands.describe(供啥="要我幫你講啥?",嵌入標題="嵌入的標題")
async def sa(ctx, 供啥: str,嵌入標題:Optional[str]):
  channel = bot.get_channel(ctx.channel.id)
  print(供啥,嵌入標題)
  try:
    webhook=await ctx.channel.webhooks()
    for w in webhook:
        if w.user==bot.user:
            webhook=w
    else:
      webhook = await channel.create_webhook(name=f"/s <@{ctx.user.id}>")
    await webhook.send(供啥,embed=embedMake(嵌入標題, end="我只是個負責轉達的，不要..阿喲!你拿游標指我這裡幹嘛?") if 嵌入標題 else None,username=f'/s by `<@{ctx.user.id}>`')
  except:
    await ctx.channel.send(供啥+f'\n/s by `<@{ctx.user.id}>`',embed=embedMake(嵌入標題, end="我只是個負責轉達的，不要..阿喲!你拿游標指我這裡幹嘛?") if 嵌入標題 else None)
  with open("US.json", "r", encoding='utf-8') as file:
    ss = json.load(file)
  if ss[str(ctx.user.id)][0] != None:
    ss[str(ctx.user.id)][0] -= 20
  with open("US.json", "w") as file:
    json.dump(ss, file, indent=4)
  await ctx.response.send_message(
    embed=embedMake("神不知鬼不覺唯有蛋汁", "你使用了/替我發言，工本費20元蛋殼（沒關係 每天發言一句就賺回來了）",
                    f"💵剩餘||{ss[str(ctx.user.id)][0]}||"),ephemeral=True)
  




@bot.tree.command(name="英文字體轉換", description="轉換英文字體")
@app_commands.describe(原文="要改造的文字", 樣式="改成怎樣?")
@app_commands.choices(樣式=[
  Choice(name='𝓐',
         value='𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃'),
  Choice(name='𝔸', value='𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤabcdefghijklmnopqrstwxyz'),
  Choice(name='𝒜手寫(疾)',
         value="𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"),
  Choice(name='𝙰',
         value='𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣'),
  Choice(name='𝔄',
         value='𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷'),
  Choice(name='𝕬(粗)',
         value='𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟'),
  Choice(name='ᴀ迷你',
         value='ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ'),
  Choice(name='Ⓐ透視',
         value='ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ'),
  Choice(name='𝓐手寫(穩)',
         value='𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃'),
  Choice(name='Ɐ倒字',
         value='ⱯꓭƆꓷƎℲꓨHIſꓘꓶWNOԀÒꓤSꓕꓵꓥMX⅄Zɐqɔpǝɟƃɥı̣ɾ̣ʞןɯuodbɹsʇnʌʍxʎz'),
  Choice(name='𝗔粗體',
         value='𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇'),
  Choice(name='ᴬ超米你',
         value='ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾǫᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ')
])
async def spac(interaction: discord.Interaction, 原文: str, 樣式: Choice[str]):
  a = ""
  az = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  for i in 原文:
    try:
      a += str(list(樣式.value)[az.index(i)])
    except ValueError:
      a += i
  await interaction.response.send_message(f"完成!```{a}```")


@bot.tree.command(name="花樣文字產生", description="產生花樣文字")
@app_commands.describe(原文="要改造的文字", 樣式="改成怎樣?")
@app_commands.choices(樣式=[
  Choice(name='螞蟻文҉', value='҉'),
  Choice(name='小尾巴꧔ꦿ', value='꧔ꦿ'),
  Choice(name='菊花文.꙲"', value=".꙲"),
  Choice(name="煙囪文'้้้้้้", value='้้้้้้'),
  Choice(name='鬍子ۣۣۣۣۣۣۣ ', value="ۣۣۣۣۣۣۣ ")
])
async def spac(interaction: discord.Interaction, 原文: str, 樣式: Choice[str]):
  a = list(原文)
  for i in range(len(a)):
    a.insert((i + 1) * 2 - 1, str(樣式.value))
  await interaction.response.send_message(f"為你生成了```按右邊複製>``` ```{''.join(a)}```",view=NM())

def malen(t=""):
    x=0
    for i in list(str(t)):
      if i in "GUXOMPQPHDJFAB%N#LVET":
        x+=26
      elif i in "234567890qeyuopasdghkzxcvbn/~$&eR_+tY<>?":
        x+=20
      elif i in "1jil:;' ()|!^`":
        x+=14
      else:
        x+=40
    return x

@bot.tree.command(name="發表名言", description="幫你畫幅名言圖")
async def usid(ctx: discord.Interaction, 名言:str):
  await ctx.user.avatar.save('avatar.png')
  user_avatar = Image.open("avatar.png")
  user_avatar = user_avatar.resize((86, 86))
  ta=re.findall(r"<@(\d+)>", 名言)
  for na in ta:
    user=bot.get_user(int(na))
    if user is not None:
        username =user.global_name
        if username ==None:
          username=user.name
        名言 = 名言.replace(f"<@{na}>", f"\"@{username}\"")
  ta=re.findall(r"<@&(\d+)>", 名言)
  for na in ta:
    名言 = 名言.replace(f"<@&{na}>", f"\"@&{na}\"")
  if len(名言)>35:
    名言==名言[:35]
  if "@" not in 名言:
    background = Image.open("tag.png").convert("RGBA").resize((1920, 96))
  else:
    background = Image.open("untag.png").convert("RGBA").resize((1920, 96))
  b = Image.new("RGBA", background.size,(255, 255, 255))
  b.paste(user_avatar, (26, 4))  
  b = Image.alpha_composite(b, background)
  del background
  draw = ImageDraw.Draw(b)
  usn=ctx.user.global_name
  
  if usn ==None:
      usn=ctx.user.name
  if "\"" in 名言:
    x=140
    for na in 名言.split("\""):
      if "@&" in na :
        na=ctx.guild.get_role(int(na[2:]))
        if na :
          col=na.color
          col=(col.r,col.g,col.b,120)
          if col==(0,0,0,120):
            col=(74, 75, 111,120)
          draw.rectangle([(x,50), (x+malen(f'@{na.name}'), 90)], fill=tuple(col))
          draw.text((x,50), "@"+na.name, fill=(201, 205, 251),font=ImageFont.truetype("TT.ttf",size=40))
        else:
          draw.rectangle([(x,50), (x+malen("deleted-role"), 90)], fill=(49,51,56,120))
          draw.text((x,50), "@deleted-role", fill=(201, 205, 251),font=ImageFont.truetype("TT.ttf",size=40))
      elif "@" in na :
        draw.rectangle([(x,50), (x+malen(na), 90)], fill=(74, 75, 111,120))
        draw.text((x,50), na, fill=(201, 205, 251),font=ImageFont.truetype("TT.ttf",size=40))
        
      else:
        draw.text((x,50), na, fill=(219,222,225),font=ImageFont.truetype("TT.ttf",size=40))
      x+=malen(na)
  else:      
    draw.text((140,50),名言,font=ImageFont.truetype("TT.ttf",size=40),fill=(219,222,225))
  draw.text((140,6),usn,font=ImageFont.truetype("TT.ttf",size=40),fill=ctx.user.top_role.color.to_rgb())
  draw.text((160+malen(usn),12),"2000/1/1 1:00",font=ImageFont.truetype("TT.ttf",size=30),fill=(148,155,164))
  
  b.save("result.png", encoding='utf-8')
  file = discord.File('result.png')
  await ctx.response.send_message(file=file)
  if os.path.exists("result.png"):
      os.remove("result.png")
      print("result.png 已刪除")
  else:
      print("找不到 result.png")

    # 刪除 avatar.png
  if os.path.exists("avatar.png"):
      os.remove("avatar.png")
      print("avatar.png 已刪除")
  else:
      print("找不到 avatar.png")


@bot.tree.command(name="進階發表名言", description="幫你畫幅名言圖")
async def usid(ctx: discord.Interaction, 名言:str,對象:discord.User,時間:str):
  await 對象.avatar.save('avatar.png')
  user_avatar = Image.open("avatar.png")
  user_avatar = user_avatar.resize((86, 86))
  ta=re.findall(r"<@(\d+)>", 名言)
  for na in ta:
    user=bot.get_user(int(na))
    if user is not None:
        username =user.global_name
        if username ==None:
          username=user.name
        名言 = 名言.replace(f"<@{na}>", f"\"@{username}\"")
  ta=re.findall(r"<@&(\d+)>", 名言)
  for na in ta:
    名言 = 名言.replace(f"<@&{na}>", f"\"@&{na}\"")
  if len(名言)>35:
    名言==名言[:35]
  if "@" not in 名言:
    background = Image.open("tag.png").convert("RGBA").resize((1920, 96))
  else:
    background = Image.open("untag.png").convert("RGBA").resize((1920, 96))
  b = Image.new("RGBA", background.size,(255, 255, 255))
  b.paste(user_avatar, (26, 4))  
  b = Image.alpha_composite(b, background)
  del background
  draw = ImageDraw.Draw(b)
  usn=對象.global_name
  
  if usn ==None:
      usn=對象.name
  if "\"" in 名言:
    x=140
    for na in 名言.split("\""):
      if "@&" in na :
        na=ctx.guild.get_role(int(na[2:]))
        if na :
          col=na.color
          col=(col.r,col.g,col.b,120)
          if col==(0,0,0,120):
            col=(74, 75, 111,120)
          draw.rectangle([(x,50), (x+malen(f'@{na.name}'), 90)], fill=tuple(col))
          draw.text((x,50), "@"+na.name, fill=(201, 205, 251),font=ImageFont.truetype("TT.ttf",size=40))
        else:
          draw.rectangle([(x,50), (x+malen("deleted-role"), 90)], fill=(49,51,56,120))
          draw.text((x,50), "@deleted-role", fill=(201, 205, 251),font=ImageFont.truetype("TT.ttf",size=40))
      elif "@" in na :
        draw.rectangle([(x,50), (x+malen(na), 90)], fill=(74, 75, 111,120))
        draw.text((x,50), na, fill=(201, 205, 251),font=ImageFont.truetype("TT.ttf",size=40))
        
      else:
        draw.text((x,50), na, fill=(219,222,225),font=ImageFont.truetype("TT.ttf",size=40))
      x+=malen(na)
  else:      
    draw.text((140,50),名言,font=ImageFont.truetype("TT.ttf",size=40),fill=(219,222,225))
  draw.text((140,6),usn,font=ImageFont.truetype("TT.ttf",size=40),fill=ctx.user.top_role.color.to_rgb())
  draw.text((160+malen(usn),12),時間,font=ImageFont.truetype("TT.ttf",size=30),fill=(148,155,164))
  
  b.save("result.png", encoding='utf-8')
  file = discord.File('result.png')
  await ctx.response.send_message(file=file)
  if os.path.exists("result.png"):
      os.remove("result.png")
      print("result.png 已刪除")
  else:
      print("找不到 result.png")

    # 刪除 avatar.png
  if os.path.exists("avatar.png"):
      os.remove("avatar.png")
      print("avatar.png 已刪除")
  else:
      print("找不到 avatar.png")

@bot.tree.command(name="全服羈絆排名", description="把伺服器羈絆前10名排出來")        
async def ppp(ctx)  :
    with open("xp.json", "r") as file:
        data = json.load(file)
    if str(ctx.guild.id) in data:
      data=data[str(ctx.guild.id)]
      d={}
      c=0
      for n in dict(sorted(data.items(), key=lambda x:x[1][1],reverse=True)):
        c+=1
        na=bot.get_user(int(n))
        if na:
            usn=na.global_name
            if usn==None:
                usn=na.name
        else:
            continue
        d[usn]=f"等級{data[n][0]},羈絆{data[n][1]}"
        if c>10:
              break
      await ctx.response.send_message(embed=EM("以下是本服羈絆前十名的成員","",d))
 
dach=Group(name="簽到通知",description="設定成員簽到時的通知")

@dach.command(name="新增", description="要設定許多個並隨機抽取的話，多次使用此指令設定") 
async def dayt(ctx,通知:discord.app_commands.Range[str,1,249]):
    if ctx.user.guild_permissions.administrator:
        pass
    else:
        await ctx.response.send_message('沒權限',view=butt())
        return
    st=通知
    with open("dayt.json", "r", encoding='utf-8') as file:
        ss = json.load(file)
    if str(ctx.guild.id) not in ss:
       a=["日一言，勝潛十年水","日行一善不如日發一言","日吐一話，健康久久","一日之計在於發言","常發言，不發炎",'有些簽到訊息可以增加智慧，有些則無，例如這句。']
       ss[str(ctx.guild.id)]=[random.choice(a)]
    if len(ss[str(ctx.guild.id)])>15:
        await ctx.response.send_message('已經滿了，使用`/簽到 管理` 來刪除',view=butt())
        return
    ss[str(ctx.guild.id)].append(st)
    with open("dayt.json", "w") as file:
        json.dump(ss, file, indent=4)
    await ctx.response.send_message('完成!!')
@dach.command(name="全刪", description="關閉所有通知") 
@discord.app_commands.choices(確定=[
  Choice(name='我確定全部關掉', value=0),])
async def daytdel(ctx,確定:Choice[int]):
    if ctx.user.guild_permissions.manage_channels:
      pass
    else:
      await ctx.response.send_message(embed=self.EM("你沒有限使用此指令"),ephemeral=True,view=butt())
      return
    with open("dayt.json", "r", encoding='utf-8') as file:
      lon= json.load(file)
    del lon[str(ctx.guild.id)]
    with open("dayt.json", "w") as file:
      json.dump(lon, file, indent=4)
    await ctx.response.send_message(embed=self.EM(f'簽到-全關!',f'已全部關掉'),ephemeral=True)
    
@dach.command(name="管理", description="選擇一個來刪") 
async def daytd(ctx):
  if ctx.user.guild_permissions.manage_channels:
      pass
  else:
      await ctx.response.send_message(embed=EM("你沒有限使用此指令"),ephemeral=True,view=butt())
  with open("dayt.json", "r", encoding='utf-8') as file:
      lon= json.load(file)
  view=View(timeout=0)
  if str(ctx.guild.id)  not in lon :lon[str(ctx.guild.id)]=[]
  op=[]
  for c,i in enumerate(lon[str(ctx.guild.id)],0):
     op.append(discord.SelectOption(label=i if len(i)<99 else i[:99], value=f'delda{c}'))
  select = discord.ui.Select(placeholder='刪除通知', options=op if op!=[] else [discord.SelectOption(label='沒有任何通知，快用/簽到，創一個吧!', value='none')])
  select.callback =deldasa
  view.add_item(select)  
  await ctx.response.send_message(embed=EM("按下底下選單刪除通知"),view=view)

async def deldasa(ctx):
    if ctx.user.guild_permissions.manage_channels:
        pass
    else:
        await ctx.response.send_message(embed=lonGroup.EM('',"你沒有限使用此指令"),ephemeral=True,view=butt())
        return
    op=ctx.data['values'][0][5:]
    with open("dayt.json", "r", encoding='utf-8') as file:
      lon= json.load(file)
    del lon[str(ctx.guild.id)][int(op)]
    with open("dayt.json", "w") as file:
      json.dump(lon, file, indent=4)
    ops = []

    for c, i in enumerate(lon[str(ctx.guild.id)], 0):
        op.append(discord.SelectOption(label=i if len(i)<99 else i[:99], value=f'delda{c}'))
    select = discord.ui.Select(placeholder='刪除通知', options=op if op!=[] else [discord.SelectOption(label='沒有任何通知，快用/簽到，創一個吧!', value='none')])

    view = View(timeout=0)

    view.add_item(select)
    await ctx.response.edit_message(embed=lonGroup.EM('','已關閉該通知'),view=view)

bot.tree.add_command(dach)   

@bot.tree.command(name="我", description="我的個狀態")   
async def ion(ctx):
    await ctx.user.avatar.save('avatar.png')
    user_avatar = Image.open("avatar.png")
    user_avatar = user_avatar.resize((200, 200))
    background = Image.open("egg.png").convert("RGBA")
    b = Image.new('RGBA', (background.size[0], background.size[1]),(255, 255, 255))
    x = b.size[0] // 5
    y = b.size[1] // 5
    b.paste(
      user_avatar,
      (40, 40),
    )
    b = Image.alpha_composite(b, background)
    si = background.size
    usn=ctx.user.global_name
    if usn ==None:
      usn=ctx.user.name
    uss=str(ctx.user)
    if "#" in uss:
      uss=uss[-5:]
    draw = ImageDraw.Draw(b)
    draw.text((140-(malen(usn)/8*3),270),
                           usn,font=ImageFont.truetype("TT.ttf",size=50))
    draw.text((140-(malen(uss)/20*3), 330),
                           uss,font=ImageFont.truetype("TT.ttf",size=25))
    lev=0
    with open("xp.json", "r") as file:
        data = json.load(file)
    if str(ctx.guild.id) in data:
        if str(ctx.user.id) in data[str(ctx.guild.id)]:
            lev=xpcont(ctx.guild.id,ctx.user.id)
        else:
          with open("US.json", "r", encoding='utf-8') as file:
            money = json.load(file)
          lev=(money[str(ctx.user.id)][0]/50)**0.5#
    nlev=int(lev)
    width = int((lev-nlev)*100) *7.7 + 90
    del background
    if nlev>4:
      col=(201,181,255)
    else:
      col=(250, 250, 0)
    if lev!=0:
        draw.rectangle([(85, 385), (si[0] - 85, 425)],
                       fill=(150, 150, 0, 255),
                       outline=(255, 255, 0, 0))
        draw.rectangle([(90, 390), (width, 420)],
                       fill=col,
                       outline=col)

        draw.ellipse([(75, 390), (105, 420)],
                     fill=col,
                     outline=col)
        draw.ellipse([(width - 15, 390), (width + 15, 420)],
                     fill=col,
                     outline=col)
        draw.ellipse([(si[0] - 105, 385), (si[0] - 65, 425)],
                     fill=(155, 155, 0),
                     outline=(155, 155, 0))
        draw.text((350, 390),f"等級:{nlev}，進度:{int((lev-nlev)*1000)/10}%",font=ImageFont.truetype("TT.ttf",size=30))
    else:
        draw.text((350, 390),"伺服器沒有設定等級計畫",font=ImageFont.truetype("TT.ttf",size=30))
    b.save("result.png", encoding='utf-8')
    file = discord.File('result.png')
    
    await ctx.response.send_message(file=file)
    del file
    del draw,user_avatar,b,lev,nlev
    # 刪除 result.jpg
    if os.path.exists("result.png"):
      os.remove("result.png")
    else:
      print("找不到 result.png")

    # 刪除 avatar.png
    if os.path.exists("avatar.png"):
      os.remove("avatar.png")
    else:
      print("找不到 avatar.png")

#:4089
# :2081
# :1975
# :1306
# animal_ears:1230
# :1163
# short_hair:1124
# twintails:1083
# blonde_hair:1013
# :985
# purple_eyes:953
# panties:943
# red_eyes:907
# cleavage:892
# :881
@bot.tree.command(name="美圖", description="生成pic.re的美圖")
@app_commands.choices(風格=[
  Choice(name='短髮',
         value='long_hair'),
  Choice(name='獸',
         value='original'),
  Choice(name='素臉',
         value='blush'),
  Choice(name='彩色頭髮',
         value='brown_hair'),
  Choice(name='短襪',
         value='thighhighs'),
  Choice(name='尾巴',
         value='tail'),
  Choice(name='肚臍',
         value='navel'),
  Choice(name='內褲',
         value='panties'),
   Choice(name='劈腿',
         value='cleavage'),
])
async def abimg(ctx,風格: Choice[str]):
  await ctx.response.defer(thinking=False)
  url = "https://pic.re/images"
  params = {
      "nin": 風格.value
  }

  response = requests.get(url, params=params)
  if ctx.channel.nsfw:
     pass
  else:
     pass
  if response.status_code == 200:
    embed=EM(' ')
    with open("anime_image.jpg", "wb") as f:
        f.write(response.content)
    embed.set_image(url='anime_image.jpg')
    await ctx.followup.send(file=discord.File('anime_image.jpg',spoiler=True))
  else:
    await ctx.followup.send(embed=EM('失敗')) 

@bot.tree.command(name="取得使用者", description="用ID取得他")
async def usid(interaction: discord.Interaction, id: Optional[str]):
  if id == None:
    id = interaction.user.id
  #try:
  # await interaction.response.send_message(f'{bot.get_user(int(id))}{(bot.get_user(int(id)).name)}')
  try:
  # msg = await bot.wait_for('message', check=lambda message: message.user == interaction.user)

  # Download user's avatar
  # if True:
    await bot.get_user(int(id)).avatar.save('avatar.png')

    user_avatar = Image.open("avatar.png")
    user_avatar = user_avatar.resize((200, 200))
    background = Image.open("egg.png").convert("RGBA")
    b = Image.new('RGBA', (background.size[0], background.size[1]),
                  (255, 255, 255))

    x = b.size[0] // 5
    y = b.size[1] // 5
    b.paste(
      user_avatar,
      (40, 40),
    )
    user_avatar = Image.new("RGBA", background.size,
                            (255, 255, 255)).paste(user_avatar, (40, 40))
    b = Image.alpha_composite(b, background)
    si = background.size
    usn=bot.get_user(int(id)).global_name
    if usn ==None:
      usn=bot.get_user(int(id)).name
    uss=str(bot.get_user(int(id)))
    if "#" in uss:
      uss=uss[-5:]
    draw = ImageDraw.Draw(b)
    draw.text((140-(malen(usn)/8*3),290),
                           usn,font=ImageFont.truetype("TT.ttf",size=50))
    draw.text((140-(malen(uss)/20*3), 330),
                           uss,font=ImageFont.truetype("TT.ttf",size=25))
    with open("US.json", "r", encoding='utf-8') as file:
      money = json.load(file)
    lev=(money[str(interaction.user.id)][0]/50)**0.5#
    nlev=int(lev)
    width = int((lev-nlev)*100) *7.7 + 90
    del background
    if nlev>4:
      col=(201,181,255)
    else:
      col=(250, 250, 0)
    draw.rectangle([(85, 385), (si[0] - 85, 425)],
                   fill=(150, 150, 0, 255),
                   outline=(255, 255, 0, 0))
    draw.rectangle([(90, 390), (width, 420)],
                   fill=col,
                   outline=col)

    draw.ellipse([(75, 390), (105, 420)],
                 fill=col,
                 outline=col)
    draw.ellipse([(width - 15, 390), (width + 15, 420)],
                 fill=col,
                 outline=col)
    draw.ellipse([(si[0] - 105, 385), (si[0] - 65, 425)],
                 fill=(155, 155, 0),
                 outline=(155, 155, 0))
    if interaction.user.id==id:
      draw.text((350, 390),f"等級:{nlev}，進度:{int((lev-nlev)*1000)/10}%",font=ImageFont.truetype("T.ttf",size=30))
    else:
      draw.text((250, 390),f"(只能看自己的)等級:{nlev}，進度:{int((lev-nlev)*1000)/10}%",font=ImageFont.truetype("T.ttf",size=30))
    b.save("result.png", encoding='utf-8')
    file = discord.File('result.png')
    
    await interaction.response.send_message(file=file)
    del interaction
    del file
    del draw,user_avatar,b,lev,nlev
    # 刪除 result.jpg
    if os.path.exists("result.png"):
      os.remove("result.png")
      print("result.png 已刪除")
    else:
      print("找不到 result.png")

    # 刪除 avatar.png
    if os.path.exists("avatar.png"):
      os.remove("avatar.png")
      print("avatar.png 已刪除")
    else:
      print("找不到 avatar.png")
  except Exception as e:
        await interaction.channel.send(f"Error: {str(e)}")
  # except:
  #   await interaction.channel.send(f'{bot.get_user(int(id))}{(bot.get_user(int(id)).name)}')

class inp(discord.ui.Modal,title="請輸入真心話"):
  answer = discord.ui.TextInput (label = "請填", style = discord. TextStyle.short, placeholder="", default="", required = True, max_length= 20)
 
  async def on_submit(self, ctx: discord. Interaction):
    embed=discord.Embed(title=f"{ctx.user.name}說出了真心話!!", url="https://sites.google.com/view/pokeegg", description=self.answer, color=0x5157fb)
    embed.set_author(name=ctx.user.name,url=ctx.user.avatar.url, icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name="真心話大填空", description="讓我隨機出題問問大家")
async def prs(ctx: discord.Interaction):
  a = []
  async for message in bot.get_channel(1127466764792508566).history(
      limit=1, oldest_first=False):
    a.append(message)
  a = eval(a[0].content)
  a = a[random.randint(0, len(a) - 1)]
  bu1 = Button(style=discord.ButtonStyle.green,
               label=f"開始填填",
               emoji="<:gr:1127209538966261780>",custom_id="re真心")
  bu2 = Button(style=discord.ButtonStyle.danger,
               label="檢舉題目",
               emoji="<a:XX:1120631053921566861>",custom_id="檢舉真心")
  async def ba(ctx):
      await ctx.response.send_modal(inp())
  async def ba2(ctx):
    await bot.get_channel(1135850441981300846).send("新的檢舉")
    await ctx.response.send_message("已收到你的檢舉",ephemeral=True)
  view = View(timeout=0)
  view.add_item(bu1).add_item(bu2)
  await ctx.response.send_message(embed=embedMake(f"今日真心話題目：{a}"),view=view)


@bot.tree.command(name="真心話出題", description="出體問大家")
async def prs(ctx: discord.Interaction, 題目: str):

  a = []
  async for message in bot.get_channel(1127466764792508566).history(
      limit=1, oldest_first=False):
    a.append(message)
  a = eval(a[0].content)
  a.append(題目)
  await bot.get_channel(1127466764792508566).send(a)
  bu1 = Button(style=discord.ButtonStyle.green,
               label=f"開始填填",
               emoji="<:gr:1127209538966261780>",custom_id="re真心")
  bu2 = Button(style=discord.ButtonStyle.danger,
               label="檢舉題目",
               emoji="<a:XX:1120631053921566861>",custom_id="檢舉真心")
  view = View(timeout=0)
  view.add_item(bu1).add_item(bu2)
  await ctx.response.send_message(embed=embedMake(題目,"使用</真心話大填空:1132088808809177089> "),view=view)

@bot.tree.command(name="紅包", description="預測今年可以拿到多少錢，請勿全部相信")
async def prs(ctx: discord.Interaction):
  r=['臺股走勢','今日星象','今日月亮與地球距離','道瓊工業指數','天氣預報','今年學測級距','太陽表面最高溫','平均月薪','平均年終獎金']
  r=random.choice(r)
  mo=random.randint(2,32)
  t=f'''AI根據{r}分析過後，推測您今年可以拿到
  > 新台幣||{mo}k||
'''
  await ctx.response.send_message(t)

@bot.tree.command(name="投幣", description="投一次硬幣來寓言")
async def prs(ctx: discord.Interaction):
  if random.randint(0, 100) < 45:
    file_path = "反面.png"
    c="等10分鐘後再來轉運"
  elif random.randint(0, 100) < 5:
    file_path = "egg.png"
    c="你把錢幣變成...XD"
  else:
    file_path = "正面.png"
    c="恭喜!趕快買樂...掰掰我先去買瞜!"
  file = discord.File(""+file_path)
  await ctx.response.send_message(c,file=file)
  if ctx.guild:
    with open("d.json", "r", encoding='utf-8') as file:
        data3 = json.load(file)
    if str(ctx.guild.id) in data3:
        if "CC" in data3[str(ctx.guild.id)]:
            xp=data3[str(ctx.guild.id)]["CC"]
            del data3
            cc=xpcont(ctx.guild,ctx.user.id,xp=xp)
            if cc[1]:
              await ctx.channel.send(f"恭喜!{ctx.user.name}的羈絆來到{data3[str(ctx.guild.id)][str(ctx.user.id)][1]}\n> 升至等級{cc[0]}",delete_after=20,mention_author=True)
            


def xpcont(guild,id,xp=0):
  with open("d.json", "r", encoding='utf-8') as file:
    data3 = json.load(file)
  ss=False
  if "ss" in data3[str(guild.id)]:
    ss=data3[str(guild.id)]["ss"]
    
  if "lv" in data3[str(guild.id)]:
    a1,a2,a3=data3[str(guild.id)]["lv"]
  else:
    a1,a2,a3=30,0,0
  with open("xp.json", "r", encoding='utf-8') as file:
    dataxp = json.load(file)
  if str(guild.id) not in dataxp:
    dataxp[str(guild.id)]={}
  if str(id) not in dataxp[str(guild.id)]:
      dataxp[str(guild.id)][str(id)]=[1,xp]
      with open("xp.json", "w") as file:
        json.dump(dataxp, file, indent=4)
      return [1,True]
  dataxp[str(guild.id)][str(id)][1]+=xp
  inv=0
  if ss:
    invites = guild.invites()
    invite_counts = {}
    for invite in invites:
      if invite.inviter in invite_counts:
            invite_counts[invite.inviter.id] += invite.uses
      else:
            invite_counts[invite.inviter.id] = invite.uses
    
    if id in invite_counts:
      inv=invite_counts[id]**ss
  if a1!=0:
    lv=int((-a2 + ((a2**2) + (-4 * a1 * (a3-dataxp[str(guild.id)][str(id)][1]-inv)))**0.5) / (a1 * 2))
  elif a2!= 0:
    lv=int(0-a3+dataxp[str(guild.id)][str(id)][1]+inv/a2)
  else:
    lv=a3
  ist=False
  if lv-dataxp[str(guild.id)][str(id)][0]>1:
      dataxp[str(guild.id)][str(id)][0]=lv
      ist=True
  with open("xp.json", "w") as file:
    json.dump(dataxp, file, indent=4)
  return [lv,ist]
  
  
    

@bot.command()
async def leave(ctx):
    # 離開語音頻道
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_connected():
        await voice_client.disconnect()


            
            
####網名
def nameMake():
  a = [
    "魔人", "射手", "月", "蛋", "菇菇", "魂", "幽", "怨靈", "聯盟", "俠", "之翼", "花", "鳴月",
    "精", "仔", "炎", "大老", "之王", "者", "雷", "風", "韻", "羽", "天","風","子"
  ]
  b = [
    "幻影", "神", "太空", "超級", "仇", "復仇", "量子", "粒子", "異", "逸", "不敗", "校", "轟",
    "鐵", "戟", "布丁", "鶴", "忍", "狙擊", "爆", "地球", "弒", "瀟","氣"
  ]
  #c = ["༄༊࿆ༀ꧁࿅࿆꧂ༀོྂཾ࿆࿐", "҉҉҉҉҉҉҉҉", ".꙲.꙲.꙲.꙲.꙲.꙲.꙲.꙲"]
  #d = random.choice(c)
  #r = d[:3]
  r = random.choice(b)
  #r += d[4]
  r += random.choice(a)
  #r += d[5:]
  return r

class NM(View):
  @discord.ui.button(style=discord.ButtonStyle.secondary,label="҉螞҉蟻҉文҉")
  async def button_callback7(self, ctx, button):
    r=ctx.message.content.split("```")
    t=" ҉".join(list(r[-2]))
    r[-2]=t
    await ctx.response.edit_message(content=f"{'```'.join(list(r))}")
  @discord.ui.button(style=discord.ButtonStyle.secondary,label='小尾巴꧔ꦿ')
  async def button_callback6(self, ctx, button):
    r=ctx.message.content.split("```")
    t="؛".join(list(r[-2]))+'꧔ꦿ'
    r[-2]=t
    await ctx.response.edit_message(content=f"{'```'.join(list(r))}")
  @discord.ui.button(style=discord.ButtonStyle.secondary,label="菊花文.꙲")
  async def button_callback5(self, ctx, button):
    r=ctx.message.content.split("```")
    t='҉'.join(list(r[-2]))
    r[-2]=t
    await ctx.response.edit_message(content=f"{'```'.join(list(r))}")
  @discord.ui.button(style=discord.ButtonStyle.secondary,label="煙囪文'้้้้้้")
  async def button_callback4(self, ctx, button):
    r=ctx.message.content.split("```")
    t="".join(list(r[-2]))+'้้้้้้'
    r[-2]=t
    await ctx.response.edit_message(content=f"{'```'.join(list(r))}")
  @discord.ui.button(style=discord.ButtonStyle.secondary,label="鬍子ۣۣۣۣۣۣۣ ")
  async def button_callback3(self, ctx, button):
    r=ctx.message.content.split("```")
    t="ۣۣۣۣۣۣۣ ".join(list(r[-2]))
    r[-2]=t
    await ctx.response.edit_message(content=f"{'```'.join(list(r))}")
  @discord.ui.button(style=discord.ButtonStyle.secondary,label="༄༊࿆ༀ天꧁使࿅࿆翅꧂膀ༀོྂཾ࿆࿐")
  async def button_callbackZ(self, ctx, button):
    r=ctx.message.content.split("```")
    t="".join(list(r[-2]))
    t=f"༄༊࿆ༀ꧁{t[:len(t)//2-1]}࿅࿆{t[len(t)//2:]}꧂ༀོྂཾ࿆࿐"
    r[-2]=t
    await ctx.response.edit_message(content=f"{'```'.join(list(r))}")
  @discord.ui.button(style=discord.ButtonStyle.success,label="設為暱稱")
  async def button_callback2(self, ctx, button):
    r="".join(ctx.message.content.split("```")[-2][3:])
    try:
          await ctx.user.edit(nickr=r)
          await ctx.response.send_message(f"改名成功```{r}```")
    except:
          await ctx.response.send_message(
            embed=saybugs(f"把我權限拉高{r}", "<a:XX:1120631053921566861>沒改名權限"),
            view=butt(
              "重設權限",
              "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
            ))   
  @discord.ui.button(style=discord.ButtonStyle.primary,label="再搞一個網名")
  async def button_callback1(self, ctx, button):
    r='```'.join(ctx.message.content.split("```")[:-1])
    r+=f"``````\n{nameMake()}```\n如果不喜歡可再用一次，可用</花樣文字產生:1132088808599470189> 修飾"
    await ctx.response.edit_message(content=r)  
  @discord.ui.button(style=discord.ButtonStyle.red,label="清空特效")
  async def button_callback0(self, ctx, button):
    r=ctx.message.content.split("```")
    t=""
    for i in list(r[-2])[3:]:
        if i not in "\"ۣۣۣۣۣۣۣ'้้้้้้.꙲꧔ꦿ文҉ ":
            t+=i
    await ctx.response.edit_message(content=f"{'```'.join(list(r[:-3]))}``````js\n{t}```{r[-1]}")  
                                      


@bot.tree.command(name="網名生成器", description="生成網名")
async def prss(interaction):
  r = nameMake()
  view = NM()
  await interaction.response.send_message(
    f"POKE機器蛋幫妳生了個網名```按右邊以複製``` \n```js\n{r}```如果不喜歡可再用一次，可用</花樣文字產生:1132088808599470189> 修飾",
    view=view)


# 設定上限///////////////////////////////////////////////////////////
@bot.tree.command(name="設定成員每分鐘字數上限", description="看名稱就知道是管理工具")
@commands.has_permissions(administrator=True)
@app_commands.describe(字數上限="規定一分鐘能講多少字，超過就禁言")
@app_commands.choices(字數上限=[
  Choice(name='關', value=False),
  Choice(name='10字', value=10),
  Choice(name='50字', value=50),
  Choice(name='100字', value=100),
  Choice(name='200字', value=200),
  Choice(name='500字', value=500)
])
async def check(ctx: discord.Interaction, 字數上限: int):
  if ctx.user.guild_permissions.administrator:
    if 字數上限 != " ":
      with open("top.json", "r", encoding='utf-8') as file:
        data = json.load(file)
      data[str(ctx.guild.id)] = 字數上限.value
      with open("top.json", "w") as file:
        json.dump(data, file)
      await ctx.response.send_message(
        embed=embedMake("完成!",
                        f"接下來所有成員每分鐘只能說{字數上限.value}",
                        end="提醒您，王子犯法遮民同罪，不爽我?把我加到伺服器然後禁言我再瘋狂批鬥我"))
  else:
    await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限還想怎樣?",
                      "把我家到你的伺服器才有用"),
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ))


@bot.tree.command(name="機器人加入語音頻道", description="把我丟進語音頻道")
@app_commands.describe(語音頻道="把我丟進哪?")
async def join(inter: discord.Interaction, 語音頻道: discord.VoiceChannel):
  await inter.response.defer(ephemeral=True, thinking=True)
  voice_channel = await 語音頻道.connect()
  await inter.response.send_message(f"已加入語音频道：{voice_channel.channel.name}")








@bot.tree.command(name="設定成員退出嘲笑通知", description="成員退出後會在指定頻道笑他")
@commands.has_permissions(administrator=True)
@app_commands.describe(頻道="要在哪裡發通知??", 嘲笑文="要怎笑他?")
async def set_leave(ctx, 頻道: discord.TextChannel, 嘲笑文: str):
  if ctx.user.guild_permissions.administrator:
    try:
      with open("leave.json", "r") as file:
        data = json.load(file)
      if len(嘲笑文) < 200:
        data[str(ctx.guild.id)] = [頻道.id, 嘲笑文]
        await ctx.response.send_message("<a:okk:1111792427464917044>資料更新成功")
      else:
        await ctx.response.send_message("<a:okk:1111792427464917044>資料太長，已自動刪去"
                                        )
        data[str(ctx.guild.id)] = [頻道.id, "".join(list(嘲笑文)[:21])]
      with open("leave.json", "w") as file:
        json.dump(data, file, indent=4)
      
    except Exception as bug:
      await ctx.response.send_message(bug)
  else:
    await ctx.response.send_message(
      embed=embedMake("<a:XX:1120631053921566861>你沒有管理權限",
                      "把我家到你的伺服器"),
      view=butt(
        "加到伺服器",
        "https://discord.com/oauth2/authorize?client_id=1132079788140531872"
      ))


@bot.tree.command(name="探險", description="探索寶可夢")
async def dex(ctx, ):
  with open("US.json", "r", encoding='utf-8') as file:
    ss = json.load(file)
  if len(ss[str(ctx.user.id)]) > 24:
    await ctx.response.send_message(
      embed=discord.Embed(title="你的隊伍已經滿了", color=0x009afa))
    return
  編號 = str(random.randint(906, 1025)).zfill(4)
  url = "https://tw.portal-pokemon.com/play/pokedex/" + 編號
  print(url)
  soup = bs(requests.get(url).content, "html.parser")
  name = soup.find(class_="pokemon-slider__main-name").get_text()
  
                
  types = [t.text for t in soup.find_all(class_="pokemon-type__type")]
  if len(types) > 1: types.insert(1, "** 和 **")
  types.append("** 屬性")
  types = "".join("".join(types).split("\n"))
  embed = discord.Embed(title="去挑戰並捕獲" + name + " 吧!",
                        url=url,
                        description="是 **" + types,
                        color=0x009afa)
  img_element = soup.find('img', class_='pokemon-img__front')
  if img_element:
    img_src = img_element['src']
    embed.set_image(url="https://tw.portal-pokemon.com" + img_src +
                    "?width=100&height=100")
  bu1 = Button(style=discord.ButtonStyle.secondary,
               label=f"💲10使用精靈球捕捉{name}#{編號}",
               emoji="<:61:1126474144138137680>")
  bu2 = Button(style=discord.ButtonStyle.blurple,
               label=f"💲20使用超級球捕捉{name}#{編號}",
               emoji="<:b2:1126481802991779931>")
  bu3 = Button(style=discord.ButtonStyle.green,
               label=f"💲30使用超級球捕捉{name}#{編號}",
               emoji="<:b3:1126482349396348929>")

  async def b1(ctx):
    m = ctx.message
    with open("US.json", "r", encoding='utf-8') as file:
      ss = json.load(file)
    if ss[str(ctx.user.id)][0] != None:
      if ss[str(ctx.user.id)][0] < 10:
        await ctx.followup.send(
          embed=embedMake("沒錢了!", "快去今天還沒講過話的伺服器發言吧(前提是那裡要有我)",
                          f"💵剩餘||{ss[str(ctx.user.id)][0]}||"))
        
        return
      ss[str(ctx.user.id)][0] -= 10
    with open("US.json", "w") as file:
      json.dump(ss, file, indent=4)
    tip="<:61:1126474144138137680>使用了精靈球工本費10元蛋殼"
    if 2 + random.randint(0, 3) > 4:
      await ctx.response.send_message(f"## 太好了!抓到{bu1.label.split('捕捉')[1]}了\n> {tip}")
      if ss[str(ctx.user.id)] != None:
        ss[str(ctx.user.id)].append(bu1.label.split('#')[1])
      with open("US.json", "w") as file:
        json.dump(ss, file, indent=4)
      await m.delete()
    elif 2 + random.randint(0, 3) > 2:
      await ctx.response.send_message(f"{bu1.label.split('捕捉')[1]}逃出來了!\n> {tip}")
    else:
      await ctx.response.send_message(f"噢不!{bu1.label.split('捕捉')[1]}逃走了!\n> {tip}")
      await m.delete()

  async def b2(ctx):
    m = ctx.message
    with open("US.json", "r", encoding='utf-8') as file:
      ss = json.load(file)
    if ss[str(ctx.user.id)][0] != None:
      if ss[str(ctx.user.id)][0] < 20:
        await ctx.followup.send(
          embed=embedMake("沒錢了!", "快去今天還沒講過話的伺服器發言吧(前提是那裡要有我)",
                          f"💵剩餘||{ss[str(ctx.user.id)][0]}||"))
        return
      ss[str(ctx.user.id)][0] -= 20
    with open("US.json", "w") as file:
      json.dump(ss, file, indent=4)
    tip="<:b2:1126481802991779931>使用了超級球工本費20元蛋殼"
    if 3 + random.randint(0, 3) > 4:
      await ctx.response.send_message(f"## 太好了!抓到{bu1.label.split('捕捉')[1]}了\n> {tip}")
      if ss[str(ctx.user.id)] != None:
        ss[str(ctx.user.id)].append(bu1.label.split('#')[1])
      with open("US.json", "w") as file:
        json.dump(ss, file, indent=4)
      await m.delete()
    elif 3 + random.randint(0, 3) > 2:
      await ctx.response.send_message(f"{bu1.label.split('捕捉')[1]}逃出來了!\n> {tip}")
    else:
      await ctx.response.send_message(f"噢不!{bu1.label.split('捕捉')[1]}逃走了!\n> {tip}")
      await m.delete()

  async def b3(ctx):
    m = ctx.message
    with open("US.json", "r", encoding='utf-8') as file:
      ss = json.load(file)
    if ss[str(ctx.user.id)][0] != None:
      if ss[str(ctx.user.id)][0] < 30:
        await ctx.response.send_message(
          embed=embedMake("沒錢了!", "快去今天還沒講過話的伺服器發言吧(前提是那裡要有我)",
                          f"💵剩餘||{ss[str(ctx.user.id)][0]}||"))
        await ctx.user.send(
          embed=embedMake(f"💵剩餘||{ss[str(ctx.user.id)][0]}||"))
        return
      ss[str(ctx.user.id)][0] -= 30
    with open("US.json", "w") as file:
      json.dump(ss, file, indent=4)
    tip="<:b3:1126482349396348929>使用了高級球工本費30元蛋殼"
    if 4 + random.randint(0, 3) > 4:
      await ctx.response.send_message(f"## 太好了!抓到{bu1.label.split('捕捉')[1]}了\n> {tip}")
      if ss[str(ctx.user.id)] != None:
        ss[str(ctx.user.id)].append(bu1.label.split('#')[1])
      with open("US.json", "w") as file:
        json.dump(ss, file, indent=4)
    elif 4 + random.randint(0, 3) > 2:
      await ctx.response.send_message(f"{bu1.label.split('捕捉')[1]}逃出來了!\n> {tip}")
    else:
      await ctx.response.send_message(f"噢不!{bu1.label.split('捕捉')[1]}逃走了!\n> {tip}")
      await m.delete()

  bu1.callback = b1
  bu2.callback = b2
  bu3.callback = b3
  view = View(timeout=0)
  view.add_item(bu1)
  view.add_item(bu2)
  view.add_item(bu3)
  await ctx.response.send_message(embed=embed, view=view)
  


@bot.tree.command(name="寶可盒子", description="列出自己的寶可夢")
async def dex(ctx):
  options = []
  await ctx.response.defer(ephemeral=True, thinking=True)
  with open("US.json", "r", encoding='utf-8') as file:
    ss = json.load(file)
  with open("dex.json", "r") as file:
    dex = json.load(file)
  co=0
  for i in ss[str(ctx.user.id)]:
    co+=1
    if type(i) == str:
      options.append(
        discord.SelectOption(label=dex["dex"][int(i) - 1],
                             value=i+str(co),
                             emoji="<:me:1122364224103006300>"))
  
  select = Select(placeholder="這是找到的", options=options)

  async def po(ctx):
    await ctx.response.defer(ephemeral=True, thinking=True)

    async def bye(ctx):
      with open("US.json", "r", encoding='utf-8') as file:
        ss = json.load(file)
      for i in range(len(ss[str(ctx.user.id)])):
        if ss[str(ctx.user.id)][i] == bu1.label.split('#')[1]:
          del ss[str(ctx.user.id)][i]
          with open("US.json", "w") as file:
            json.dump(ss, file, indent=4)
          await ctx.response.edit_message(embed=discord.Embed(title=f"完成把```{dn}```傳送的任務", color=0x009afa))
          return
      await ctx.response.edit_message(
        embed=discord.Embed(title=f"你沒有```{dn}```", color=0x009afa))

    dn = dex["dex"][int(select.values[0][:-1]) - 1]
    url = "https://tw.portal-pokemon.com/play/pokedex/" + str(
      select.values[0]).zfill(4)
    soup = bs(requests.get(url).content, "html.parser")
    img_element = soup.find('img', class_='pokemon-img__front')
    embed = discord.Embed(title=f"要把{dn}送給POKE機器蛋嗎?", color=0x009afa)
    if img_element:
      img_src = img_element['src']
      embed.set_image(url="https://tw.portal-pokemon.com" + img_src +
                      "?width=100&height=100")
    bu1 = Button(style=discord.ButtonStyle.danger,
                 label=f"我確定傳送{dn}#{select.values[0][:-1]}",
                 emoji="<:61:1126474144138137680>")
    bu1.callback = bye
    view = View()
    view.add_item(bu1)
    await ctx.followup.send(embed=embed, view=view)

  select.callback = po
  view = View()
  view.add_item(select)
  if len(options) == 0:
    await ctx.followup.send(embed=embedMake("你沒有半隻,用/探險 開始抓寶"))
  else:
    await ctx.followup.send(embed=embedMake("這是找到的"), view=view)

class PDG(View):
  @discord.ui.button(style=discord.ButtonStyle.secondary,label="上一個",emoji="◀️")
  async def button_callbackN(self, ctx, button):
    r=await dexf(int(ctx.message.embeds[0].footer.text)-1)
    await ctx.response.edit_message(embed=r[0],view=r[1])
  @discord.ui.button(style=discord.ButtonStyle.secondary,label="下一個",emoji="▶️")
  async def button_callbacklN(self, ctx, button):
    r=await dexf(int(ctx.message.embeds[0].footer.text)+1)
    await ctx.response.edit_message(embed=r[0],view=r[1])
    
async def dexf(編號):
    if 0 < int(編號) < 1026:
      編號 = str(編號).zfill(4)
      url = "https://tw.portal-pokemon.com/play/pokedex/" + 編號
      # 發送 GET 請求
      # 解析 HTML 文件
    else:
      編號 = str(random.randint(1, 1010)).zfill(4)
      url = "https://tw.portal-pokemon.com/play/pokedex/" + 編號
    #print(url)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=makehead()) as response:
                    content = await response.text()
                    soup = bs(content, "html.parser")
        except Exception as e:
            return EM(f"Error occurred while fetching {url}: {e}")
            
    name = soup.find(class_="pokemon-slider__main-name").get_text()
    types = [t.text for t in soup.find_all(class_="pokemon-type__type")]
    height_element = soup.find(class_="pokemon-info__height")
    height = height_element.find(class_="pokemon-info__value").get_text(
      strip=True)
    category_element = soup.find(class_="pokemon-info__category")
    category = category_element.find(class_="pokemon-info__value").get_text(
      strip=True)
    weight_element = soup.find(class_="pokemon-info__weight")
    weight = weight_element.find(class_="pokemon-info__value").get_text(
      strip=True)
    ability_element = soup.find(class_="pokemon-info__abilities")
    ability = ability_element.find(class_="pokemon-info__value").get_text(
      strip=True)
    title_element = soup.find(class_="pokemon-story__title")
    title = title_element.get_text(strip=True)
    story_elements = soup.find_all(class_="pokemon-story__body")
    stories = [story.get_text(strip=True) for story in story_elements]
    evolution_elements = soup.find_all(
      class_="pokemon-evolution-item__info-name size-14")
    evolutions = [
      evolution.get_text(strip=True) for evolution in evolution_elements
    ]
    pokemon_boxes = soup.find_all(class_="pokemon-style-box")
    img_element = soup.find('img', class_='pokemon-img__front')
    trp = types[0].split("\n")[2]
    if len(types) > 1: types.insert(1, "** 和 **")
    types.append("** 屬性")
    types = "".join("".join(types).split("\n"))
    category += "，是 **" + types
    color = {
      "一般": [220, 220, 220],
      "火": [253, 106, 0],
      "水": [15, 186, 252],
      "草": [10, 250, 13],
      "電": [255, 225, 3],
      "冰": [20, 226, 235],
      "格鬥": [222, 103, 0],
      "毒": [194, 131, 197],
      "地面": [250, 220, 30],
      "飛行": [90, 180, 100],
      "超能力": [238, 141, 218],
      "蟲": [150, 50, 51],
      "岩石": [180, 138, 100],
      "幽靈": [115, 105, 187],
      "龍": [30, 18, 86],
      "惡": [9, 19, 30],
      "鋼": [113, 135, 162],
      "妖精": [220, 154, 190]
    }
    color = color[trp]
    embed = discord.Embed(title=name,
                          url=url,
                          description=category,
                          color=discord.Color.from_rgb(
                            color[0], color[1], color[2]))  #color=0x006efe)
    if img_element:
      img_src = img_element['src']
      embed.set_thumbnail(url="https://tw.portal-pokemon.com" + img_src +
                      "?width=100&height=100")
    embed.add_field(name="身高", value=height, inline=True)
    embed.add_field(name="體重", value=weight, inline=True)
    embed.add_field(name="特性", value=ability, inline=True)
    view = PDG()

    for i, story in enumerate(stories):
      embed.add_field(name=f"圖鑑版本 {i+1}", value=story, inline=False)
    if evolutions is not None:
      evolutions.insert(1, ">")
      evolutions.insert(3, ">")
    else:
      evolutions = "無"
    x = 0
    for box in pokemon_boxes:
      name = box.find(class_="pokemon-style-box__name").text
      subname = box.find(class_="pokemon-style-box__subname").text
      button = Button(
        label=f"{name}{subname}",
        emoji="<:me:1122364224103006300>",
        url=f"https://tw.portal-pokemon.com/play/pokedex/{編號}_{x}",
        style=discord.ButtonStyle.link)
      view.add_item(button)
      x += 1
    if len(pokemon_boxes) < 1:
      button = Button(label=f"{name}",
                      emoji="<:me:1122364224103006300>",
                      url=f"https://tw.portal-pokemon.com/play/pokedex/{編號}",
                      style=discord.ButtonStyle.link)
      view.add_item(button)
    embed.add_field(name="進化", value="".join(evolutions), inline=False)
    embed.set_footer( text=編號)
    return [embed, view]    
#dex
@bot.tree.command(name="pokedex", description="寶可圖鑑")
async def dex(ctx, 關鍵字或圖鑑編號:str):
  await ctx.response.defer( thinking=True)


  try:
    圖鑑編號=int(關鍵字或圖鑑編號)
  except:
    關鍵字=關鍵字或圖鑑編號
  else:
    an = await dexf(圖鑑編號)
    await ctx.followup.send(embed=an[0], view=an[1])
  if 關鍵字:
    with open("dex.json", "r") as file:
      dex = json.load(file)
    
    options = []
    oss=[]
    cc=len(關鍵字)//2
    dex = dex["dex"]
    for i,d in enumerate(dex,1):
      if 關鍵字 in d:
        options.append(discord.SelectOption(label=d,
                               value=i,
                               emoji="<:me:1122364224103006300>"))
      elif len(set(關鍵字)&set(d))>cc:
        oss.append((d,i))
    if len(options)<24:
        options+=[discord.SelectOption(label=i[0],value=i[1],emoji="<:me:1122364224103006300>") for i in oss]
        options=options[:24]
    if len(options)>0:
        async def bac(ctx):
            an = await dexf(select.values[0])
            try:
                await ctx.response.send_message(embed=an[0], view=an[1])
            except:
                await ctx.channel.send(embed=an[0], view=an[1])
        options= options if len(options)<25 else options[:24]
        select = Select(placeholder="這是找到的", options=options)
        select.callback = bac
        view = View()
        view.add_item(select)
        await ctx.followup.send(embed=embedMake(f"已找到{len(options)}個"), view=view)
    else:
      async def randex(ctx):
          async def bac(ctx):
            an =await  dexf(selects.values[0])
            try:
              await ctx.response.send_message(embed=an[0], view=an[1])
            except:
              await ctx.channel.send(embed=an[0], view=an[1])

          with open("dex.json", "r") as file:
            dex = json.load(file)
          a = select.values[0].split("-")
          options = []
          b = list(range(int(a[0]), int(a[1])))
          random.shuffle(b)
          for i in b[:24]:
            options.append(
              discord.SelectOption(label=dex["dex"][i],
                                   value=i + 1,
                                   emoji="<:me:1122364224103006300>"))
          selects = Select(placeholder="結果", options=options)
          selects.callback = bac
          view = View()
          view.add_item(selects)
          await ctx.response.send_message(embed=embedMake("完成!"), view=view)
      select = Select(placeholder="隨機搜索",
                        options=[
                          discord.SelectOption(label="全國圖鑑1-1025",
                                               value='1-1025',
                                               emoji="🌐"),
                          discord.SelectOption(label="關都1-151紅綠",
                                               value="1-151",
                                               emoji="💠"),
                          discord.SelectOption(label="城都152-251金銀",
                                               value="152-251",
                                               emoji="💠"),
                          discord.SelectOption(label="豐緣252-386紅寶石藍寶石",
                                               value="252-386",
                                               emoji="💠"),
                          discord.SelectOption(label="神奧387-493鑽石珍珠",
                                               value="387-493",
                                               emoji="💠"),
                          discord.SelectOption(label="喜翠899-905傳說*阿爾宙斯",
                                               value="899-905",
                                               emoji="💠"),
                          discord.SelectOption(label="合眾494-649黑白",
                                               value="494-649",
                                               emoji="💠"),
                          discord.SelectOption(label="卡洛斯650-721XY",
                                               value="650-721",
                                               emoji="💠"),
                          discord.SelectOption(label="阿羅拉722-807太陽月亮",
                                               value="722-807",
                                               emoji="💠"),
                          discord.SelectOption(label="珈勒爾808-898劍盾",
                                               value="808-898",
                                               emoji="💠"),
                          discord.SelectOption(label="帕底亞906-1010朱紫",
                                               value="906-1010",
                                               emoji="💠"),
                        ])
      select.callback = randex
      view = View()
      view.add_item(select)
      await ctx.followup.send(embed=embedMake("歡迎使用寶可夢圖鑑!",
                                                        "請用關鍵字或編號來找尋想要的寶可夢",
                                                        "以下是隨機搜索"),
                                        view=view)



def makehead():
    user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozill5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']
    return {'User-Agent': random.choice(user_agents),
    'cookie':
    'cf_clearance=dbae418fe0c6a07fe6280635e7057f44f0c5aeca-1576140663-0-150; __cfduid=de4411bb1db85959721be2c90e1ed0a721576140663;ASP.NET_SessionId=mxu4rworc32oovw3ftckcuo1; _ga=GA1.3.241510402.1576140666; _gid=GA1.3.640675067.1576140666; _gat=1'}
  
def scearchg(s):
  編號 = s.replace(" ","_")
  headers = makehead()
  t = time.time()
  url = "https://www.google.com/search?q=" + 編號
  # print(url, )
  soup = bs(requests.get(url, headers=headers).content, "html.parser")
  links = soup.find_all('a')
  o = []
  
  for link in links:
    c = 0
    try:
      href = link['href']
      h3_text = link.h3.get_text()
      if c < 24 and h3_text and href.startswith(
          "/search?") != True and "google.com" not in href and href:
        if len(href) > 100:
          href = href[:98]
        c += 1
        o.append(
          discord.SelectOption(label=h3_text,
                               value=href,
                               emoji="<a:ing:1138322474782691389>"))
      # 提取 h3 标签文本内容

    except:
      pass
  tt = time.time() - t
  url = f"https://www.bing.com/search?q={編號}&sxsrf=AB5stBjAs2upiJCBDmxPN0ReijRhGp1WQA:1689581233148&source=lnt&tbs=lr:lang_1zh-TW&lr=lang_zh-TW&sa=X&ved=2ahUKEwix9eHJpJWAAxV2UvUHHbVDBFcQpwV6BAgEEAg&biw=1128&bih=738&dpr=2"
  # print(url, )
  soup = bs(requests.get(url, headers=headers).content, "html.parser")

  c = 0
  oo = []
  
  results = soup.find_all("li", class_="b_algo")

  for result in results:
    c = 0
    try:
      href = result.find("a")["href"]
      h3_text = result.find("h2").get_text()
      if c < 24 and h3_text and href.startswith(
          "/search?") != True and "google.com" not in href and href:
        if len(href) > 100:
          href = href[:98]
        c += 1
        oo.append(
          discord.SelectOption(label=h3_text,
                               value=href,
                               emoji="<a:ing:1138322474782691389>>"))
      # 提取 h3 标签文本内容

    except:
      pass
  if len(oo) < 1:
    oo.append(
      discord.SelectOption(label="沒有找到",
                           value="https://www.bing.com",
                           emoji="<a:ing:1138322474782691389>"))

  return o,oo,tt,t

async def gback(ctx):
    value=ctx.data['values'][0]
    links = str(value).split(".")[0]
    if len(links) > 50:
      links = links[:50]
    await ctx.response.defer()
    try:
      response = requests.get(value)
      soup = bs(response.text, 'html.parser')
      title = soup.title.string.strip() if soup.title else "無法取得標題"
      og_title = soup.find('meta', property='og:title')['content'] if soup.find('meta', property='og:title') else "沒有說明"
      em=EM(title,og_title,{})
    except Exception as bug:
       em=EM("無法分析此網站",bug,{})
    await ctx.followup.send(embed=em,view=butt(str(links),value))
@bot.tree.context_menu(name="搜尋網路")
async def sa(ctx, s: discord.Message):
  o,oo,tt,t=scearchg(s.content)
  
  select = Select(placeholder=f"google搜尋結果({len(o)}項{tt}秒", options=o)
  selects = Select(placeholder=f"bing搜尋結果({len(oo)}項{time.time()-t-tt}",
                   options=oo)

  

  select.callback = gback
  selects.callback = gback
  view = View(timeout=0)
  view.add_item(select)
  view.add_item(selects)
  await ctx.response.send_message(embed=embedMake("這是找到的", f"花了{time.time()-t}秒"),
                         view=view)

@bot.tree.command(name="搜尋網路", description="如同safari一樣")
async def google(ctx, 關鍵字: str):
  o,oo,tt,t=scearchg(關鍵字)
  select = Select(placeholder=f"google搜尋結果({len(o)}項{tt}秒", options=o)
  selects = Select(placeholder=f"bing搜尋結果({len(oo)}項{time.time()-t-tt}",
                   options=oo)



  select.callback = gback
  selects.callback = gback
  view = View(timeout=0)
  view.add_item(select)
  view.add_item(selects)
  await ctx.response.send_message(embed=embedMake("這是找到的", f"花了{time.time()-t}秒", 關鍵字),
                         view=view)


@bot.event
async def on_member_remove(member):
  with open("leave.json", "r", encoding='utf-8') as file:
    data = json.load(file)
  if str(member.guild.id) in data:
    channel = bot.get_channel(data[str(member.guild.id)][0])
    button = Button(label="幫我弄緊", emoji="🦪", style=discord.ButtonStyle.green)
    button2 = Button(label="緊了!", emoji="✅", style=discord.ButtonStyle.green)
    view = View()
    view.add_item(button2)
    view.add_item(button)
    if "@u" in str(data[str(member.guild.id)][1]):
      a = str(data[str(member.guild.id)][1]).split("@u")
      usn=member.global_name
  
      if usn ==None:
        usn=member.name
      await channel.send(embed=embedMake(f"{a[0]}@{member}{a[1]}",
                                         f"{usn}離開了😥",
                                         "大家最近皮繃緊一點阿，我也得小心了"),
                         view=view)
    else:
      await channel.send(embed=discord.Embed(
        title=data[str(member.guild.id)][1],
        url="https://sites.google.com/view/pokeegg"),
                         view=view)

@bot.tree.command(name="孔乙己", description="寫出一篇孔乙己")
@app_commands.describe(姓啥="主角姓氏", 做甚麼="惡行",喝什麼='飲品')
async def gm(it: discord.Interaction, 姓啥:app_commands.Range[str, 1, 10], 做甚麼:app_commands.Range[str, 1, 10],喝什麼:app_commands.Range[str, 0, 10]):
    await it.response.send_message(content=f'''
    這伺服器的活躍度，是和別處不同的：平常安靜的很，只有{姓啥}乙己出現時才熱鬧的多。
　　{姓啥}乙己是站著喝酒而穿長衫的唯一的人。他身材很高大；青白臉色，皺紋間時常夾些傷痕；一部亂蓬蓬的花白的鬍子。穿的雖然是長衫，可是又髒又破，似乎十多年沒有補，也沒有洗。他對人說話，總是滿口之乎者也，教人半懂不懂的。因為他姓{姓啥}，別人便從描紅紙上的「上大人孔乙己」，這半懂不懂的話裏，替他取下一個綽號，叫作{姓啥}乙己。{姓啥}乙己一到店，所有喝酒的人便都看著他笑，有的叫道：「{姓啥}乙己，你又{做甚麼}了！」他不回答，對櫃裡說：「溫兩碗酒，要一碟茴香豆。」便排出九文大錢。他們又故意的高聲嚷道：「{做甚麼}可真賺！」{姓啥}乙己睜大眼晴說：「你怎麼這樣憑空污人清白……」「什麼清白？我前天親眼見你{做甚麼}，吊著打。」{姓啥}乙己便漲紅了臉，額上的青筋條條綻出，爭辯道：「{做甚麼}……不能算{做甚麼}！……這伺服器的事，能算{做甚麼}麼？」接連便是難懂的話，什麼「君子固窮」，什麼「者乎」之類，引得眾人都哄笑起來：店內外充滿了快活的空氣。
    ''')
    
@bot.tree.command(name="淦文產生", description="寫出一篇有聲有色的淦文")
@app_commands.describe(主題="文章題目", 字數="要寫多少?")
async def gm(interaction: discord.Interaction, 主題:app_commands.Range[str, 1, 60] , 字數: app_commands.Range[int, 200, 5000]):
  if 字數 < 200:
    字數=200
  elif 字數 > 5000:
    字數=5000
  try:
    with open("gun.json", "r", encoding='utf-8') as file:
      data = json.load(file)
    名人名言 = data["famous"]  # a 代表前面垫话，b代表后面垫话
    前幹 = data["before"]  # 在名人名言前面弄点废话
    後幹 = data['after']  # 在名人名言后面弄点废话
    幹 = data['bosh']  # 代表文章主要废话来源

    def 洗牌(列表):
      池 = list(列表) * 2
      while True:
        random.shuffle(池)
        for 元素 in 池:
          yield 元素

    下一句廢話 = 洗牌(幹)
    下一句名言 = 洗牌(名人名言)

    def 来點名人名言():
      xx = next(下一句名言)
      xx = xx.replace("a", random.choice(前幹))
      xx = xx.replace("b", random.choice(後幹))
      return xx

    def 另起一段():
      xx = "\n"
      xx += "    "
      return xx

    tmp = str()
    tmp += f"        {主題}\n    "
    if 字數 < 650:
      for x in range(4):
        while (len(tmp) < 字數 * (x + 1) / 4 + 10):
          分支 = random.randint(0, 100)

          if 分支 < 20:
            tmp += 来點名人名言()
          else:
            tmp += next(下一句廢話)
        tmp += 另起一段()
        tmp = tmp.replace("x", 主題)
    else:
      for x in range(5):
        while (len(tmp) < 字數 * (x + 1) / 5 + 20):
          分支 = random.randint(0, 100)

          if 分支 < 20:
            tmp += 来點名人名言()
          else:
            tmp += next(下一句廢話)
        tmp += 另起一段()
        tmp = tmp.replace("x", 主題)
    if len(tmp)>2000:
        with open('ganm.txt', 'w') as f:
            f.write(tmp)
        with open('ganm.txt', 'rb') as f:
            file = discord.File(f)
        await interaction.response.send_message(f"🤬POKEAI製造了{字數}字的幹文一篇```只是字數超過diacord限制",file=file)
        os.remove('ganm.txt')
    else:              
        await interaction.response.send_message(f"🤬POKEAI製造了{字數}字的幹文一篇```txt\n{tmp}```")
  except Exception as e:
    await interaction.response.send_message(embed=saybug('出現問題',e))



@bot.tree.command(name="情書產生", description="小出一篇有很有效果的情書")
@app_commands.describe(對象="對象", 字數="要寫多少?")
async def lo(ctx, 對象: app_commands.Range[str, 1, 60], 字數: app_commands.Range[int, 201, 5000]):
  if 字數 < 200:
    await ctx.response.send_message("字數太少，至少200")
  elif 字數 > 5000:
    await ctx.response.send_message("太多了!，很燒腦")
  else:
    with open("love.json", "r", encoding='utf-8') as file:
      data = json.load(file)
    一 = data["1"]  # a 代表前面垫话，b代表后面垫话
    二 = data["2"]  # 在名人名言前面弄点废话
    三 = data['3']  # 在名人名言后面弄点废话
    四 = data['4']  # 代表文章主要废话来源

    def 洗牌(列表):
      池 = list(列表)
      while True:
        random.shuffle(池)
        for 元素 in 池:
          yield 元素

    第一 = 洗牌(一)
    第二 = 洗牌(二)
    第三 = 洗牌(三)
    第四 = 洗牌(四)

    def 另起一段():
      xx = "\n"
      xx += "    "
      return xx

    tmp = str()
    tmp += f"親愛的{對象}❤💖:\n    "
    if 字數 < 650:
      for x in range(4):
        while (len(tmp) < int(字數 * (x + 1)) / 4 + 30):
          if x == 0:
            tmp += next(第一)
          elif x == 1:
            tmp += next(第二)
          elif x == 2:
            tmp += next(第三)
          else:
            tmp += next(第四)
        tmp += 另起一段()
        tmp = tmp.replace("x", 對象)
    if len(tmp)>2000:
        with open('ganm.txt', 'w') as f:
            f.write(tmp)
        with open('ganm.txt', 'rb') as f:
            file = discord.File(f)
        await interaction.response.send_message(f"POKEAI製造了{字數}字的情書一篇只是字數超過diacord限制",file=file)
        os.remove('ganm.txt')
        return
    await ctx.response.send_message(
      f"POKEAI製造了{字數}字的情書一篇```{tmp}\n                          愛你的<@{ctx.user.name}>敬上```"
    )


@bot.event
async def on_guild_join(ctx):
  # Get the system channel of the guild
  system_channel = ctx.system_channel
  select = helpchi()

  button = Button(
    label="報修單",
    emoji="🛠",
    url=
    "https://docs.google.com/forms/d/e/1FAIpQLSePDj_iVFkeKHlC1sEFWF9vvj06055ELuI-C9EpuYcNKRgq_g/viewform?usp=sf_link",
    style=discord.ButtonStyle.link)
  butt2 = Button(
    label=
    "官้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้網้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้",
    emoji="<a:okk:1277864492163928166>",
    url="http://owo.freeserver.tw:20371/",
    style=discord.ButtonStyle.link)
  butt3 = Button(
    label="把我抓進你的伺服器",
    emoji="<a:cc:1147777573074522172>",
    url=
    "https://discord.com/oauth2/authorize?client_id=1132079788140531872",
    style=discord.ButtonStyle.link)
  butt4 = Button(label="訂閱我",
                 emoji="🎉",
                 url="https://www.youtube.com/@xHSK",
                 style=discord.ButtonStyle.link)
  embed = None

  

  view = View(timeout=0)
  view.add_item(select)
  view.add_item(button)
  view.add_item(butt2)
  view.add_item(butt3)
  # view.add_item(butt4)
  # Check if the system channel exists and the bot has permissions to send messages
  if system_channel and system_channel.permissions_for(ctx.me).send_messages:

    embed = discord.Embed(title="謝謝把我帶回家",
                          url="https://sites.google.com/view/pokeegg")
    embed.add_field(
      name="選則底下的功能來詢問",
      value=
      "嗨嗨，你發現了酷東西!使用我來讓你的discord更棒!!想要了解某個類別請使用下方的選單，如要查看特定的指令請使用</help:1106476433875927102> 或`/客服`你也可以到**官網**https://sites.google.com/view/pokeegg 有教學\n\n在輸入欄打/來看有哪些斜線命令\n\n||如果真的有問題請按《開始客服》||",
      inline=False)
    await system_channel.send(embed=embed, view=view)
  else:
    embed = discord.Embed(title="謝謝把我帶回家",
                          url="https://sites.google.com/view/pokeegg")
    embed.add_field(
      name="選則底下的功能來詢問",
      value=
      "嗨嗨，你發現了酷東西!使用我來讓你的discord更棒!!想要了解某個類別請使用下方的選單，如要查看特定的指令請使用</help:1106476433875927102> 或`/客服`你也可以到**官網**https://sites.google.com/view/pokeegg 有教學\n\n在輸入欄打/來看有哪些斜線命令\n\n||如果真的有問題請按《開始客服》||",
      inline=False)
    for channel in ctx.channels:
      try:
        await channel.send(embed=embed, view=view)
      except:
        pass
      else:
        return
@bot.tree.command(name="大量生成電郵", description="製造一堆名稱")
@app_commands.describe(電郵前名="例如:S",起始數字="例如100",結尾數字="例如:500",尾網域="例如:gmail.com")
async def maill(ctx,電郵前名:Optional[str],起始數字:int,結尾數字:int,電郵後名:Optional[str],尾網域:str):
  if 電郵前名==None:
    電郵前名=""
  if 電郵後名==None:
    電郵後名=""
  c=結尾數字-起始數字
  n=""
  if c>200:c=200
  for i in range(c):
    n+=f"{電郵前名}{起始數字+i}{電郵後名}@{尾網域},"
  await ctx.response.send_message(f"```txt\n {n[:1900]}\n```",allowed_mentions=discord.AllowedMentions( everyone=False, users=False, roles=False, replied_user=False))
  

  

####
class getcou(discord.ui.Modal,title="客服"):
  def __init__(self, title):
        super().__init__(timeout=60.0)
        self.questions = [] 
    
  def add_question(self,q,type="*QS"):
      a={"QS":discord.TextStyle.short,"QL":discord.TextStyle.paragraph}
      b={"*":True,"-":False}
      c={"*QS":"我需要幫助","*QL":"是這樣的:","-QS":"","-QL":""}
      question= discord.ui.TextInput(label = q, style = a[type[-2:]], placeholder="", default=c[type], required = b[type[-3]], max_length= 150)
      self.add_item(question)
      self.questions.append(question)
  
  async def on_submit(self, ctx: discord. Interaction):
    for channel in ctx.guild.channels:
      if channel.name=="客服資料":
        c=channel
    r=c.topic.split("|>")[1:]
    print(self)
    embed=discord.Embed(title="新的客服回報", url="https://discord.gg/CaFUuFTUzQ")
    embed.set_author(name=ctx.user, url="https://discord.gg/CaFUuFTUzQ",icon_url=ctx.user.avatar.url)
    d=0
    for i in self.questions:
      embed.add_field(name=r[d], value=i.value, inline=False)
      d+=1
    await c.send(embed=embed)
    await ctx.response.send_message(content="完成!",ephemeral=True)

def EM(tt="",d="",f=""):
  embed=discord.Embed(title=tt, url="https://discord.gg/CaFUuFTUzQ", description=d, color=0x3a85fd)
  if f!="":
    for i in f:
      embed.add_field(name=i, value=f[i], inline=False)
  return embed

#客服
@bot.tree.command(name="客服", description="如何使用")
async def he(ctx):
  select = helpchi()
  cout=Button(
    label="伺服器客服",
    emoji="🤖",
    style=discord.ButtonStyle.green)
  button = Button(
    label="報修單",
    emoji="🛠",
    url=
    "https://docs.google.com/forms/d/e/1FAIpQLSePDj_iVFkeKHlC1sEFWF9vvj06055ELuI-C9EpuYcNKRgq_g/viewform?usp=sf_link",
    style=discord.ButtonStyle.link)
  butt2 = Button(
    label=
    "官้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้網้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้้",
    emoji="<a:okk:1277864492163928166>",
    url="http://owo.freeserver.tw:20371/",
    style=discord.ButtonStyle.link)
  butt3 = Button(
    label="把我抓進你的伺服器",
    emoji="<a:cc:1147777573074522172>",
    url=
    "https://discord.com/oauth2/authorize?client_id=1132079788140531872",
    style=discord.ButtonStyle.link)
  butt4 = Button(label="訂閱我",
                 emoji="🎉",
                 url="https://www.youtube.com/@xHSK",
                 style=discord.ButtonStyle.link)
  embed = None

  
  async def coutback(ctx):
    if ctx.guild==None:
      await ctx.response.send_message("這裡不是伺服器")
      return

    await cought(ctx)
  
  cout.callback=coutback
  view = View(timeout=60)
  view.add_item(select)
  view.add_item(cout)
  view.add_item(button)
  view.add_item(butt2)
  view.add_item(butt3)
  view.add_item(butt4)
  embed = discord.Embed(title="客服",
                        url="https://sites.google.com/view/pokeegg")
  embed.add_field(
    name="選則底下的功能來詢問",
    value=
    "嗨嗨，你發現了酷東西!使用我來讓你的discord更棒!!想要了解某個類別請使用下方的選單，如要查看特定的指令請使用</help:1106476433875927102> 或`/客服`你也可以到**官網**https://sites.google.com/view/pokeegg 有教學\n\n在輸入欄打/來看有哪些斜線命令\n\n||如果真的有問題請按《開始客服》||",
    inline=False)
  await ctx.response.send_message(embed=embed, view=view)



bot.run(token=你還沒放token,reconnect=True)
async def playai():  
   
    await bot.start(token=你還沒放token,reconnect=True)
