(function(e){function t(t){for(var n,r,o=t[0],l=t[1],c=t[2],u=0,p=[];u<o.length;u++)r=o[u],Object.prototype.hasOwnProperty.call(i,r)&&i[r]&&p.push(i[r][0]),i[r]=0;for(n in l)Object.prototype.hasOwnProperty.call(l,n)&&(e[n]=l[n]);d&&d(t);while(p.length)p.shift()();return s.push.apply(s,c||[]),a()}function a(){for(var e,t=0;t<s.length;t++){for(var a=s[t],n=!0,o=1;o<a.length;o++){var l=a[o];0!==i[l]&&(n=!1)}n&&(s.splice(t--,1),e=r(r.s=a[0]))}return e}var n={},i={app:0},s=[];function r(t){if(n[t])return n[t].exports;var a=n[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,r),a.l=!0,a.exports}r.m=e,r.c=n,r.d=function(e,t,a){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(r.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)r.d(a,n,function(t){return e[t]}.bind(null,n));return a},r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],l=o.push.bind(o);o.push=t,o=o.slice();for(var c=0;c<o.length;c++)t(o[c]);var d=l;s.push([1,"chunk-vendors"]),a()})({0:function(e,t){},"039a":function(e,t,a){"use strict";a("7174")},1:function(e,t,a){e.exports=a("56d7")},"1baa":function(e,t,a){e.exports=a.p+"static/img/main.37da6a91.png"},2:function(e,t){},"2d25":function(e,t,a){"use strict";a("7b74")},3:function(e,t){},3004:function(e,t,a){"use strict";a("b70e")},"52cb":function(e,t,a){"use strict";a("ea84")},"56d7":function(e,t,a){"use strict";a.r(t);a("cadf"),a("551c"),a("f751"),a("097d");var n=a("2b0e"),i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"app"}},[a("router-view")],1)},s=[],r={name:"App"},o=r,l=a("2877"),c=Object(l["a"])(o,i,s,!1,null,null,null),d=c.exports,u=a("5c96"),p=a.n(u),h=(a("0fae"),a("8c4f")),m=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",[a("headers")],1)])},g=[],f=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"headers"}},[n("div",{staticClass:"title"},[n("img",{staticClass:"title-img",attrs:{src:a("f773"),alt:""}}),n("span",{staticClass:"title-text"},[e._v("自动化测试平台")]),n("el-dropdown",{staticStyle:{float:"right"},on:{command:e.logout}},[n("Icon",{attrs:{type:"ios-contact-outline",size:"35",color:"white"}}),n("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[n("el-dropdown-item",[e._v(" 注销 ")])],1)],1)],1),n("div",[n("el-menu",{staticClass:"el-menu",attrs:{"default-active":e.activeIndex,mode:"horizontal","background-color":"white","text-color":"black","active-text-color":"#00A4FF",router:""}},[n("el-menu-item",{attrs:{index:"/requirement"}},[e._v("测试需求")]),n("el-menu-item",{attrs:{index:"/run"}},[e._v("用例执行")]),n("el-menu-item",{attrs:{index:"/job"}},[e._v("任务管理")]),n("el-menu-item",{attrs:{index:"/log"}},[e._v("日志查询")])],1)],1)])},v=[],b={name:"headers",props:["activeIndex"],data:function(){return{}},methods:{logout:function(){var e=this,t=this.GLOBAL.httpUrl+"loginOut/";this.$axios.post(t,{}).then((function(t){console.log(t.data),"0"===t.data["status"]&&(e.$message("已退出登录"),e.$router.push({path:"/"}))}))}}},x=b,w=(a("3004"),Object(l["a"])(x,f,v,!1,null,null,null)),y=w.exports,C={name:"Home",components:{headers:y}},_=C,k=(a("2d25"),Object(l["a"])(_,m,g,!1,null,null,null)),S=k.exports,L=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"login"}},[n("div",{staticClass:"login_form"},[n("img",{staticClass:"icon",attrs:{src:a("1baa"),alt:""}}),n("div",{staticClass:"text"},[e._v(" 自动化测试平台 ")]),n("el-tabs",{staticClass:"login_tab",attrs:{type:"border-card"},model:{value:e.activeName,callback:function(t){e.activeName=t},expression:"activeName"}},[n("el-tab-pane",{attrs:{label:"登录",name:"login"}},[n("el-form",{ref:"loginRuleForm",attrs:{model:e.loginRuleForm,"status-icon":"",rules:e.loginRules,"label-width":"0px"}},[n("el-form-item",{attrs:{label:"",prop:"name"}},[n("el-input",{attrs:{type:"text",placeholder:"请输入用户名"},model:{value:e.loginRuleForm.name,callback:function(t){e.$set(e.loginRuleForm,"name",t)},expression:"loginRuleForm.name"}})],1),n("el-form-item",{attrs:{label:"",prop:"pass"}},[n("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"请输入密码"},model:{value:e.loginRuleForm.pass,callback:function(t){e.$set(e.loginRuleForm,"pass",t)},expression:"loginRuleForm.pass"}})],1),n("el-form-item",[n("el-button",{staticClass:"login_style",attrs:{type:"primary"},on:{click:function(t){return e.login("loginRuleForm")}}},[e._v("提交")])],1)],1)],1),n("el-tab-pane",{attrs:{label:"注册",name:"register"}},[n("el-form",{ref:"registerRuleForm",attrs:{model:e.registerRuleForm,"status-icon":"",rules:e.registerRules,"label-width":"0px"}},[n("el-form-item",{attrs:{label:"",prop:"name"}},[n("el-input",{attrs:{type:"text",placeholder:"请输入用户名"},model:{value:e.registerRuleForm.name,callback:function(t){e.$set(e.registerRuleForm,"name",t)},expression:"registerRuleForm.name"}})],1),n("el-form-item",{attrs:{label:"",prop:"pass"}},[n("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"请输入密码"},model:{value:e.registerRuleForm.pass,callback:function(t){e.$set(e.registerRuleForm,"pass",t)},expression:"registerRuleForm.pass"}})],1),n("el-form-item",{attrs:{label:"",prop:"checkPass"}},[n("el-input",{attrs:{type:"password",autocomplete:"off",placeholder:"请确认密码"},model:{value:e.registerRuleForm.checkPass,callback:function(t){e.$set(e.registerRuleForm,"checkPass",t)},expression:"registerRuleForm.checkPass"}})],1),n("el-form-item",[n("el-button",{staticClass:"login_style",attrs:{type:"primary"},on:{click:function(t){return e.register("registerRuleForm")}}},[e._v("提交 ")])],1)],1)],1)],1)],1)])},$=[],O=(a("7f7f"),{data:function(){var e=this,t=function(e,t,a){if(!t)return a(new Error("用户名不能为空"));a()},a=function(t,a,n){""===a?n(new Error("请输入密码")):(""!==e.loginRuleForm.checkPass&&e.$refs.loginRuleForm.validateField("checkPass"),n())},n=function(t,a,n){""===a?n(new Error("请输入密码")):(""!==e.registerRuleForm.checkPass&&e.$refs.registerRuleForm.validateField("checkPass"),n())},i=function(t,a,n){""===a?n(new Error("请再次输入密码")):a!==e.registerRuleForm.pass?n(new Error("两次输入密码不一致!")):n()};return{activeName:"login",userName:"",password:"",loginRuleForm:{userName:"",password:""},registerRuleForm:{pass:"",checkPass:"",name:""},loginRules:{pass:[{validator:a,trigger:"blur"}],name:[{validator:t,trigger:"blur"}]},registerRules:{pass:[{validator:n,trigger:"blur"}],checkPass:[{validator:i,trigger:"blur"}],name:[{validator:t,trigger:"blur"}]}}},methods:{register:function(e){var t=this;this.$refs[e].validate((function(e){if(!e)return console.log("error submit!!"),!1;var a=t.GLOBAL.httpUrl+"register/",n=new FormData;n.append("username",t.registerRuleForm.name),n.append("password",t.registerRuleForm.pass),t.$axios.post(a,n).then((function(e){console.log(e.data),"用户名已存在"===e.data?t.$message("用户名已存在"):(t.$message("注册成功"),t.activeName="login")}))}))},login:function(e){var t=this;this.$refs[e].validate((function(e){if(!e)return console.log("error submit!!"),!1;var a=t.GLOBAL.httpUrl+"login/",n=new FormData;n.append("username",t.loginRuleForm.name),n.append("password",t.loginRuleForm.pass),t.$axios.post(a,n).then((function(e){console.log(e.data),"登录成功"===e.data?(t.$message("登录成功"),t.$router.push({path:"/manage"})):"用户名不存在"===e.data?t.$message("用户不存在"):t.$message("验证失败")}))}))}}}),R=O,z=(a("039a"),Object(l["a"])(R,L,$,!1,null,null,null)),N=z.exports,D=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("headers",{attrs:{activeIndex:"/requirement"}}),a("div",{attrs:{id:"detail"}},[a("el-tabs",{attrs:{id:"tabs"},on:{"tab-click":e.handleClick},model:{value:e.activeName,callback:function(t){e.activeName=t},expression:"activeName"}},[a("el-tab-pane",{attrs:{label:"组件配置",name:"first"}},[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-remove-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-circle-plus-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}})]),a("el-table",{staticStyle:{"align-content":"center",width:"auto","font-size":"0.6vw",margin:"0","line-height":"0.6vw"},attrs:{data:e.scenesSets,border:"True","highlight-current-row":"",height:"500px","header-cell-style":{},"cell-style":{}}},[a("el-table-column",{attrs:{prop:"component_name",label:"组件名称"}})],1),a("div",{staticClass:"set_params"},[a("el-tabs",{on:{"tab-click":e.handleClick2},model:{value:e.activeName2,callback:function(t){e.activeName2=t},expression:"activeName2"}},[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-remove-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-circle-plus-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}})]),a("el-tab-pane",{attrs:{label:"数值传递",name:"first"}},[a("el-table",{staticStyle:{"align-content":"center",width:"auto","font-size":"0.6vw",margin:"0","line-height":"0.6vw"},attrs:{data:e.setIo,border:"True","highlight-current-row":"",height:"500px","header-cell-style":{},"cell-style":{}}},[a("el-table-column",{attrs:{prop:"name",label:"源数据","show-overflow-tooltip":!0}}),a("el-table-column",{attrs:{prop:"assign",label:"目标栏位","show-overflow-tooltip":!0}})],1)],1),a("el-tab-pane",{attrs:{label:"数值校验",name:"second"}},[e._v(" 配置管理 ")])],1)],1)],1),a("el-tab-pane",{attrs:{label:"用例数据",name:"second"}},[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-remove-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-circle-plus-outline",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-download",staticStyle:{margin:"0",padding:"10px"},on:{click:e.exportExcel}})]),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.pictLoading,expression:"pictLoading"}],staticStyle:{"align-content":"center",width:"auto","font-size":"0.6vw",margin:"0","line-height":"0.6vw"},attrs:{id:"casesTableExcel",data:e.scenesCasesIo,border:"True",fit:"True",height:"500px","header-cell-style":{padding:0,margin:0,background:"white",color:"#2b303b"},"header-row-style":{}}},[a("el-table-column",{attrs:{fixed:"",prop:"name",label:"用例名称",width:"300px","show-overflow-tooltip":!0}}),e._l(e.scenesSets,(function(t,n){return a("el-table-column",{key:t,attrs:{label:t.component_name,align:"center","show-overflow-tooltip":!0}},e._l(e.scenesParams[n][t.component_name],(function(e){return a("el-table-column",{key:e,attrs:{label:e.target_field,prop:"sequence_"+(n+1)+"_"+e.target_field,resizable:"True",width:"100px","show-overflow-tooltip":!0}})})),1)}))],2),a("div",{staticClass:"block"},[a("div",{staticClass:"block"},[a("el-pagination",{attrs:{"current-page":e.currentPage,"page-sizes":[5,10,20,30,50,100],"page-size":e.pageSize,layout:"total, sizes, prev, pager, next, jumper",total:e.total},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1)])],1)],1)],1)],1)},F=[],P=a("21a6"),q=a.n(P),T=a("1146"),j=a.n(T),I={name:"Cases",components:{headers:y},data:function(){return{id:this.$route.query.rqid,scenesSets:[],scenesCases:[],scenesCasesIo:[],scenesParams:[],activeName:"first",activeName2:"first",pageSize:5,currentPage:1,pictLoading:!1,setIo:[]}},mounted:function(){this.getScenesSet(this.id),this.getSceneParams(this.id),this.getScenesCases(this.id),this.tableRowClassName(),this.getSceneCasesIo(this.id,this.currentPage,this.pageSize)},methods:{handleClick2:function(e){"数值传递"===e.label&&this.getSetIo(this.id,"3")},getScenesSet:function(e){var t=this;this.$axios.get(this.GLOBAL.httpUrl+"sceneDetail/",{params:{rqid:e}}).then((function(e){t.scenesSets=e.data}))},getScenesCases:function(e){var t=this;this.$axios.get(this.GLOBAL.httpUrl+"cases/",{params:{rqid:e}}).then((function(e){t.scenesCases=e.data,t.total=t.scenesCases.length}))},getSceneParams:function(e){var t=this;this.$axios.get(this.GLOBAL.httpUrl+"sceneParams/",{params:{rqid:e}}).then((function(e){t.scenesParams=e.data}))},handleSizeChange:function(e){this.pageSize=e,this.getSceneCasesIo(this.id,this.currentPage,this.pageSize)},handleCurrentChange:function(e){this.currentPage=e,this.getSceneCasesIo(this.id,this.currentPage,this.pageSize)},tableRowClassName:function(){return"success-row"},getSceneCasesIo:function(e,t,a){var n=this;this.pictLoading=!0,this.$axios.get(this.GLOBAL.httpUrl+"sceneCasesIo/",{params:{rqid:e,currentPage:t,pageSize:a}}).then((function(e){n.scenesCasesIo=e.data,n.pictLoading=!1}))},getSetIo:function(e,t){var a=this;this.$axios.get(this.GLOBAL.httpUrl+"sceneSetIo/",{params:{rqid:e,type:t}}).then((function(e){a.setIo=e.data}))},exportExcel:function(){var e={raw:!0},t=j.a.utils.table_to_book(document.querySelector("#casesTableExcel"),e),a=j.a.write(t,{bookType:"xlsx",bookSST:!0,type:"array"});try{q.a.saveAs(new Blob([a],{type:"application/octet-stream"}),"审核情况表.xlsx")}catch(n){}return a}}},A=I,B=(a("d96e"),Object(l["a"])(A,D,F,!1,null,null,null)),E=B.exports,G=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",[a("headers",{attrs:{activeIndex:"/requirement"}})],1),a("div",{attrs:{id:"Requirement"}},[a("el-container",{staticStyle:{"background-color":"white",height:"100%","min-height":"100vh"},attrs:{direction:"vertical"}},[a("el-container",[a("el-aside",{attrs:{id:"requirement-left"}},[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-edit",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-share",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}})]),a("div",{attrs:{id:"req-tree"}},[a("el-tree",{ref:"tree",attrs:{lazy:"",load:e.loadNode,"node-key":"id","expand-on-click-node":!0},on:{"node-click":e.nodeClick},scopedSlots:e._u([{key:"default",fn:function(t){t.node;var n=t.data;return a("span",{staticClass:"tree-node",attrs:{title:n.name}},[a("span",[e._v(e._s(n.name))])])}}])})],1)]),a("el-main",{attrs:{id:"requirement-main"}},[a("div",{staticClass:"main_div"},[a("el-table",{staticStyle:{"align-content":"center",width:"auto","font-size":"0.6vw",margin:"0","line-height":"0.6vw"},attrs:{data:e.tableData,border:"","highlight-current-row":"",fit:"","header-cell-style":{padding:0,margin:0,background:"white",color:"#2b303b"},"row-style":{padding:0,margin:0,height:"10px"}}},[a("el-table-column",{attrs:{prop:"id",label:"场景ID"}}),a("el-table-column",{attrs:{prop:"scene_name",label:"场景名称"}}),a("el-table-column",{attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{size:"mini"},on:{click:function(a){return e.handleDetail(t.row)}}},[e._v("查看 ")]),a("el-button",{attrs:{size:"mini"},on:{click:function(a){return e.handleEdit(t.$index,t.row)}}},[e._v("编辑 ")]),a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){return e.handleDelete(t.$index,t.row)}}},[e._v("删除 ")])]}}])})],1)],1)])],1)],1)],1)])},U=[],M={components:{headers:y},name:"requirement",data:function(){return{tableData:[]}},methods:{loadNode:function(e,t){if(0===e.level){var a=this.GLOBAL.httpUrl+"req/";this.$axios.get(a,{}).then((function(e){return t(e.data)}))}else this.getTreeChild(e.data.id,t)},getTreeChild:function(e,t){var a=this.GLOBAL.httpUrl+"req/";this.$axios.get(a,{params:{rqid:e}}).then((function(e){return t(e.data)}))},nodeClick:function(e,t){var a=this,n=this.GLOBAL.httpUrl+"scene/";this.$axios.get(n,{params:{rqid:t.data.id}}).then((function(e){a.tableData=e.data}))},handleDetail:function(e){var t=this.$router.resolve({path:"./cases",query:{rqid:e["id"]}}),a=t.href;window.open(a,"_blank")}}},K=M,H=(a("8fab"),Object(l["a"])(K,G,U,!1,null,null,null)),J=H.exports,V=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("headers",{attrs:{activeIndex:"/run"}}),a("div",[a("el-container",{staticStyle:{"background-color":"white",height:"100%","min-height":"100vh"},attrs:{direction:"vertical"}},[a("el-container",[a("el-aside",[a("div",{staticStyle:{"padding-left":"10px"}},[a("i",{staticClass:"el-icon-edit",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-share",staticStyle:{margin:"0",padding:"10px"}}),a("i",{staticClass:"el-icon-delete",staticStyle:{margin:"0",padding:"10px"}})]),a("div",{staticClass:"req-tree"},[a("el-tree",{ref:"setTree",attrs:{lazy:"",load:e.loadSetNode,"node-key":"rqid","expand-on-click-node":!0},on:{"node-click":e.clickSetNode},scopedSlots:e._u([{key:"default",fn:function(t){t.node;var n=t.data;return a("span",{staticClass:"req-tree-node",attrs:{title:n.name}},[a("span",[e._v(e._s(n.name))])])}}])})],1)]),a("el-main",{attrs:{id:"run-main"}},[a("div",{attrs:{id:"run-main-ico"}},[a("Button",{attrs:{type:"primary"},on:{click:e.run}},[e._v("执行")]),a("Modal",{attrs:{title:"新建执行任务",draggable:!0},on:{"on-ok":e.ok,"on-cancel":e.cancel},model:{value:e.modal1,callback:function(t){e.modal1=t},expression:"modal1"}},[a("div",{staticStyle:{padding:"10px",background:"#f8f8f9"}},[a("Card",{staticStyle:{width:"300px"},attrs:{title:"选择执行器",icon:"ios-options",padding:0,shadow:""}},[a("CellGroup",[a("p",[e._v("用例数量 ："+e._s(e.casesNum))]),a("Input",{attrs:{placeholder:"执行器IP"},model:{value:e.ip,callback:function(t){e.ip=t},expression:"ip"}}),a("br"),a("Input",{attrs:{placeholder:"端口"},model:{value:e.port,callback:function(t){e.port=t},expression:"port"}}),a("br"),a("Input",{attrs:{placeholder:"执行名称"},model:{value:e.runName,callback:function(t){e.runName=t},expression:"runName"}}),a("br")],1)],1)],1)])],1),a("div",{directives:[{name:"loading",rawName:"v-loading.body",value:e.caseLoading,expression:"caseLoading",modifiers:{body:!0}}],staticClass:"set-tree-div"},[a("el-tree",{key:e.timer,ref:"reqTree",attrs:{id:"set-tree",props:e.setTreeProps,lazy:"",load:e.loadReqNode,"node-key":"set","expand-on-click-node":!0,"show-checkbox":""},on:{"node-expand":e.setTreeExpand,check:e.check},scopedSlots:e._u([{key:"default",fn:function(t){t.node;var n=t.data;return a("span",{staticClass:"set-tree-node",attrs:{title:n.name}},[a("span",[e._v(e._s(n.name))])])}}])})],1)])],1)],1)],1)],1)},X=[],Q=(a("6b54"),{name:"run",components:{headers:y},data:function(){return{switchValue:!0,modal1:!1,getReqLeafRes:[],setData:"",caseLoading:!1,setTreeProps:{isLeaf:"leaf"},timer:"",ip:"",port:"",runName:"",casesToRun:[],casesNum:0}},methods:{run:function(){var e=this;this.caseLoading=!0,this.casesToRun=[];var t=this.$refs.reqTree.getCheckedNodes();if(0===t.length)this.caseLoading=!1,this.$message({showClose:!0,message:"未选中测试用例",type:"warning"});else{for(var a=[],n=t.length-1;n>=0;n--){var i=t[n];a.push(i["id"]+" "+i["case_id"]+" "+i["tier"])}var s=this.GLOBAL.httpUrl+"casesToRun/";this.$axios.get(s,{params:{checkedCases:a+"",set:this.setData}}).then((function(t){e.casesToRun=t.data,e.caseLoading=!1,e.modal1=!0,e.casesNum=e.casesToRun.length,console.log(e.casesToRun)})).catch((function(e){console.log(e)}))}},ok:function(){var e=this,t=this.GLOBAL.httpUrl+"run/";this.$axios.get(t,{params:{nameSrvAddr:this.ip+":"+this.port,runName:this.runName,setNames:this.casesToRun.toString(),setId:this.setData}}).then((function(t){-1===t.data.indexOf("exceptions")&&-1===t.data.indexOf("error")||e.$message({message:t.data,type:"warning"}),console.log(t.data)})).catch((function(e){console.log(e)}))},cancel:function(){this.$Message.info("Clicked cancel")},loadSetNode:function(e,t){var a=this,n=this.GLOBAL.httpUrl+"set/";0===e.level?this.$axios.get(n,{params:{level:0}}).then((function(e){return t(e.data)})):this.$axios.get(n,{params:{level:1,id:e.data.id}}).then((function(n){if(0===n.data.length){var i=u["Loading"].service({fullscreen:!1,text:"加载测试集..."});e.isLeaf=!0,a.setData=e.data.set_id,a.timer=(new Date).getTime(),i.close()}return t(n.data)}))},clickSetNode:function(e,t){if(t.isLeaf){var a=u["Loading"].service({fullscreen:!1,text:"加载测试集..."});this.setData=t.data.set_id,this.timer=(new Date).getTime(),a.close()}},loadReqNode:function(e,t){void 0!==this.$refs.reqTree&&(this.checkedKeys=this.$refs.reqTree.getCheckedKeys());var a=this.GLOBAL.httpUrl+"reqOfCase/";0===e.level?this.$axios.get(a,{params:{level:"0",set:this.setData,tier:""}}).then((function(e){return t(e.data)})).catch((function(e){console.log(e)})):this.$axios.get(a,{params:{level:e.level,set:this.setData,tier:e.data.tier}}).then((function(e){if(0===e.data.length)return t(e.data);if("000"===e.data[0].tier.slice(-3))for(var a=0;a<e.data.length;a++)e.data[a].leaf=!0;return t(e.data)})),void 0!==this.$refs.reqTree&&this.$refs.reqTree.setCheckedKeys(this.checkedKeys)},check:function(e,t){t.checkedNodes.length},setTreeExpand:function(e,t){t.expanded=!0;for(var a=t.childNodes,n=a.length-1;n>=0;n--);t.checked}}}),W=Q,Y=(a("771a"),Object(l["a"])(W,V,X,!1,null,"53975449",null)),Z=Y.exports,ee=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("headers",{attrs:{activeIndex:"/log"}}),a("div",[a("el-table",{staticStyle:{"align-content":"center",width:"auto","font-size":"0.6vw",margin:"0","line-height":"0.6vw"},attrs:{size:"mini",data:e.run,border:"","highlight-current-row":""},on:{"row-dblclick":e.rowDblClick}},[a("el-table-column",{attrs:{prop:"run_name",label:"执行名称"}}),a("el-table-column",{attrs:{prop:"start",label:"开始时间"}}),a("el-table-column",{attrs:{prop:"finish",label:"结束时间"}})],1)],1),a("el-drawer",{attrs:{title:"执行记录!",visible:e.drawer,size:"80%","with-header":!1},on:{"update:visible":function(t){e.drawer=t}}},[a("el-pagination",{attrs:{"page-sizes":[20,50,100,200,300,500],"page-size":e.pageSize,layout:"total, sizes, prev, pager, next, jumper"},on:{"size-change":e.sizeChange,"current-change":e.currentChange}}),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loadingSet,expression:"loadingSet"}],attrs:{size:"mini","element-loading-text":"加载用例中",data:e.runData.slice((e.currentPage-1)*e.pageSize,e.currentPage*e.pageSize)},on:{"row-dblclick":e.showCaseComp}},[a("el-table-column",{attrs:{prop:"case_clazz",label:"用例名称"}})],1),a("el-drawer",{attrs:{title:"组件信息",visible:e.drawerOne,size:"60%","append-to-body":!0,"with-header":!1},on:{"update:visible":function(t){e.drawerOne=t}}},[a("el-table",{attrs:{data:e.runDataOne,size:"mini"},on:{"row-dblclick":e.showCaseCompDetail,"expand-change":e.showCaseCompDetail}},[a("el-table-column",{attrs:{type:"expand"}},[[a("el-table",{attrs:{size:"mini",data:e.valueDescriptionList}},[a("el-table-column",{attrs:{prop:"description",label:"栏位"}}),a("el-table-column",{attrs:{prop:"value",label:"值"}})],1)]],2),a("el-table-column",{attrs:{prop:"component_name",label:"组件名称"}})],1)],1)],1)],1)},te=[],ae=(a("28a5"),{name:"Log",components:{headers:y},data:function(){return{value1:!1,run:[],drawer:!1,runData:[],runDataOne:[],drawerOne:!1,loadingSet:!1,pageSize:20,currentPage:1,runDataOneDetail:[],compData:[],valueDescriptionList:[]}},mounted:function(){this.getRun()},methods:{getRun:function(){var e=this,t=this.GLOBAL.httpUrl+"runLog/";this.$axios.get(t,{params:{}}).then((function(t){console.log(t.data),e.run=t.data}))},rowDblClick:function(e){var t=this;this.drawer=!0,console.log(e["run_id"]),this.runData=[],this.loadingSet=!0;var a=this.GLOBAL.httpUrl+"runLog/set/";this.$axios.get(a,{params:{run_id:e["run_id"]}}).then((function(e){console.log(e.data),t.runData=e.data,t.loadingSet=!1}))},showCaseComp:function(e){var t=this;this.drawerOne=!0;var a=this.GLOBAL.httpUrl+"runLog/set/one";this.$axios.get(a,{params:{run_id:e["run_id"],case_id:e["case_id"]}}).then((function(e){t.runDataOne=e.data}))},showCaseCompDetail:function(e){this.valueDescriptionList=[];for(var t=e["value"].split("\0"),a=e["description"].split("\0"),n=0;n<a.length;n++){var i={description:a[n],value:t[n]};this.valueDescriptionList.push(i)}console.log(this.valueDescriptionList)},currentChange:function(e){this.currentPage=e},sizeChange:function(e){this.pageSize=e}}}),ne=ae,ie=(a("ede9"),Object(l["a"])(ne,ee,te,!1,null,null,null)),se=ie.exports,re=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("headers",{attrs:{activeIndex:"/job"}})],1)},oe=[],le={name:"job",components:{headers:y},data:function(){return{percentage:this.GLOBAL.jobPercentage[0]}}},ce=le,de=Object(l["a"])(ce,re,oe,!1,null,"01989e4e",null),ue=de.exports,pe=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-container",{staticStyle:{height:"100%"}},[n("el-header",[n("div",{staticClass:"title"},[n("img",{staticClass:"title-img",attrs:{src:a("f773"),alt:""}}),n("span",{staticClass:"title-text"},[e._v("自动化测试平台")]),n("el-dropdown",{staticStyle:{float:"right"},on:{command:e.logout}},[n("Icon",{attrs:{type:"ios-contact-outline",size:"35",color:"white"}}),n("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[n("el-dropdown-item",[e._v(" 注销 ")])],1)],1)],1)]),n("el-container",[n("el-aside",{attrs:{width:"36%"}}),n("el-main",[n("div",[n("el-card",{staticClass:"box-card"},[n("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("项目管理")]),n("el-button",{staticStyle:{float:"right",padding:"3px 0"},attrs:{type:"text"}},[e._v("新建项目")])],1),e._l(e.projects,(function(t){return n("div",{key:t,staticClass:"text item"},[n("el-button",{staticStyle:{float:"left",padding:"3px 0"},attrs:{type:"text"}},[e._v(e._s("项目： "+t))])],1)}))],2)],1),n("div",[n("el-card",{staticClass:"box-card"},[n("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("成员管理")]),n("el-button",{staticStyle:{float:"right",padding:"3px 0"},attrs:{type:"text"}},[e._v("新建项目")])],1),e._l(4,(function(t){return n("div",{key:t,staticClass:"text item"},[e._v(" "+e._s("列表内容 "+t)+" ")])}))],2)],1)])],1)],1)},he=[],me={name:"manage",data:function(){return{projects:["融资融券2.0"]}},methods:{logout:function(){var e=this,t=this.GLOBAL.httpUrl+"loginOut/";this.$axios.post(t,{}).then((function(t){console.log(t.data),"0"===t.data["status"]&&(e.$message("已退出登录"),e.$router.push({path:"/"}))}))}}},ge=me,fe=(a("52cb"),Object(l["a"])(ge,pe,he,!1,null,"01696c77",null)),ve=fe.exports,be=h["a"].prototype.push;h["a"].prototype.push=function(e){return be.call(this,e).catch((function(e){return e}))},n["default"].use(h["a"]);var xe,we,ye=new h["a"]({mode:"hash",routes:[{path:"/",name:"Login",component:N},{path:"/home",name:"Home",component:S},{path:"/cases",name:"Cases",component:E},{path:"/requirement",name:"requirement",component:J},{path:"/run",name:"run",component:Z},{path:"/log",name:"log",component:se},{path:"/job",name:"job",component:ue},{path:"/manage",name:"manage",component:ve}]}),Ce=a("e069"),_e=a.n(Ce),ke=(a("dcad"),a("bc3a")),Se=a.n(ke),Le="http://127.0.0.1:8090/apis/",$e=[],Oe={name:"global",httpUrl:Le,jobPercentage:$e},Re=Oe,ze=Object(l["a"])(Re,xe,we,!1,null,"3d16648b",null),Ne=ze.exports,De=a("a78e"),Fe=a.n(De);n["default"].use(Fe.a),n["default"].http.interceptors.push((function(e,t){e.headers.set("X-CSRFToken",Fe.a.get("csrftoken")),t((function(e){return e}))})),n["default"].config.productionTip=!1,n["default"].use(p.a),n["default"].use(_e.a),n["default"].prototype.$axios=Se.a,Se.a.defaults.withCredentials=!0,n["default"].prototype.GLOBAL=Ne,n["default"].prototype.$axios.defaults.withCredentials=!0,n["default"].prototype.$Cookies=Fe.a,new n["default"]({render:function(e){return e(d)},router:ye}).$mount("#app")},7174:function(e,t,a){},"771a":function(e,t,a){"use strict";a("bd45")},"7b74":function(e,t,a){},"7c13":function(e,t,a){},"8fab":function(e,t,a){"use strict";a("ea2c")},"9cfb":function(e,t,a){},b70e:function(e,t,a){},bd45:function(e,t,a){},d96e:function(e,t,a){"use strict";a("9cfb")},ea2c:function(e,t,a){},ea84:function(e,t,a){},ede9:function(e,t,a){"use strict";a("7c13")},f773:function(e,t,a){e.exports=a.p+"static/img/title.234cae8b.png"}});
//# sourceMappingURL=app.01e10960.js.map