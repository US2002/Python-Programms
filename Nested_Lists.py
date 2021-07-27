def Nested_List():
    marksheet = []
    second_lowest_names = []
    scoresheet = set()

    for _ in range(0, int(input())):
        names = input()
        scores = float(input())
        marksheet.append([names, scores])
        scoresheet.add(scores)

    second_lowest = sorted(scoresheet)[1]

    for names, score in marksheet:
        if score == second_lowest:
            second_lowest_names.append(names)

    for names in sorted(second_lowest_names):
        print(names, end='\n')


Nested_List()
