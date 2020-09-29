#!/usr/bin/env python3

import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open('https://google.com')
print('Original Page: ')
for form in br.forms():
    print (form)

# try to change the language. hl=nl firld, readonly:
br.select_form(nr=0)
# overwrite, enables to mof read only form fields, typically hidden
br.form.set_all_readonly(False)
br.form['hl']='fr'
br.submit()

# check forms again to see if lang changed
print('\npage with different language: ')
for form in br.forms():
    print(form)
