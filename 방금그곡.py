def changecode(code):
    code = code.replace("C#", "c")
    code = code.replace("D#", "d")
    code = code.replace("F#", "f")
    code = code.replace("G#", "g")
    code = code.replace("A#", "a")

    return code


def solution(m, musicinfos):
    save_song = []  # 재생시간, 재생 곡
    m = changecode(m)

    # musicinfos에서 시간을 이용해서 몇분이나 재생되었는지 구해야함
    for musicinfo in musicinfos:
        start, end, song, melody = musicinfo.split(",")

        start_hour, start_min = map(int, start.split(":"))
        end_hour, end_min = map(int, end.split(":"))

        song_min = (end_hour - start_hour) * 60
        song_min = song_min + (end_min - start_min)

        melody = changecode(melody)

        # 몇분이나 재생되었는지를 이용해서 멜로디를 이어붙여줌
        if len(melody) < song_min:
            melody = melody * (song_min // len(melody) + 1)

        full_melody = melody[:song_min]

        # m과 재생된 멜로디를 비교해서 일치하면 그 곳이 내가 찾는 그곡
        if m in full_melody:
            # 처음에는 없으면 무조건 넣어줌
            if save_song == []:
                save_song.append(song_min)
                save_song.append(song)

            # 일치하는게 여러개면 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환.
            # 재생 시간도 같으면 먼저 입력된 음악 제목 반환
            elif save_song and save_song[0] < song_min:
                save_song[0] = song_min
                save_song[1] = song

    # 찾는게 없다면 ''을 반환
    if save_song == []:
        return "(None)"
    else:
        return save_song[1]