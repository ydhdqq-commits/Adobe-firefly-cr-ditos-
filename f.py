import pathlib,re
p=pathlib.Path('index.html')
s=p.read_text()
# solo toco el primer banner (el de arriba)
s=s.replace('max-width:380px;margin:12px auto;padding:14px','max-width:95%;width:92%;margin:8px auto;padding:6px 18px',1)
s=s.replace('font:900 32px Arial','font:900 22px Arial',1)
s=re.sub(r'<div class=af>','<div class=af style="max-width:95%;width:92%;padding:6px 18px">',s,1)
p.write_text(s)
print('top fino OK')
