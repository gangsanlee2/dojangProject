from fake2_tatanic.models import TitanicModel
from src.cmm.service.dataset import Dataset


class TitanicController(object):
    model = TitanicModel()

    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()

    def preprocess(self, train, test) -> object:  # 전처리
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)   # new_model : 프로토타입
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        # columns 편집과정
        # this = model.pclass_ordinal(this) 데이터 자체가 이미 오디널이다
        this = model.sex_nominal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_nominal(this)
        this = model.title_nominal(this)
        '''
        this = model.drop_features(this, 'PassengerId')
        this = model.drop_features(this, 'Name')
        this = model.drop_features(this, 'Sex')
        this = model.drop_features(this, '...')
        ... -> not pythonic
        for i in ['','','','', ... ]:
            model.drop_features(this, i) -> not pythonic
        '''
        this = model.drop_features(this, 'PassengerId', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin')
        return this

    def modeling(self, train, test) -> object:  # 모델생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this

    def learning(self, train, test):  # 기계학습
        this = self.modeling(train, test)
        accuracy = self.model.get_accuracy(this)
        print(f"랜덤포레스트분류기 알고리즘 정확도 : {accuracy}%")

    def submit(self):  # 배포
        pass

if __name__ == '__main__':
    c = TitanicController()
    this = c.modeling('train.csv','test.csv')
    print(this.train.columns)
    print(this.train.head())