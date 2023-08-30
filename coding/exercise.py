n = int(input())

student_name_result = {}
test_name_result = {}
for i in range(n):
    name_and_tests = input().split()

    name = name_and_tests[0]
    student_name_result[name] = []
    print(student_name_result)
"""
    for test in name_and_tests[1:]:
        test_name, result = test.split(":")
        result = float(result)
        student_name_result[name].append(result)

        if test_name in test_name_result:
            test_name_result[test_name].append(result)
        else:
            test_name_result[test_name] = [result]

        # print(test_name, result)

for key in sorted(student_name_result.keys()):
    results = student_name_result[key]
    print(key, sum(results) / len(results))

for key in sorted(test_name_result.keys()):
    results = test_name_result[key]
    print(key, sum(results) / len(results))
"""
