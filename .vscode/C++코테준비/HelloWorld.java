
public class HelloWorld {

    // 메서드
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }

    // 자료형
    // - 정수형 : byte, char, short, int, long
    // - 실수형 : float, double
    // - 논리형 : boolean
    
    // 변수 선언    
    int num1 = 10;
    String msg = "Hello";
    char c1 = 'A';
    double num3 = 3.14;
    boolean result = true;

    // 멤버 변수 : 클래스부에 선언된 변수들로 객체의 속성 (인스턴스 변수, 클래스 변수로 구분됨)
    // 인스턴스 변수 : 클래스가 인스턴스될 때 초기화되는 변수, 인스턴스를 통해서만 접근가능
    // 매개 변수 : 메서드 내에서 지역변수처럼 사용
    // 지역 변수 : 메서드 내에서 선언된 변수
    // 클래스 변수 : static으로 선언된 변수 [ 클래스이름.변수명 ]으로 사용가능, main() 메서드에서 참조 가능
    
}