#__init__.py 안에 코드를 쓰는 것은 단지 중간 점검 목적. 완성 후엔 빈 파일로 제출

from fake_tatanic.models import TitanicModel
from fake_tatanic.template import Plot
from fake_tatanic.views import TitanicController
from src.cmm.service.common import Common

if __name__ == '__main__':
    api = TitanicController()
    while True:
        menu = Common.menu(["종료","시각화","모델링","머신러닝","배포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_sex()
            plot.draw_pclass()
            plot.draw_embarked()
            model = TitanicModel()
        elif menu == "2":
            print(" ### 모델링 ### ")
            df = api.modeling('train.csv', 'test.csv')
        elif menu == "3":
            print(" ### 머신러닝 ### ")
            df = api.learning('train.csv', 'test.csv')
        elif menu == "4":
            print(" ### 배포 ### ")
            df = api.submit('train.csv', 'test.csv')
        else:
            print(" ### 해당 메뉴 없음 ### ")
