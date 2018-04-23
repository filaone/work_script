require 'terminal-table'

rows = []
rows << ['属性', 'Channel请求', 'Channel请求', 'keyword请求','keyword请求']
rows << ['from_id', 'm503949', 'null', 'null','null']
rows << ['channel_id','null', '14414961060', 'null','null']
rows << ['ctype', 'null', 'null','video','weibo']
rows << ['count', 'null', 'null','100','1']
rows << ['words', 'null', 'null','null','abc']
rows << ['q','null','null','tag:vtpc_list//646','null']
table = Terminal::Table.new :rows => rows
puts table
