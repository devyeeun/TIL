# 코어자바스크립트(위키북스)


## 3장 - this

### this
this는 자바스크립트에서 가장 혼란스럽고 어려운 개념 중 하나이다.  
자바스크립트에서의 this는 어디서든 사용할 수 있다.  
this는 함수가 호출될 때마다 다르게 바인딩된다.(상황에 따라 this가 바라보는 대상이 달라진다.)

자바스크립트에서 this는 기본적으로 실행 컨텍스트가 생성될 때 함께 결정된다.
즉, **this는 함수를 호출할 때 결정된다!**
함수를 어떤 방식으로 호출하느냐에 따라 값이 달라지는 것.


#### 전역공간에서의 this
전역공간에서 this는 전역 객체를 가리킨다.  
브라우저에서는 window 객체가 전역 객체이므로 this는 window를 가리킨다.  
(전역 객체는 자바스크립트 런타임 환경에 따라 다른 이름과 정보를 지닌다.)

```javascript
console.log(this); // window
console.log(window); // window
console.log(this === window); // true
```

--- 
> ***참고***:   
> 전역변수를 선언하면 JS엔진은 이를 전역객체의 프로퍼티로도 만든다. 변수이면서 객체의 프로퍼티이기도 하다.

```javascript
var a = 1;
console.log(a); // 1
console.log(window.a); // 1
console.log(this.a); // 1
```

자바스크립트의 모든 변수는 특정 객체의 프로퍼티로서 동작하기 때문에 전부 값이 1인 것.

---





