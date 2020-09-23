if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for x in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for s,y in student_marks.items():
        if s == query_name:
            result=0
            for u in y:
                result+=u
            result /=3
            foo = format(result, '.2f')
            print(foo)