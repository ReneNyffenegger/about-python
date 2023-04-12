import matplotlib.pyplot as plt
import numpy             as np
from   scipy.ndimage import gaussian_filter


gridStr = '''
                                        xx                             
                                       xxxx                            
                                      xxxxx x                          
                                      xxxxxxxx xx                      
                                         xxxxxxxxxxx                   
                         xx  xx   xxx  x xxxxxxxxxxxx                  
                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                 
                xxxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx               
                xxxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
               xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
               xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
                 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              
                xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx               
               xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx               
              xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              
             xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx            
           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       xx 
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       xx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   xxxxx
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxxx
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   xxx
  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       
  xxxxxx    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x xxxxxxxxx       
  xxxx        xxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxx  xxxxxxxxxxxx     
   xx        xxxxxxxxxxxxxxxxxxxxxxxx  xxxxxxxxxxxxx   xxxxx   xxx     
   x        xxxxxxxxxxxxxxxxxxxxxxxx   xxxxxxxxxxxxxx  xxxxx   xx      
  xx         xxxxxxxxxxxxxxxxxxxxxxx   xxxxxxxxxxxxx    xxx    xxx     
 xx xx        xxxxxxxxxxxxxxxxxxxx     xxxxxxxxxxxxx            xx     
xxxxx        xxxxxxxxxxxxxxxxxxxxxx    xxxxxxxxxxxx             x      
xxxx         xxxxxxxxxxxxxxxxxxxxxx    xxxxxxxxxxxx                    
             xxxxxxxxxxxxxxxxxxxxxx      xxxxxxxxx                     
              xxxxxxxxxxxxxxxxxxx         x xxxxx                      
              xxxxxxxxxxxxxxxxxxx            xxx                       
                xxxxxxxxxxxxxxxx            xxxxx                      
                 xxxxxxxx  xxxxx             xxx                       
                 xxxxxx     xx                xxx                      
                  x                           xxx                      
                                               xx                      '''


lines = gridStr.splitlines()[1:] # Remove first line

grid = [ [ False if cell==' ' else True  for cell in line ] for line in lines]

height = len(grid   )
width  = len(grid[0])

np.random.seed(2808)
values = np.random.rand(height, width)
values = gaussian_filter(values, sigma=1.4)

# print(f'Size: {width}x{height}')

for  x in range(width):
 for y in range(height):

     if not grid[y][x]:
        values[y, x] = None

plt.imshow(values, cmap = 'coolwarm')
plt.axis('off')

fig = plt.gcf() # gcf = get current figure

fig.subplots_adjust(
    top    = 0.95,
    bottom = 0.05,
    left   = 0.0,
    right  = 1.0
#   hspace=0.0,
#   wspace=0.0
)

plt.show()
