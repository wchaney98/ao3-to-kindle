from nicegui import ui
import methods

smiley = '''
    <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <circle cx="100" cy="100" r="78" fill="#ffde34" stroke="black" stroke-width="3" />
        <circle cx="80" cy="85" r="8" />
        <circle cx="120" cy="85" r="8" />
        <path d="m60,120 C75,150 125,150 140,120" style="fill:none; stroke:black; stroke-width:8; stroke-linecap:round" />
    </svg>
'''

downloader = methods.AO3_Downloader() 

def parse_urls(textarea_input):
    downloader.clear_urls()
    for url in textarea_input.value.split('\n'):
        downloader.add_url(url)\

def click_validate_urls():
    success = downloader.validate_urls()
    if success:
        print("success")
    else:
        dialog.open()
        

with ui.dialog() as dialog, ui.card():
            ui.label('Validation failed.')
            ui.button('OK', on_click=dialog.close)

ui.dark_mode().enable()
    
ui.label('Ao3-To-Kindle!').classes('justify-center')#.tailwind.font_size('5xl').text_align('center').align_content('stretch')

with ui.column().classes('fixed-center'):
    
    with ui.card():
        with ui.row().classes('w-full'):
            ui.input('Ao3 Username')
            ui.input('Ao3 Password', password=True)
        ui.button('Login', on_click=downloader.login).classes('w-full')

    ui.separator()
    with ui.card().classes('w-full'):
        with ui.column().classes('w-full'):
            ui.textarea(label='URLs', placeholder='Put an Ao3 URL, 1 URL per line.', on_change=parse_urls).classes('w-full')
            ui.button('Validate urls', on_click=click_validate_urls).classes('w-full')
            ui.label("Validated!").bind_visibility_from(downloader, "urls_validated").tailwind.text_color('green-500')

ui.run(title="Ao3-to-Kindle", favicon=smiley)
