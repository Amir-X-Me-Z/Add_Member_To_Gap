from pyrogram import *
import time
import os
#  @X_Me_Z  :  سازنده اسکریپت
from pyrogram.types import *
from pyrogram.raw import functions
from colorama import *
from pyfiglet import Figlet
init()#  @X_Me_Z  :  سازنده اسکریپت
os.system('pip install pyrogram')
os.system('pip install colorama')
os.system('pip install pyfiglet')
api_id=  18784007
api_hash = '21135f3177117d805354422adfd08603'
proxy = {"scheme":"socks5" ,"hostname":"127.0.0.1", "port" : 9150}
X_Me_Z = Client('X_Me_Z-Bot',
		api_id=api_id,
		api_hash=api_hash,
		proxy=proxy
		)
with X_Me_Z:
	X_Me_Z.send_message('me', 'ربات امیرشاه فعال شد !')
figlett = Figlet()#  @X_Me_Z  :  سازنده اسکریپت
textt = figlett.renderText('T . M e / X _ Me _ Z')
print(Fore.GREEN + textt)
figlett = Figlet(font='term')
text1 = figlett.renderText('send '.title())
text2 = figlett.renderText('{run} '.title())
text3 = figlett.renderText('in telegram : '.title())
print(Fore.GREEN+'Send '+Fore.RED+'{Run} '+Fore.GREEN+'In Telegram »»»\n')
# Add member Group to Group
admin = [1189966163]
@X_Me_Z.on_message(filters.me & filters.text ,group=1)
async def add_group_to_group(Client  , message):
	text = message.text#  @X_Me_Z  :  سازنده اسکریپت
	if text.lower() == 'run':
		mabda = str(input(Fore.CYAN+'{1} '+ Fore.WHITE+'- Enter the source group ››› '.title()))
		if mabda == mabda :
			await X_Me_Z.send_message('me' , f'گروه مبدأ  : [`{mabda}`] \n توجه آیدی گروه باید به صورت [ @GlassTheme یا GlassTheme ] یا همان عمومی باشد. در غیر این صورت عملیات با خطا مواجه خواهد شد.')
		async for member in X_Me_Z.get_chat_members(mabda):
			with open('chat_id.txt' , 'a+') as file: #  @X_Me_Z  :  سازنده اسکریپت
				file.write(f'{member.user.id}\n')
		maghsad = str(input(Fore.CYAN+'{2} ' + Fore.WHITE+'- Entr le groupe de destination ››› '.title()))
		await X_Me_Z.send_message('me' , f'گروه مقصد : {maghsad} \nتوجه : کاربران به این گروه اضافه میشوند.!' )
		print(Fore.YELLOW+'starting ...'.title())
		user_chat = open('chat_id.txt' , 'r').read().split()
		for x in user_chat:
			try:
				time.sleep(15)
				await X_Me_Z.add_chat_members(maghsad, x)
				print(Fore.GREEN+f'[+] '+Fore.WHITE+f'- added user : [ {Fore.GREEN + x} ]'.title())
			except :print(Fore.RED+f'[-] '+ Fore.WHITE+f'- not added user : [ {Fore.RED +x} ]'.title())
		os.remove('chat_id.txt')
	elif text == 'ربات' : await message.reply_text('Bot is Online ')
X_Me_Z.run()
#  @X_Me_Z  :  سازنده اسکریپت
