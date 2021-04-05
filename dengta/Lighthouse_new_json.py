#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 已知题库的JSON字符串，生成JS文件
import json

# subjectType:0单选1多选
j = '{"msg":"操作成功!","code":200,"success":true,"data":{"subjectInfoList":[{"subjectTitle":"习近平总书记在纪念邓小平同志诞辰110周年座谈会的讲话中指出，（），是邓小平同志一生最鲜明的政治品格，也永远是中国共产党人应该挺起的精神脊梁。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"信念坚定","isRight":"1","optionType":"A"},{"optionTitle":"热爱人民","isRight":"0","optionType":"B"},{"optionTitle":"执着精神","isRight":"0","optionType":"C"},{"optionTitle":"实事求是","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是中国特色社会主义最本质的特征。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"马克思主义的指导","isRight":"0","optionType":"A"},{"optionTitle":"解放生产力，发展生产力","isRight":"0","optionType":"B"},{"optionTitle":"中国共产党的领导","isRight":"1","optionType":"C"},{"optionTitle":"实现共同富裕","isRight":"0","optionType":"D"}]},{"subjectTitle":"坚持党中央集中统一领导，确立和维护党的（），是全党全国各族人民的共同愿望，是推进全面从严治党、提高党的创造力凝聚力战斗力的迫切要求，是保持党和国家事业发展正确方向的根本保证。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"领导核心","isRight":"1","optionType":"A"},{"optionTitle":"领导权威","isRight":"0","optionType":"B"},{"optionTitle":"领导地位","isRight":"0","optionType":"C"},{"optionTitle":"领导能力","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们将继续坚持以（）为中心，致力于建设改革发展成果真正惠及人民，经济、政治、文化、社会、生态文明全面发展的小康社会。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"稳定发展","isRight":"0","optionType":"A"},{"optionTitle":"改革开放","isRight":"0","optionType":"B"},{"optionTitle":"社会和谐","isRight":"0","optionType":"C"},{"optionTitle":"经济建设","isRight":"1","optionType":"D"}]},{"subjectTitle":"党的十八大以来，党中央从坚持和发展中国特色社会主义全局出发，提出并形成了全面建成小康社会、全面深化改革、全面依法治国、全面从严治党的战略布局。全面建成小康社会是我们的（），全面深化改革、全面依法治国、全面从严治党是三大（）。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"发展目标 战略措施","isRight":"0","optionType":"A"},{"optionTitle":"奋斗目标 具体举措","isRight":"0","optionType":"B"},{"optionTitle":"战略目标 战略举措","isRight":"1","optionType":"C"},{"optionTitle":"发展方略 发展举措","isRight":"0","optionType":"D"}]},{"subjectTitle":"发展依然是当代中国的第一要务，中国执政者的首要使命就是集中力量（），逐步实现共同富裕。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"做大经济总量","isRight":"0","optionType":"A"},{"optionTitle":"提高发展质量","isRight":"0","optionType":"B"},{"optionTitle":"提高人民生活水平","isRight":"1","optionType":"C"},{"optionTitle":"推进城乡一体化发展","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是国家的生命线、人民的幸福线，我们要坚持把以经济建设为中心作为兴国之要、把四项基本原则作为立国之本、把改革开放作为强国之路，不能有丝毫动摇。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"以人民为中心","isRight":"0","optionType":"A"},{"optionTitle":"中国特色社会主义道路","isRight":"0","optionType":"B"},{"optionTitle":"党的基本路线","isRight":"1","optionType":"C"},{"optionTitle":"全面建成小康社会","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是党执政兴国的第一要务，是解决中国所有问题的关键。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"改革","isRight":"0","optionType":"A"},{"optionTitle":"稳定","isRight":"0","optionType":"B"},{"optionTitle":"开放","isRight":"0","optionType":"C"},{"optionTitle":"发展","isRight":"1","optionType":"D"}]},{"subjectTitle":"（）是当代中国最鲜明的特色，是我们党在新的历史时期最鲜明的旗帜，是决定当代中国命运的关键抉择。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"改革开放","isRight":"1","optionType":"A"},{"optionTitle":"经济发展","isRight":"0","optionType":"B"},{"optionTitle":"社会稳定","isRight":"0","optionType":"C"},{"optionTitle":"理论创新","isRight":"0","optionType":"D"}]},{"subjectTitle":"带领人民创造幸福生活，是我们党始终不渝的奋斗目标。我们要顺应人民群众对美好生活的向往，坚持（）的发展思想。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"以提高质量和效益为中心","isRight":"0","optionType":"A"},{"optionTitle":"适应和引领新常态","isRight":"0","optionType":"B"},{"optionTitle":"以人民为中心","isRight":"1","optionType":"C"},{"optionTitle":"中高速发展","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是中国共产党的根本政治立场，是马克思主义政党区别于其他政党的显著标志。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"人民立场","isRight":"1","optionType":"A"},{"optionTitle":"共产主义","isRight":"0","optionType":"B"},{"optionTitle":"以人为本","isRight":"0","optionType":"C"},{"optionTitle":"群众路线","isRight":"0","optionType":"D"}]},{"subjectTitle":"坚持不忘初心、继续前进，就要始终不渝走和平发展道路，始终不渝奉行（）的开放战略，加强同各国的友好往来，同各国人民一道，不断把人类和平与发展的崇高事业推向前进。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"平等互惠","isRight":"0","optionType":"A"},{"optionTitle":"平等友善","isRight":"0","optionType":"B"},{"optionTitle":"互利共赢","isRight":"1","optionType":"C"},{"optionTitle":"独立自主","isRight":"0","optionType":"D"}]},{"subjectTitle":"全党要以（）的政治勇气，着力解决党自身存在的突出问题，不断增强党自我净化、自我完善、自我革新、自我提高能力，经受“四大考验”、克服“四种危险”。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"改革创新","isRight":"0","optionType":"A"},{"optionTitle":"自我革命","isRight":"1","optionType":"B"},{"optionTitle":"管党治党","isRight":"0","optionType":"C"},{"optionTitle":"全面从严","isRight":"0","optionType":"D"}]},{"subjectTitle":"中国共产党作为执政党，面临的最大威胁就是（）。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"腐败","isRight":"1","optionType":"A"},{"optionTitle":"脱离群众","isRight":"0","optionType":"B"},{"optionTitle":"能力不足","isRight":"0","optionType":"C"},{"optionTitle":"作风问题","isRight":"0","optionType":"D"}]},{"subjectTitle":"伟大长征精神，是中国共产党人及其领导的人民军队革命风范的生动反映，是中华民族自强不息的民族品格的集中展示，是以（）为核心的民族精神的最高体现。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"爱国主义","isRight":"1","optionType":"A"},{"optionTitle":"集体主义","isRight":"0","optionType":"B"},{"optionTitle":"艰苦奋斗","isRight":"0","optionType":"C"},{"optionTitle":"独立自主","isRight":"0","optionType":"D"}]},{"subjectTitle":"长征胜利启示我们：心中有（），脚下有力量；没有牢不可破的理想信念，没有崇高理想信念的有力支撑，要取得长征胜利是不可想象的。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"信念","isRight":"0","optionType":"A"},{"optionTitle":"理想","isRight":"0","optionType":"B"},{"optionTitle":"目标","isRight":"0","optionType":"C"},{"optionTitle":"信仰","isRight":"1","optionType":"D"}]},{"subjectTitle":"在新的长征路上，全党必须牢记，（）的问题，是检验一个政党、一个政权性质的试金石。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"作风建设","isRight":"0","optionType":"A"},{"optionTitle":"为什么人、靠什么人","isRight":"1","optionType":"B"},{"optionTitle":"理想信念","isRight":"0","optionType":"C"},{"optionTitle":"我是谁、为了谁","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是引领发展的第一动力，我们必须解放思想、实事求是、与时俱进，坚定不移推进理论创新、实践创新、制度创新以及其他各方面创新，让党和国家事业始终充满创造活力、不断打开创新局面。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"科技","isRight":"0","optionType":"A"},{"optionTitle":"人才","isRight":"0","optionType":"B"},{"optionTitle":"改革","isRight":"0","optionType":"C"},{"optionTitle":"创新","isRight":"1","optionType":"D"}]},{"subjectTitle":"（），是中国革命、建设、改革不断取得胜利最根本的保证，是中国特色社会主义最本质的特征，也是中国特色社会主义的最大优势，必须毫不动摇坚持和完善。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"以人民为中心","isRight":"0","optionType":"A"},{"optionTitle":"中国共产党的领导","isRight":"1","optionType":"B"},{"optionTitle":"以马克思主义为指导","isRight":"0","optionType":"C"},{"optionTitle":"加强党的建设","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是改革开放以来党的全部理论和实践的主题。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"以人民为中心","isRight":"0","optionType":"A"},{"optionTitle":"实现共同富裕","isRight":"0","optionType":"B"},{"optionTitle":"中国特色社会主义","isRight":"1","optionType":"C"},{"optionTitle":"实现中华民族伟大复兴","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们坚定不移推进全面从严治党，着力解决人民群众反映最强烈、对党的执政基础威胁最大的突出问题，形成了反腐败斗争（）态势。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"决胜性","isRight":"0","optionType":"A"},{"optionTitle":"决定性","isRight":"0","optionType":"B"},{"optionTitle":"震慑性","isRight":"0","optionType":"C"},{"optionTitle":"压倒性","isRight":"1","optionType":"D"}]},{"subjectTitle":"中国特色社会主义不断取得的重大成就，意味着近代以来久经磨难的中华民族实现了（）的历史性飞跃，意味着社会主义在中国焕发出强大生机活力并不断开辟发展新境界，意味着中国特色社会主义拓展了发展中国家走向现代化的途径，为解决人类问题贡献了中国智慧、提供了中国方案。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"从站起来、富起来到强起来","isRight":"1","optionType":"A"},{"optionTitle":"马克思主义中国化","isRight":"0","optionType":"B"},{"optionTitle":"马克思主义基本原理同中国具体实际相结合","isRight":"0","optionType":"C"},{"optionTitle":"中华民族伟大复兴","isRight":"0","optionType":"D"}]},{"subjectTitle":"在新的时代条件下，我们要进行伟大斗争、建设伟大工程、推进伟大事业、实现伟大梦想，仍然需要保持和发扬马克思主义政党（）的理论品格，勇于推进实践基础上的理论创新。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"理论联系实际","isRight":"0","optionType":"A"},{"optionTitle":"实事求是","isRight":"0","optionType":"B"},{"optionTitle":"与时俱进","isRight":"1","optionType":"C"},{"optionTitle":"改革创新","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们党是用马克思主义武装起来的政党，（）是我们共产党人理想信念的灵魂。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"科学社会主义","isRight":"0","optionType":"A"},{"optionTitle":"马克思主义","isRight":"1","optionType":"B"},{"optionTitle":"共产主义","isRight":"0","optionType":"C"},{"optionTitle":"人的全面发展","isRight":"0","optionType":"D"}]},{"subjectTitle":"新中国成立以来特别是改革开放以来，中国发生了深刻变革，置身这一历史巨变之中的中国人更有资格、更有能力揭示这其中所蕴含的历史经验和发展规律，为发展马克思主义作出中国的（）贡献。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"原创性","isRight":"1","optionType":"A"},{"optionTitle":"拓展性","isRight":"0","optionType":"B"},{"optionTitle":"创新性","isRight":"0","optionType":"C"},{"optionTitle":"发展性","isRight":"0","optionType":"D"}]},{"subjectTitle":"回顾党的奋斗历程可以发现，我们党之所以能够不断历经艰难困苦创造新的辉煌，很重要的一条就是我们党始终重视（），坚持用科学理论武装广大党员、干部的头脑，使全党始终保持统一的思想、坚定的意志、强大的战斗力。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"党的作风建设","isRight":"0","optionType":"A"},{"optionTitle":"党的理论建设","isRight":"0","optionType":"B"},{"optionTitle":"思想建党、理论强党","isRight":"1","optionType":"C"},{"optionTitle":"党的组织建设","isRight":"0","optionType":"D"}]},{"subjectTitle":"到2020年（），是我们党向人民、向历史作出的庄严承诺。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"人民生活总体达到小康水平","isRight":"0","optionType":"A"},{"optionTitle":"全面建设小康社会","isRight":"0","optionType":"B"},{"optionTitle":"人民生活基本达到小康水平","isRight":"0","optionType":"C"},{"optionTitle":"全面建成小康社会","isRight":"1","optionType":"D"}]},{"subjectTitle":"我们不仅要全面建成小康社会，而且要考虑更长远时期的发展要求，加快形成（）的经济发展方式。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"适应经济发展新常态","isRight":"1","optionType":"A"},{"optionTitle":"平稳增长","isRight":"0","optionType":"B"},{"optionTitle":"规模扩张式","isRight":"0","optionType":"C"},{"optionTitle":"质量效益型","isRight":"0","optionType":"D"}]},{"subjectTitle":"关于转方式调结构的重点任务，《中共中央关于制定国民经济和社会发展第十三个五年规划的建议》提出了具体要求，关键是要实现（）的发展。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"可持续","isRight":"0","optionType":"A"},{"optionTitle":"集约型","isRight":"0","optionType":"B"},{"optionTitle":"稳增长","isRight":"0","optionType":"C"},{"optionTitle":"有质量、有效益","isRight":"1","optionType":"D"}]},{"subjectTitle":"（）是国土空间开发保护的基础制度，也是从源头上保护生态环境的根本举措。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"资源功能区","isRight":"0","optionType":"A"},{"optionTitle":"环境保护区","isRight":"0","optionType":"B"},{"optionTitle":"主体功能区","isRight":"1","optionType":"C"},{"optionTitle":"资源保护区","isRight":"0","optionType":"D"}]},{"subjectTitle":"全面小康，覆盖的人口要全面，是惠及（）的小康。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"最广大人民群众","isRight":"0","optionType":"A"},{"optionTitle":"绝大多数人口","isRight":"0","optionType":"B"},{"optionTitle":"全体人民","isRight":"1","optionType":"C"},{"optionTitle":"不同社会群体","isRight":"0","optionType":"D"}]},{"subjectTitle":"《中共中央关于制定国民经济和社会发展第十三个五年规划的建议》把（）作为全面建成小康社会的基本标志，强调实施精准扶贫、精准脱贫，以更大决心、更精准思路、更有力措施，采取超常举措，实施脱贫攻坚工程，确保我国现行标准下农村贫困人口实现脱贫、贫困县全部摘帽、解决区域性整体贫困。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"农村贫困人口脱贫","isRight":"1","optionType":"A"},{"optionTitle":"城乡贫困人口脱贫","isRight":"0","optionType":"B"},{"optionTitle":"贫困县脱贫","isRight":"0","optionType":"C"},{"optionTitle":"区域脱贫","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们要立下愚公移山志，咬定目标、苦干实干，坚决打赢脱贫攻坚战，确保到（）所有贫困地区和贫困人口一道迈入全面小康社会。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"2019年","isRight":"0","optionType":"A"},{"optionTitle":"2020年","isRight":"1","optionType":"B"},{"optionTitle":"2025年","isRight":"0","optionType":"C"},{"optionTitle":"2030年","isRight":"0","optionType":"D"}]},{"subjectTitle":"加快推进深度贫困地区脱贫攻坚，要按照党中央统一部署，坚持（）基本方略，坚持中央统筹、省负总责、市县抓落实的管理体制，坚持党政一把手负总责的工作责任制，坚持专项扶贫、行业扶贫、社会扶贫等多方力量、多种举措有机结合和互为支撑的“三位一体”大扶贫格局。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"政策扶贫资金扶贫","isRight":"0","optionType":"A"},{"optionTitle":"精准扶贫精准脱贫","isRight":"1","optionType":"B"},{"optionTitle":"区域扶贫整体脱贫","isRight":"0","optionType":"C"},{"optionTitle":"扶贫到户扶贫到人","isRight":"0","optionType":"D"}]},{"subjectTitle":"深度贫困地区党委和政府要坚持把（）作为“十三五”期间头等大事和第一民生工程来抓。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"赶超发展","isRight":"0","optionType":"A"},{"optionTitle":"脱贫攻坚","isRight":"1","optionType":"B"},{"optionTitle":"城乡统筹","isRight":"0","optionType":"C"},{"optionTitle":"公共服务","isRight":"0","optionType":"D"}]},{"subjectTitle":"把（）的发展思想体现在经济社会发展各个环节，做到老百姓关心什么、期盼什么，改革就要抓住什么、推进什么，通过改革给人民群众带来更多获得感。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"可持续","isRight":"0","optionType":"A"},{"optionTitle":"以人民为中心","isRight":"1","optionType":"B"},{"optionTitle":"统筹兼顾","isRight":"0","optionType":"C"},{"optionTitle":"以人为本","isRight":"0","optionType":"D"}]},{"subjectTitle":"各地区各部门要牢固树立全局意识、责任意识，把抓改革作为一项重大政治责任，坚定改革决心和信心，增强推进改革的思想自觉和行动自觉，既当改革（）、又当改革（）。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"谋划者 参与者","isRight":"0","optionType":"A"},{"optionTitle":"促进派 实干家","isRight":"1","optionType":"B"},{"optionTitle":"谋划者 实干家","isRight":"0","optionType":"C"},{"optionTitle":"促进派 急先锋","isRight":"0","optionType":"D"}]},{"subjectTitle":"（），是社会主义法治的根本要求，是全面推进依法治国题中应有之义。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"坚持中国特色社会主义","isRight":"0","optionType":"A"},{"optionTitle":"坚持四项基本原则","isRight":"0","optionType":"B"},{"optionTitle":"坚持以人民为中心","isRight":"0","optionType":"C"},{"optionTitle":"坚持党的领导","isRight":"1","optionType":"D"}]},{"subjectTitle":"（）是社会主义法律的基本属性，是社会主义法治的基本要求。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"公平","isRight":"0","optionType":"A"},{"optionTitle":"正义","isRight":"0","optionType":"B"},{"optionTitle":"平等","isRight":"1","optionType":"C"},{"optionTitle":"以人为本","isRight":"0","optionType":"D"}]},{"subjectTitle":"在推进依法治国过程中，必须大力弘扬（），弘扬中华传统美德，培育社会公德、职业道德、家庭美德、个人品德，提高全民族思想道德水平，为依法治国创造良好人文环境。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"集体主义精神","isRight":"0","optionType":"A"},{"optionTitle":"社会主义核心价值观","isRight":"1","optionType":"B"},{"optionTitle":"共产主义理想","isRight":"0","optionType":"C"},{"optionTitle":"社会主义法治观念","isRight":"0","optionType":"D"}]},{"subjectTitle":"全面推进依法治国总目标是（），建设社会主义法治国家。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"构建社会主义法治体系","isRight":"0","optionType":"A"},{"optionTitle":"形成法治实施体系","isRight":"0","optionType":"B"},{"optionTitle":"形成法律规范体系","isRight":"0","optionType":"C"},{"optionTitle":"建设中国特色社会主义法治体系","isRight":"1","optionType":"D"}]},{"subjectTitle":"要完善党内法规制定体制机制，注重党内法规同国家法律的衔接和协调，构建以（）为根本、若干配套党内法规为支撑的党内法规制度体系，提高党内法规执行力。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"党章","isRight":"1","optionType":"A"},{"optionTitle":"宪法","isRight":"0","optionType":"B"},{"optionTitle":"国家法律","isRight":"0","optionType":"C"},{"optionTitle":"各类法律","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是我国宪法确定的治理国家的基本方略。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"依法行政","isRight":"0","optionType":"A"},{"optionTitle":"依法执政","isRight":"0","optionType":"B"},{"optionTitle":"依法治国","isRight":"1","optionType":"C"},{"optionTitle":"依法决策","isRight":"0","optionType":"D"}]},{"subjectTitle":"要坚持把（）作为依法治国的长期基础性工作，采取有力措施加强法制宣传教育。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"全民守法","isRight":"0","optionType":"A"},{"optionTitle":"全民普法","isRight":"0","optionType":"B"},{"optionTitle":"全民普法和守法","isRight":"1","optionType":"C"},{"optionTitle":"全民法治观念","isRight":"0","optionType":"D"}]},{"subjectTitle":"要坚持司法体制改革的正确政治方向，坚持以（）为根本尺度，坚持符合国情和遵循司法规律相结合，坚持问题导向、勇于攻坚克难，坚定信心，凝聚共识，锐意进取，破解难题，坚定不移深化司法体制改革，不断促进社会公平正义。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"提高司法水平","isRight":"0","optionType":"A"},{"optionTitle":"完善司法责任制","isRight":"0","optionType":"B"},{"optionTitle":"完善司法管理体制","isRight":"0","optionType":"C"},{"optionTitle":"提高司法公信力","isRight":"1","optionType":"D"}]},{"subjectTitle":"（）是维护社会公平正义的最后一道防线。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"司法","isRight":"1","optionType":"A"},{"optionTitle":"社会保障","isRight":"0","optionType":"B"},{"optionTitle":"执法","isRight":"0","optionType":"C"},{"optionTitle":"立法","isRight":"0","optionType":"D"}]},{"subjectTitle":"要紧紧牵住（）这个“牛鼻子”，凡是进入法官、检查官员额的，要在司法一线办案，对案件质量终身负责。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"司法公正","isRight":"0","optionType":"A"},{"optionTitle":"司法责任制","isRight":"1","optionType":"B"},{"optionTitle":"司法监督","isRight":"0","optionType":"C"},{"optionTitle":"司法权力运行机制","isRight":"0","optionType":"D"}]},{"subjectTitle":"法律是准绳，任何时候都必须遵循；道德是（），任何时候都不可忽视。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"基石","isRight":"1","optionType":"A"},{"optionTitle":"关键","isRight":"0","optionType":"B"},{"optionTitle":"基础","isRight":"0","optionType":"C"},{"optionTitle":"原则","isRight":"0","optionType":"D"}]},{"subjectTitle":"革命理想高于天。（）是我们共产党人的最高理想，而这个最高理想是需要一代又一代人接力奋斗的。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"实现社会主义","isRight":"0","optionType":"A"},{"optionTitle":"实现中国梦","isRight":"0","optionType":"B"},{"optionTitle":"实现中华民族伟大复兴","isRight":"0","optionType":"C"},{"optionTitle":"实现共产主义","isRight":"1","optionType":"D"}]},{"subjectTitle":"在所有党的纪律和规矩中，第一位的是（）。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"政治纪律和政治规矩","isRight":"1","optionType":"A"},{"optionTitle":"组织纪律","isRight":"0","optionType":"B"},{"optionTitle":"群众纪律","isRight":"0","optionType":"C"},{"optionTitle":"廉洁纪律","isRight":"0","optionType":"D"}]},{"subjectTitle":"各级党委要在思想认识、方法措施上跟上全面从严治党战略部署，把纪律挺在前面，发现问题就要提提领子、扯扯袖子，使（）成为常态。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"红红脸、出出汗","isRight":"1","optionType":"A"},{"optionTitle":"洗洗澡、治治病","isRight":"0","optionType":"B"},{"optionTitle":"组织处理","isRight":"0","optionType":"C"},{"optionTitle":"纪律处分","isRight":"0","optionType":"D"}]},{"subjectTitle":"作风问题本质上是（）问题。对我们共产党人来讲，能不能解决好作风问题，是衡量对马克思主义信仰、对社会主义和共产主义信念、对党和人民忠诚的一把十分重要的尺子。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"信仰","isRight":"0","optionType":"A"},{"optionTitle":"党性","isRight":"1","optionType":"B"},{"optionTitle":"纪律","isRight":"0","optionType":"C"},{"optionTitle":"宗旨","isRight":"0","optionType":"D"}]},{"subjectTitle":"坚持党对国有企业的领导不动摇，发挥企业党组织的（）作用，保证党和国家方针政策、重大部署在国有企业贯彻执行。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"领导核心","isRight":"0","optionType":"A"},{"optionTitle":"政治核心","isRight":"0","optionType":"B"},{"optionTitle":"领导核心和政治核心","isRight":"1","optionType":"C"},{"optionTitle":"战斗堡垒","isRight":"0","optionType":"D"}]},{"subjectTitle":"（），是我国国有企业的光荣传统，是国有企业的“根”和“魂”，是我国国有企业的独特优势。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"坚持党的领导、加强党的建设","isRight":"1","optionType":"A"},{"optionTitle":"全心全意依靠工人阶级","isRight":"0","optionType":"B"},{"optionTitle":"国有企业党组织的领导作用","isRight":"0","optionType":"C"},{"optionTitle":"党管干部","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是党内政治生活的重要内容和载体，是党组织对党员进行教育管理监督的重要形式。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"党的作风建设","isRight":"0","optionType":"A"},{"optionTitle":"党的组织生活","isRight":"1","optionType":"B"},{"optionTitle":"党的政治纪律","isRight":"0","optionType":"C"},{"optionTitle":"党的政治规矩","isRight":"0","optionType":"D"}]},{"subjectTitle":"全党要深刻认识到，（）是永葆党的肌体健康的生命之源，要不断增强向体内病灶开刀的自觉性，使积极开展监督、主动接受监督成为全党的自觉行动。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"舆论监督","isRight":"0","optionType":"A"},{"optionTitle":"群众监督","isRight":"0","optionType":"B"},{"optionTitle":"纪委监督","isRight":"0","optionType":"C"},{"optionTitle":"党内监督","isRight":"1","optionType":"D"}]},{"subjectTitle":"共享理念实质就是坚持（）的发展思想，体现的是逐步实现共同富裕的要求。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"成果共享","isRight":"0","optionType":"A"},{"optionTitle":"以人民为中心","isRight":"1","optionType":"B"},{"optionTitle":"为人民服务","isRight":"0","optionType":"C"},{"optionTitle":"公平公正","isRight":"0","optionType":"D"}]},{"subjectTitle":"推进（），是适应和引领经济发展新常态的重大创新，是适应国际金融危机发生后综合国力竞争新形势的主动选择，是适应我国经济发展新常态的必然要求。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"供给侧结构性改革","isRight":"1","optionType":"A"},{"optionTitle":"产业结构改革","isRight":"0","optionType":"B"},{"optionTitle":"区域协调发展","isRight":"0","optionType":"C"},{"optionTitle":"“五位一体”协调发展","isRight":"0","optionType":"D"}]},{"subjectTitle":"推进供给侧结构性改革，要从（）入手，重点是促进产能过剩有效化解，促进产业优化重组，降低企业成本，发展战略性新兴产业和现代服务业，增加公共产品和服务供给，提高供给结构对需求变化的适应性和灵活性。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"生产端","isRight":"1","optionType":"A"},{"optionTitle":"消费端","isRight":"0","optionType":"B"},{"optionTitle":"投资端","isRight":"0","optionType":"C"},{"optionTitle":"供给端","isRight":"0","optionType":"D"}]},{"subjectTitle":"实施（）战略，是应对发展环境变化、把握发展自主权、提高核心竞争力的必然选择，是加快转变经济发展方式、破解经济发展深层次矛盾和问题的必然选择，是更好引领我国经济发展新常态、保持我国经济持续健康发展的必然选择。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"科技创新","isRight":"0","optionType":"A"},{"optionTitle":"创新驱动发展","isRight":"1","optionType":"B"},{"optionTitle":"供给侧结构性改革","isRight":"0","optionType":"C"},{"optionTitle":"协调发展","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是生态文明建设的必然要求，代表了当今科技和产业变革方向，是最有前途的发展领域。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"绿色发展","isRight":"1","optionType":"A"},{"optionTitle":"协调发展","isRight":"0","optionType":"B"},{"optionTitle":"共享发展","isRight":"0","optionType":"C"},{"optionTitle":"环保产业","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是科技和经济紧密结合的重要力量，应该成为技术创新决策、研发投入、科研组织、成果转化的主体。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"企业","isRight":"1","optionType":"A"},{"optionTitle":"高校","isRight":"0","optionType":"B"},{"optionTitle":"科研院所","isRight":"0","optionType":"C"},{"optionTitle":"创新平台","isRight":"0","optionType":"D"}]},{"subjectTitle":"防止发生（）金融风险是金融工作的永恒主题。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"衍生性","isRight":"0","optionType":"A"},{"optionTitle":"规模性","isRight":"0","optionType":"B"},{"optionTitle":"连锁性","isRight":"0","optionType":"C"},{"optionTitle":"系统性","isRight":"1","optionType":"D"}]},{"subjectTitle":"坚定中国特色社会主义制度自信，首先要坚定对中国特色社会主义（）的自信，增强走中国特色社会主义政治发展道路的信心和决心。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"经济制度","isRight":"0","optionType":"A"},{"optionTitle":"政治制度","isRight":"1","optionType":"B"},{"optionTitle":"社会制度","isRight":"0","optionType":"C"},{"optionTitle":"文化制度","isRight":"0","optionType":"D"}]},{"subjectTitle":"在全面深化改革进程中，我们要积极稳妥推进政治体制改革，以（）为根本，以增强党和国家活力、调动人民积极性为目标，不断建设社会主义政治文明。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"保证人民当家作主","isRight":"1","optionType":"A"},{"optionTitle":"全心全意为人民服务","isRight":"0","optionType":"B"},{"optionTitle":"提高人民生活水平","isRight":"0","optionType":"C"},{"optionTitle":"增加人民收入","isRight":"0","optionType":"D"}]},{"subjectTitle":"社会主义民主不仅需要完整的（），而且需要完整的参与实践。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"程序设计","isRight":"0","optionType":"A"},{"optionTitle":"法制程序","isRight":"0","optionType":"B"},{"optionTitle":"制度程序","isRight":"1","optionType":"C"},{"optionTitle":"制度体系","isRight":"0","optionType":"D"}]},{"subjectTitle":"社会主义（），是中国社会主义民主政治的特有形式和独特优势，是中国共产党的群众路线在政治领域的重要体现。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"民主协商","isRight":"0","optionType":"A"},{"optionTitle":"协商民主","isRight":"1","optionType":"B"},{"optionTitle":"民主选举","isRight":"0","optionType":"C"},{"optionTitle":"基层民主","isRight":"0","optionType":"D"}]},{"subjectTitle":"在中国社会主义制度下，有事好商量，众人的事情由众人商量，找到全社会意愿和要求的（），是人民民主的真谛。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"最大关注点","isRight":"0","optionType":"A"},{"optionTitle":"最大交汇点","isRight":"0","optionType":"B"},{"optionTitle":"最大公约数","isRight":"1","optionType":"C"},{"optionTitle":"最强共鸣点","isRight":"0","optionType":"D"}]},{"subjectTitle":"党对统一战线的领导主要是（），即政治原则、政治方向、重大方针政策的领导。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"思想领导","isRight":"0","optionType":"A"},{"optionTitle":"组织领导","isRight":"0","optionType":"B"},{"optionTitle":"政治领导","isRight":"1","optionType":"C"},{"optionTitle":"工作领导","isRight":"0","optionType":"D"}]},{"subjectTitle":"做好新形势下统战工作，必须正确处理一致性和多样性关系，关键是要坚持（）。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"达成共识","isRight":"0","optionType":"A"},{"optionTitle":"求同存异","isRight":"1","optionType":"B"},{"optionTitle":"畅所欲言","isRight":"0","optionType":"C"},{"optionTitle":"肝胆相照","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们必须根据形势和任务发展变化，加强和改进党的群团工作，把工人阶级主力军、青年生力军、妇女半边天作用和（）第一资源作用充分发挥出来，把13亿多人民的积极性充分调动起来。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"人才","isRight":"1","optionType":"A"},{"optionTitle":"人力","isRight":"0","optionType":"B"},{"optionTitle":"智库","isRight":"0","optionType":"C"},{"optionTitle":"知识分子","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是群团组织的灵魂，是第一位的。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"政治性","isRight":"1","optionType":"A"},{"optionTitle":"先进性","isRight":"0","optionType":"B"},{"optionTitle":"群众性","isRight":"0","optionType":"C"},{"optionTitle":"创新性","isRight":"0","optionType":"D"}]},{"subjectTitle":"优秀传统文化是一个国家、一个民族传承和发展的根本，如果丢掉了，就割断了（）。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"精神文脉","isRight":"0","optionType":"A"},{"optionTitle":"精神血脉","isRight":"0","optionType":"B"},{"optionTitle":"精神根脉","isRight":"0","optionType":"C"},{"optionTitle":"精神命脉","isRight":"1","optionType":"D"}]},{"subjectTitle":"（）是文艺创作的源头活水。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"生活","isRight":"0","optionType":"A"},{"optionTitle":"群众","isRight":"0","optionType":"B"},{"optionTitle":"实践","isRight":"0","optionType":"C"},{"optionTitle":"人民","isRight":"1","optionType":"D"}]},{"subjectTitle":"一部好的作品，应该是经得起人民评价、专家评价、市场检验的作品，应该是把（）放在首位，同时也应该是社会效益和经济效益相统一的作品。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"市场效益","isRight":"0","optionType":"A"},{"optionTitle":"经济效益","isRight":"0","optionType":"B"},{"optionTitle":"社会效益","isRight":"1","optionType":"C"},{"optionTitle":"产品效益","isRight":"0","optionType":"D"}]},{"subjectTitle":"党的新闻舆论工作坚持（）原则，最根本的是坚持党对新闻舆论工作的领导。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"政治","isRight":"0","optionType":"A"},{"optionTitle":"真理","isRight":"0","optionType":"B"},{"optionTitle":"领导","isRight":"0","optionType":"C"},{"optionTitle":"党性","isRight":"1","optionType":"D"}]},{"subjectTitle":"各级党政机关和领导干部要学会通过网络（），经常上网看看，潜潜水、聊聊天、发发声，了解群众所思所愿，收集好想法好建议，积极回应网民关切、解疑释惑。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"去了解舆情","isRight":"0","optionType":"A"},{"optionTitle":"走群众路线","isRight":"1","optionType":"B"},{"optionTitle":"寻解决之道","isRight":"0","optionType":"C"},{"optionTitle":"来更新信息","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是更基本、更深沉、更持久的力量。历史和现实都表明，一个抛弃了或者背叛了自己历史文化的民族，不仅不可能发展起来，而且很可能上演一场历史悲剧。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"文化底蕴","isRight":"0","optionType":"A"},{"optionTitle":"文化传承","isRight":"0","optionType":"B"},{"optionTitle":"文化自信","isRight":"1","optionType":"C"},{"optionTitle":"文化价值","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们的哲学社会科学有没有中国特色，归根到底要看有没有主体性、（）。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"原创性","isRight":"1","optionType":"A"},{"optionTitle":"自觉性","isRight":"0","optionType":"B"},{"optionTitle":"本体性","isRight":"0","optionType":"C"},{"optionTitle":"民族性","isRight":"0","optionType":"D"}]},{"subjectTitle":"领导干部的（），不仅关系自己的家庭，而且关系党风政风。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"作风","isRight":"0","optionType":"A"},{"optionTitle":"家风","isRight":"1","optionType":"B"},{"optionTitle":"家庭意识","isRight":"0","optionType":"C"},{"optionTitle":"裙带意识","isRight":"0","optionType":"D"}]},{"subjectTitle":"教育公平是社会公平的重要基础，要不断促进教育发展成果更多更公平惠及（），以教育公平促进社会公平正义。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"全体人民","isRight":"1","optionType":"A"},{"optionTitle":"城乡居民","isRight":"0","optionType":"B"},{"optionTitle":"更广泛的群体","isRight":"0","optionType":"C"},{"optionTitle":"农村和贫困人口","isRight":"0","optionType":"D"}]},{"subjectTitle":"解决好房地产问题，要坚持（）这个定位。出发点要站准，落脚点要站好，不要搞偏了。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"“居者有其屋”","isRight":"0","optionType":"A"},{"optionTitle":"“房子是用来住的、不是用来炒的”","isRight":"1","optionType":"B"},{"optionTitle":"抑制房地产泡沫","isRight":"0","optionType":"C"},{"optionTitle":"既尽力而为，又量力而行","isRight":"0","optionType":"D"}]},{"subjectTitle":"扩大中等收入群体，必须完善收入分配制度，坚持按劳分配为主体、多种分配方式并存的制度，把按劳分配和按生产要素分配结合起来，处理好（）三者分配关系。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"政府、社会、个人","isRight":"0","optionType":"A"},{"optionTitle":"政府、企业、居民","isRight":"1","optionType":"B"},{"optionTitle":"政府、企业、个人","isRight":"0","optionType":"C"},{"optionTitle":"政府、社会、集体","isRight":"0","optionType":"D"}]},{"subjectTitle":"要倡导（）的生活方式，树立大卫生、大健康的观念，把以治病为中心转变为以人民健康为中心，建立健全健康教育体系，提升全民健康素养，推动全民健身和全民健康深度融合。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"健康文明","isRight":"1","optionType":"A"},{"optionTitle":"健康卫生","isRight":"0","optionType":"B"},{"optionTitle":"积极健康","isRight":"0","optionType":"C"},{"optionTitle":"全民健康","isRight":"0","optionType":"D"}]},{"subjectTitle":"要准确把握国家安全形势，牢固树立和认真贯彻总体国家安全观，以（）安全为宗旨，走中国特色国家安全道路，努力开创国家安全工作新局面，为中华民族伟大复兴中国梦提供坚实安全保障。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"国土","isRight":"0","optionType":"A"},{"optionTitle":"人民","isRight":"1","optionType":"B"},{"optionTitle":"社会","isRight":"0","optionType":"C"},{"optionTitle":"政治","isRight":"0","optionType":"D"}]},{"subjectTitle":"发展是硬道理，（）也是硬道理，抓发展、抓（）两手都要硬。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"改革","isRight":"0","optionType":"A"},{"optionTitle":"法治","isRight":"0","optionType":"B"},{"optionTitle":"稳定","isRight":"1","optionType":"C"},{"optionTitle":"安全","isRight":"0","optionType":"D"}]},{"subjectTitle":"实行能源和水资源消耗、建设用地等（）双控行动，是一项推进生态文明建设，解决资源约束趋紧、环境污染严重、生态系统退化问题的硬措施。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"规模和效益","isRight":"0","optionType":"A"},{"optionTitle":"总量和质量","isRight":"0","optionType":"B"},{"optionTitle":"规模和强度","isRight":"0","optionType":"C"},{"optionTitle":"总量和强度","isRight":"1","optionType":"D"}]},{"subjectTitle":"实行耕地轮作休耕制度，国家可以根据（）状况，重点在地下水漏斗区、重金属污染区、生态严重退化地区开展试点，安排一定面积的耕地用于休耕，对休耕农民给予必要的粮食或现金补助。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"财力和粮食供求","isRight":"1","optionType":"A"},{"optionTitle":"财政和市场供应","isRight":"0","optionType":"B"},{"optionTitle":"中央和地方统筹","isRight":"0","optionType":"C"},{"optionTitle":"地域和农业发展","isRight":"0","optionType":"D"}]},{"subjectTitle":"生态环境破坏和污染不仅影响经济社会可持续发展，而且对人民群众健康的影响已经成为一个突出的（）问题，必须下大气力解决好。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"社会","isRight":"0","optionType":"A"},{"optionTitle":"民生","isRight":"1","optionType":"B"},{"optionTitle":"大健康","isRight":"0","optionType":"C"},{"optionTitle":"公共卫生","isRight":"0","optionType":"D"}]},{"subjectTitle":"各级党委、政府及各有关方面要把生态文明建设作为一项重要任务，扎实工作、合力攻坚，坚持不懈、务求实效，切实把党中央关于生态文明建设的决策部署落到实处，为（）、维护全球生态安全作出更大贡献。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"构建文明和谐社会","isRight":"0","optionType":"A"},{"optionTitle":"实施绿色健康发展","isRight":"0","optionType":"B"},{"optionTitle":"守住守好绿水青山","isRight":"0","optionType":"C"},{"optionTitle":"建设美丽中国","isRight":"1","optionType":"D"}]},{"subjectTitle":"推动形成绿色发展方式和生活方式是贯彻新发展理念的必然要求，必须把（）建设摆在全局工作的突出地位。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"道德法制","isRight":"0","optionType":"A"},{"optionTitle":"精神文明","isRight":"0","optionType":"B"},{"optionTitle":"绿水青山","isRight":"0","optionType":"C"},{"optionTitle":"生态文明","isRight":"1","optionType":"D"}]},{"subjectTitle":"我军根本职能是打仗，（）标准是军队建设唯一的根本的标准。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"听指挥","isRight":"0","optionType":"A"},{"optionTitle":"战斗力","isRight":"1","optionType":"B"},{"optionTitle":"敢打硬仗","isRight":"0","optionType":"C"},{"optionTitle":"作战能力","isRight":"0","optionType":"D"}]},{"subjectTitle":"人民军队发展史，就是一部（）史。我军之所以始终充满蓬勃朝气，同我军与时俱进不断推进自身改革是紧密联系在一起的。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"艰苦奋斗","isRight":"0","optionType":"A"},{"optionTitle":"浴血奋战","isRight":"0","optionType":"B"},{"optionTitle":"改革创新","isRight":"1","optionType":"C"},{"optionTitle":"与时俱进","isRight":"0","optionType":"D"}]},{"subjectTitle":"把握深化国防和军队改革的指导思想，关键是要抓住党在新形势下的（）这个“牛鼻子”，坚持用（）审视、引领、推进改革。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"强军战略","isRight":"0","optionType":"A"},{"optionTitle":"强军思想","isRight":"0","optionType":"B"},{"optionTitle":"强军道路","isRight":"0","optionType":"C"},{"optionTitle":"强军目标","isRight":"1","optionType":"D"}]},{"subjectTitle":"把军民融合发展上升为（），是我们长期探索经济建设和国防建设协调发展规律的重大成果，是从国家发展和安全全局出发作出的重大决策，是应对复杂安全威胁、赢得国家战略优势的重大举措。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"国家意志","isRight":"0","optionType":"A"},{"optionTitle":"国家战略","isRight":"1","optionType":"B"},{"optionTitle":"创新战略","isRight":"0","optionType":"C"},{"optionTitle":"改革试点","isRight":"0","optionType":"D"}]},{"subjectTitle":"党对军队的绝对领导是（）的本质特征，是党和国家的重要政治优势，是人民军队的建军之本、强军之魂。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"中国特色人民军队","isRight":"0","optionType":"A"},{"optionTitle":"中国特色强军之路","isRight":"0","optionType":"B"},{"optionTitle":"中国特色社会主义","isRight":"1","optionType":"C"},{"optionTitle":"中国特色强军目标","isRight":"0","optionType":"D"}]},{"subjectTitle":"人民军队之所以不断发展壮大，关键在于始终坚持先进（）的指导。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"军事理论","isRight":"1","optionType":"A"},{"optionTitle":"政治思想","isRight":"0","optionType":"B"},{"optionTitle":"强军目标","isRight":"0","optionType":"C"},{"optionTitle":"军队文化","isRight":"0","optionType":"D"}]},{"subjectTitle":"要全面实施（）战略，坚持自主创新的战略基点，瞄准世界军事科技前沿，加强前瞻谋划设计，加快战略性、前沿性、颠覆性技术发展，不断提高科技创新对人民军队建设和战斗力发展的贡献率。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"创新强军","isRight":"0","optionType":"A"},{"optionTitle":"改革创新","isRight":"0","optionType":"B"},{"optionTitle":"军民融合","isRight":"0","optionType":"C"},{"optionTitle":"科技兴军","isRight":"1","optionType":"D"}]},{"subjectTitle":"我们高兴地看到，宪法和基本法规定的澳门特别行政区的（）秩序得到尊重和维护，中央全面管治权有效行使，特别行政区享有的高度自治权受到充分保障。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"政治","isRight":"0","optionType":"A"},{"optionTitle":"社会","isRight":"0","optionType":"B"},{"optionTitle":"宪制","isRight":"1","optionType":"C"},{"optionTitle":"法律","isRight":"0","optionType":"D"}]},{"subjectTitle":"继续统筹谋划，积极推动澳门走经济（）可持续发展道路。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"趋多元化","isRight":"0","optionType":"A"},{"optionTitle":"适度多元","isRight":"1","optionType":"B"},{"optionTitle":"广泛多元","isRight":"0","optionType":"C"},{"optionTitle":"主体多元","isRight":"0","optionType":"D"}]},{"subjectTitle":"“一国两制”的提出首先是为了实现和维护国家统一。在中英谈判时期，我们旗帜鲜明提出（）问题不容讨论。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"统一","isRight":"0","optionType":"A"},{"optionTitle":"边境","isRight":"0","optionType":"B"},{"optionTitle":"主权","isRight":"1","optionType":"C"},{"optionTitle":"驻军","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是永恒的主题，是香港的立身之本，也是解决香港各种问题的金钥匙。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"稳定","isRight":"0","optionType":"A"},{"optionTitle":"治理","isRight":"0","optionType":"B"},{"optionTitle":"改革","isRight":"0","optionType":"C"},{"optionTitle":"发展","isRight":"1","optionType":"D"}]},{"subjectTitle":"着眼于新形势新任务，积极推动对外工作理论和实践创新，我们提出和践行（）的周边外交理念、真实亲诚的对非工作方针。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"亲诚惠容","isRight":"1","optionType":"A"},{"optionTitle":"互利共赢","isRight":"0","optionType":"B"},{"optionTitle":"惠容真实","isRight":"0","optionType":"C"},{"optionTitle":"真诚惠容","isRight":"0","optionType":"D"}]},{"subjectTitle":"要充分估计世界经济调整的曲折性，更要看到（）不会改变。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"市场主导性作用","isRight":"0","optionType":"A"},{"optionTitle":"经济全球化进程","isRight":"1","optionType":"B"},{"optionTitle":"市场经济的发展","isRight":"0","optionType":"C"},{"optionTitle":"复苏乏力的趋势","isRight":"0","optionType":"D"}]},{"subjectTitle":"要切实落实好正确义利观，做好对外援助工作，真正做到（）。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"重义轻利","isRight":"0","optionType":"A"},{"optionTitle":"先义后利","isRight":"0","optionType":"B"},{"optionTitle":"弘义融利","isRight":"1","optionType":"C"},{"optionTitle":"义利相兼","isRight":"0","optionType":"D"}]},{"subjectTitle":"在2016年二十国集团领导人杭州峰会上，首次全面阐释我国的（）观。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"发展创新","isRight":"0","optionType":"A"},{"optionTitle":"绿色金融","isRight":"0","optionType":"B"},{"optionTitle":"全球经济治理","isRight":"1","optionType":"C"},{"optionTitle":"全球贸易发展","isRight":"0","optionType":"D"}]},{"subjectTitle":"要提高我国参与（）的能力，着力增强规则制定能力、议程设置能力、舆论宣传能力、统筹协调能力。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"全球治理","isRight":"1","optionType":"A"},{"optionTitle":"国际事务","isRight":"0","optionType":"B"},{"optionTitle":"世界市场","isRight":"0","optionType":"C"},{"optionTitle":"国际组织","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）为世界经济增长提供了强劲动力，促进了商品和资本流动、科技和文明进步、各国人民交往。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"自由贸易","isRight":"0","optionType":"A"},{"optionTitle":"全球一体化","isRight":"0","optionType":"B"},{"optionTitle":"区域合作","isRight":"0","optionType":"C"},{"optionTitle":"经济全球化","isRight":"1","optionType":"D"}]},{"subjectTitle":"推进“一带一路”建设，既要发挥政府把握方向、统筹协调作用，又要发挥（）作用。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"企业","isRight":"0","optionType":"A"},{"optionTitle":"民间资本","isRight":"0","optionType":"B"},{"optionTitle":"市场","isRight":"1","optionType":"C"},{"optionTitle":"多行为主体","isRight":"0","optionType":"D"}]},{"subjectTitle":"“一带一路”建设植根于丝绸之路的历史土壤，重点面向（），同时向所有朋友开放。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"亚洲国家","isRight":"0","optionType":"A"},{"optionTitle":"中亚国家","isRight":"0","optionType":"B"},{"optionTitle":"亚欧大陆","isRight":"0","optionType":"C"},{"optionTitle":"亚欧非大陆","isRight":"1","optionType":"D"}]},{"subjectTitle":"中国是（）在联合国宪章上签字的国家，将继续维护以联合国宪章宗旨和原则为核心的国际秩序和国际体系。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"第二个","isRight":"0","optionType":"A"},{"optionTitle":"第二批","isRight":"0","optionType":"B"},{"optionTitle":"第一批","isRight":"0","optionType":"C"},{"optionTitle":"第一个","isRight":"1","optionType":"D"}]},{"subjectTitle":"《联合国宪章》确立的（）原则是当代国际关系的基本准则，覆盖国与国交往各个领域，其原则和精神也应该适用于网络空间。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"国家不分大小一律平等","isRight":"0","optionType":"A"},{"optionTitle":"主权平等","isRight":"1","optionType":"B"},{"optionTitle":"互不干涉内政","isRight":"0","optionType":"C"},{"optionTitle":"互不侵犯","isRight":"0","optionType":"D"}]},{"subjectTitle":"习近平在第二届世界互联网大会开幕式上的讲话中指出，要加强网络伦理、网络文明建设，发挥道德教化引导作用，用人类文明优秀成果滋养网络空间，修复（）。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"网络生态","isRight":"1","optionType":"A"},{"optionTitle":"网络系统","isRight":"0","optionType":"B"},{"optionTitle":"网络问题","isRight":"0","optionType":"C"},{"optionTitle":"网络安全","isRight":"0","optionType":"D"}]},{"subjectTitle":"2017年1月18日，习近平在联合国日内瓦总部的演讲中指出，（）的达成是全球气候治理史上的里程碑。我们不能让这一成果付诸东流。各方要共同推动协定实施。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"哥本哈根会议","isRight":"0","optionType":"A"},{"optionTitle":"《京都议定书》","isRight":"0","optionType":"B"},{"optionTitle":"《巴黎协定》","isRight":"1","optionType":"C"},{"optionTitle":"波恩气候大会共识","isRight":"0","optionType":"D"}]},{"subjectTitle":"1971年，中国恢复在联合国的合法席位、重返日内瓦国际机构后，逐步参与裁军、经贸、人权、社会等各领域事务，为重大问题解决和重要规则制定提供了（）。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"中国智慧","isRight":"0","optionType":"A"},{"optionTitle":"中国力量","isRight":"0","optionType":"B"},{"optionTitle":"中国元素","isRight":"0","optionType":"C"},{"optionTitle":"中国方案","isRight":"1","optionType":"D"}]},{"subjectTitle":"2014年8月20日，习近平总书记在纪念邓小平同志诞辰110周年座谈会上指出，我们要学习邓小平同志对祖国、对人民的深情大爱，始终为人民利益而奋斗，任何时候任何条件下都（），把自己的一生交给党和人民，为党和人民事业鞠躬尽瘁、死而后已。","subjectType":"1","answer":"A,C","optionInfoList":[{"optionTitle":"忠于祖国、忠于人民","isRight":"1","optionType":"A"},{"optionTitle":"理论联系实际","isRight":"0","optionType":"B"},{"optionTitle":"脚踏实地践行党的宗旨","isRight":"1","optionType":"C"},{"optionTitle":"一切从实际出发","isRight":"0","optionType":"D"}]},{"subjectTitle":"党的十八大以来，党中央从坚持和发展中国特色社会主义全局出发，提出并形成了（）的战略布局。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"全面建成小康社会","isRight":"1","optionType":"A"},{"optionTitle":"全面深化改革","isRight":"1","optionType":"B"},{"optionTitle":"全面依法治国","isRight":"1","optionType":"C"},{"optionTitle":"全面从严治党","isRight":"1","optionType":"D"}]},{"subjectTitle":"坚持不忘初心、继续前进，就要坚持中国特色社会主义（），坚持党的基本路线不动摇，不断把中国特色社会主义伟大事业推向前进。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"道路自信","isRight":"1","optionType":"A"},{"optionTitle":"理论自信","isRight":"1","optionType":"B"},{"optionTitle":"制度自信","isRight":"1","optionType":"C"},{"optionTitle":"文化自信","isRight":"1","optionType":"D"}]},{"subjectTitle":"中国共产党将在（）原则的基础上，同各国各地区政党和政治组织发展交流合作，促进国家关系发展。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"独立自主","isRight":"1","optionType":"A"},{"optionTitle":"完全平等","isRight":"1","optionType":"B"},{"optionTitle":"相互尊重","isRight":"1","optionType":"C"},{"optionTitle":"互不干涉内部事务","isRight":"1","optionType":"D"}]},{"subjectTitle":"坚持和发展中国特色社会主义，总任务是（）和（）。","subjectType":"1","answer":"B,C","optionInfoList":[{"optionTitle":"改革开放","isRight":"0","optionType":"A"},{"optionTitle":"实现社会主义现代化","isRight":"1","optionType":"B"},{"optionTitle":"中华民族伟大复兴","isRight":"1","optionType":"C"},{"optionTitle":"实现共产主义","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们坚定不移全面深化改革，推动改革呈现（）的崭新局面。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"更高质量","isRight":"0","optionType":"A"},{"optionTitle":"全面发力","isRight":"1","optionType":"B"},{"optionTitle":"多点突破","isRight":"1","optionType":"C"},{"optionTitle":"纵深推进","isRight":"1","optionType":"D"}]},{"subjectTitle":"发展是硬道理的战略思想要坚定不移坚持，同时必须坚持科学发展，加大结构性改革力度，坚持以提高发展质量和效益为中心，实现（）的发展。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"更高质量","isRight":"1","optionType":"A"},{"optionTitle":"更有效率","isRight":"1","optionType":"B"},{"optionTitle":"更加公平","isRight":"1","optionType":"C"},{"optionTitle":"更可持续","isRight":"1","optionType":"D"}]},{"subjectTitle":"（）三大战略，是今后一个时期要重点拓展的发展新空间，要有力有序推进。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"“一带一路”建设","isRight":"1","optionType":"A"},{"optionTitle":"珠三角经济带建设","isRight":"0","optionType":"B"},{"optionTitle":"京津冀协同发展","isRight":"1","optionType":"C"},{"optionTitle":"长江经济带建设","isRight":"1","optionType":"D"}]},{"subjectTitle":"转方式调结构是“十三五”时期的关键任务。要以（）为主线调整完善相关政策，构建产业新体系，培育一批战略性产业，构建现代农业产业体系，加快建设制造强国，加快发展现代服务业。","subjectType":"1","answer":"B,D","optionInfoList":[{"optionTitle":"创新产业技能","isRight":"0","optionType":"A"},{"optionTitle":"结构深度调整","isRight":"1","optionType":"B"},{"optionTitle":"调整产业结构","isRight":"0","optionType":"C"},{"optionTitle":"振兴实体经济","isRight":"1","optionType":"D"}]},{"subjectTitle":"（）和（）一直是驱动经济全球化向前发展的两个轮子。","subjectType":"1","answer":"A,C","optionInfoList":[{"optionTitle":"多边贸易体制","isRight":"1","optionType":"A"},{"optionTitle":"对外开放","isRight":"0","optionType":"B"},{"optionTitle":"区域贸易安排","isRight":"1","optionType":"C"},{"optionTitle":"对外贸易","isRight":"0","optionType":"D"}]},{"subjectTitle":"加快实施自由贸易区战略，是我国积极参与国际经贸规则制定、争取全球经济治理制度性权力的重要平台，我们不能当旁观者、跟随者，而是要做（），善于通过自由贸易区建设增强我国国际竞争力，在国际规则制定中发出更多中国声言、注入更多中国元素，维护和拓展我国发展利益。","subjectType":"1","answer":"B,C","optionInfoList":[{"optionTitle":"践行者","isRight":"0","optionType":"A"},{"optionTitle":"参与者","isRight":"1","optionType":"B"},{"optionTitle":"引领者","isRight":"1","optionType":"C"},{"optionTitle":"推动者","isRight":"0","optionType":"D"}]},{"subjectTitle":"注重（）是全面深化改革的内在要求，也是推进改革的重要方法。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"系统性","isRight":"1","optionType":"A"},{"optionTitle":"整体性","isRight":"1","optionType":"B"},{"optionTitle":"协同性","isRight":"1","optionType":"C"},{"optionTitle":"区域性","isRight":"0","optionType":"D"}]},{"subjectTitle":"准确把握全面推进依法治国重点任务，着力推进（）。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"科学立法","isRight":"1","optionType":"A"},{"optionTitle":"严格执法","isRight":"1","optionType":"B"},{"optionTitle":"公正司法","isRight":"1","optionType":"C"},{"optionTitle":"全民守法","isRight":"1","optionType":"D"}]},{"subjectTitle":"我国专门的法治队伍主要包括（）。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"通过律师资格考试的人员","isRight":"0","optionType":"A"},{"optionTitle":"在人大和政府从事立法工作的人员","isRight":"1","optionType":"B"},{"optionTitle":"在行政机关从事执法工作的人员","isRight":"1","optionType":"C"},{"optionTitle":"在司法机关从事司法工作的人员","isRight":"1","optionType":"D"}]},{"subjectTitle":"社会主义法治必须坚持党的领导，党的领导必须依靠社会主义法治。（），这就是党的领导力量的体现。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"法是党的主张和人民意愿的统一体现","isRight":"1","optionType":"A"},{"optionTitle":"党领导人民制定宪法法律","isRight":"1","optionType":"B"},{"optionTitle":"党领导人民实施宪法法律","isRight":"1","optionType":"C"},{"optionTitle":"党自身必须在宪法法律范围内活动","isRight":"1","optionType":"D"}]},{"subjectTitle":"把权力关进制度的笼子里，就是要依法（）。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"设定权力","isRight":"1","optionType":"A"},{"optionTitle":"规范权力","isRight":"1","optionType":"B"},{"optionTitle":"制约权力","isRight":"1","optionType":"C"},{"optionTitle":"监督权力","isRight":"1","optionType":"D"}]},{"subjectTitle":"完善司法制度、深化司法体制改革，要遵循司法活动的客观规律，体现（）的要求。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"权责统一","isRight":"1","optionType":"A"},{"optionTitle":"权力制约","isRight":"1","optionType":"B"},{"optionTitle":"公开公正","isRight":"1","optionType":"C"},{"optionTitle":"尊重程序","isRight":"1","optionType":"D"}]},{"subjectTitle":"习近平总书记在中央党校县委书记研修班学员座谈会上强调，做县委书记，就要做焦裕禄式的县委书记，必须始终做到（）。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"心中有党","isRight":"1","optionType":"A"},{"optionTitle":"心中有民","isRight":"1","optionType":"B"},{"optionTitle":"心中有责","isRight":"1","optionType":"C"},{"optionTitle":"心中有戒","isRight":"1","optionType":"D"}]},{"subjectTitle":"我们党的党内规矩是党的各级组织和全体党员必须遵守的行为规范和规则。党的规矩总的包括（）。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"党章","isRight":"1","optionType":"A"},{"optionTitle":"党的纪律","isRight":"1","optionType":"B"},{"optionTitle":"国家法律","isRight":"1","optionType":"C"},{"optionTitle":"党在长期实践中形成的优良传统和工作惯例","isRight":"1","optionType":"D"}]},{"subjectTitle":"我们要清醒看到，党风廉政建设和反腐败斗争形势依然严峻复杂。从党的十八大以来查处的中管干部违纪违法案件看，腐败分子往往集（）于一身。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"政治蜕变","isRight":"1","optionType":"A"},{"optionTitle":"经济贪婪","isRight":"1","optionType":"B"},{"optionTitle":"生活腐化","isRight":"1","optionType":"C"},{"optionTitle":"作风专横","isRight":"1","optionType":"D"}]},{"subjectTitle":"2016年1月开始实施的（），明确了党员追求的高标准和管党治党的戒尺。","subjectType":"1","answer":"B,D","optionInfoList":[{"optionTitle":"《关于新形势下党内政治生活的若干准则》","isRight":"0","optionType":"A"},{"optionTitle":"《中国共产党廉洁自律准则》","isRight":"1","optionType":"B"},{"optionTitle":"《中国共产党问责条例》","isRight":"0","optionType":"C"},{"optionTitle":"《中国共产党纪律处分条例》","isRight":"1","optionType":"D"}]},{"subjectTitle":"惩治腐败这一手必须紧抓不放、利剑高悬，坚持（）。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"无禁区","isRight":"1","optionType":"A"},{"optionTitle":"严要求","isRight":"0","optionType":"B"},{"optionTitle":"全覆盖","isRight":"1","optionType":"C"},{"optionTitle":"零容忍","isRight":"1","optionType":"D"}]},{"subjectTitle":"行政监察法要体现党中央关于中央纪委、监察部合署办公，中央纪委履行（）和（）两项职能，对党中央全面负责的精神。","subjectType":"1","answer":"A,D","optionInfoList":[{"optionTitle":"党的纪律检查","isRight":"1","optionType":"A"},{"optionTitle":"党的问责制度","isRight":"0","optionType":"B"},{"optionTitle":"纪律建设","isRight":"0","optionType":"C"},{"optionTitle":"政府行政监察","isRight":"1","optionType":"D"}]},{"subjectTitle":"“两学一做”学习教育是加强党的思想政治建设的一项重大部署，是协调推进“四个全面”战略布局特别是推动全面从严治党向基层延伸的有力抓手，（）。","subjectType":"1","answer":"B,D","optionInfoList":[{"optionTitle":"关键在落实","isRight":"0","optionType":"A"},{"optionTitle":"基础在学","isRight":"1","optionType":"B"},{"optionTitle":"突出问题导向","isRight":"0","optionType":"C"},{"optionTitle":"关键在做","isRight":"1","optionType":"D"}]},{"subjectTitle":"党对国有企业的领导是（）的有机统一。国有企业党组织发挥领导核心和政治核心作用，归结到一点，就是把方向、管大局、保落实。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"政治领导","isRight":"1","optionType":"A"},{"optionTitle":"思想领导","isRight":"1","optionType":"B"},{"optionTitle":"组织领导","isRight":"1","optionType":"C"},{"optionTitle":"经营领导","isRight":"0","optionType":"D"}]},{"subjectTitle":"全面从严治党要在国有企业落实落地，必须从（）严起。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"基本组织","isRight":"1","optionType":"A"},{"optionTitle":"基本队伍","isRight":"1","optionType":"B"},{"optionTitle":"基本制度","isRight":"1","optionType":"C"},{"optionTitle":"基本要求","isRight":"0","optionType":"D"}]},{"subjectTitle":"《中共中央关于制定国民经济和社会发展第十三个五年规划的建议》提出要坚持创新、（）的发展理念。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"协调","isRight":"1","optionType":"A"},{"optionTitle":"绿色","isRight":"1","optionType":"B"},{"optionTitle":"开放","isRight":"1","optionType":"C"},{"optionTitle":"共享","isRight":"1","optionType":"D"}]},{"subjectTitle":"党的十八届五中全会提出的共享发展理念，其内涵主要有（）。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"共享是全民共享","isRight":"1","optionType":"A"},{"optionTitle":"共享是全面共享","isRight":"1","optionType":"B"},{"optionTitle":"共享是共建共享","isRight":"1","optionType":"C"},{"optionTitle":"共享是渐进共享","isRight":"1","optionType":"D"}]},{"subjectTitle":"习近平总书记在省部级主要领导干部学习贯彻党的十八届五中全会精神专题研讨班的讲话中指出，当前“为官不为”的主要有3种情况：（）。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"能力不足而“不能为”","isRight":"1","optionType":"A"},{"optionTitle":"动力不足而“不想为”","isRight":"1","optionType":"B"},{"optionTitle":"担当不足而“不敢为”","isRight":"1","optionType":"C"},{"optionTitle":"认识不足而“不善为”","isRight":"0","optionType":"D"}]},{"subjectTitle":"新常态下，我国经济发展的主要特点是：（）。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"增长速度要从高速转向中高速","isRight":"1","optionType":"A"},{"optionTitle":"发展方式要从规模速度型转向质量效率型","isRight":"1","optionType":"B"},{"optionTitle":"经济结构调整要从增量扩能为主转向调整存量、做优增量并举","isRight":"1","optionType":"C"},{"optionTitle":"发展动力要从主要依靠资源和低成本劳动力等要素投入转向创新驱动","isRight":"1","optionType":"D"}]},{"subjectTitle":"供给侧结构性改革，重点是解放和发展社会生产力，用改革的办法推进结构调整，（），增强供给结构对需求变化的适应性和灵活性，提高全要素生产率。","subjectType":"1","answer":"A,B","optionInfoList":[{"optionTitle":"减少无效和低端供给","isRight":"1","optionType":"A"},{"optionTitle":"扩大有效和中高端供给","isRight":"1","optionType":"B"},{"optionTitle":"推动科技创新","isRight":"0","optionType":"C"},{"optionTitle":"化解产能过剩","isRight":"0","optionType":"D"}]},{"subjectTitle":"新型政商关系应该是什么样的？概括起来说，就是（）两个字。","subjectType":"1","answer":"A,B","optionInfoList":[{"optionTitle":"“亲”","isRight":"1","optionType":"A"},{"optionTitle":"“清”","isRight":"1","optionType":"B"},{"optionTitle":"“情”","isRight":"0","optionType":"C"},{"optionTitle":"“密”","isRight":"0","optionType":"D"}]},{"subjectTitle":"发展不协调是我国长期存在的突出问题，集中表现在区域、城乡、（）等关系上。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"工业和农业","isRight":"0","optionType":"A"},{"optionTitle":"经济和社会","isRight":"1","optionType":"B"},{"optionTitle":"物质文明和精神文明","isRight":"1","optionType":"C"},{"optionTitle":"经济建设和国防建设","isRight":"1","optionType":"D"}]},{"subjectTitle":"2017年7月14日，习近平在全国金融工作会议上指出，必须加强党对金融工作的指导，坚持稳中求进工作总基调，遵循金融发展规律，紧紧围绕（）三项任务，创新和完善金融调控，健全现代金融企业制度，完善金融市场体系，推进构建现代金融监管框架，加快转变金融发展方式，健全金融法治，保障国家金融安全，促进经济和金融良性循环、健康发展。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"服务实体经济","isRight":"1","optionType":"A"},{"optionTitle":"防控金融风险","isRight":"1","optionType":"B"},{"optionTitle":"深化金融改革","isRight":"1","optionType":"C"},{"optionTitle":"加强行业监管","isRight":"0","optionType":"D"}]},{"subjectTitle":"党对统一战线的领导主要是政治领导，即（）的领导。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"政治主张","isRight":"0","optionType":"A"},{"optionTitle":"政治原则","isRight":"1","optionType":"B"},{"optionTitle":"政治方向","isRight":"1","optionType":"C"},{"optionTitle":"重大方针政策","isRight":"1","optionType":"D"}]},{"subjectTitle":"工会、共青团、妇联等群团组织一定要坚持解放思想、改革创新、锐意进取、扎实苦干，切实保持和增强党的群团工作和群团组织的（），组织动员广大人民群众更加紧密地团结在党的周围。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"政治性","isRight":"1","optionType":"A"},{"optionTitle":"先进性","isRight":"1","optionType":"B"},{"optionTitle":"群众性","isRight":"1","optionType":"C"},{"optionTitle":"创新性","isRight":"0","optionType":"D"}]},{"subjectTitle":"文艺要反映好人民心声，就要坚持（）这个基本方向。","subjectType":"1","answer":"A,C","optionInfoList":[{"optionTitle":"为人民服务","isRight":"1","optionType":"A"},{"optionTitle":"为基层服务","isRight":"0","optionType":"B"},{"optionTitle":"为社会主义服务","isRight":"1","optionType":"C"},{"optionTitle":"为经济建设服务","isRight":"0","optionType":"D"}]},{"subjectTitle":"紧密结合培养和践行社会主义核心价值观，大力倡导共产党人的（），坚守共产党人的精神家园。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"益利观","isRight":"0","optionType":"A"},{"optionTitle":"世界观","isRight":"1","optionType":"B"},{"optionTitle":"人生观","isRight":"1","optionType":"C"},{"optionTitle":"价值观","isRight":"1","optionType":"D"}]},{"subjectTitle":"（），是党的新闻舆论工作必须遵循的基本方针。","subjectType":"1","answer":"B,C","optionInfoList":[{"optionTitle":"求真务实客观","isRight":"0","optionType":"A"},{"optionTitle":"团结稳定鼓劲","isRight":"1","optionType":"B"},{"optionTitle":"正面宣传为主","isRight":"1","optionType":"C"},{"optionTitle":"做好舆情管理","isRight":"0","optionType":"D"}]},{"subjectTitle":"中国特色哲学社会科学应该具有的特点是：（）。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"体现开拓性、包容性","isRight":"0","optionType":"A"},{"optionTitle":"体现继承性、民族性","isRight":"1","optionType":"B"},{"optionTitle":"体现原创性、时代性","isRight":"1","optionType":"C"},{"optionTitle":"体现系统性、专业性","isRight":"1","optionType":"D"}]},{"subjectTitle":"在推进健康中国建设的过程中，要坚持正确的卫生与健康工作方针，（），将健康融入所有政策，人民共建共享。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"以基层为重点","isRight":"1","optionType":"A"},{"optionTitle":"以改革创新为动力","isRight":"1","optionType":"B"},{"optionTitle":"预防为主","isRight":"1","optionType":"C"},{"optionTitle":"中西医并重","isRight":"1","optionType":"D"}]},{"subjectTitle":"高校思想政治工作关系高校培养什么样的人、如何培养人以及为谁培养人这个根本问题。要坚持把立德树人作为中心环节，把思想政治工作贯穿教育全过程，实现（），努力开创我国高等教育事业发展新局面。","subjectType":"1","answer":"A,B","optionInfoList":[{"optionTitle":"全程育人","isRight":"1","optionType":"A"},{"optionTitle":"全方位育人","isRight":"1","optionType":"B"},{"optionTitle":"以德育人","isRight":"0","optionType":"C"},{"optionTitle":"以思想育人","isRight":"0","optionType":"D"}]},{"subjectTitle":"要坚定不移走中国特色社会主义社会治理之路，善于把党的领导和我国社会主义制度优势转化为社会治理优势，着力推进社会治理（），不断完善中国特色社会主义社会治理体系，确保人民安居乐业、社会安定有序、国家长治久安。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"系统化","isRight":"1","optionType":"A"},{"optionTitle":"科学化","isRight":"1","optionType":"B"},{"optionTitle":"智能化","isRight":"1","optionType":"C"},{"optionTitle":"法治化","isRight":"1","optionType":"D"}]},{"subjectTitle":"推进生态文明建设，解决（）的问题，必须采取一些硬措施，真抓实干才能见效。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"资源约束趋紧","isRight":"1","optionType":"A"},{"optionTitle":"能源结构失衡","isRight":"0","optionType":"B"},{"optionTitle":"环境污染严重","isRight":"1","optionType":"C"},{"optionTitle":"生态系统退化","isRight":"1","optionType":"D"}]},{"subjectTitle":"生态环境，特别是（）污染严重，已成为全面建成小康社会的突出短板。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"辐射","isRight":"0","optionType":"A"},{"optionTitle":"大气","isRight":"1","optionType":"B"},{"optionTitle":"水","isRight":"1","optionType":"C"},{"optionTitle":"土壤","isRight":"1","optionType":"D"}]},{"subjectTitle":"要结合推进供给侧结构性改革，加快推动（）发展，形成节约资源、保护环境的生产生活方式。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"绿色","isRight":"1","optionType":"A"},{"optionTitle":"持续","isRight":"0","optionType":"B"},{"optionTitle":"循环","isRight":"1","optionType":"C"},{"optionTitle":"低碳","isRight":"1","optionType":"D"}]},{"subjectTitle":"要深化生态文明体制改革，尽快把生态文明制度的“四梁八柱”建立起来，把生态文明建设纳入（）轨道。","subjectType":"1","answer":"B,D","optionInfoList":[{"optionTitle":"机制化","isRight":"0","optionType":"A"},{"optionTitle":"制度化","isRight":"1","optionType":"B"},{"optionTitle":"规范化","isRight":"0","optionType":"C"},{"optionTitle":"法治化","isRight":"1","optionType":"D"}]},{"subjectTitle":"人类发展活动必须（），否则就会遭到大自然的报复。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"改造自然","isRight":"0","optionType":"A"},{"optionTitle":"尊重自然","isRight":"1","optionType":"B"},{"optionTitle":"顺应自然","isRight":"1","optionType":"C"},{"optionTitle":"保护自然","isRight":"1","optionType":"D"}]},{"subjectTitle":"要充分认识形成绿色发展方式和生活方式的重要性、紧迫性、艰巨性，把推动形成绿色发展方式和生活方式摆在更加突出的位置，加快构建（）。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"科学适度有序的国土空间布局体系","isRight":"1","optionType":"A"},{"optionTitle":"绿色循环低碳发展的产业体系","isRight":"1","optionType":"B"},{"optionTitle":"约束和激励并举的生态文明制度体系","isRight":"1","optionType":"C"},{"optionTitle":"政府企业公众共治的绿色行动体系","isRight":"1","optionType":"D"}]},{"subjectTitle":"绿色发展方式和生活方式的三大红线是：（）。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"生态功能保障基线","isRight":"1","optionType":"A"},{"optionTitle":"循环生产排放红线","isRight":"0","optionType":"B"},{"optionTitle":"环境质量安全底线","isRight":"1","optionType":"C"},{"optionTitle":"自然资源利用上线","isRight":"1","optionType":"D"}]},{"subjectTitle":"2014年10月31日，习近平在全军政治工作会议上强调，要适应强军目标要求，把握新形势下铸魂育人的特点和规律，着力培养（）的新一代革命军人。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"有灵魂","isRight":"1","optionType":"A"},{"optionTitle":"有本事","isRight":"1","optionType":"B"},{"optionTitle":"有血性","isRight":"1","optionType":"C"},{"optionTitle":"有品德","isRight":"1","optionType":"D"}]},{"subjectTitle":"2015年11月24日，习近平在中央军委改革工作会议上强调，要着眼于贯彻新形势下政治建军的要求，推进领导掌握部队和高效指挥部队有机统一，形成（）的格局。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"军委管总","isRight":"1","optionType":"A"},{"optionTitle":"战区主战","isRight":"1","optionType":"B"},{"optionTitle":"军种主建","isRight":"1","optionType":"C"},{"optionTitle":"部队落实","isRight":"0","optionType":"D"}]},{"subjectTitle":"2014年11月28日，习近平在中央外事工作会议上强调，要高举（）的旗帜，统筹国内国际两个大局，统筹发展安全两件大事。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"和平","isRight":"1","optionType":"A"},{"optionTitle":"发展","isRight":"1","optionType":"B"},{"optionTitle":"合作","isRight":"1","optionType":"C"},{"optionTitle":"共赢","isRight":"1","optionType":"D"}]},{"subjectTitle":"我们要在总结实践经验的基础上，丰富和发展对外工作理念，使我国对外工作有鲜明的（）。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"中国特色","isRight":"1","optionType":"A"},{"optionTitle":"中国风格","isRight":"1","optionType":"B"},{"optionTitle":"中国气派","isRight":"1","optionType":"C"},{"optionTitle":"中国文化","isRight":"0","optionType":"D"}]},{"subjectTitle":"“一带一路”建设不应仅仅着眼于我国自身发展，而是要以我国发展为契机，让更多国家搭上我国发展“快车”，帮助他们实现发展目标。要坚持正确的义利观，（），不急功近利，不搞短期行为。","subjectType":"1","answer":"A,B","optionInfoList":[{"optionTitle":"以义为先","isRight":"1","optionType":"A"},{"optionTitle":"义利并举","isRight":"1","optionType":"B"},{"optionTitle":"宁义勿利","isRight":"0","optionType":"C"},{"optionTitle":"以利为主","isRight":"0","optionType":"D"}]},{"subjectTitle":"我们要摒弃一切形式的冷战思维，树立（）的新观念。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"共同","isRight":"1","optionType":"A"},{"optionTitle":"综合","isRight":"1","optionType":"B"},{"optionTitle":"合作","isRight":"1","optionType":"C"},{"optionTitle":"可持续安全","isRight":"1","optionType":"D"}]},{"subjectTitle":"2017年1月18日，习近平在联合国日内瓦总部的演讲中指出，让和平的薪火代代相传，让发展的动力源源不断，让文明的光芒熠熠生辉，是各国人民的期待，也是我们这一代政治家应有的担当。中国方案是：（）。","subjectType":"1","answer":"A,C","optionInfoList":[{"optionTitle":"构建人类命运共同体","isRight":"1","optionType":"A"},{"optionTitle":"构建全球治理体系","isRight":"0","optionType":"B"},{"optionTitle":"实现共赢共享","isRight":"1","optionType":"C"},{"optionTitle":"实现共建共治","isRight":"0","optionType":"D"}]},{"subjectTitle":"全面从严治党，必须坚持和加强党的全面领导。坚持党的领导，最根本的是（）。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"坚持四项基本原则","isRight":"0","optionType":"A"},{"optionTitle":"坚持党中央权威和集中统一领导","isRight":"1","optionType":"B"},{"optionTitle":"坚持民主集中制","isRight":"0","optionType":"C"},{"optionTitle":"坚持以人民为中心","isRight":"0","optionType":"D"}]},{"subjectTitle":"2018年1月11日，习近平在中国共产党第十九届中央纪律检查委员会第二次全体会议上强调，我们要乘势而上，牢牢把握（）这条主线，发挥标本兼治综合效应，确保党成为始终走在时代前列、人民衷心拥护、勇于自我革命、经得起各种风浪考验、朝气蓬勃的马克思主义执政党。","subjectType":"1","answer":"B,C","optionInfoList":[{"optionTitle":"加强党的自身建设","isRight":"0","optionType":"A"},{"optionTitle":"加强党的长期执政能力建设","isRight":"1","optionType":"B"},{"optionTitle":"先进性和纯洁性建设","isRight":"1","optionType":"C"},{"optionTitle":"作风建设","isRight":"0","optionType":"D"}]},{"subjectTitle":"党的十八大后，我们紧紧盯住（）这个症结，坚持发扬我们党历史上行之有效的好经验好做法，深化对管党治党规律的认识、创造新的经验，全面从严治党成效卓著。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"管党治党宽松软","isRight":"0","optionType":"A"},{"optionTitle":"腐败","isRight":"0","optionType":"B"},{"optionTitle":"“四风”问题","isRight":"0","optionType":"C"},{"optionTitle":"全面从严治党不力","isRight":"1","optionType":"D"}]},{"subjectTitle":"坚持思想建党和制度治党相统一，既要解决思想问题，也要解决制度问题，把（）作为根本任务，把制度建设贯穿到党的各项建设之中。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"坚定理想信念","isRight":"1","optionType":"A"},{"optionTitle":"执政能力建设","isRight":"0","optionType":"B"},{"optionTitle":"深化反腐败斗争","isRight":"0","optionType":"C"},{"optionTitle":"“三严三实”","isRight":"0","optionType":"D"}]},{"subjectTitle":"长期坚持、不断深化全面从严治党，要坚持行使权力和担当责任相统一，真正把落实管党治党政治责任作为最根本的政治担当，紧紧咬住“责任”二字，抓住（）这个要害。","subjectType":"0","answer":"D","optionInfoList":[{"optionTitle":"“从严”","isRight":"0","optionType":"A"},{"optionTitle":"“执纪”","isRight":"0","optionType":"B"},{"optionTitle":"“监督”","isRight":"0","optionType":"C"},{"optionTitle":"“问责”","isRight":"1","optionType":"D"}]},{"subjectTitle":"长期坚持、不断深化全面从严治党，要坚持党内监督和群众监督相统一，以（）带动其他监督，积极畅通人民群众建言献策和批评监督渠道，充分发挥群众监督、舆论监督作用。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"群众监督","isRight":"0","optionType":"A"},{"optionTitle":"党外监督","isRight":"0","optionType":"B"},{"optionTitle":"党内监督","isRight":"1","optionType":"C"},{"optionTitle":"政治监督","isRight":"0","optionType":"D"}]},{"subjectTitle":"党中央作出的决策部署，所有党组织都要不折不扣贯彻落实，始终在（）上同党中央保持高度一致。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"政治立场","isRight":"1","optionType":"A"},{"optionTitle":"政治方向","isRight":"1","optionType":"B"},{"optionTitle":"政治原则","isRight":"1","optionType":"C"},{"optionTitle":"政治道路","isRight":"1","optionType":"D"}]},{"subjectTitle":"要锲而不舍落实中央八项规定精神，保持党同人民群众的血肉联系。要继续在（）上下功夫，密切关注享乐主义、奢靡之风新动向新表现，坚决防止回潮复燃。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"严和长","isRight":"0","optionType":"A"},{"optionTitle":"常和长","isRight":"1","optionType":"B"},{"optionTitle":"严和实","isRight":"1","optionType":"C"},{"optionTitle":"深和细","isRight":"1","optionType":"D"}]},{"subjectTitle":"纠正形式主义、官僚主义，（）要负总责。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"一把手","isRight":"1","optionType":"A"},{"optionTitle":"省部级领导干部","isRight":"0","optionType":"B"},{"optionTitle":"市县级领导干部","isRight":"0","optionType":"C"},{"optionTitle":"各级领导干部","isRight":"0","optionType":"D"}]},{"subjectTitle":"加强作风建设必须紧扣（）这个关键。领导干部要坚决反对特权思想、特权现象，保持对人民的赤子之心，坚持工作重心下移，扑下身子深入群众，面对面、心贴心、实打实做好群众工作，着力解决群众反映强烈的突出问题。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"管党治党政治责任","isRight":"0","optionType":"A"},{"optionTitle":"中央八项规定精神","isRight":"0","optionType":"B"},{"optionTitle":"保持党同人民群众血肉联系","isRight":"1","optionType":"C"},{"optionTitle":"以人民为中心","isRight":"0","optionType":"D"}]},{"subjectTitle":"2018年1月11日，习近平在中国共产党第十九届中央纪律检查委员会第二次全体会议上强调，要坚持无禁区、全覆盖、零容忍，坚持（），坚持受贿行贿一起查，坚决减存量、重点遏增量。","subjectType":"1","answer":"A,B,D","optionInfoList":[{"optionTitle":"重遏制","isRight":"1","optionType":"A"},{"optionTitle":"强高压","isRight":"1","optionType":"B"},{"optionTitle":"常巡视","isRight":"0","optionType":"C"},{"optionTitle":"长震慑","isRight":"1","optionType":"D"}]},{"subjectTitle":"2018年1月，习近平对政法工作作出重要指示，希望全国政法战线深入学习贯彻党的十九大精神，强化“四个意识”，坚持党对政法工作的绝对领导，坚持以人民为中心的发展思想，履行好（）的主要任务，努力创造安全的政治环境、稳定的社会环境、公正的法治环境、优质的服务环境，增强人民群众获得感、幸福感、安全感。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"维护国家政治安全","isRight":"1","optionType":"A"},{"optionTitle":"确保社会大局稳定","isRight":"1","optionType":"B"},{"optionTitle":"促进社会公平正义","isRight":"1","optionType":"C"},{"optionTitle":"保障人民安居乐业","isRight":"1","optionType":"D"}]},{"subjectTitle":"建立城乡居民基本养老保险待遇确定和基础养老金正常调整机制，要按照（）的要求，建立激励约束有效、筹资权责清晰、保障水平适度的待遇确定和基础养老金正常调整机制。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"兜底线","isRight":"1","optionType":"A"},{"optionTitle":"稳大局","isRight":"0","optionType":"B"},{"optionTitle":"织密网","isRight":"1","optionType":"C"},{"optionTitle":"建机制","isRight":"1","optionType":"D"}]},{"subjectTitle":"实行地方党政领导干部安全生产责任制，要坚持（），牢固树立发展决不能以牺牲安全为代价的红线意识，明确地方党政领导干部主要安全生产职责，综合运用巡查督查、考核考察、激励惩戒等措施，强化地方各级党政领导干部“促一方发展、保一方平安”的政治责任。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"党政同责","isRight":"1","optionType":"A"},{"optionTitle":"一岗双责","isRight":"1","optionType":"B"},{"optionTitle":"齐抓共管","isRight":"1","optionType":"C"},{"optionTitle":"失职追责","isRight":"1","optionType":"D"}]},{"subjectTitle":"2018年是站在新的历史起点上接力探索、接续奋进的关键之年，要全面贯彻党的十九大精神，以习近平新时代中国特色社会主义思想为指导，统筹推进党的十八大以来部署的改革举措和党的十九大部署的改革任务，更加注重改革的（）。","subjectType":"1","answer":"B,C,D","optionInfoList":[{"optionTitle":"统一性","isRight":"0","optionType":"A"},{"optionTitle":"系统性","isRight":"1","optionType":"B"},{"optionTitle":"整体性","isRight":"1","optionType":"C"},{"optionTitle":"协同性","isRight":"1","optionType":"D"}]},{"subjectTitle":"建设（）是我国发展的战略目标，也是转变经济发展方式、优化经济结构、转换经济增长动力的迫切要求。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"现代化经济体系","isRight":"1","optionType":"A"},{"optionTitle":"中国特色社会主义市场经济","isRight":"0","optionType":"B"},{"optionTitle":"社会主义市场经济体系","isRight":"0","optionType":"C"},{"optionTitle":"现代化市场体系","isRight":"0","optionType":"D"}]},{"subjectTitle":"要建设创新引领、协同发展的产业体系，实现（）协同发展，使科技创新在实体经济发展中的贡献份额不断提高，现代金融服务实体经济的能力不断增强，人力资源支撑实体经济发展的作用不断优化。","subjectType":"1","answer":"A,B,C,D","optionInfoList":[{"optionTitle":"实体经济","isRight":"1","optionType":"A"},{"optionTitle":"科技创新","isRight":"1","optionType":"B"},{"optionTitle":"现代金融","isRight":"1","optionType":"C"},{"optionTitle":"人力资源","isRight":"1","optionType":"D"}]},{"subjectTitle":"要建设统一开放、竞争有序的市场体系，实现市场准入畅通、市场开放有序、市场竞争充分、市场秩序规范，加快形成（）的现代市场体系。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"企业自主经营公平竞争","isRight":"1","optionType":"A"},{"optionTitle":"政府调控相机抉择","isRight":"0","optionType":"B"},{"optionTitle":"消费者自由选择自主消费","isRight":"1","optionType":"C"},{"optionTitle":"商品和要素自由流动平等交换","isRight":"1","optionType":"D"}]},{"subjectTitle":"2018年1月30日，习近平在中共中央政治局第三次集体学习时强调，要建设充分发挥市场作用、更好发挥政府作用的经济体制，实现（）。","subjectType":"1","answer":"A,B,C","optionInfoList":[{"optionTitle":"市场机制有效","isRight":"1","optionType":"A"},{"optionTitle":"微观主体有活力","isRight":"1","optionType":"B"},{"optionTitle":"宏观调控有度","isRight":"1","optionType":"C"},{"optionTitle":"社会协同参与","isRight":"0","optionType":"D"}]},{"subjectTitle":"（）是一国经济的立身之本，是财富创造的根本源泉，是国家强盛的重要支柱。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"现代金融","isRight":"0","optionType":"A"},{"optionTitle":"实体经济","isRight":"1","optionType":"B"},{"optionTitle":"虚拟经济","isRight":"0","optionType":"C"},{"optionTitle":"民营经济","isRight":"0","optionType":"D"}]},{"subjectTitle":"2018年2月6日，习近平在同党外人士座谈并共迎新春时强调，要认真开展（）主题教育活动，组织中共中央发布“五一口号”70周年系列纪念活动，重温多党合作历史，弘扬优良传统。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"“铭记历史，肝胆相照”","isRight":"0","optionType":"A"},{"optionTitle":"“不忘初心，牢记使命”","isRight":"0","optionType":"B"},{"optionTitle":"“不忘合作初心，继续携手前进”","isRight":"1","optionType":"C"},{"optionTitle":"“肝胆相照，荣辱与共”","isRight":"0","optionType":"D"}]},{"subjectTitle":"2018年2月6日，习近平在同党外人士座谈并共迎新春时指出，要加强民主党派（）特别是领导班子建设，建立健全民主集中制、民主生活会制度以及各项议事决策制度，增进班子成员团结，提高各级领导班子成员的政治把握能力、参政议政能力、组织领导能力、合作共事能力、解决自身问题能力，把中国特色社会主义参政党建设提高到新水平。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"思想","isRight":"1","optionType":"A"},{"optionTitle":"作风","isRight":"0","optionType":"B"},{"optionTitle":"组织","isRight":"1","optionType":"C"},{"optionTitle":"制度","isRight":"1","optionType":"D"}]},{"subjectTitle":"脱贫攻坚面临的困难挑战依然巨大，需要解决的突出问题依然不小。今后3年要实现脱贫（）人，压力不小，难度不小，而且越往后越是难啃的硬骨头。","subjectType":"0","answer":"B","optionInfoList":[{"optionTitle":"2500多万","isRight":"0","optionType":"A"},{"optionTitle":"3000多万","isRight":"1","optionType":"B"},{"optionTitle":"3500多万","isRight":"0","optionType":"C"},{"optionTitle":"4000多万","isRight":"0","optionType":"D"}]},{"subjectTitle":"全面打好脱贫攻坚战，要按照党中央统一部署，把（）放在首位，聚焦深度贫苦地区，扎实推进各项工作。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"减少贫困人口","isRight":"0","optionType":"A"},{"optionTitle":"增加贫困户收入","isRight":"0","optionType":"B"},{"optionTitle":"提高扶贫质量","isRight":"1","optionType":"C"},{"optionTitle":"增加扶贫投入","isRight":"0","optionType":"D"}]},{"subjectTitle":"强化监管，做到阳光扶贫、廉洁扶贫。要健全（）制度，省、市、县扶贫资金分配结果一律公开，乡、村两级扶贫项目安排和资金使用情况一律公告公示，接受群众和社会监督。","subjectType":"0","answer":"A","optionInfoList":[{"optionTitle":"公告公示","isRight":"1","optionType":"A"},{"optionTitle":"公开透明","isRight":"0","optionType":"B"},{"optionTitle":"民主监督","isRight":"0","optionType":"C"},{"optionTitle":"科学管理","isRight":"0","optionType":"D"}]},{"subjectTitle":"党中央已经明确，将2018年作为脱贫攻坚（）。","subjectType":"0","answer":"C","optionInfoList":[{"optionTitle":"项目建设年","isRight":"0","optionType":"A"},{"optionTitle":"质量建设年","isRight":"0","optionType":"B"},{"optionTitle":"作风建设年","isRight":"1","optionType":"C"},{"optionTitle":"制度建设年","isRight":"0","optionType":"D"}]},{"subjectTitle":"打好脱贫攻坚战，关键在人，在人的观念、能力、干劲。对基层干部，重点是提高实际能力，培育（）的扶贫干部队伍。","subjectType":"1","answer":"A,C,D","optionInfoList":[{"optionTitle":"懂扶贫","isRight":"1","optionType":"A"},{"optionTitle":"愿扶贫","isRight":"0","optionType":"B"},{"optionTitle":"会帮扶","isRight":"1","optionType":"C"},{"optionTitle":"作风硬","isRight":"1","optionType":"D"}]},{"subjectTitle":"贫困群众既是脱贫攻坚的对象，又是脱贫致富的主体。要加强扶贫同（）相结合，激发贫困群众积极性和主动性，激励和引导他们靠自己的努力改变命运。","subjectType":"1","answer":"C,D","optionInfoList":[{"optionTitle":"扶人","isRight":"0","optionType":"A"},{"optionTitle":"扶技","isRight":"0","optionType":"B"},{"optionTitle":"扶志","isRight":"1","optionType":"C"},{"optionTitle":"扶智","isRight":"1","optionType":"D"}]}],"totalSubject":200,"chapterTitle":"2018年3月学习竞赛题库"}}'
questions = json.loads(j)['data']['subjectInfoList']
topics = []
for question in questions:
    subjectType = question['subjectType']
    subjectTitle = question['subjectTitle']
    optionTitleA = question['optionInfoList'][0]['optionTitle']
    optionTitleB = question['optionInfoList'][1]['optionTitle']
    optionTitleC = question['optionInfoList'][2]['optionTitle']
    optionTitleD = question['optionInfoList'][3]['optionTitle']
    answer = question['answer']
    if subjectType == '0':
        if subjectTitle.count('（') == 1:
            if answer == 'A':
                topic = subjectTitle.replace('（）', optionTitleA)
                topics.append(topic)
            elif answer == 'B':
                topic = subjectTitle.replace('（）', optionTitleB)
                topics.append(topic)
            elif answer == 'C':
                topic = subjectTitle.replace('（）', optionTitleC)
                topics.append(topic)
            elif answer == 'D':
                topic = subjectTitle.replace('（）', optionTitleD)
                topics.append(topic)
            else:
                topics.append(subjectTitle)
        elif subjectTitle.count('（') == 2:
            if answer == 'A':
                s = optionTitleA.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            elif answer == 'B':
                s = optionTitleB.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            elif answer == 'C':
                s = optionTitleC.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            elif answer == 'D':
                s = optionTitleD.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topics.append(topic2)
            else:
                topics.append(subjectTitle)
        elif subjectTitle.count('（') == 3:
            if answer == 'A':
                s = optionTitleA.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            elif answer == 'B':
                s = optionTitleB.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            elif answer == 'C':
                s = optionTitleC.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            elif answer == 'D':
                s = optionTitleD.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topics.append(topic3)
            else:
                topics.append(subjectTitle)
        elif subjectTitle.count('（') == 4:
            if answer == 'A':
                s = optionTitleA.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            elif answer == 'B':
                s = optionTitleB.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            elif answer == 'C':
                s = optionTitleC.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            elif answer == 'D':
                s = optionTitleD.split(' ')
                if len(s) == 1:
                    topic1 = subjectTitle.replace('（）', s[0])
                    topics.append(topic1)
                else:
                    topic1 = subjectTitle.replace('（）', s[0], 1)
                    topic2 = topic1.replace('（）', s[1], 1)
                    topic3 = topic2.replace('（）', s[2], 1)
                    topic4 = topic3.replace('（）', s[3], 1)
                    topics.append(topic4)
            else:
                topics.append(subjectTitle)
        else:
            pass
    elif subjectType == '1':
        if subjectTitle.count('（') == 1:
            As = ''
            if answer.find('A') != -1:
                As = As + optionTitleA + '，'
            if answer.find('B') != -1:
                As = As + optionTitleB + '，'
            if answer.find('C') != -1:
                As = As + optionTitleC + '，'
            if answer.find('D') != -1:
                As = As + optionTitleD
            topic = subjectTitle.replace('（）', As.rstrip('，'))
            topics.append(topic)
        elif subjectTitle.count('（') == 2:
            if answer.find('A') != -1:
                topic = subjectTitle.replace('（）', optionTitleA, 1)
            if answer.find('B') != -1:
                topic = topic.replace('（）', optionTitleB, 1)
            if answer.find('C') != -1:
                topic = topic.replace('（）', optionTitleC, 1)
            if answer.find('D') != -1:
                topic = topic.replace('（）', optionTitleD, 1)
            topics.append(topic)
        elif subjectTitle.count('（') == 3:
            if answer.find('A') != -1:
                topic = subjectTitle.replace('（）', optionTitleA, 1)
            if answer.find('B') != -1:
                topic = topic.replace('（）', optionTitleB, 1)
            if answer.find('C') != -1:
                topic = topic.replace('（）', optionTitleC, 1)
            if answer.find('D') != -1:
                topic = topic.replace('（）', optionTitleD, 1)
            topics.append(topic)
        elif subjectTitle.count('（') == 4:
            if answer.find('A') != -1:
                topic = subjectTitle.replace('（）', optionTitleA, 1)
            if answer.find('B') != -1:
                topic = topic.replace('（）', optionTitleB, 1)
            if answer.find('C') != -1:
                topic = topic.replace('（）', optionTitleC, 1)
            if answer.find('D') != -1:
                topic = topic.replace('（）', optionTitleD, 1)
            topics.append(topic)
        else:
            pass
    else:
        pass

topicNumber = 0
top = open("C:\\灯塔.js", "w", encoding='utf-8')
top.write('var topic = new Array();' + '\n')
for topic in topics:
    t = 'topic[' + str(topicNumber) + ']={title:"' + topic + '"};'
    topicNumber = topicNumber + 1
    top.write(t + '\n')
js = '''
//去掉两边的空白
function trim(s){
    return trimRight(trimLeft(s));
}
//去掉左边的空白
function trimLeft(s){
    if(s == null) {
        return "";
    }
    var whitespace = new String(" \t\n\r");
    var str = new String(s);
    if (whitespace.indexOf(str.charAt(0)) != -1) {
        var j=0, i = str.length;
        while (j < i && whitespace.indexOf(str.charAt(j)) != -1){
            j++;
        }
        str = str.substring(j, i);
    }
    return str;
}

//去掉右边的空白
function trimRight(s){
    if(s == null) return "";
    var whitespace = new String(" \t\n\r");
    var str = new String(s);
    if (whitespace.indexOf(str.charAt(str.length-1)) != -1){
        var i = str.length - 1;
        while (i >= 0 && whitespace.indexOf(str.charAt(i)) != -1){
            i--;
        }
        str = str.substring(0, i+1);
    }
    return str;
}
localStorage.setItem('anniujia', 21)
var obj = JSON.parse(sessionStorage.getItem('allDatajingsai'))
// var allDatajingsai= ""
// var obj = JSON.parse(allDatajingsai)
var As, Bs, Cs, Ds, an, y
for (var i = 0; i < obj.data.subjectInfoList.length; i++) {
    y = i + 1
    var subjectType = obj.data.subjectInfoList[i].subjectType.toString()
    var subjectTitle = trim(obj.data.subjectInfoList[i].subjectTitle).toString()
    var optionTitleA = trim(obj.data.subjectInfoList[i].optionInfoList[0].optionTitle).toString()
    var optionTitleB = trim(obj.data.subjectInfoList[i].optionInfoList[1].optionTitle).toString()
    var optionTitleC = trim(obj.data.subjectInfoList[i].optionInfoList[2].optionTitle).toString()
    var optionTitleD = trim(obj.data.subjectInfoList[i].optionInfoList[3].optionTitle).toString()
    var S = subjectTitle.split('（）')
    As = optionTitleA.split(' ')
    Bs = optionTitleB.split(' ')
    Cs = optionTitleC.split(' ')
    Ds = optionTitleD.split(' ')
    // 一个空格
    if (S.length == 2) {
        for (var j = 0; j < topic.length; j++) {
            // 空格不在开头
            if (S[0] != '') {
                if (topic[j].title.indexOf(S[0]) != -1) {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        an = topic[j].title.replace(S[0], '').replace(S[1], '')
                        console.group("第" + y + "题：" + topic[j].title)
                        //单选题
                        if (subjectType == 0) {
                            if (an.indexOf(optionTitleA) != -1 && subjectTitle.replace("（）", optionTitleA) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[0].checked = true
                                console.log(optionTitleA)
                            }else{}
                            if (an.indexOf(optionTitleB) != -1 && subjectTitle.replace("（）", optionTitleB) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[1].checked = true
                                console.log(optionTitleB)
                            }else{}
                            if (an.indexOf(optionTitleC) != -1 && subjectTitle.replace("（）", optionTitleC) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[2].checked = true
                                console.log(optionTitleC)
                            }else{}
                            if (an.indexOf(optionTitleD) != -1 && subjectTitle.replace("（）", optionTitleD) == topic[j].title) {
                                document.getElementsByName("ra_" + i)[3].checked = true
                                console.log(optionTitleD)
                            }else{}
                        }else{
                            if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                            if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                            if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                            if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                        }
                        console.groupEnd()
                    }
                }
            } else {
                if (topic[j].title.indexOf(S[1]) != -1) {
                    an = topic[j].title.replace(S[1], '')
                    console.group("第" + y + "题：" + topic[j].title)
                    //单选题
                    if (subjectType == 0) {
                        if (an.indexOf(optionTitleA) != -1 && subjectTitle.replace("（）", optionTitleA) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[0].checked = true
                            console.log(optionTitleA)
                        }else{}
                        if (an.indexOf(optionTitleB) != -1 && subjectTitle.replace("（）", optionTitleB) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[1].checked = true
                            console.log(optionTitleB)
                        }else{}
                        if (an.indexOf(optionTitleC) != -1 && subjectTitle.replace("（）", optionTitleC) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[2].checked = true
                            console.log(optionTitleC)
                        }else{}
                        if (an.indexOf(optionTitleD) != -1 && subjectTitle.replace("（）", optionTitleD) == topic[j].title) {
                            document.getElementsByName("ra_" + i)[3].checked = true
                            console.log(optionTitleD)
                        }else{}
                    }else {
                        if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                        if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                        if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                        if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                    }
                    console.groupEnd()
                }
            }

        }
    // 两个空格
    } else if (S.length == 3) {
        //   选项中只有一个内容
        if (As.length == 1) {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                console.groupEnd()
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            an = topic[j].title.replace(S[1], '').replace(S[2], '')
                            console.group("第" + y + "题：" + topic[j].title)
                            if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                            if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                            if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                            if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                            console.groupEnd()
                        }
                    }
                }
            }
            //    选项中有多个内容
        } else {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA)  }
                                if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB)  }
                                if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC)  }
                                if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD)  }
                                console.groupEnd()
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            an = topic[j].title.replace(S[1], '').replace(S[2], '')
                            console.group("第" + y + "题：" + topic[j].title)
                            if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA)  }
                            if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB)  }
                            if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC)  }
                            if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD)  }
                            console.groupEnd()
                        }
                    }
                }
            }
        }
    // 三个空格
    } else if (S.length == 4) {
        //   选项中只有一个内容
        if (As.length == 1) {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                console.groupEnd()
                            }
                        }
                    }
                }
            }
        //    选项中有多个内容
        } else {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '')
                                console.group("第" + y + "题：" + topic[j].title)
                                if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                console.groupEnd()
                            }
                        }
                    }
                }
            }
        }
    // 有四个空格
    } else {
        //   选项中只有一个内容
        if (As.length == 1) {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    if (topic[j].title.indexOf(S[4]) != -1) {
                                        an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                        console.group("第" + y + "题：" + topic[j].title)
                                        if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                        if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                        if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                        if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                        console.groupEnd()
                                    }
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                if (topic[j].title.indexOf(S[4]) != -1) {
                                    an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(optionTitleA) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(optionTitleB) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(optionTitleC) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(optionTitleD) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                }
            }
            //    选项中有多个内容
        } else {
            for (var j = 0; j < topic.length; j++) {
                if (S[0] != '') {
                    if (topic[j].title.indexOf(S[0]) != -1) {
                        if (topic[j].title.indexOf(S[1]) != -1) {
                            if (topic[j].title.indexOf(S[2]) != -1) {
                                if (topic[j].title.indexOf(S[3]) != -1) {
                                    if (topic[j].title.indexOf(S[4]) != -1) {
                                        an = topic[j].title.replace(S[0], '').replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                        console.group("第" + y + "题：" + topic[j].title)
                                        if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                        if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                        if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                        if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                        console.groupEnd()
                                    }
                                }
                            }
                        }
                    }
                } else {
                    if (topic[j].title.indexOf(S[1]) != -1) {
                        if (topic[j].title.indexOf(S[2]) != -1) {
                            if (topic[j].title.indexOf(S[3]) != -1) {
                                if (topic[j].title.indexOf(S[4]) != -1) {
                                    an = topic[j].title.replace(S[1], '').replace(S[2], '').replace(S[3], '').replace(S[4], '')
                                    console.group("第" + y + "题：" + topic[j].title)
                                    if (an.indexOf(As[0]) != -1 && an.indexOf(As[1]) != -1 && an.indexOf(As[2]) != -1) { document.getElementsByName("ra_" + i)[0].checked = true; console.log(optionTitleA) }
                                    if (an.indexOf(Bs[0]) != -1 && an.indexOf(Bs[1]) != -1 && an.indexOf(Bs[2]) != -1) { document.getElementsByName("ra_" + i)[1].checked = true; console.log(optionTitleB) }
                                    if (an.indexOf(Cs[0]) != -1 && an.indexOf(Cs[1]) != -1 && an.indexOf(Cs[2]) != -1) { document.getElementsByName("ra_" + i)[2].checked = true; console.log(optionTitleC) }
                                    if (an.indexOf(Ds[0]) != -1 && an.indexOf(Ds[1]) != -1 && an.indexOf(Ds[2]) != -1) { document.getElementsByName("ra_" + i)[3].checked = true; console.log(optionTitleD) }
                                    console.groupEnd()
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

var tags=document.getElementsByTagName("span")
for (var k in tags) {
    var tag=tags[k]
    if (tag.className == "W_fr W_mr10 W_quan W_mt22 jiaojuanss W_jiaoquancol") {
        tag.className="W_fr W_mr10 W_quan W_mt22 jiaojuanss "
        break
    }
}
'''
top.write(js + '\n')
top.close()
print("代码生成完毕！")
