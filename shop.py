# 쇼핑몰 장바구니 프로그램

# 쇼핑몰 메뉴 출력
# print("=" *58)
# print("1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
# print("=" *58)

# 상품 클래스 생성 (상품의 이름, 가격, 재고 관리)
class Product():
  
    counter = 0
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
               
        Product.counter += 1

        self.number = Product.counter
    def __str__(self):
        if self.stock == 0:
            return f"{self.number}. {self.name} {self.price:,}원 재고: (품절)"
        else:
            return f"{self.number}. {self.name} {self.price:,}원 재고: {self.stock}개"

item_a = Product("무선이어폰", 89_000, 3)
item_b = Product("텀블러", 15_000, 10)
item_c = Product("보조배터리",32_000, 5)
item_d = Product("마우스패드",9_000, 0)
item_e = Product("USB허브",18_000, 4)


products = [item_a, item_b, item_c, item_d, item_e]


cart = []
# 부모
class Discount():
    def discount_amount(self, total):
        return 0
# 자슥
class RateDiscount(Discount):
    def __init__(self, rate, max_amount):
        self.rate = rate
        self.max_amount = max_amount 
    
    def discount_amount(self, total):
        discount = total * self.rate     
        if discount > self.max_amount:
            return self.max_amount 
        else:
            return int(discount)



class FixedDiscount(Discount):
    def __init__(self, amount, min_total):
        self.amount = amount
        self.min_total = min_total

    def discount_amount(self, total):
        if total >= self.min_total:
            return self.amount
        else:
            return 0
    
coupon_a = Discount()
coupon_b = RateDiscount(0.1, 5000)
coupon_c = FixedDiscount(3000, 20000)
coupon = coupon_a

while True:
    print("=" *58)
    print("1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("=" *58)
    choice = input("선택: ")
 
    if choice == "q":
        print("쇼핑 이제그만...")
        break

    # 1번: 상품 목록 조회
    if choice == "1":
        for product in products:
            print(product)
    

    # 2번: 장바구니에 상품 담기
    if choice == "2":
               
        product_number = input("담을 상품을 골라주세요: ")
            
        if not product_number.isdecimal() or not 1 <= int(product_number) <= len(products):
            print("번호 잘보세유")
            continue
        selected_product = products[int(product_number) - 1]
               
        if selected_product.stock == 0:
            print("품절 입니다.")
            continue
                    
        quantity = input("수량: ")
               
        if not quantity.isdecimal() or int(quantity) <= 0:
            print("1 이상의 숫자를 입력해주세요.")
            continue

        quantity = int(quantity)

        if quantity > selected_product.stock:
            print("재고가 부족합니다.")
            continue

        for existing_item in cart:
            if existing_item["product"] == selected_product:
                if existing_item["quantity"] + quantity > selected_product.stock:
                    print("재고가 부족합니다.")
                    break

                else:
                    existing_item["quantity"] += quantity
                    print(f"{existing_item["product"].name} {existing_item['quantity']}개 담았습니다.")
                    break
                            
        else:
            cart.append({"product": selected_product, "quantity": quantity})
            print(f"{selected_product.name} {quantity}개 담았습니다.")

    # 3번: 장바구니에서 상품 빼기
    if choice == "3":
        product_number = input("뺄 상품 번호를 골라주세요: ")

    # 번호 확인
        if not product_number.isdecimal() or not 1 <= int(product_number) <= len(products):
            print("상품 번호중 그런 번호는 없습니다.")
            continue
            
    # 선택한 상품 찾기
        selected_product = products [int(product_number) -1]
        for existing_item in cart:
            if existing_item["product"] == selected_product:
                cart.remove(existing_item)
                print("상품을 뺏습니다.")
                break
        else:
            print("장바구니에 없는 상품입니다.")
    # 장바구니 확인
    if choice == "4":
        if not cart:
            print("장바구니에 담은 물건이 없습니다.") 
        else:
            total = 0
        
            print("-" * 30)
            for existing_item in cart:
                item_total = existing_item["product"].price * existing_item['quantity']
                total += item_total
                print(f"{existing_item["product"].name} x {existing_item['quantity']}개 {item_total:,}원")
            print("-" * 30)
            print(f"상품 합계: {total:,}원")
            
    # 쿠폰
    if choice == "5":
        print("1. 쿠폰없음")
        print("2. 10% 할인 최대 5,000원")
        print("3. 3,000원 할인 20,000원 이상 구매 시")
        coupon_number =  input("쿠폰 번호:" )

        if coupon_number == "1":
            coupon = coupon_a
        elif coupon_number == "2":
            coupon = coupon_b
        elif coupon_number == "3":
            coupon = coupon_c

        if not coupon_number.isdecimal() or not 1 <= int(coupon_number) <= 3:
            print("번호좀 잘 눌러봐..")
            continue
