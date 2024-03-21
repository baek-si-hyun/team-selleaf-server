# QUERYSET

## CRUD

####
    일반적으로 기존 객체에 자주 영향을 미치는 메서드는 자신(self)을 리턴하지 않도록 하는 것이 Python에서 좋은 사례로 간주된다. 
    만약 객체로 접근한 메서드가 자신(self)를 리턴하게 되면 계속 이어서 코드를 작성하게 되고(메서드 체인), 
    이 때 특정 버그나 문제가 발생했을 때 찾기 힘들 뿐더러 전체 기능에 문제가 될수 도 있다.

<br/>

### 생성(CREATE)
#### create()
```  
  - 모델명.object.create()
  - 전달한 값으로 초기화한 뒤 새로운 객체를 생성하고 테이블에 저장된다.
```
#### save()
```  
  - 객체명.save()
  - 전달한 값으로 테이블에 저장된다.
```  
#### bulk_create()
```  
  - 모델명.objects.bulk_craete([])
  - 전달한 list로 초기화 된 여러 객체를 생성하고 테이블에 저장한다.
  - 생성된 객체들은 list 타입으로 리턴 된다.
```  
#### get_or_create()
```  
  - 모델명.objects.get_or_create()
  - 테이블에 객체가 있으면 가져오고, 없으면 테이블에 저장되고 만들어진 객체를 리턴한다.
  - 추가된 정보는 defaults={}로 전달해서 create일 경우 사용된다.
  - 두 칸짜리 tuple 타입으로 리턴되며, 첫번째는 객체, 두번째는 생성여부인 bool타입이 담긴다.
```  
<br/>

### 조회(READ)
#### get()
```  
  - 모델명.objects.get()
  - 테이블에서 조건에 맞는 한 개의 객체를 조회한다.
  - 조회된 객체가 없으면 DoseNotExist, 2개 이상이면 MultipleObjectsReturnd 가 발생하기 때문에 초회할 값이 1개일 때만 사용한다.
```  
#### all()
```  
  - 모델명.objects.all()
  - 테이블에서 전체 정보를 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
    QuerySet이란, 쿼리의 결과를 전달받은 모델 객체의 목록이다.
  - list와 구조는 같지만, 파이썬 기본 자료구조가 아니기 때문에 형변환이나 serializer가 필요하다.
```  
#### values()
```  
  - 테이블에서 전체 정보를 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체가 dict타입으로 들어있다
  - 필드 이름을 전달하면 원하는 필드 정보만 가져올 수 있다.
  - 참조중인 테이블의 필드를 가져오기 위해서는 '[참조중인 객체명]\_\_[필드명]' 으로 작성한다.
```  
#### values_list()
```  
  - 테이블에서 전체 정보를 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체가 tuple 타입으로 들어있다.
  - 모든 필드를 순서대로 가져오고 싶을때 인덱스로 접근해서 가져올 수 있다.
```  
#### filter()
```  
  - 조건에 맞는 행을 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
  - 조건에 맞는 결과가 한개도 없을 경우 비어있는 QuerySet이 리턴된다.
```  
#### exists()
```  
  - filter()와 함께 사용해서 filter 조건에 맞는 데이터가 있는지 조회한다.
```  
#### exclude()
```  
  - 조건에 맞지 않는 행을 조회한다.
  - QuerySet 객체를 리턴하며, 조회된 객체들이 들어있다.
  - 조건에 맞는 결과가 한개도 없을 경우 비어있는 QuerySet이 리턴된다.
```  
#### AND, OR
```  
  - 모델명.objects.filter() & 모델명.objects.filter()
  - 모델명.objects.filter() | 모델명.objects.filter()

  - 모델명.objects.filter(key=value, key=value)
  - 모델명.objects.filter(Q(key=value) | Q(key=value))
```  
#### first(), last()
```  
  - 모델명.objects.filter().first()
  - 조건에 맞는 QuerySet 결과 중 첫 번째 객체만 가져오기

  - 모델명.objects.filter().last()
  - 조건에 맞는 QuerySet 결과 중 마지막 객체만 가져오기
```  
#### count()
```  
  - 모델명.objects.filter().count()
  - 조건에 맞는 결과의 총 개수를 리턴한다.
```  
#### order_by()
```  
  - 모델명.objects.order_by("필드명")
  - 모델명.objects.order_by("-필드명")

  - 각 오름차순과 내림차순 정렬이다.
```  
#### annotate()
```  
  - 모델명.objects.annotate().values()
  - 결과 테이블에서 컬럼을 다른 이름으로 사용하거나 다른 연산을 수행한 뒤 새로운 이름을 만들어낸다.
```  
#### aggregate()
```  
  - QuerySet객체.aggregate(key=집계함수('필드명'))
  - QuerySet객체.values("묶을 필드명").annotate(key=집계함수('필드명'))

  - 각 전체 대상과 그룹 대상이다.
```  
<br/>

### 수정(UPDATE)
#### save() 
```  
  - 존재하는 객체를 조회한 뒤 전체 필드를 수정하고 혹시 없는 객체라면 추가한다.
  - 수정 목적으로 사용할 때에는 어던 필드가 수정되엇는 지를 정확히 알려주어야 한다
  - save(ipdate_fields=['',...])와 같이 수정할 컬럼명을 작성해서 전달한다.
  ```  
#### update()
```  
  - QuerySet객체로 사용할 수 있으며, 해당 객체들을 수정하고 수정된 행의 수를 리턴한다.
```  
<br/>

### 삭제(DELETE)
#### delete()
```  
    - 객체.delete()로 사용하며 조건에 맞는 행을 삭제한다
    - get(), filter(), all()과 같이 사용한다.
```  
<br/><br/>

# REST
```
  - Representational State Transfer
  - 언제 어디서든 누구든 서버에 요청을 보낼때 URI만으로도 
    데이터 또는 행위(CRUD) 상태를 이해할 수 있도록 설계하는 규칙
```

1. 소문자로 작성한다.
    - 대문자로 작성 시 문제가 발생할 수 있기 때문에 소문자로 작성한다.

2. 언더바 대신 하이픈을 사용한다.
    - 가독성을 높이기 위해 하이픈으로 구분하는 것이 좋다.

3. URI 마지막에 슬래시를 작성하지 않는다.
    - 마지막에 작성하는 슬래시는 의미가 없다

4. 계층 관게 표현시 슬래시 구분자로 사용한다.
    - 계층 관계(포함 관계)에서는 슬래시로 구분해준다.

5. 파일 확장자는 포함시키지 않는다.
    - 파일 확장자는 URI로 표현하지 않고 Header의 Content-Type을 사용하여 body의 내용을 처리하도록 설계한다.
6. 데이터를 대표할 때에는 명사를 사용하고, 상태를 대표할 때에는 동사를 사용한다.
    - http://www.app.com/members/get/1 (X)
    - http://www.app.com/members/delete/1 (O)
7. URI에 사용되는 영어 단어는 복수로 시작한다.

<br/><br/>

# Model

- Django에서 models.Model이라는 추상화된 클래스를 사용하여 데이터베이스에 테이블을 정의 할 수 있다
- models.Model 을 상속받은 클래스로 구현할 수 있으며, 내부 클래스로 Meta 클래스를 선언할 수 있다.

## Model Convention

    모델 내 코드를 작성할 때 아래의 순서에 맞춰 작성하는 것을 권장한다.
    1. Constant for choices
    2. All databases Field
    3. Custom manager attributes
    4. class Meta
    5. def __str__()
    6. def save()
    7. def get_absolute_url()
    8. Any custom methods

### 1. Constant for choices

- DB에 저장할 값과 실제 화면에 보여지는 값이 다를 경우 미리 튜플 형태로 선언해 놓고 사용한다.

####

      CONSTANT = [
        ('DB 저장 값', '화면 출력 값'),
        ...
      ]

### 2. All databases Field

####

    ForeignKey(to, verbose_name, related_name, related_query_name, on_delete, null)
    OneToOneField(to, verbose_name, related_name, related_query_name, on_delete, null)
    ManyToManyField(to, verbose_name, related_name, related_query_name, on_delete, null)

    - related_name
      - 역참조가 필요한 다대다 또는 일대다 관계에서 유용하게 사용된다.
      - B필드에 a객체 선언 후 참조 시 b.a로 접근할 수 있으나
      - 역참조인 a.b로는 접근할 수 없다. A필드에는 b객체가 없기 때문이다.
      - _set객체를 사용하면 역참조가 가능하고 a.b_set으로 역참조가 가능하다.
      - 만약 _set객체의 이름을 다른 이름으로 사용하고자 할 때 바로 related_name을 사용한다.

- 문자열

  - 문자열 필드는 null=False로 하고 필수 요소가 아니라면 blank=True로 설정한다.
  - 이렇게 설정하는 이유는 null과 빈 값을 "null이거나 빈 문자일 경우 빈 값이다"라고 검사할 필요 없이 빈 문자열인지로만 판단할 수 있게 되기 때문이다.

  ####

      최대 길이 제한이 필요한 경우
      CharField(verbose_name, max_length, choices, blank, null, default)

      최대 길이 제한이 필요 없을 경우
      TextField(verbose_name, null=False, blank=True)

- 정수

  - max_length를 지정하지 않고 기본적으로 byte가 정해져있다.

  ####

      PositiveSmallIntegerField(verbose_name, choices, null, default)
      SmallIntegerField(verbose_name, choices, null, default)
      IntegerField(verbose_name, choices, null, default): 4byte
      BigIntegerField(verbose_name, choices, null, default)
      BooleanField(verbose_name, default): 1byte

- 날짜

####

- auto_now_add=True

  - 최초 한 번만 자동으로 필드 값을 현재 시간으로 설정한다.
  - 보통 등록 날짜 항목으로 사용된다.

- auto_now=True

  - 객체가 변경될 때마다 자동으로 필드 값을 현재 시간으로 수정한다.
  - 보통 수정된 날짜 항목으로 사용된다.
  - 하지만, save()를 사용해야 적용되고 update()를 사용하면 적용되지 않는다.
  - auto_now=True처럼 사용하고 싶다면, default=timezone.now을 사용하는 것이 올바르다.
  - ※ django.utils.timezone.now으로 설정한 뒤 update할 때 마다 그 때의 now로 넣어준다.

  ####

      DateField(verbose_name, null, default, auto_now_add, auto_now)
      TimeField(verbose_name, null, default, auto_now_add, auto_now)
      DateTimeField(verbose_name, null, default, auto_now_add, auto_now)

### 3. Custom manager attributes

- 데이터베이스와 상호작용하는 인터페이스(틀)이며 Model.object 속성을 통해 사용한다.
- Custom Manager와 Custop QuerySet을 통해 사용할 수 있으며,
  공통적으로 사용되는 쿼리를 공통 함수로 정의할 수 있고 싱제 동작을 숨길 수 있다.
<br/><br/>

### 4. class Meta

- Model클래스 안에 선언되는 내부 클래스이며, 모델에 대한 기본 설정들을 변경할 수 있다
- Meta 클래스가 작동하기 위해서는 정해진 속성과 속성값을 작성해야 하고, 이를 통해, Django를 훨씬 편하게 사용할 수 있다.

- 데이터 조회 시 정렬 방법 설정
  - ordering = ['필드명']
  - ordering = ['-필드명']
- 테이블 생성시 이름 설정
  - db_table = '테이블명'
- 테이블을 생성할 것인지 설정
  - abstract = False
<br/><br/>

### 5. def \_\_str\_\_()

- 객체 조회 시 원하는 데이터를 직접 눈으로 확인하고자 할 때 사용하며, 객체 출력시 자동으로 사용되는 메서드이다.
- 모델 필드 내에서 재정의하여 원하는 필드를 문자열로 리턴하면 앞으로 객체 출력 시 해당 값이 출력된다.
<br/><br/>

### 6. def save()

- 모델 클래스를 객체화한 뒤 save()를 사용하면 INSERT 또는 UPDATE 쿼리가 발생한다.
- 이는 Django ORM이 save()를 구현해놨기 때문이다.
- save() 사용시, INSERT 또는 UPDATE 쿼리 발생 외 다른 로직이 필요할 경우 재정의 할 수 있다.
- 하지만 재정의를 하면, 객체를 대량으로 생성하거나 수정할 때 동작하지 않는다.
<br/><br/>

### 7. def get_absolute_url()

- 모델에 대해서 상세보기(DetailView)를 제작한다면, redirect(모델 객체)를 통해
  자동으로 get_absolute_url()을 호출한다.
- 추가 혹은 수정 서비스 이후 상세보기 페이지로 이동하게 된다면,
  매번 redirect에 경로를 작성하지 않고 get_absolute_url()을 재정의해서 사용하는 것을 추천한다.
