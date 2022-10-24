try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 수를 입력하세요 : "))
    num2 = int(input("두번째 수를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10 :
        raise ValueError
    print(f'{num1} / {num2} = {float(num1 / num2)}')

    # nums = []
    # nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    # nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    # print(f'{nums[0]} / {nums[1]} = {nums[0]/nums[1]}')
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다. ")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)