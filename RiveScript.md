_____________________________________________________________________________________________________

#                       Tutorials for RIVESCRIPT 1.12.3 python version
_____________________________________________________________________________________________________

# learn object
_____________________________________________________________________________________________________
write trigger and reply on .rive file for permanent learning,
import both informations on bot for immediate use (no need to restart program and read .rive files)

// ex : "memorize a golden apple is a yellow fruit"

// object converts and write :

// + a golden apple

// - a yellow fruit

// I ask : "what is a golden apple"

// bot replies : "it's a yellow fruit"

    object memorize python

    a = args
    
    b = ', '.join(a).replace(',','').replace('(','').replace(')','') # clean string
    
    c = b.replace(' -','\n-') # insert '\n' separation for stream export
    
    rs.stream (c)
    
    rs.sort_replies()
    
    file = open("./eg/neo_brain/neo_Auto_Learning.rive", "a")
    
    file.write("\n\n")
    
    file.write(str(c))
    
    file.close()
    
    object
_____________________________________________________________________________________________________
