(function(e){function t(t){for(var n,r,l=t[0],o=t[1],c=t[2],d=0,p=[];d<l.length;d++)r=l[d],i[r]&&p.push(i[r][0]),i[r]=0;for(n in o)Object.prototype.hasOwnProperty.call(o,n)&&(e[n]=o[n]);u&&u(t);while(p.length)p.shift()();return s.push.apply(s,c||[]),a()}function a(){for(var e,t=0;t<s.length;t++){for(var a=s[t],n=!0,l=1;l<a.length;l++){var o=a[l];0!==i[o]&&(n=!1)}n&&(s.splice(t--,1),e=r(r.s=a[0]))}return e}var n={},i={app:0},s=[];function r(t){if(n[t])return n[t].exports;var a=n[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,r),a.l=!0,a.exports}r.m=e,r.c=n,r.d=function(e,t,a){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(r.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)r.d(a,n,function(t){return e[t]}.bind(null,n));return a},r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],o=l.push.bind(l);l.push=t,l=l.slice();for(var c=0;c<l.length;c++)t(l[c]);var u=o;s.push([1,"chunk-vendors"]),a()})({0:function(e,t){},"0546":function(e,t,a){},"0927":function(e,t,a){},1:function(e,t,a){e.exports=a("56d7")},2:function(e,t){},"2d25":function(e,t,a){"use strict";var n=a("0927"),i=a.n(n);i.a},3:function(e,t){},3004:function(e,t,a){"use strict";var n=a("0546"),i=a.n(n);i.a},5153:function(e,t,a){},"56d7":function(e,t,a){"use strict";a.r(t);a("cadf"),a("551c"),a("f751"),a("097d");var n=a("2b0e"),i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"app"}},[a("router-view")],1)},s=[],r={name:"App"},l=r,o=a("2877"),c=Object(o["a"])(l,i,s,!1,null,null,null),u=c.exports,d=a("5c96"),p=a.n(d),h=(a("0fae"),a("8c4f")),m=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",[a("headers")],1)])},f=[],g=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"headers"}},[e._m(0),a("div",[a("el-menu",{staticClass:"el-menu",attrs:{"default-active":e.activeIndex,mode:"horizontal","background-color":"white","text-color":"black","active-text-color":"#00A4FF",router:""},on:{select:e.handleSelect}},[a("el-menu-item",{attrs:{index:"/requirement"}},[e._v("测试需求")]),a("el-menu-item",{attrs:{index:"/run"}},[e._v("用例执行")]),a("el-menu-item",{attrs:{index:"/log"}},[e._v("日志管理")])],1)],1)])},v=[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"title"},[n("img",{staticClass:"title-img",attrs:{src:a("f773"),alt:""}}),n("span",{staticClass:"title-text"},[e._v("自动化测试平台")])])}],b={name:"headers",data:function(){return{activeIndex:"/requirement"}},methods:{handleSelect:function(){}}},x=b,y=(a("3004"),Object(o["a"])(x,g,v,!1,null,null,null)),S=y.exports,C={name:"Home",components:{headers:S}},_=C,w=(a("2d25"),Object(o["a"])(_,m,f,!1,null,null,null)),k=w.exports,q=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("div",{staticClass:"login_form"},[n("img",{staticClass:"icon",attrs:{src:a("f773"),alt:""}}),n("div",{staticClass:"text"},[e._v("\n            自动化测试平台\n        ")]),n("div",{staticClass:"login_text"},[n("input",{directives:[{name:"model",rawName:"v-model",value:e.userName,expression:"userName"}],staticClass:"username",attrs:{type:"text",placeholder:"用户名"},domProps:{value:e.userName},on:{input:function(t){t.target.composing||(e.userName=t.target.value)}}}),n("input",{directives:[{name:"model",rawName:"v-model",value:e.password,expression:"password"}],staticClass:"password",attrs:{type:"text",placeholder:"密码"},domProps:{value:e.password},on:{input:function(t){t.target.composing||(e.password=t.target.value)}}}),n("el-button",{staticClass:"login_btn",attrs:{type:"primary",round:"",loading:e.isBtnLoading},nativeOn:{click:function(t){return e.login(t)}}},[e._v("登录\n            ")])],1)])])},z=[],P={data:function(){return{userName:"",password:"",isBtnLoading:!1}},methods:{login:function(){this.$router.push({path:"/home"})}}},N=P,O=(a("5c62"),Object(o["a"])(N,q,z,!1,null,null,null)),j=O.exports,I=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("headers"),a("div",{attrs:{id:"detail"}},[a("el-tabs",{attrs:{id:"tabs"},on:{"tab-click":e.handleClick},model:{value:e.activeName,callback:function(t){e.activeName=t},expression:"activeName"}},[a("el-tab-pane",{attrs:{label:"组件配置",name:"first"}},[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-remove-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-circle-plus-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}})]),a("el-table",{staticStyle:{"align-content":"center",width:"auto","font-size":"8px",margin:"0","line-height":"8px"},attrs:{data:e.scenesSets,border:"True","highlight-current-row":"",height:"500px","header-cell-style":{},"cell-style":{}}},[a("el-table-column",{attrs:{prop:"case_name",label:"组件名称"}})],1),a("div",{staticClass:"set_params"},[a("el-tabs",{on:{"tab-click":e.handleClick2},model:{value:e.activeName2,callback:function(t){e.activeName2=t},expression:"activeName2"}},[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-remove-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-circle-plus-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}})]),a("el-tab-pane",{attrs:{label:"数值传递",name:"first"}},[a("el-table",{staticStyle:{"align-content":"center",width:"auto","font-size":"8px",margin:"0","line-height":"8px"},attrs:{data:e.setIo,border:"True","highlight-current-row":"",height:"500px","header-cell-style":{},"cell-style":{}}},[a("el-table-column",{attrs:{prop:"name",label:"源数据","show-overflow-tooltip":!0}}),a("el-table-column",{attrs:{prop:"assign",label:"目标栏位","show-overflow-tooltip":!0}})],1)],1),a("el-tab-pane",{attrs:{label:"数值校验",name:"second"}},[e._v("\n                            配置管理\n                        ")])],1)],1)],1),a("el-tab-pane",{attrs:{label:"用例数据",name:"second"}},[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-remove-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-circle-plus-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-download",staticStyle:{margin:"0",padding:"10px"},on:{click:e.exportExcel}})]),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.pictLoading,expression:"pictLoading"}],staticStyle:{"align-content":"center",width:"auto","font-size":"8px",margin:"0","line-height":"8px"},attrs:{id:"casesTableExcel",data:e.scenesCasesIo,border:"True",fit:"True",height:"500px","header-cell-style":{padding:0,margin:0,background:"white",color:"#2b303b"},"header-row-style":{}}},[a("el-table-column",{attrs:{fixed:"",prop:"name",label:"用例名称",width:"300px","show-overflow-tooltip":!0}}),e._l(e.scenesSets,function(t,n){return a("el-table-column",{key:t,attrs:{label:t.case_name,align:"center","show-overflow-tooltip":!0}},e._l(e.scenesParams[n][t.case_name],function(e){return a("el-table-column",{key:e,attrs:{label:e.target_field,prop:"sequence_"+(n+1)+"_"+e.target_field,resizable:"True",width:"100px","show-overflow-tooltip":!0}})}),1)})],2),a("div",{staticClass:"block"},[a("div",{staticClass:"block"},[a("el-pagination",{attrs:{"current-page":e.currentPage,"page-sizes":[5,10,20,30,50,100],"page-size":e.pageSize,layout:"total, sizes, prev, pager, next, jumper",total:e.total},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1)])],1)],1)],1)],1)},T=[],$=a("bc3a"),E=a.n($),L=a("21a6"),D=a.n(L),M=a("1146"),A=a.n(M),B={name:"Cases",components:{headers:S},data:function(){return{id:this.$route.query.rqid,scenesSets:[],scenesCases:[],scenesCasesIo:[],scenesParams:[],activeName:"first",activeName2:"first",pageSize:5,currentPage:1,pictLoading:!1,setIo:[]}},mounted:function(){this.getScenesSet(this.id),this.getSceneParams(this.id),this.getScenesCases(this.id),this.tableRowClassName(),this.getSceneCasesIo(this.id,this.currentPage,this.pageSize)},methods:{handleClick2:function(e){"数值传递"===e.label&&this.getSetIo(this.id,"3")},getScenesSet:function(e){var t=this;E.a.get("http://127.0.0.1:8000/atf/sceneDetail/",{params:{rqid:e}}).then(function(e){t.scenesSets=e.data})},getScenesCases:function(e){var t=this;E.a.get("http://127.0.0.1:8000/atf/cases/",{params:{rqid:e}}).then(function(e){t.scenesCases=e.data,t.total=t.scenesCases.length})},getSceneParams:function(e){var t=this;E.a.get("http://127.0.0.1:8000/atf/sceneParams/",{params:{rqid:e}}).then(function(e){t.scenesParams=e.data})},handleSizeChange:function(e){this.pageSize=e,this.getSceneCasesIo(this.id,this.currentPage,this.pageSize)},handleCurrentChange:function(e){this.currentPage=e,this.getSceneCasesIo(this.id,this.currentPage,this.pageSize)},tableRowClassName:function(){return"success-row"},getSceneCasesIo:function(e,t,a){var n=this;this.pictLoading=!0,E.a.get("http://127.0.0.1:8000/atf/sceneCasesIo/",{params:{rqid:e,currentPage:t,pageSize:a}}).then(function(e){n.scenesCasesIo=e.data,n.pictLoading=!1})},getSetIo:function(e,t){var a=this;E.a.get("http://127.0.0.1:8000/atf/sceneSetIo/",{params:{rqid:e,type:t}}).then(function(e){a.setIo=e.data})},exportExcel:function(){var e={raw:!0},t=A.a.utils.table_to_book(document.querySelector("#casesTableExcel"),e),a=A.a.write(t,{bookType:"xlsx",bookSST:!0,type:"array"});try{D.a.saveAs(new Blob([a],{type:"application/octet-stream"}),"审核情况表.xlsx")}catch(n){}return a}}},R=B,F=(a("d96e"),Object(o["a"])(R,I,T,!1,null,null,null)),H=F.exports,J=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",[a("headers")],1),a("div",{attrs:{id:"Requirement"}},[a("el-container",{staticStyle:{"background-color":"white",height:"100%","min-height":"100vh"},attrs:{direction:"vertical"}},[a("el-container",[a("el-aside",[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-edit",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-share",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}})]),a("div",{staticClass:"req-tree"},[a("el-tree",{ref:"tree",attrs:{props:e.props,lazy:"",load:e.loadNode,"node-key":"rqid","expand-on-click-node":!1},on:{"node-click":e.nodeClick},scopedSlots:e._u([{key:"default",fn:function(t){t.node;var n=t.data;return a("span",{staticClass:"tree-node",attrs:{title:n.name}},[a("span",[e._v(e._s(n.name))])])}}])})],1)]),a("el-main",[a("div",{staticClass:"main_div"},[a("el-table",{staticStyle:{"align-content":"center",width:"auto","font-size":"8px",margin:"0","line-height":"8px"},attrs:{data:e.tableData,border:"True","highlight-current-row":"",fit:"True","header-cell-style":{padding:0,margin:0,background:"white",color:"#2b303b"},"row-style":{padding:0,margin:0,height:"10px"}}},[a("el-table-column",{attrs:{prop:"pk_id",label:"场景ID"}}),a("el-table-column",{attrs:{prop:"scene_name",label:"场景名称"}}),a("el-table-column",{attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{size:"mini"},on:{click:function(a){return e.handleDetail(t.row)}}},[e._v("查看\n                                    ")]),a("el-button",{attrs:{size:"mini"},on:{click:function(a){return e.handleEdit(t.$index,t.row)}}},[e._v("编辑\n                                    ")]),a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){return e.handleDelete(t.$index,t.row)}}},[e._v("删除\n                                    ")])]}}])})],1)],1)])],1)],1)],1)])},G=[],K={components:{headers:S},name:"requirement",data:function(){return{tableData:[]}},methods:{loadNode:function(e,t){if(0===e.level){var a="http://127.0.0.1:8000/atf/req/";E.a.get(a,{}).then(function(e){return t(e.data)})}else this.getTreeChild(e.data.rqid,t)},getTreeChild:function(e,t){var a="http://127.0.0.1:8000/atf/req/";E.a.get(a,{params:{rqid:e}}).then(function(e){return t(e.data)})},nodeClick:function(e,t){var a=this,n="http://127.0.0.1:8000/atf/scene/";E.a.get(n,{params:{rqid:t.data.rqid}}).then(function(e){a.tableData=e.data})},handleDetail:function(e){var t=this.$router.resolve({path:"./cases",query:{rqid:e["pk_id"]}}),a=t.href;window.open(a,"_blank")}}},Q=K,U=(a("8fab"),Object(o["a"])(Q,J,G,!1,null,null,null)),V=U.exports,W=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("headers"),a("div")],1)},X=[],Y={name:"run",components:{headers:S}},Z=Y,ee=Object(o["a"])(Z,W,X,!1,null,"67729e49",null),te=ee.exports,ae=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("headers"),a("div")],1)},ne=[],ie={name:"Log",components:{headers:S},return:{value1:!1}},se=ie,re=Object(o["a"])(se,ae,ne,!1,null,null,null),le=re.exports;n["default"].use(h["a"]);var oe=new h["a"]({mode:"hash",routes:[{path:"/",name:"Login",component:j},{path:"/home",name:"Home",component:k},{path:"/cases",name:"Cases",component:H},{path:"/requirement",name:"requirement",component:V},{path:"/run",name:"run",component:te},{path:"/log",name:"log",component:le}]}),ce=a("e069"),ue=a.n(ce);a("dcad");n["default"].config.productionTip=!1,n["default"].use(p.a),n["default"].use(ue.a),new n["default"]({render:function(e){return e(u)},router:oe}).$mount("#app")},"5c62":function(e,t,a){"use strict";var n=a("5153"),i=a.n(n);i.a},"8fab":function(e,t,a){"use strict";var n=a("e5b8"),i=a.n(n);i.a},"9a79":function(e,t,a){},d96e:function(e,t,a){"use strict";var n=a("9a79"),i=a.n(n);i.a},e5b8:function(e,t,a){},f773:function(e,t,a){e.exports=a.p+"static/img/title.234cae8b.png"}});
//# sourceMappingURL=app.dbcce146.js.map