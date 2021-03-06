import sys,re
STRINGOS1=[]
MapFile_name='Project_Memory_Map_File.map'
for name in sys.argv[1:]:
  print(name) 
  try:
    f=open(MapFile_name,'r')
    STRINGOS=f.read()
    flie=open(name+'.txt',"a")
    text=re.findall(r'(?:\w*\+)(\w+)(?:\s+\.)(text)(?:\s+)('+(name)+')(\w+)(?:\.o)',STRINGOS)
    rodata=re.findall(r'(?:\w*\+)(\w+)(?:\s+\.)(rodata)(?:\s+)('+(name)+')(\w+)(?:\.o)',STRINGOS)
    data=re.findall(r'(?:\w*\+)(\w+)(?:\s+\.)(data)(?:\s+)('+(name)+')(\w+)(?:\.o)',STRINGOS)
    bss=re.findall(r'(?:\w*\+)(\w+)(?:\s+\.)(bss)(?:\s+)('+(name)+')(\w+)(?:\.o)',STRINGOS)
    sum_text=0
    sum_data=0
    sum_rodata=0
    sum_bss=0
    if text:
      for tuple in text:
        sum_text=sum_text+int(tuple[0],16)    
      flie.write('            '+'*****'+name+' '+'component Info'+'*****'+"\n")
      flie.write(' '+'Size of .text   section in '+name+' '+'component is = '+str(sum_text)+'Bytes'+"\n")
      
      #flie.write(STRINGOS(sum_text))
    if rodata:
      for tuple in rodata:
        if tuple[2]==name:
          sum_rodata=sum_rodata+int(tuple[0],16)
      flie.write(' '+'Size of .rodata section in '+name+' '+'component is = '+str(sum_rodata)+'Bytes'+"\n")
      flie.write("\n")
  
    if data:
      for tuple in data:
        if tuple[2]==name:
          sum_data=sum_data+int(tuple[0],16)        
    

      flie.write(' '+'Size of .data   section in '+name+' '+'component is = '+str(sum_data)+'Bytes'+"\n")                
          
    if bss:
      for tuple in bss:
        if tuple[2]==name:
          sum_bss=sum_bss+int(tuple[0],16)

      flie.write(' '+'Size of .bss    section in '+name+' '+'component is = '+str(sum_bss)+'Bytes'+"\n")
      flie.write("\n")
    ROM=int(sum_text)+int(sum_bss)
    RAM=int(sum_data)+int(sum_rodata)
    flie.write(' '+'-> Size of ROM in '+name+'component is = '+str(ROM)+'Bytes'+"\n")
    flie.write(' '+'-> Size of RAM in '+name+'component is = '+str(RAM)+'Bytes'+"\n")
    
  
    f.close() 
  except IOError:
      print("File not accessible")
  finally:
      f.close() 
