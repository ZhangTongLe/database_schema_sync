# database_schema_sync
用于软件开发过程中多个环境中数据库结构的同步，目前基本的模式都是，研发》测试》UAT》生产。在人员参与比较多的项目中，如果单靠人为维护难免会有疏忽。

这个小软件就是为了解决这个问题。

软件中没有加入定时机制，如果你是UNIX系统，你可以把它加入到corn中，继而实现周期性检查的目的。