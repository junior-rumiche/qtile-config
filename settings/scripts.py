import psutil


def cpu_percent():
    cpu = psutil.cpu_percent(1, True)
    media = 0
    for i in cpu:
        media += i
    
    return f"   {media/len(cpu)}% "

