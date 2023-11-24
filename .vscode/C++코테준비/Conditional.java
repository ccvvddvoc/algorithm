import java.util.Scanner;

public class Conditional {
    void login() {
        Scanner scan = new Scanner(System.in); // 입력을 받기 위한 Scanner 객체 생성

        System.out.print("## 아이디를 입력하세요 : ");
        String uname = scan.next(); // scanner를 통해 입력받음

        System.out.print("# 비밀번호를 입력하세요 : ");
        String pwd = scan.next();

        if (uname.equals("hong") && pwd.equals("1234")) {
            System.out.println("인증 확인!! -> 로그인 성공");
        }
        else {
            System.out.println("아이디 혹은 비밀번호가 잘못되었습니다!");
        }
    }
    void check() {
        int cnt = 10;
        String msg = cnt > 0 ? "새로운 쪽지가 있다!" : "새로운 쪽지가 없다";
        System.out.println(msg);
    }

    public static void main(String[] args) {
        Conditional con = new Conditional();

        while(true) {
            System.out.printf("# 메뉴를 선택하세요 (1:로그인, 2:쪽지확인, x:종료) ==>");
            Scanner scan = new Scanner(System.in);
            String sel = scan.next();

            switch(sel) {
                case "1" : con.login(); break;
                case "2" : con.check(); break;
                case "x" : System.exit(0); // System.exit(0) : 프로그램 종료
                default : System.out.println("잘못된 입력입니다.!!");
            }
        }
    }
}
