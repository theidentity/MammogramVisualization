import cv2



labels = open('data/labels').read()
labels = labels.split('\n')

stats ={}
stats['normal'] = 0
stats['abnormal'] = 0
stats['exception'] = 0
stats['total'] = 0

for label in labels:
	
	components = label.split()
	stats['total'] += 1

	if len(components) == 3:
		print('--------------------NORMAL----------------------------')
		name,bg_tissue,abn = components
		img = cv2.imread('data/pgm/'+name+'.pgm')
		print(img.shape)
		
		new_name = '.'.join([abn,bg_tissue,name,'png'])
		cv2.imwrite('tmp/neg/'+new_name,img)
		print(new_name)

		stats['normal'] += 1
	elif len(components) == 7:
		print('--------------------ABNORMAL----------------------------')
		name,bg_tissue,abn,severity,x,y,r = components
		img = cv2.imread('data/pgm/'+name+'.pgm')
		print(img.shape)
		
		new_name = '.'.join([abn,bg_tissue,severity,x,y,r,name,'png'])
		cv2.imwrite('tmp/pos/'+new_name,img)

		circle_img = img.copy()
		x,y,r = int(x),int(y),int(r)
		cv2.circle(circle_img,(x,y), r, (0,255,0),3)
		print(circle_img.shape)
		cv2.imwrite('tmp/pos_visual/'+new_name,circle_img)
		print(new_name)

		stats['abnormal'] += 1
	else:
		print('---------EXCEPTION------------')
		print(components)
		print(len(components))

		stats['exception'] += 1


print(stats)