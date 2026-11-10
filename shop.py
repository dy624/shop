# 쇼핑몰 장바구니 프로그램

# 쇼핑몰 메뉴 출력
print("=" *58)
print("1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
print("=" *58)

# 상품 클래스 생성 (상품의 이름, 가격, 재고 관리)
class Product():

    # 클래스 변수: 상품 번호를 자동으로 부여하기 위한 카운터
    counter = 0

    # 생성자: 상품 객체를 생성할 때 이름, 가격, 재고 초기화
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

        # 상품 객체가 생성될 때마다 번호를 1씩 증가
        Product.counter += 1

        # 증가한 번호를 해당 상품의 번호로 저장
        self.number = Product.counter

    # __str__: 상품 객체를 출력할 때 보여줄 문자열 설정
    def __str__(self):

        # 조건문: 재고가 0이면 품절 표시
        if self.stock == 0:
            return f"{self.number}. {self.name} {self.price:,}원 재고: (품절)"
        else:
            # 재고가 있으면 상품 정보와 재고 수량 출력
            return f"{self.number}. {self.name} {self.price:,}원 재고: {self.stock}개"


# Product 클래스를 이용해 상품 객체 5개 생성
item_a = Product("무선이어폰", 89_000, 3)
item_b = Product("텀블러", 15_000, 10)
item_c = Product("보조배터리",32_000, 5)
item_d = Product("마우스패드",9_000, 0)
item_e = Product("USB허브",18_000, 4)

# 리스트: 생성한 상품 객체 5개를 하나로 묶어 관리
products = [item_a, item_b, item_c, item_d, item_e]

# 빈 리스트 생성: 장바구니에 상품과 수량을 저장할 공간
cart = []

# while True: 사용자가 종료할 때까지 메뉴 반복
while True:

    # input(): 사용자에게 메뉴 번호 입력받기
    choice = input("선택: ")

    # q를 입력하면 break로 반복문 종료
    if choice == "q":
        print("쇼핑 이제그만...")
        break

    # 1번: 상품 목록 조회
    if choice == "1":

        # for문: 상품 리스트에 있는 객체를 하나씩 출력
        for product in products:
            print(product)

    # 2번: 장바구니에 상품 담기
    if choice == "2":

        # 담을 상품 번호 입력받기
        product_number = input("담을 상품을 골라주세요: ")

        # isdecimal(): 숫자 입력 확인
        # len(): 상품 개수 확인
        # 잘못된 번호면 continue로 다시 메뉴 선택
        if not product_number.isdecimal() or not 1 <= int(product_number) <= len(products):
            print("번호 잘보세유")
            continue

        # 입력한 번호에 해당하는 상품 객체 선택
        # 리스트 인덱스는 0부터 시작하므로 -1 사용
        selected_product = products[int(product_number) - 1]

        # 선택한 상품의 재고가 0이면 품절 처리
        if selected_product.stock == 0:
            print("품절 입니다.")
            continue

        # 구매할 수량 입력받기
        quantity = input("수량: ")

        # 숫자가 아니거나 0 이하인 수량은 입력 거부
        if not quantity.isdecimal() or int(quantity) <= 0:
            print("1 이상의 숫자를 입력해주세요.")
            continue

        # 입력받은 문자열을 정수형으로 변환
        quantity = int(quantity)

        # 구매 수량이 상품 재고보다 많으면 담지 않음
        if quantity > selected_product.stock:
            print("재고가 부족합니다.")
            continue

        # for문: 장바구니에 같은 상품이 이미 있는지 확인
        for existing_item in cart:

            # 딕셔너리의 product 값과 선택한 상품 비교
            if existing_item["product"] == selected_product:

                # 기존 수량 + 추가 수량이 재고를 초과하는지 확인
                if existing_item["quantity"] + quantity > selected_product.stock:
                    print("재고가 부족합니다.")

                else:
                    # += 연산자: 기존 수량에 새 수량 추가
                    existing_item["quantity"] += quantity
                    print(f"총 {existing_item['quantity']}개 담았습니다.")

                # 같은 상품을 찾았으므로 반복문 종료
                break

        # for...else: 같은 상품을 찾지 못했을 때 실행
        else:

            # append(): 딕셔너리로 상품과 수량을 함께 저장
            cart.append({"product": selected_product, "quantity": quantity})
            print(f"{selected_product.name} {quantity}개 담았습니다.")

    # 3번: 장바구니에서 상품 빼기
    if choice == "3":

        # 제거할 상품 번호 입력받기
        product_number = input("뺄 상품 번호를 골라주세요: ")
        