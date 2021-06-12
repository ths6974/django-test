from dataclasses import dataclass

@dataclass  # 장고 데코레이터
class Dataset(object):

    context: str # 경로
    fname: str # 파일명
    train: object # train.csv 가 DF 로 전환된 객체
    test: object # test.csv 가 DF 로 전환된 객체
    id: str # 승객ID로 문제가 된다.
    label: str # 승객ID에 따른 생존여부로 답이된다.

    # 데이터를 읽고(getter = property) / 쓰기(setter) 기능을 추가한다.

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label
