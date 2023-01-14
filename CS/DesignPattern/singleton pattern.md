# 싱글톤 패턴

**하나의 클래스에 오직 하나의 인스턴스

**주로 데이터베이스 연결 모듈에 사용

**하나의 인스턴스를 다른 모듈들이 공유

**중간에 의존성 주입자가 간접적으로 의존성 주입

---

**인스턴스 생성 비용 감소

**모듈 교체, 테스팅, 마이그레이션 수월

**일관된 의존성 방향, 모듈 간 관계 명확

---

**의존성이 높음

**각 테스트마다 독립적인 인스턴스가 필요한 단위 테스트에 어려움

**모듈들이 분리 => 클래스 수 증가 => 복잡 + 런타임 페널티

```java
class Singleton {
    private static class SingleInstance {
        private static final Singleton instance = new Singleton();
    }
    public static Singleton getInstance() {
        return SingleInstance.instance;
    }
}

public class Main {
    public static void main(String[] args) {
        Singleton a = Singleton.getInstance();
        Singleton b = Singleton.getInstance();

        // hashcode는 객체를 식별하는 Integer 값
        System.out.println(a.hashCode());
        System.out.println(b.hashCode());
        System.out.println(a==b);
    }
}

/* 출력 결과
1784662007
1784662007
true
*/
```

##### 데이터베이스 연결 모듈에 사용되는 싱글톤 패턴
```javascript
const URL = 'http://localhost:8080
const connection = url => ({"url : url})
class DB {
    constructor(url) {
        if(!DB.instance) {
            DB.instance = connection(url)
        }
        return DB.instance
    }
    connect() {
        return this.instance
    }
}
const a = new DB(url)
const b = new DB(url)
console.log(a==b)
```
