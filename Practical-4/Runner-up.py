## Aim:- Find Runner-up From Given list.
## Student_Name:- Darshan Shah
## Student_ID:- 20CS077

if __name__ == '__main__':
    k = int(input('Insert size: '))
    position_arr = map(int, input('Scores are: ').split())
    print(sorted(list(set(position_arr)))[-2])
