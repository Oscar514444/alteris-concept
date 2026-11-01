from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)

def el(tag, text='', **attrs):
    attr=' '.join(f'{k.replace("_", "-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())
    return f'<{tag} {attr}>{escape(text)}</{tag}>'

def text(x,y,s,size=21,color='#e4e9f5',weight=400,**attrs):
    return el('text',s,x=x,y=y,fill=color,font_size=size,font_weight=weight,font_family='Inter, Segoe UI, Arial, sans-serif',**attrs)

def rect(x,y,w,h,fill='#141c2e',stroke='#2d3853',rx=18,**attrs):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" '+ ' '.join(f'{k.replace("_","-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())+'/>'

def svg(name,width,height,body,title,desc):
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#10192b"/><stop offset="1" stop-color="#090f1c"/></linearGradient><linearGradient id="line"><stop stop-color="#78e5cd"/><stop offset="1" stop-color="#849dff"/></linearGradient><radialGradient id="orb"><stop stop-color="#91eadb" stop-opacity=".55"/><stop offset=".55" stop-color="#7b9afe" stop-opacity=".17"/><stop offset="1" stop-color="#6987e8" stop-opacity="0"/></radialGradient></defs><rect width="{width}" height="{height}" rx="24" fill="url(#bg)"/>{body}</svg>'''
    (OUT/name).write_text(s,encoding='utf-8')

b=rect(44,40,205,32,'#162a30','#31534f',16)+text(58,62,'КОНЦЕПЦИЯ · НЕ ПРОДУКТ',12,'#96e2d1',700)
b+=text(48,142,'ALTERIS',66,'#f4f7ff',750)+text(50,184,'Цифровой контекст, ориентированный на человека',23,'#bdc9df')
b+=text(50,234,'Идея о том, как предпочтения, факты и связи',20,'#a6b4cc')+text(50,263,'могут помогать при работе с цифровыми задачами.',20,'#a6b4cc')
b+=rect(48,311,477,46,'#151f32','#33435a',13)+text(65,341,'Портфолио  /  исследовательское направление',16,'#b8c5dc')
b+='<circle cx="860" cy="202" r="190" fill="url(#orb)"/><circle cx="860" cy="202" r="103" fill="none" stroke="#7297cf" stroke-opacity=".45"/><circle cx="860" cy="202" r="69" fill="none" stroke="#8ce2d0" stroke-opacity=".5"/><circle cx="860" cy="202" r="27" fill="#91eadb" fill-opacity=".72"/>'
for x,y,label in [(755,148,'ФАКТЫ'),(952,150,'СВЯЗИ'),(735,278,'КОНТЕКСТ'),(952,285,'ГРАНИЦЫ')]:
    b+=f'<line x1="860" y1="202" x2="{x}" y2="{y}" stroke="#8babc8" stroke-opacity=".5"/><circle cx="{x}" cy="{y}" r="5" fill="#9be5d6"/>'+text(x-26,y-15,label,12,'#c7d6e8',650)
svg('01-alteris-hero.svg',1120,400,b,'ALTERIS — концепция','Иллюстрация идеи личного цифрового контекста; не описание готовой системы.')

b=text(44,65,'01  /  ИЗ ЧЕГО СКЛАДЫВАЕТСЯ КОНТЕКСТ',17,'#8bd5c9',700)+text(44,106,'Не архив сообщений, а смысловые связи',29,'#f4f7ff',700)
for i,(title,detail,detail2) in enumerate([('Факты','Что известно','из доступных источников'),('Связи','Как сведения','относятся друг к другу'),('Предпочтения','Что важно человеку','в его решениях'),('Границы','Что разрешено','и что требует согласия')]):
    x=44+i*265;b+=rect(x,143,248,148)+text(x+20,183,f'0{i+1}',14,'#80cbbb',700)+text(x+20,217,title,21,'#f3f6ff',700)+text(x+20,247,detail,16,'#adbbd2')+text(x+20,271,detail2,16,'#adbbd2')
b+=text(44,337,'Схема отражает замысел, а не подтверждённую реализацию памяти или политик.',16,'#9aaac2')
svg('02-context.svg',1120,380,b,'Компоненты контекста','Концептуальные элементы: факты, связи, предпочтения и границы.')

b=text(44,65,'02  /  ПРЕДПОЛАГАЕМЫЙ ПУТЬ',17,'#8bd5c9',700)+text(44,106,'От запроса человека к решению',29,'#f4f7ff',700)
for i,(title,sub) in enumerate([('Человек','намерение'),('Контекст','факты и связи'),('Обсуждение','подготовка решения'),('Действие','только в границах')]):
    x=44+264*i;b+=rect(x,149,234,110)+text(x+18,190,title,21,'#f3f6ff',700)+text(x+18,224,sub,15,'#adbbd2')
    if i<3:b+=f'<path d="M{x+239} 204 h17 m-6 -6 l6 6 -6 6" fill="none" stroke="#83d9ca" stroke-width="2"/>'
b+=text(44,316,'Направление исследования: такой рабочий процесс здесь не реализован.',16,'#9aaac2')
svg('03-flow.svg',1120,355,b,'Предполагаемый процесс ALTERIS','Концептуальная последовательность от намерения человека через контекст к решению и действию.')

b=text(44,65,'03  /  ЧЕСТНЫЕ ГРАНИЦЫ',17,'#8bd5c9',700)+text(44,106,'Задумано ≠ реализовано',29,'#f4f7ff',700)
b+=rect(44,143,503,174,'#172638','#37536a')+text(67,183,'Что представляет репозиторий',20,'#eaf5ff',700)+text(67,218,'Публичное описание идеи и визуальные схемы.',16,'#b8c9db')+text(67,247,'Помогает обсудить направление и границы.',16,'#b8c9db')+text(67,278,'Не содержит личную память или исходные данные.',16,'#b8c9db')
b+=rect(572,143,504,174,'#261f30','#59415a')+text(595,183,'Чего он не доказывает',20,'#f6eaf1',700)+text(595,218,'Работу автономного цифрового двойника.',16,'#d5bdcc')+text(595,247,'Реальную интеграцию памяти или действий.',16,'#d5bdcc')+text(595,278,'Гарантированную приватность или безопасность.',16,'#d5bdcc')
svg('04-boundaries.svg',1120,365,b,'Границы концепции','Портфолио и схемы без готовой реализации или гарантий безопасности.')
print('Created four SVG diagrams in',OUT)
