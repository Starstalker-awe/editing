import os

join=lambda *a:os.path.join(os.getcwd(), *a)

def main():
    FILES = os.listdir(os.path.join(os.getcwd(), 'Good for BG'))
    try:
        for ind, fil in enumerate(FILES):
            os.rename(join(fil), f'{ind+1:04}.{fil.split(".")[-1]}')
    except Exception:
        return False
    print('Renamed all files')
    return True

if __name__ == '__main__':
    main()
