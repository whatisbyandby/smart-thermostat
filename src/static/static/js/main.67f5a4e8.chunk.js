(this["webpackJsonpthermostat-frontend"]=this["webpackJsonpthermostat-frontend"]||[]).push([[0],{32:function(e,t,n){},53:function(e,t,n){"use strict";n.r(t);var r,c=n(0),s=n.n(c),u=n(21),a=n.n(u),o=(n(32),n(3)),i=n(9),l=n(4),j=n(1),d=l.a.div(r||(r=Object(o.a)(["\n  height: 100%;\n  display: flex;\n  flex-direction: column;\n  align-items: stretch;\n  button {\n    height: 100%;\n  }\n"])));function p(e){var t=e.onClick;return Object(j.jsxs)(d,{children:[Object(j.jsx)("button",{onClick:function(){return t("UP")},children:Object(j.jsx)("h2",{children:Object(j.jsx)(i.b,{})})}),Object(j.jsx)("button",{onClick:function(){return t("DOWN")},children:Object(j.jsx)("h2",{children:Object(j.jsx)(i.a,{})})})]})}var b,f=n(8),h=n.n(f),O=n(10),m=n(25),x=n(27),v=n(26),g=n.n(v);function T(e){var t=e.setTemperature,n=e.currentTemperature;return Object(j.jsxs)("div",{className:"temperature-display",children:[Object(j.jsxs)("h2",{children:["Set Temp: ",t]}),Object(j.jsxs)("h2",{children:["Current Temp: ",n]})]})}function w(e){var t=e.handleButtonPress;return Object(j.jsx)("div",{className:"control-panel",children:Object(j.jsx)(p,{onClick:t})})}var k=l.a.div(b||(b=Object(o.a)(["\n  display: flex;\n  align-items: stretch;\n  .temperature-display {\n    flex-grow: 3;\n    display: flex;\n    flex-direction: column;\n    text-align: center;\n  }\n  .control-panel {\n    flex-grow: 1;\n  }\n"])));function C(e){var t=Object(c.useState)({setTemperature:67,currentTemperature:70,mode:null,status:null}),n=Object(x.a)(t,2),r=n[0],s=n[1],u=Object(c.useRef)(null);Object(c.useEffect)((function(){return u.current=new WebSocket("ws://localhost:5000/ws"),u.current.onopen=function(){return console.log("ws opened")},u.current.onmessage=function(e){return s(JSON.parse(e.data))},u.current.onclose=function(){return console.log("ws closed")},function(){u.current.close()}}),[]);var a=function(){var e=Object(m.a)(h.a.mark((function e(t){var n;return h.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,g.a.post("/api",Object(O.a)(Object(O.a)({},r),{},{setTemperature:t}));case 2:n=e.sent,s(n.data);case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();return Object(j.jsxs)(k,{children:[Object(j.jsx)(T,{setTemperature:r.setTemperature,currentTemperature:r.currentTemperature}),Object(j.jsx)(w,{handleButtonPress:function(e){console.log("Button Press"),"UP"===e&&a(r.setTemperature+1),"DOWN"===e&&a(r.setTemperature-1)}})]})}var y=function(){return Object(j.jsx)("div",{className:"App",children:Object(j.jsx)(C,{})})},P=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,54)).then((function(t){var n=t.getCLS,r=t.getFID,c=t.getFCP,s=t.getLCP,u=t.getTTFB;n(e),r(e),c(e),s(e),u(e)}))};a.a.render(Object(j.jsx)(s.a.StrictMode,{children:Object(j.jsx)(y,{})}),document.getElementById("root")),P()}},[[53,1,2]]]);
//# sourceMappingURL=main.67f5a4e8.chunk.js.map