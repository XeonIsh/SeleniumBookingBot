from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='BRL')
        bot.select_place_to_go('Fernando de Noronha')
        bot.select_dates(check_in_date='2022-02-12',
                         check_out_date='2022-02-20')
        bot.select_adults(1)
        bot.click_search()
        bot.apply_filtrations()
        bot.report_results()


except Exception as e:
    if 'in PATH' in str(e):
        print(
            'Voce esta tentando rodar o bot atraves de uma CLI \n'
            'Por favor adicione: to path your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;F:path-do-folder \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
