# 코어자바스크립트(위키북스)


## 1장 - 데이터 타입

### undefined와 null
undefined : 값이 할당되지 않은 상태   
null : 값이 없음을 의도적으로 명시한 상태

1) undefined  
undefined는 사용자가 명시적으로 지정할 수도 있지만 값이 존재하지 않을 때 자바스크립트 엔진이 자동으로 부여하는 경우가 있다.  
사용자가 어떤 값을 지정할 것이라고 예상되는 상황에서 값이 지정되지 않았을 때 undefined가 부여된다.  
>- 값을 대입하지 않은 변수에 접근할 때
>- 객체 내부에 존재하지 않는 프로퍼티에 접근할 때
>- return 문이 없거나 호출되지 않은 함수의 실행 결과

```javascript
var a;
console.log(a);   // undefined


var obj = { a : 1 };
console.log(obj.a);  // 1
console.log(obj.b);  // undefined
console.log(b);      // ReferenceError: b is not defined


var func = function(){ };
var c = func();
console.log(c);      // undefined
```

> 비어있는 요소와 undefined을 할당한 요소는 다르다.

<br/>

```javascript
var arr1 = [undefined, 1];
var arr2 = [];
arr2[1] = 1;

arr1.forEach((v, i)=> console.log(v, i));
// undefined 0
// 1 1
arr2.forEach((v, i)=> console.log(v, i)); // 1 1

arr1.map((v, i)=> v+i);  // [NaN, 2]
arr2.map((v, i)=> v+i);  // [비어 있음, 2]

arr1.filter((v)=> !v);   // [undefined]
arr2.filter((v)=> !v);   // []

arr1.reduce((p, c, i)=> p+c+i, '');   // 'undefined011'
arr2.reduce((p, c, i)=> p+c+i, '');   // '11'
```

> 직접 undefined를 할당한 arr1은 배열의 모든 요소를 순회해서 결과를 출력하지만,  
비어있는 요소를 가진 arr2는 비어있는 요소를 무시하고 결과를 출력한다.

배열도 객체와 마찬가지로 특정 인덱스에 값을 지정할 때 비로소 빈 공간을 확보하고 인덱스를 이름으로 지정하고 데이터의 주솟값을 저장하는 등의 동작을 한다.  
즉, 값을 지정하지 않은 인덱스는 **아직은 존재하지 않는 프로퍼티**

undefined가 '비어있음'을 의미하긴 하지만 하나의 값으로 동작   
=> 프로퍼티나 배열의 요소는 고유의 키값(프로퍼티 이름)이 존재, 순회의 대상이 된다.

그러나 js 엔진이 반환하는 undefined는 해당 프로퍼티, 배열의 키값(인덱스) 자체가 존재하지 않음을 의미.


2) null  
비어있음을 명시적으로 표현하는 값  
null의 type은 object이다.
```javascript
var n = null;
console.log(null == undefined);   // true
console.log(null === undefined);  // false
```
