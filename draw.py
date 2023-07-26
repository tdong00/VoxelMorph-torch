# encoding: utf-8
import matplotlib.pyplot as plt

file = open(r'D:/Software/Xie-registration/voxelmorph/VoxelMorph-torch/Log/15000_0.0004_4.0.txt')  #打开文档
data = file.readlines() #读取文档数据
x = []  #新建列表，用于保存第一列数据
loss = []  #新建列表，用于保存第二列数据
sim = []
grad = []
for num in data:
	# split用于将每一行数据用逗号分割成多个对象
    #取分割后的第0列，转换成float格式后添加到para_1列表中
    x.append(float(num.split(',')[0]))
    #取分割后的第1列，转换成float格式后添加到para_1列表中
    loss.append(float(num.split(',')[1]))
    sim.append(float(num.split(',')[2]))
    grad.append(float(num.split(',')[3]))
#plt.xlabel('Iters')
#plt.ylabel('Loss')
#plt.title('voxelmorph')
plt.plot(x, loss, 'b-', label = 'Loss')
print(min(loss))
print(loss.index(min(loss)))
print(max(loss))
print(loss.index(max(loss)))
#plt.plot(x, sim, 'g-', label = 'Sim')
#plt.plot(x, grad, 'r-', label = 'Grad')
plt.legend()
plt.show()