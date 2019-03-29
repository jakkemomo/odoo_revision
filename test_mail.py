from odoo.tools import mail

mail.html_keep_url('https://icode.by/')
# <a href="https://icode.by/" target="_blank">https://icode.by/</a>

html = '''
<html>
    <head>
        <script src="/module/static/src/js/script.js"/>
    </head>
    <body>
        <p>
            <span>
                Тут Марис пишет очередной шаблон письма для Лаймонаса
                 <a href="https://icode.by/" target="_blank">ICode.by</a
            </span>
                    <div style="  height: 100px;
             line-height: inherit  ;">Message sent from </div>alexolikov@gmail.com
        </p>
    </body>
</html>
'''

mail.html_sanitize(html, strip_style=True)
#
#
#         <p>
#             <span>
#                 Тут Марис пишет очередной шаблон письма для Лаймонаса
#                  <a href="https://icode.by/" target="_blank">ICode.by</a>
#                     <div>Message sent from </div>alexolikov@gmail.com
#         </span></p>


text = 'Here Maris writes another template for Laimonas with a link to https://icode.by/'

mail.plaintext2html(text)
# <p>Here Maris writes another template for Laimonas with a link to <a href="https://icode.by/" target="_blank">https://icode.by/</a></p>

mail.html2plaintext(html)
# Тут Марис пишет очередной шаблон письма для Лаймонаса
# ICode.by [1]
# Message sent from alexolikov@gmail.com
#
#
#
# [1] https://icode.by/
