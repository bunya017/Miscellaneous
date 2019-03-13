import json



filename = str(input('Write the name or path of snippets file: \n$ '))
with open(filename, encoding='utf-8') as f_obj:
	vs_code_snippets = json.load(f_obj)

xx = list(vs_code_snippets.keys())
c = '%s.sublime-snippet' % (vs_code_snippets[xx[0]]['prefix'])
b = '''
<snippet>
	<content><![CDATA[
%s
]]></content>
	<tabTrigger>%s</tabTrigger>
	<description>%s</description>
</snippet>
''' % (
	vs_code_snippets[xx[0]]['body'][0],
	vs_code_snippets[xx[0]]['prefix'],
	vs_code_snippets[xx[0]]['description']
)
with open(c, 'w') as w_obj:
	w_obj.write(b.strip())

print('Completed successfully')