// When you want to see the arguments passed without touching the existing program behavior when a method is called
Java.perform(function() { 
  YourClass.Method.implementation = function(arg1, arg2) { // rely on the number of args.
    console.log("arg1 : " + arg1);
    console.log("arg2 : " + arg2);
    return this.Method;
  }
});


