3 5
Ballad
Rock
Rock
Ballad
Ballad

#  => 3
    

def how_much_ballad(idx):
    song_str = ''
    for i in range(idx, idx + song_num):
        song_str += themes[i]
    return song_str.count('Ballad')

if __name__ == "__main__":
    song_num, tracks = map(int, input().split())
    themes = [input().split()]
#     for _ in range(tracks):
#     themes.append(input())
    max_ballad_idx = 0
    max_ballad_num = how_much_ballad(0)
    for idx in range(0, tracks - song_num + 1):
         if max_ballad_num < how_much_ballad(idx):
                max_ballad_idx = idx
                max_ballad_num = how_much_ballad(idx)
    if max_ballad_num == 0:
        print(0)
    else:
        print(idx + 1)
        