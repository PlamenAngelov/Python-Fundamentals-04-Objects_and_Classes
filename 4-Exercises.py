class Exercises:
    def __init__(self, topic, course_name, judge_contest_link, problem_list):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problem_list = problem_list

data = input()
j = 0
ex_list = []

while data != "go go go":
    j += 1
    temp_list = list(map(str,data.split(" -> ")))
    temp_problem_list = list(map(str, temp_list[3].split(", ")))
    ex_list.append(Exercises(temp_list[0], temp_list[1], temp_list[2], temp_problem_list))

    data = input()


for i in range(0, len(ex_list)):
    print(f"Exercises: {ex_list[i].topic}")
    print(f"Problems for exercises and homework for the \"{ex_list[i].course_name}\" course @ SoftUni.")
    print(f"Check your solutions here: {ex_list[i].judge_contest_link}")
    for k in range(0, len(ex_list[i].problem_list)):
        print(f"{k+1}. {ex_list[i].problem_list[k]}")
