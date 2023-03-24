# [1] Getting Started

## Where does JV code gets executed ?

* Every Browser has Javascript engine which can run javascript code. Example FireFox has SpiderMonkey and Chrome has v8.

## What is node ?

* Node is a C++ program that includes google v8 Javascript engine. Hence now we can execute javascript commands outside browser using node.

## What is difference between JavaScript and ECMAScript ?

* ECMAScript is a specification and JavaScript programming language confirms to this standards. Organization ECMA provides ECMAScript specifications.
* From ES2015/ES6 many new features are defined for JavaScript.

## How to run the JV code in Webserver ?

* Create index.html file in Visual Studio and then open it up with extension live server. This is the address from where our web application is served from.

## Where to place script element ?

* At the end of the body of the html file. If we add it in the head then the browser will get busy executing the JV Script element and the user will get the bad user experience. 

## JS is used to implement behavior

* We want to extract the JS code from HTML code. This is called "separation of concerns".

* Hence we want to separate HTML code which is "all about contents" from JavaScript code which is "all about behavior".

* Hence index.js is created and index.html file references index.js in it.

  

