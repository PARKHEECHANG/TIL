# 팩토리 패턴

**객체 사용 코드에서 객체 생성 부분을 분리 => 추상화

**상위 클래스에서 틀을 결정, 하위 클래스에서 구체적인 객체 생성 내용 결정

---

**상위 클래스와 하위 클래스의 분리로 유연성 확보

**상위 클래스에서는 하위 클래스 객체 생성 내용을 알 필요가 없음

**리팩터링시 한 곳만 유지 보수 가능


```java
abstract class Car {
    public abstract String getModel();

    @Override
    public String toString() {
        return "model is " + this.getModel();
    }
} // Car

class CarFactory {

    public static Car getCar(String type, String model) {
        // main에서 전달받은 타입에 따라 다른 객체 생성
        if ("Sedan".equalsIgnoreCase(type)) {
            return new Sedan(model);
        } else if ("SUV".equalsIgnoreCase(type)) {
            return new SUV(model);
        }
        return null;
    }
} // CarFactory
// 상위 클래스(CarFactory)에서 인스턴스를 생성하지 않음
// 상위 클래스(CarFactory)에서 static 정적 메서드로 호출 => 메모리 절약, 자유로운 함수 정의

class Sedan extends Car {
    private String model;

    public Sedan(String model) {
        this.model = model;
    }

    @Override
    public String getModel() {
        return this.model;
    }
} // Sedan

class SUV extends Car {
    private String model;

    public SUV(String model) {
        this.model = model;
    }

    @Override
    public String getModel() {
        return this.model;
    }
} // SUV

public class Main {
    public static void main(String[] args) throws Exception {
        // 하위 클래스(Sedan||SUV)에서 생성한 것을 상위 클래스에 주입 (의존성 주입)
        Car sedan = CarFactory.getCar("Sedan", "SD-001");
        Car suv = CarFactory.getCar("SUV", "SV-002");
        System.out.println("sedan :: " + sedan);
        System.out.println("suv :: " + suv);
    }
} // Main

/* 출력 결과
sedan :: model is SD-001
suv :: model is SV-002
*/

```
