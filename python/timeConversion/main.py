def timeConversion(time):
    periodDay = time[-2:]
    convertedTime = time[:-2].split(':')
 
    if periodDay == 'AM' and convertedTime[0] == '12':
        convertedTime[0] = '00'
    
    elif periodDay == 'PM' and convertedTime[0] != '12':
        convertedTime[0] = str(int(convertedTime[0]) + 12)

    result = ':'.join(convertedTime)
    return result

if __name__ == '__main__':
    time = '07:05:45PM'
    time = '12:00:00PM'
    result = timeConversion(time)
    print(result)