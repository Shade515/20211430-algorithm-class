class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node

# 도서 정보 --------------------

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[{self.book_id}] {self.title} / {self.author} / {self.year}"

#단순 연결 리스트 ------------------------

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, book):
        """리스트 끝에 도서 추가"""
        new_node = Node(book)
        if self.isEmpty():
            self.head = new_node
        else:
            p = self.head
            while p.link is not None:
                p = p.link
            p.link = new_node

    def find_by_title(self, title):
        """책 제목으로 도서를 찾기"""
        p = self.head
        while p is not None:
            if p.data.title == title:
                return p.data
            p = p.link
        return None

    def find_pos_by_title(self, title):
        """책 제목을 기반으로 도서의 이전 노드 위치 반환"""
        if self.isEmpty():
            return None
        if self.head.data.title == title:
            return None  # 첫 번째 노드인 경우 이전 노드 없음
        p = self.head
        while p.link is not None:
            if p.link.data.title == title:
                return p
            p = p.link
        return None

    def find_by_id(self, book_id):
        """책 번호 중복 확인용"""
        p = self.head
        while p is not None:
            if p.data.book_id == book_id:
                return p.data
            p = p.link
        return None

    def delete_by_title(self, title):
        """책 제목으로 삭제"""
        if self.isEmpty():
            return False
        if self.head.data.title == title:
            self.head = self.head.link
            return True
        prev = self.find_pos_by_title(title)
        if prev is not None:
            prev.popNext()
            return True
        return False

    def display_all(self):
        """전체 도서 목록 출력"""
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        p = self.head
        while p is not None:
            print(p.data)
            p = p.link

#프로그램 실행-----------------

class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.books.find_by_id(book_id) is not None:
            print(" 오류: 중복된 책 번호입니다.")
            return
        book = Book(book_id, title, author, year)
        self.books.insert(book)
        print(f" '{title}' 도서가 성공적으로 추가되었습니다.")

    def remove_book(self, title):
        result = self.books.delete_by_title(title)
        if result:
            print(f" '{title}' 도서가 삭제되었습니다.")
        else:
            print(f" '{title}' 도서를 찾을 수 없습니다.")

    def search_book(self, title):
        book = self.books.find_by_title(title)
        if book:
            print(f" 조회 결과: {book}")
        else:
            print(f" '{title}' 도서를 찾을 수 없습니다.")

    def display_books(self):
        print("\n===== 전체 도서 목록 =====")
        self.books.display_all()

    def run(self):
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로)")
            print("3. 도서 조회 (책 제목으로)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")

            choice = input("메뉴를 선택하세요: ").strip()

            if choice == "1":
                try:
                    book_id = int(input("책 번호: "))
                    title = input("책 제목: ").strip()
                    author = input("저자: ").strip()
                    year = input("출판 연도: ").strip()
                    self.add_book(book_id, title, author, year)
                except ValueError:
                    print("책 번호는 숫자로 입력해야 합니다.")

            elif choice == "2":
                title = input("삭제할 책 제목: ").strip()
                self.remove_book(title)

            elif choice == "3":
                title = input("조회할 책 제목: ").strip()
                self.search_book(title)

            elif choice == "4":
                self.display_books()

            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~5 중에서 선택하세요.")


# 실행 ----------------

if __name__ == "__main__":
    manager = BookManagement()
    manager.run()


