# 아래 클래스를 수정하시오.
class UserInfo:
    check = True

    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            name = input('이름을 입력하세요 : ')
            age = int(input('나이를 입력하세요 : '))
            self.user_data[name] = age
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
            UserInfo.check = False

    def display_user_info(self):
        if self.user_data and UserInfo.check:
            print(f"사용자 정보 :")
            name_age = list(self.user_data.items())
            print(f'이름 : {name_age[0][0]}')
            print(f'나이 : {name_age[0][1]}')


user = UserInfo()
user.get_user_info()
user.display_user_info()
