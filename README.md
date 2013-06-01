#salt dashboard


salt-dashboard is based on salt-client,and use mysql returner as result backend


---------------------------------------

#1:returner:


salt [mysql returner ](http://docs.saltstack.com/ref/returners/all/salt.returners.mysql.html#module-salt.returners.mysql "Title")

add time to salt_returns:
<pre>
alter table salt_returns add time timestamp;
</pre>

the auth sql like this:
<pre>
grant all on salt.* to 'salt'@'localhost' identified by 'salt';
</pre>

there is a bug when schedule use mysql return,fixed by this [schedule return by mysql ](https://github.com/halfss/salt/commit/3f5805f7b38fc867a3d12b8c36efd023b4957792)

#2:scheduler:
<pre>
/srv/pillar/top.sls
<pre>
base:
  "*":
    - schedule
</pre>
/srv/pillar/schedule.sls
<pre>
schedule:
  highstate:
    function: state.highstate
    minutes: 30
    returner: mysql
</pre>
</pre>

then waiting minions update scheduler info by himself or run this command:
<pre>
salt '*' saltutil.refresh_pillar
</pre>

#3:salt-dashboard
  this dashboard is based on django+bootstrap+amcharts
 
  demo screen like this:
    here just on minion, so is seems very simple
    
    
  ![index](https://raw.github.com/halfss/salt-dashboard/master/screenshot/index.png)
  ![minions](https://raw.github.com/halfss/salt-dashboard/master/screenshot/minions.png)
  ![execute](https://raw.github.com/halfss/salt-dashboard/master/screenshot/execute.png)
   
   
   
    