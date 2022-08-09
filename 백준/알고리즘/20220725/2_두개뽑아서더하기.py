# # https://school.programmers.co.kr/learn/courses/30/lessons/68644
# def solution(numbers):
#     answer = []
#     return answer
#     for i in range(len(numbers)):
#         for j in range()

        

# print(solution([2, 1, 3, 4, 1]))
# print(solution([5, 0, 2, 7]))

def solution(numbers):
    # 결과를 담을 리스트 박스
    answer = []

    # 길이만큼 반복
    for i in range(len(numbers)):
        # 길이만큼 반복하는데 i 다음의 수부터 시작
        for j in range(i+1, len(numbers)):
            # 두 수를 더한 값이 answer 안에 없다면
            if numbers[i] + numbers[j] not in answer:
                # 더한 값을 추가
                answer.append(numbers[i] + numbers[j])

    # 오름차순으로 정렬
    answer.sort()

    return answer
