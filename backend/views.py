# Create your views here.

from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .log.log import Log
from .models import *

from .rocketmq.producer import MyProducer
from .rocketmq.push_consumer import *

from multiprocessing import Process
import os
# 新建子进程用于获取mq接收的日志
print("当前进程PID ", os.getpid(), "对应父进程PID", os.getppid())
p = Process(target=start_consume_message)
p.start()

log = Log()
output = '{"账户参数表":{"component_script_model":["0","账户参数表"],"acct_id":["0","3"],"case_acct":["0","RZRQ_ZL_1"],"custid":["0","110303000001"],"custorgid":["0","1103"],"trdpwd":["0","123321"],"netaddr":["0","127.0.0.1"],"orgid":["0","1103"],"operway":["0","7"],"ext":["0","0"],"custcert":["0",""],"operid":["0",""],"operpwd":["0",""],"ticket":["0",""],"market":["0","0"],"fundid":["0","99004149"],"secuid":["0","0600061611"],"sz_secuid":["0","600061611"],"sh_secuid":["0","E000617679"],"stkcode":["0","000001"],"bsflag":["0","0B"],"creditid":["0","0"],"creditflag":["0","6"],"zxjt_trade_type":["0","深A买"],"zxjt_orderfrztype":["0",""],"zxjt_price_type":["0",""],"zxjt_yq_qty":["0","1000"],"zxjt_usetype1":["0","beforeorder"],"zxjt_usetype2":["0","afterorder"],"zxjt_usetype3":["0","cancelorder"],"zxjt_ip":["0",""],"zxjt_wt_cj_flag":["0",""],"remark":["0",""],"ar_sleep":["0",""],"remark1":["0",""],"remark2":["0",""],"remark3":["0",""],"remark4":["0",""],"remark5":["0",""],"locked":["0","0"],"starttime":["0","2020-10-14 15:24:28"],"tc_allowerror":["0","1"],"tc_result":["0",""],"tc_out":["0",""],"tc_out_check":["0",""]},"410203-证券信息":{"component_script_model":["0","410203-证券信息"],"custid":["账户参数表.custid","110303000001"],"custorgid":["账户参数表.custorgid","1103"],"trdpwd":["账户参数表.trdpwd","123321"],"netaddr":["账户参数表.netaddr","127.0.0.1"],"orgid":["账户参数表.orgid","1103"],"operway":["账户参数表.operway","7"],"ext":["账户参数表.ext","0"],"funcid":["0","410203"],"market":["账户参数表.market","0"],"stklevel":["0",""],"stkcode":["账户参数表.stkcode","000001"],"poststr":["0",""],"rowcount":["0",""],"stktype":["0",""],"zxjt_trade_type":["0",""],"zxjt_yq_qty":["账户参数表.zxjt_yq_qty","1000"],"zxjt_price_type":["账户参数表.zxjt_price_type",""],"zxjt_yq_price":["0","16.06"],"zxjt_yq_orderfrzamt":["0",""],"zxjt_orderfrztype":["0",""],"zxjt_bsflag":["0",""],"zxjt_yq_stkcode":["0",""],"marginratefund":["0",""],"marginratestk":["0",""],"pledgerate":["0",""],"pledgerateoff":["0",""],"rzmarginrateoff":["0",""],"fundavl":["0",""],"stkavl":["0",""],"lastprice":["0",""],"poststr_out":["0",""],"market_out":["0","0"],"moneytype":["0","0"],"stkname":["0","平安银行"],"stkcode_out":["0","000001"],"stktype_out":["0","0"],"priceunit":["0","10"],"maxrisevalue":["0","17.670"],"maxdownvalue":["0","14.450"],"stopflag":["0","F"],"mtkcalflag":["0","1"],"bondintr":["0",".00000000"],"maxqty":["0","1000000"],"minqty":["0","1"],"buyunit":["0","100"],"saleunit":["0","1"],"stkstatus":["0","N"],"stklevel_out":["0","N"],"trdid":["0",""],"quitdate":["0","0"],"fixprice":["0",""],"priceflag":["0",""],"memotext":["0",""],"tc_flag":["0","0"],"tc_checkStr":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;证券信息查询成功"],"resultstate":["0","0"],"dtosbond":["0",""],"nOverTime":["0","1200"],"szReceiveQName":["0","ans1"],"protocol":["0","0"],"szSendQName":["0","req1"],"voterights":["0","N"],"ip":["0","10.4.6.16"],"usename":["0","KCXP00"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"nProtocal":["0","0"],"nPort":["0","21000"],"stkfullname":["0",""],"serverName":["0","Cails"],"szAddress":["0","10.4.6.14"],"receiveQName":["0","ans1"],"isvie":["0","N"],"isreg":["0","N"],"marketmaxqty":["0","1000000"],"Password":["0","888888"],"marketminqty":["0","1"],"UserName":["0","KCXP00"],"stkattr":["0",""],"noprofit":["0","N"],"tc_out":["0","字段名称tc_out不存在"],"szServerName":["0","KCXP01"],"ServerName":["0","KCXP01"]},"410502委托前-资金查询":{"component_script_model":["0","410502-资金查询"],"custid":["账户参数表.custid","110303000001"],"custorgid":["账户参数表.custorgid","1103"],"trdpwd":["账户参数表.trdpwd","123321"],"netaddr":["账户参数表.netaddr","127.0.0.1"],"orgid":["账户参数表.orgid","1103"],"operway":["账户参数表.operway","7"],"ext":["账户参数表.ext","0"],"funcid":["0","410502"],"fundid":["账户参数表.fundid","99004149"],"moneytype":["0","0"],"remark":["0",""],"zxjt_usetype":["账户参数表.zxjt_usetype1","beforeorder"],"zxjt_orderfrztype":["0",""],"zxjt_trade_type":["0",""],"zxjt_yq_price":["0",""],"zxjt_yq_qty":["0",""],"zxjt_yq_orderfrzamt":["0",""],"zxjt_pre_fundavl":["0",""],"zxjt_pre_fundbal":["0",""],"zxjt_pre_fund":["0",""],"zxjt_bondintr":["0",""],"zxjt_pre_creditbal":["0",""],"zxjt_pre_creditavl":["0",""],"zxjt_yq_restcreditrepay":["0",""],"zxjt_yq_orderfrzamt_fundavl":["0",""],"zxjt_stkcode":["0",""],"bsflag":["0",""],"zxjt_wt_cj_flag":["0",""],"market":["0",""],"creditrepayunfrz":["0",""],"feeunfrz":["0",""],"matchqty":["0",""],"matchamt":["0",""],"clearamt":["0",""],"matchqty2":["0",""],"clearamt2":["0",""],"zxjt_ar_sleep":["0",""],"custid_out":["0","110303000001"],"fundid_out":["0","99004149"],"orgid_out":["0","1103"],"moneytype_out":["0","0"],"fundbal":["0","900000000000.00"],"fundavl":["0","899999678780.00"],"marketvalue":["0","903025381855.27"],"fund":["0","899999678780.00"],"stkvalue":["0","3025703075.27"],"fundseq":["0","0"],"fundloan":["0",""],"fundbuy":["0","321220.00"],"fundsale":["0","0.00"],"fundfrz":["0","0.00"],"fundlastbal":["0","900000000000.00"],"creditbal":["0","0.00"],"creditavl":["0","0.00"],"fundavl_check":["0",""],"fundbal_check":["0",""],"fund_check":["0",""],"creditavl_check":["0",""],"creditbal_check":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;资金查询成功"],"resultstate":["0","0"],"nOverTime":["0","1200"],"szReceiveQName":["0","ans1"],"protocol":["0","0"],"szSendQName":["0","req1"],"ip":["0","10.4.6.16"],"usename":["0","KCXP00"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"nProtocal":["0","0"],"nPort":["0","21000"],"serverName":["0","Cails"],"creditamtused":["0","0.00"],"szAddress":["0","10.4.6.14"],"receiveQName":["0","ans1"],"Password":["0","888888"],"UserName":["0","KCXP00"],"tc_out":["0","字段名称tc_out不存在"],"szServerName":["0","KCXP01"],"ServerName":["0","KCXP01"]},"410410-取最大交易数量":{"component_script_model":["0","410410-取最大交易数量"],"custid":["账户参数表.custid","110303000001"],"custorgid":["账户参数表.custorgid","1103"],"trdpwd":["账户参数表.trdpwd","123321"],"netaddr":["账户参数表.netaddr","127.0.0.1"],"orgid":["账户参数表.orgid","1103"],"operway":["账户参数表.operway","7"],"ext":["账户参数表.ext","0"],"funcid":["0","410410"],"market":["账户参数表.market","0"],"secuid":["账户参数表.secuid","0600061611"],"fundid":["账户参数表.fundid","99004149"],"stkcode":["账户参数表.stkcode","000001"],"bsflag":["账户参数表.bsflag","0B"],"price":["410203-证券信息.zxjt_yq_price","16.06"],"bankcode":["0",""],"hiqtyflag":["0",""],"creditid":["账户参数表.creditid","0"],"creditflag":["账户参数表.creditflag","6"],"linkmarket":["0",""],"linksecuid":["0",""],"sorttype":["0",""],"prodcode":["0",""],"zxjt_yq_qty":["0","1000"],"zxjt_orderfrztype":["0",""],"zxjt_yq_orderfrzamt":["0",""],"zxjt_yq_orderfrzamt_stkavl":["0",""],"transoutline":["0",""],"lastprice":["0",""],"stkcode_stk":["0",""],"stkavl":["0",""],"stkcodeamt":["0",""],"stkcodeamt1":["0",""],"fundavl":["0",""],"orderprice":["0",""],"marginavl":["0",""],"positionid":["0",""],"positionid_out":["0",""],"avlamt":["0",""],"matchqty":["0",""],"stkcode_credit":["0",""],"zxjt_marketvalue":["0",""],"stkrepayunfrz":["0",""],"maxstkqty":["0","1000000"],"maxstkqty_check":["0",""],"tc_flag":["0","0"],"tc_checkStr":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;取可买数量成功"],"tc_out":["0",""],"tc_out_check":["0",""],"resultstate":["0","0"],"nOverTime":["0","1200"],"serverName":["0","Cails"],"szReceiveQName":["0","ans1"],"szAddress":["0","10.4.6.14"],"protocol":["0","0"],"receiveQName":["0","ans1"],"Password":["0","888888"],"szSendQName":["0","req1"],"UserName":["0","KCXP00"],"ip":["0","10.4.6.16"],"usename":["0","KCXP00"],"szServerName":["0","KCXP01"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"ServerName":["0","KCXP01"],"nProtocal":["0","0"],"nPort":["0","21000"]},"410411-买卖委托":{"component_script_model":["0","410411-买卖委托"],"custid":["账户参数表.custid","110303000001"],"custorgid":["账户参数表.custorgid","1103"],"trdpwd":["账户参数表.trdpwd","123321"],"netaddr":["账户参数表.netaddr","127.0.0.1"],"orgid":["账户参数表.orgid","1103"],"operway":["账户参数表.operway","7"],"ext":["账户参数表.ext","0"],"funcid":["0","410411"],"market":["账户参数表.market","0"],"secuid":["账户参数表.secuid","0600061611"],"fundid":["账户参数表.fundid","99004149"],"stkcode":["账户参数表.stkcode","000001"],"bsflag":["账户参数表.bsflag","0B"],"price":["410203-证券信息.zxjt_yq_price","16.06"],"qty":["账户参数表.zxjt_yq_qty","1000"],"ordergroup":["0",""],"bankcode":["0",""],"creditid":["账户参数表.creditid","0"],"creditflag":["账户参数表.creditflag","6"],"remark":["0",""],"targetseat":["0",""],"promiseno":["0",""],"risksno":["0",""],"autoflag":["0",""],"enddate":["0",""],"linkman":["0",""],"linkway":["0",""],"linkmarket":["0",""],"linksecuid":["0",""],"sorttype":["0",""],"mergematchcode":["0",""],"mergematchdate":["0",""],"oldorderid":["0",""],"prodcode":["0",""],"pricetype":["0",""],"blackflag":["0",""],"ordersno":["0","978"],"orderid":["0","AC000491"],"ordergroup_out":["0",""],"tc_flag":["0","0"],"tc_checkStr":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;委托成功"],"tc_out":["0",""],"tc_out_check":["0",""],"resultstate":["0","0"],"nOverTime":["0","1200"],"szReceiveQName":["0","ans1"],"protocol":["0","0"],"szSendQName":["0","req1"],"ip":["0","10.4.6.16"],"usename":["0","KCXP00"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"nProtocal":["0","0"],"nPort":["0","21000"],"serverName":["0","Cails"],"szAddress":["0","10.4.6.14"],"receiveQName":["0","ans1"],"Password":["0","888888"],"UserName":["0","KCXP00"],"szServerName":["0","KCXP01"],"ServerName":["0","KCXP01"]},"410510-当日委托明细查询":{"component_script_model":["0","410510-当日委托明细查询"],"custid":["账户参数表.custid","110303000001"],"custorgid":["账户参数表.custorgid","1103"],"trdpwd":["账户参数表.trdpwd","123321"],"netaddr":["账户参数表.netaddr","127.0.0.1"],"orgid":["账户参数表.orgid","1103"],"operway":["账户参数表.operway","7"],"ext":["账户参数表.ext","0"],"funcid":["0","410510"],"market":["账户参数表.market","0"],"fundid":["账户参数表.fundid","99004149"],"secuid":["账户参数表.secuid","0600061611"],"stkcode":["账户参数表.stkcode","000001"],"ordersno":["410411-买卖委托.ordersno","978"],"ordergroup":["0",""],"bankcode":["0",""],"qryflag":["0","0"],"count":["0","1"],"poststr":["0","20201014|978"],"extsno":["0",""],"qryoperway":["0",""],"zxjt_yq_orderfrzamt":["410203-证券信息.zxjt_yq_orderfrzamt",""],"zxjt_wt_cj_flag":["账户参数表.zxjt_wt_cj_flag",""],"zxjt_orderfrztype":["0",""],"pre_orderid":["0",""],"zxjt_usetype":["0",""],"orderdate":["0","20201014"],"ordersno_out":["0","978"],"ordergroup_out":["0","978"],"custid_out":["0","110303000001"],"custname":["0","测试001"],"fundid_out":["0","99004149"],"moneytype":["0","0"],"orgid_out":["0","1103"],"secuid_out":["0","0600061611"],"bsflag":["0","0B"],"orderid":["0","AC000491"],"reporttime":["0","000000"],"opertime":["0","152428"],"market_out":["0","0"],"stkcode_out":["0","000001"],"stkname":["0","平安银行"],"prodcode":["0",""],"prodname":["0",""],"orderprice":["0","16.060"],"orderqty":["0","1000"],"orderfrzamt":["0","16061.00"],"matchqty":["0","0"],"matchamt":["0",".00"],"cancelqty":["0","0"],"orderstatus":["0","A"],"seat":["0","390599"],"cancelflag":["0","F"],"operdate":["0","20201014"],"bondintr":["0",""],"operway_out":["0","7"],"remark":["0",""],"matchamt_check":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;委托查询成功"],"creditflag":["0","6"],"resultstate":["0","0"],"nOverTime":["0","1200"],"szReceiveQName":["0","ans1"],"protocol":["0","0"],"szSendQName":["0","req1"],"ip":["0","10.4.6.16"],"creditmethod":["0","0"],"usename":["0","KCXP00"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"nProtocal":["0","0"],"nPort":["0","21000"],"Ordergroup":["0","字段名称Ordergroup不存在"],"serverName":["0","Cails"],"szAddress":["0","10.4.6.14"],"receiveQName":["0","ans1"],"Password":["0","888888"],"UserName":["0","KCXP00"],"tc_out":["0","字段名称tc_out不存在"],"szServerName":["0","KCXP01"],"creditid":["0","0"],"ServerName":["0","KCXP01"]},"410502委托后-资金查询":{"component_script_model":["0","410502-资金查询"],"custid":["410502委托前-资金查询.custid","110303000001"],"custorgid":["410502委托前-资金查询.custorgid","1103"],"trdpwd":["410502委托前-资金查询.trdpwd","123321"],"netaddr":["410502委托前-资金查询.netaddr","127.0.0.1"],"orgid":["410502委托前-资金查询.orgid","1103"],"operway":["410502委托前-资金查询.operway","7"],"ext":["410502委托前-资金查询.ext","0"],"funcid":["0","410502"],"fundid":["410502委托前-资金查询.fundid","99004149"],"moneytype":["410502委托前-资金查询.moneytype","0"],"remark":["0",""],"zxjt_usetype":["账户参数表.zxjt_usetype2","afterorder"],"zxjt_orderfrztype":["0",""],"zxjt_trade_type":["账户参数表.zxjt_trade_type","深A买"],"zxjt_yq_price":["410203-证券信息.zxjt_yq_price","16.06"],"zxjt_yq_qty":["410203-证券信息.zxjt_yq_qty","1000"],"zxjt_yq_orderfrzamt":["0","16061.0"],"zxjt_pre_fundavl":["410502委托前-资金查询.fundavl","899999678780.00"],"zxjt_pre_fundbal":["410502委托前-资金查询.fundbal","900000000000.00"],"zxjt_pre_fund":["410502委托前-资金查询.fund","899999678780.00"],"zxjt_bondintr":["410203-证券信息.bondintr",""],"zxjt_pre_creditbal":["0",""],"zxjt_pre_creditavl":["0",""],"zxjt_yq_restcreditrepay":["0",""],"zxjt_yq_orderfrzamt_fundavl":["0",""],"zxjt_stkcode":["0",""],"bsflag":["0",""],"zxjt_wt_cj_flag":["0",""],"market":["0",""],"creditrepayunfrz":["0",""],"feeunfrz":["0",""],"matchqty":["0",""],"matchamt":["0",""],"clearamt":["0",""],"matchqty2":["0",""],"clearamt2":["0",""],"zxjt_ar_sleep":["410502委托前-资金查询.zxjt_ar_sleep",""],"custid_out":["0","110303000001"],"fundid_out":["0","99004149"],"orgid_out":["0","1103"],"moneytype_out":["0","0"],"fundbal":["0","900000000000.00"],"fundavl":["0","899999662719.00"],"marketvalue":["0","903025381855.27"],"fund":["0","899999678780.00"],"stkvalue":["0","3025703075.27"],"fundseq":["0","0"],"fundloan":["0",""],"fundbuy":["0","337281.00"],"fundsale":["0","0.00"],"fundfrz":["0","0.00"],"fundlastbal":["0","900000000000.00"],"creditbal":["0","0.00"],"creditavl":["0","0.00"],"fundavl_check":["0","16061.0;16061.0;true"],"fundbal_check":["0",""],"fund_check":["0",""],"creditavl_check":["0",""],"creditbal_check":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;资金查询成功"],"resultstate":["0","0"],"nOverTime":["0","1200"],"szReceiveQName":["0","ans1"],"protocol":["0","0"],"szSendQName":["0","req1"],"ip":["0","10.4.6.16"],"usename":["0","KCXP00"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"nProtocal":["0","0"],"nPort":["0","21000"],"serverName":["0","Cails"],"creditamtused":["0","0.00"],"szAddress":["0","10.4.6.14"],"receiveQName":["0","ans1"],"Password":["0","888888"],"UserName":["0","KCXP00"],"tc_out":["0","字段名称tc_out不存在"],"szServerName":["0","KCXP01"],"ServerName":["0","KCXP01"]},"410413-委托撤单":{"component_script_model":["0","410413-委托撤单"],"custid":["410411-买卖委托.custid","110303000001"],"custorgid":["410411-买卖委托.custorgid","1103"],"trdpwd":["410411-买卖委托.trdpwd","123321"],"netaddr":["410411-买卖委托.netaddr","127.0.0.1"],"orgid":["410411-买卖委托.orgid","1103"],"operway":["410411-买卖委托.operway","7"],"ext":["410411-买卖委托.ext","0"],"funcid":["0","410413"],"zxjt_wt_cj_flag":["账户参数表.zxjt_wt_cj_flag",""],"orderdate":["0","0"],"fundid":["410411-买卖委托.fundid","99004149"],"ordersno":["410411-买卖委托.ordersno","978"],"bsflag":["0",""],"msgok":["0",""],"cancel_status":["0",""],"ordersno_out":["0",""],"tc_flag":["0","0"],"tc_checkStr":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","-410413020;-410413020[-990268050]该笔委托已经全部成交或全部撤单ordersno = 978, orderdate = 20201014"],"tc_out":["0",""],"tc_out_check":["0",""],"resultstate":["0","1"],"nOverTime":["0","1200"],"serverName":["0","Cails"],"szReceiveQName":["0","ans1"],"szAddress":["0","10.4.6.14"],"protocol":["0","0"],"receiveQName":["0","ans1"],"Password":["0","888888"],"szSendQName":["0","req1"],"UserName":["0","KCXP00"],"ip":["0","10.4.6.16"],"usename":["0","KCXP00"],"szServerName":["0","KCXP01"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"ServerName":["0","KCXP01"],"nProtocal":["0","0"],"nPort":["0","21000"]},"410502撤单后-资金查询":{"component_script_model":["0","410502-资金查询"],"custid":["410502委托前-资金查询.custid","110303000001"],"custorgid":["410502委托前-资金查询.custorgid","1103"],"trdpwd":["410502委托前-资金查询.trdpwd","123321"],"netaddr":["410502委托前-资金查询.netaddr","127.0.0.1"],"orgid":["410502委托前-资金查询.orgid","1103"],"operway":["410502委托前-资金查询.operway","7"],"ext":["410502委托前-资金查询.ext","0"],"funcid":["0","410502"],"fundid":["410502委托前-资金查询.fundid","99004149"],"moneytype":["410502委托前-资金查询.moneytype","0"],"remark":["0",""],"zxjt_usetype":["账户参数表.zxjt_usetype3","cancelorder"],"zxjt_orderfrztype":["0",""],"zxjt_trade_type":["账户参数表.zxjt_trade_type","深A买"],"zxjt_yq_price":["410203-证券信息.zxjt_yq_price","16.06"],"zxjt_yq_qty":["410203-证券信息.zxjt_yq_qty","1000"],"zxjt_yq_orderfrzamt":["0","0.0"],"zxjt_pre_fundavl":["410502委托前-资金查询.fundavl","899999678780.00"],"zxjt_pre_fundbal":["410502委托前-资金查询.fundbal","900000000000.00"],"zxjt_pre_fund":["410502委托前-资金查询.fund","899999678780.00"],"zxjt_bondintr":["0",""],"zxjt_pre_creditbal":["0",""],"zxjt_pre_creditavl":["0",""],"zxjt_yq_restcreditrepay":["0",""],"zxjt_yq_orderfrzamt_fundavl":["0",""],"zxjt_stkcode":["0",""],"bsflag":["0",""],"zxjt_wt_cj_flag":["0",""],"market":["0",""],"creditrepayunfrz":["0",""],"feeunfrz":["0",""],"matchqty":["0",""],"matchamt":["0",""],"clearamt":["0",""],"matchqty2":["0",""],"clearamt2":["0",""],"zxjt_ar_sleep":["410502委托前-资金查询.zxjt_ar_sleep",""],"custid_out":["0","110303000001"],"fundid_out":["0","99004149"],"orgid_out":["0","1103"],"moneytype_out":["0","0"],"fundbal":["0","900000000000.00"],"fundavl":["0","899999662719.00"],"marketvalue":["0","903025381694.27"],"fund":["0","899999662719.00"],"stkvalue":["0","3025718975.27"],"fundseq":["0","0"],"fundloan":["0",""],"fundbuy":["0","337281.00"],"fundsale":["0","0.00"],"fundfrz":["0","0.00"],"fundlastbal":["0","900000000000.00"],"creditbal":["0","0.00"],"creditavl":["0","0.00"],"fundavl_check":["0","0.0;16061.0;false"],"fundbal_check":["0",""],"fund_check":["0",""],"creditavl_check":["0",""],"creditbal_check":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;资金查询成功"],"resultstate":["0","0"],"nOverTime":["0","1200"],"szReceiveQName":["0","ans1"],"protocol":["0","0"],"szSendQName":["0","req1"],"ip":["0","10.4.6.16"],"usename":["0","KCXP00"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"nProtocal":["0","0"],"nPort":["0","21000"],"serverName":["0","Cails"],"creditamtused":["0","0.00"],"szAddress":["0","10.4.6.14"],"receiveQName":["0","ans1"],"Password":["0","888888"],"UserName":["0","KCXP00"],"tc_out":["0","字段名称tc_out不存在"],"szServerName":["0","KCXP01"],"ServerName":["0","KCXP01"]},"410510-撤单后-当日委托明细查询":{"component_script_model":["0","410510-当日委托明细查询"],"custid":["410510-当日委托明细查询.custid","110303000001"],"custorgid":["410510-当日委托明细查询.custorgid","1103"],"trdpwd":["410510-当日委托明细查询.trdpwd","123321"],"netaddr":["410510-当日委托明细查询.netaddr","127.0.0.1"],"orgid":["410510-当日委托明细查询.orgid","1103"],"operway":["410510-当日委托明细查询.operway","7"],"ext":["410510-当日委托明细查询.ext","0"],"funcid":["0","410510"],"market":["410510-当日委托明细查询.market","0"],"fundid":["410510-当日委托明细查询.fundid","99004149"],"secuid":["410510-当日委托明细查询.secuid","0600061611"],"stkcode":["410510-当日委托明细查询.stkcode","000001"],"ordersno":["0",""],"ordergroup":["0",""],"bankcode":["0",""],"qryflag":["0","1"],"count":["0","200"],"poststr":["0","20201014|4,20201014|953,20201014|954,20201014|955,20201014|958,20201014|960,20201014|961,20201014|963,20201014|965,20201014|966,20201014|967,20201014|968,20201014|969,20201014|970,20201014|971,20201014|972,20201014|973,20201014|974,20201014|975,20201014|976,20201014|977,20201014|978"],"extsno":["0",""],"qryoperway":["0",""],"zxjt_yq_orderfrzamt":["0",""],"zxjt_wt_cj_flag":["0",""],"zxjt_orderfrztype":["0",""],"pre_orderid":["0",""],"zxjt_usetype":["0",""],"orderdate":["0","20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014"],"ordersno_out":["0","4,953,954,955,958,960,961,963,965,966,967,968,969,970,971,972,973,974,975,976,977,978"],"ordergroup_out":["0","4,953,954,955,958,960,961,963,965,966,967,968,969,970,971,972,973,974,975,976,977,978"],"custid_out":["0","110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001,110303000001"],"custname":["0","测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001,测试001"],"fundid_out":["0","99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149,99004149"],"moneytype":["0","0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"],"orgid_out":["0","1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103,1103"],"secuid_out":["0","0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611,0600061611"],"bsflag":["0","0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B"],"orderid":["0","AC000002,AC000467,AC000468,AC000469,AC000471,AC000473,AC000474,AC000476,AC000478,AC000479,AC000480,AC000481,AC000482,AC000483,AC000484,AC000485,AC000486,AC000487,AC000488,AC000489,AC000490,AC000491"],"reporttime":["0","000000,151255,151309,151319,151539,151611,151642,151713,151744,151816,151847,151918,151949,152020,152051,152122,152153,152224,152255,152326,152357,152428"],"opertime":["0","094338,151255,151308,151319,151539,151611,151642,151713,151744,151816,151847,151918,151949,152020,152051,152122,152153,152224,152255,152326,152357,152428"],"market_out":["0","0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"],"stkcode_out":["0","000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001,000001"],"stkname":["0","平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行,平安银行"],"prodcode":["0",""],"prodname":["0",""],"orderprice":["0","16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060,16.060"],"orderqty":["0","1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000"],"orderfrzamt":["0",".00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00,16061.00"],"matchqty":["0","0,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000"],"matchamt":["0",".00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00,16060.00"],"cancelqty":["0","1000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"],"orderstatus":["0","6,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8"],"seat":["0","390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599,390599"],"cancelflag":["0","F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F"],"operdate":["0","20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014,20201014"],"bondintr":["0",""],"operway_out":["0","7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7"],"remark":["0",",,,,,,,,,,,,,,,,,,,,,"],"matchamt_check":["0",""],"tc_allowerror":["0","1"],"tc_result":["0","0;委托查询成功"],"creditflag":["0","6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6"],"resultstate":["0","0"],"nOverTime":["0","1200"],"szReceiveQName":["0","ans1"],"protocol":["0","0"],"szSendQName":["0","req1"],"ip":["0","10.4.6.16"],"creditmethod":["0","0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"],"usename":["0","KCXP00"],"port":["0","21000"],"sendQName":["0","req1"],"passwd":["0","888888"],"nProtocal":["0","0"],"nPort":["0","21000"],"Ordergroup":["0","字段名称Ordergroup不存在"],"serverName":["0","Cails"],"szAddress":["0","10.4.6.14"],"receiveQName":["0","ans1"],"Password":["0","888888"],"UserName":["0","KCXP00"],"tc_out":["0","字段名称tc_out不存在"],"szServerName":["0","KCXP01"],"creditid":["0","0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"],"ServerName":["0","KCXP01"]},"账号解锁":{"component_script_model":["0","账号解锁"],"acct_id":["账户参数表.acct_id",""],"starttime":["账户参数表.starttime",""],"runtime":["0",""],"tc_allowerror":["0","1"],"tc_result":["0",""],"tc_flag":["0","0"],"tc_checkStr":["0",""],"tc_out":["0",""],"tc_out_check":["0",""]}}'
log.init_log_data(output,'test','test')


SET_TEMP = []


@api_view(['GET', 'POST'])
def get_req(request):
    """
    获取需求
    :param request:
    :return:
    """
    cases = None
    rqid = request.GET.get('rqid')  # 需求id
    if rqid is None:  # 查询需求根节点
        cases = Requirement.objects.filter(parent_id=0).values('id', 'name', 'parent_id')
    elif rqid is not None:  # 查询点击节点子需求
        cases = Requirement.objects.filter(parent_id=rqid).values('id', 'name', 'parent_id')
    return Response(cases)


@api_view(['GET', 'POST'])
def get_scene(request):
    """
    获取需求下场景
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 需求ID
    scene = ReqScene.objects.filter(req_id=rqid).values('id', 'scene_name')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_scene_detail(request):
    """
    获取场景组件
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 需求id
    scene = SceneSet.objects.filter(scene_id=rqid).values('component_name', 'com_id').order_by('order_id')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_cases(request):
    """
    获取场景下用例名称
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')
    scene = Cases.objects.filter(scene_id=rqid).values('name', 'case_id')
    return Response(scene)


@api_view(['GET', 'POST'])
def get_cases_io(request):
    """
    获取用例IO
    :param request:
    :return:
    """
    case_name = request.GET.get('case_name')  #
    scenes = SceneSetIo.objects.filter(name=case_name).values('description', 'value').order_by('sequence')
    case_io = []
    for scene in scenes:
        name = scene['description'].split("\0")
        value = scene['value'].split("\0")
        case_io.append(dict(zip(name, value)))
    return Response(case_io)


@api_view(['GET', 'POST'])
def get_component_col(request):
    """
    获取组件栏位值
    :param request:
    :return:
    """
    component = request.GET.get('component')  #
    component_id = Components.objects.filter(script_name=component).values('id')
    component_col = ParameterRules.objects.filter(fk_com_id=component_id[0]['id']).values('target_field',
                                                                                          'description',
                                                                                          'parameter_value').order_by(
        'id')
    return Response(component_col)


@api_view(['GET', 'POST'])
def get_scene_params(request):
    """
    获取场景组件栏位值，默认值等信息
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 场景id
    component_ids = SceneSet.objects.filter(scene_id=rqid).values('com_id', 'component_name').order_by('order_id')
    components_params = []
    for component_id in component_ids:
        component_col = ParameterRules.objects.filter(fk_com_id=component_id['com_id']).values('target_field',
                                                                                               'description',
                                                                                               'parameter_value').order_by(
            'id')
        components_params.append({component_id['component_name']: component_col})
    return Response(components_params)


@api_view(['GET', 'POST'])
def get_scene_cases_io(request):
    """
    获取场景组件栏位值，默认值等信息
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 场景ID
    current_page = int(request.GET.get('currentPage'))  # 当前页数
    page_size = int(request.GET.get('pageSize'))  # 每页数据数
    cases_list = Cases.objects.filter(scene_id=rqid).values('case_id', 'name').order_by('name')[
                 (current_page - 1) * page_size:current_page * page_size]
    cases_io = []
    for case in cases_list:
        case_id = case.get('case_id')
        case_name = case.get('name')
        case_io_all = CaseSetIo.objects.filter(case_id=case_id).values('name', 'description', 'value',
                                                                       'sequence').order_by('sequence')
        case_io_one = {'name': case_name}
        for set_io in case_io_all:
            description = set_io['description'].split("\0")
            io_value = set_io['value'].split("\0")
            sequence = set_io['sequence']
            set_io_dict = dict(zip(description, io_value))
            for key, value in set_io_dict.items():  # 暂时将各个组件IO放在一个字典中，用sequence标识区分
                case_io_one["sequence_" + str(sequence) + "_" + key] = value.lstrip('[').rstrip(']')
        cases_io.append(case_io_one)
    return Response(cases_io)


@api_view(['GET', 'POST'])
def get_scene_set_io(request):
    """
    获取场景下值传递、校验点等信息
    :param request:
    :return:
    """
    rqid = request.GET.get('rqid')  # 场景id
    data_type = request.GET.get('type')  # 数据类型
    set_io = SceneSetIo.objects.filter(scene_id=rqid, type=data_type).values('name', 'assign').order_by(
        'sequence')
    return Response(set_io)


@api_view(['GET', 'POST'])
def get_set(request):
    """
    获取测试集
    :param request:
    :return:
    """
    level = request.GET.get('level')  # 级别
    if level == '0':
        s = Sets.objects.filter(level=0).values('id', 'group_name').order_by(
            'id')
        for index in range(len(s)):
            s[index]['name'] = s[index]['group_name']
    else:
        set_id = request.GET.get('id')  # 测试集ID
        s = Sets.objects.filter(parent_id=set_id).values('id', 'set_name', 'set_id').order_by(
            'id')
        # 统一输出格式
        for index in range(len(s)):
            s[index]['name'] = s[index]['set_name']
    return Response(s)


@api_view(['GET', 'POST'])
def get_cases_in_set(request):
    """
    获取测试集下用例
    :param request:
    :return:
    """
    test_set = request.GET.get('set')
    cases = CasesInSet.objects.filter(set_id=test_set).values('name', 'case_id').order_by('order_id')
    return Response(cases)


@api_view(['GET', 'POST'])
def get_req_of_case(request):
    """
    获取用例所在场景，第一级
    :param request:
    :return:
    """
    global SET_TEMP
    level = request.GET.get('level')  # 级别
    set_id = request.GET.get('set')
    tier = request.GET.get('tier')
    if level == "0":
        SET_TEMP = []
        with connection.cursor() as cursor:
            cursor.execute(
                "select distinct cases.tier from cases join cases_in_set on cases.case_id = cases_in_set.case_id where cases_in_set.set_id = %s",
                [set_id])
            row = cursor.fetchall()
        row_list = []
        for r in row:
            if r[0][0:3] not in row_list:
                row_list.append(r[0][0:3])
        for r in row:
            i = 0
            length = len(r[0])
            while i + 3 < length:
                if r[0][0:i + 3] not in SET_TEMP:
                    SET_TEMP.append(r[0][0:i + 3])
                i = i + 3
        req = Cases.objects.filter(tier__in=row_list).values("id", "name", "case_id", "tier")
        return Response(req)
    else:
        set_row = []
        for s in SET_TEMP:
            if s[:-3] == tier:
                set_row.append(s)
        req = Cases.objects.filter(tier__in=set_row).values("id", "name", "case_id", "tier")
        if len(req) == 0 and tier[-3:] is not "000":
            tier = tier + "000"
            with connection.cursor() as cursor:
                cursor.execute(
                    "select cases.id,cases_in_set.name,cases.case_id,cases.tier from cases join cases_in_set on cases.case_id = cases_in_set.case_id where cases_in_set.set_id = %s and cases.tier = %s",
                    [set_id, tier])
                row = cursor.fetchall()
            req_temp = []
            for r in row:
                req_temp.append(dict(zip(['id', 'name', 'case_id', 'tier'], list(r))))
            req = req_temp
        return Response(req)


@api_view(['GET', 'POST'])
def run(request):
    namesrv_addr = request.GET.get('nameSrvAddr')
    topic = request.GET.get('topic')
    set_names = request.GET.get('setNames')
    my_producer = MyProducer(namesrv_addr, topic)
    my_producer.start()
    ret = my_producer.producing(set_names.split(','))
    my_producer.shutdown()
    return Response(ret)


def get_req_leaf_in_set(test_set, set_id, all_req):
    req = SetReq.objects.filter(set_id=test_set, parent_id=set_id).values('id', 'parent_id', 'name', 'tier').order_by('id')
    if len(req) == 0:
        set_id = SetReq.objects.filter(set_id=test_set, id=set_id).values('id').order_by('id')
        for i in set_id:
            if i['id'] not in all_req:
                all_req.append(i['id'])
    else:
        for child in req:
            get_req_leaf_in_set(test_set, child['id'], all_req)


@api_view(['GET', 'POST'])
def get_cases_to_run(request):
    # 用例或场景id
    checked_cases = request.GET.get('checkedCases').split(',')
    # 测试集id
    set_id = request.GET.get('set')
    cases = []
    req_all = []
    # 遍历id,若已是用例id,直接将其加入cases列表,若是场景id,则循环递归出该场景下所有用例id并加入cases列表
    for node in checked_cases:
        case_id = Cases.objects.filter(id=node).values('case_id')[0]['case_id']
        if case_id is None:
            req = []
            get_req_leaf_in_set(set_id, node, req)
            for r in req:
                if r not in req_all:
                    req_all.append(r)
        else:
            if case_id not in cases:
                cases.append(case_id)
    for r in req_all:
        case_id_temp = Cases.objects.filter(parent_id=r).values('case_id').order_by('id')
        for case in case_id_temp:
            case_id = CasesInSet.objects.filter(case_id=case['case_id'], set_id=set_id).values('case_id')
            if case['case_id'] not in cases and len(case_id) is not 0:
                cases.append(case['case_id'])
    return Response(cases)


# 获取所有执行记录
@api_view(['GET', 'POST'])
def get_run(request):
    run_log = Run.objects.values('run_name', 'start', 'finish', 'run_id')
    return Response(run_log)


# 获取指定执行记录具体信息
@api_view(['GET', 'POST'])
def get_run_set(request):
    run_id = request.GET.get('run_id')
    run_set = RunSet.objects.filter(run_id=run_id, case_type='0').values('case_clazz', 'case_id',
                                                                         'case_state').order_by('order_id')
    return Response(run_set)
