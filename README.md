QUERYSET
CRUD
일반적으로 기존 객체에 자주 영향을 미치는 메서드는 자신(self)을 리턴하지 않도록 하는 것이 Python에서 좋은 사례로 간주된다. 
만약 객체로 접근한 메서드가 자신(self)를 리턴하게 되면 계속 이어서 코드를 작성하게 되고(메서드 체인), 
이 때 특정 버그나 문제가 발생했을 때 찾기 힘들 뿐더러 전체 기능에 문제가 될수 도 있다.

생성(CREATE)
create()
  - 모델명.object.create()
  - 전달한 값으로 초기화한 뒤 새로운 객체를 생성하고 테이블에 저장된다.
save()
  - 객체명.save()
  - 전달한 값으로 테이블에 저장된다.
bulk_create()
  - 모델명.objects.bulk_craete([])
  - 전달한 list로 초기화 된 여러 객체를 생성하고 테이블에 저장한다.
  - 생성된 객체들은 list 타입으로 리턴 된다.
get_or_create()
  - 모델명.objects.get_or_create()
  - 테이블에 객체가 있으면 가져오고, 없으면 테이블에 저장되고 만들어진 객체를 리턴한다.
  - 추가된 정보는 defaults={}로 전달해서 create일 경우 사용된다.
  - 두 칸짜리 tuple 타입으로 리턴되며, 첫번째는 객체, 두번째는 생성여부인 bool타입이 담긴다.

조회(READ)
get()
  - 모델명.objects.get()
  - 테이블에서 조건에 맞는 한 개의 객체를 조회한다.
  - 조회된 객체가 없으면 DoseNotExist, 2개 이상이면 MultipleObjectsReturnd 가 발생하기 때문에 초회할 값이 1개일 때만 사용한다.
all()
  - 모델명.objects.all()
  - 테이블에서 전체 정보를 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
    QuerySet이란, 쿼리의 결과를 전달받은 모델 객체의 목록이다.
  - list와 구조는 같지만, 파이썬 기본 자료구조가 아니기 때문에 형변환이나 serializer가 필요하다.
values()
  - 테이블에서 전체 정보를 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체가 dict타입으로 들어있다
  - 필드 이름을 전달하면 원하는 필드 정보만 가져올 수 있다.
  - 참조중인 테이블의 필드를 가져오기 위해서는 '[참조중인 객체명]\_\_[필드명]' 으로 작성한다.
values_list()
  - 테이블에서 전체 정보를 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체가 tuple 타입으로 들어있다.
  - 모든 필드를 순서대로 가져오고 싶을때 인덱스로 접근해서 가져올 수 있다.
filter()
  - 조건에 맞는 행을 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
  - 조건에 맞는 결과가 한개도 없을 경우 비어있는 QuerySet이 리턴된다.
exists()
  - filter()와 함께 사용해서 filter 조건에 맞는 데이터가 있는지 조회한다.
exclude()
  - 조건에 맞지 않는 행을 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
  - 조건에 맞는 결과가 한개도 없을 경우 비어있는 QuerySet이 리턴된다.
AND, OR
  - 모델명.objects.filter() & 모델명.objects.filter()
  - 모델명.objects.filter() | 모델명.objects.filter()

  - 모델명.objects.filter(key=value, key=value)
  - 모델명.objects.filter(Q(key=value) | Q(key=value))
first(), last()
  - 모델명.objects.filter().first()
  - 조건에 맞는 QuerySet 결과 중 첫 번째 객체만 가져오기

  - 모델명.objects.filter().last()
  - 조건에 맞는 QuerySet 결과 중 마지막 객체만 가져오기
count()
  - 모델명.objects.filter().count()
  - 조건에 맞는 결과의 총 개수를 리턴한다.
order_by()
  - 모델명.objects.order_by("필드명")
  - 모델명.objects.order_by("-필드명")

  - 각 오름차순과 내림차순 정렬이다.
annotate()
  - 모델명.objects.annotate().values()
  - 결과 테이블에서 컬럼을 다른 이름으로 사용하거나 다른 연산을 수행한 뒤 새로운 이름을 만들어낸다.
aggregate()
  - QuerySet객체.aggregate(key=집계함수('필드명'))
  - QuerySet객체.values("묶을 필드명").annotate(key=집계함수('필드명'))

  - 각 전체 대상과 그룹 대상이다.

수정(UPDATE)
save()
  - 존재하는 객체를 조회한 뒤 전체 필드를 수정하고 혹시 없는 객체라면 추가한다.
  - 수정 목적으로 사용할 때에는 어던 필드가 수정되엇는 지를 정확히 알려주어야 한다
  - save(ipdate_fields=['',...])와 같이 수정할 컬럼명을 작성해서 전달한다.
update()
  - QuerySet객체로 사용할 수 있으며, 해당 객체들을 수정하고 수정된 행의 수를 리턴한다.

삭제(DELETE)
delete()
    - 객체.delete()로 사용하며 조건에 맞는 행을 삭제한다
    - get(), filter(), all()과 같이 사용한다.



REST
  - Representational State Transfer
  - 언제 어디서든 누구든 서버에 요청을 보낼때 URI만으로도 
    데이터 또는 행위(CRUD) 상태를 이해할 수 있도록 설계하는 규칙
소문자로 작성한다.

대문자로 작성 시 문제가 발생할 수 있기 때문에 소문자로 작성한다.
언더바 대신 하이픈을 사용한다.

가독성을 높이기 위해 하이픈으로 구분하는 것이 좋다.
URI 마지막에 슬래시를 작성하지 않는다.

마지막에 작성하는 슬래시는 의미가 없다
계층 관게 표현시 슬래시 구분자로 사용한다.

계층 관계(포함 관계)에서는 슬래시로 구분해준다.
파일 확장자는 포함시키지 않는다.

파일 확장자는 URI로 표현하지 않고 Header의 Content-Type을 사용하여 body의 내용을 처리하도록 설계한다.
데이터를 대표할 때에는 명사를 사용하고, 상태를 대표할 때에는 동사를 사용한다.

http://www.app.com/members/get/1 (X)
http://www.app.com/members/delete/1 (O)
URI에 사용되는 영어 단어는 복수로 시작한다.
