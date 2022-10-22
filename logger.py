from datetime import datetime as dt
def write_log(data):
    time = dt.now().strftime('%d.%m.%Y - %H:%M:%S')
    with open('log_info.csv', 'a') as file:
        file.write('{} - Operations - {}\n'
                    .format(time, data))