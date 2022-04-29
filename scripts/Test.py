// 메소드가 호출될 때 기존의 프로그램 동작은 건들지 않고 전달되는 인자를 보고싶을 때
Java.perform(function() { 
  YourClass.Method.implementation = function(arg1, arg2) { // rely on the number of args.
    console.log("arg1 : " + arg1);
    console.log("arg2 : " + arg2);
    return this.Method;
  }
});
