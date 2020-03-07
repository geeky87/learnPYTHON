def solution(S):
    Dict = dict((x.strip(), y.strip()) for x, y in (element.split(' ') for element in S.splitlines()))
    print(Dict)

    resultDict = {'music': '', 'images': '', 'movies': '', 'other': ''}

    music = 0
    images = 0
    movies = 0
    other = 0

    for key in Dict:
        size = Dict[key]
        if key in ('mp3', 'aac', 'flac'):
            music += int(size[0:-1])

        if key in ('jpg', 'bmp', 'gif'):
            images += int(size[0:-1])

        if key in ('mp4', 'avi', 'mkv'):
            movies += int(size[0:-1])

        if key in ('7z', 'txt', 'zip'):
            other += int(size[0:-1])

    resultDict['music'] = str(music) + 'b'
    resultDict['images'] = str(images) + 'b'
    resultDict['movies'] = str(movies) + 'b'
    resultDict['other'] = str(other) + 'b'

    return str(resultDict)

S= """"my.song.mp3 11b
greatSong.flac 1000b
not3.txt 5b
video.mp4 200b
game.exe 100b
mov!e.mkv 10000b"""

print(solution(S))
