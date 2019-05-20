import os
import sys
import pandas as pd
import pickle

opt_layer='fc6'
act_layer='fc8'
#units=['0','1']
xy='1'

# Hyperparam settings for visualizing AlexNet
iters=100
weights=[0.001]
rates=[0.05]
end_lr=1e-3
#net_weights='nets/Urban/caffe_model_beauty_city_augmented_iter_400.caffemodel'
#net_weights='nets/Urban/caffe_model_beauty_city_augmented_iter_2000.caffemodel'
#net_weights='nets/Urban/caffe_model_beauty_augmented_iter_10000.caffemodel'
net_weights='nets/Urban/caffe_model_1_iter_24732.caffemodel'
#net_weights='nets/Urban/caffe_model_beauty_binary_iter_10000.caffemodel'
net_definition='nets/Urban/caffenet_deploy_1.prototxt'

#imageList = "/datasets_1/sagarj/BellLabs/Data/fringeImages.pkl"
imageList = "/datasets_1/sagarj/BellLabs/Data/bostonDf.pkl"

debug = 1
# Clipping
clip=0
multiplier=1
bound_file= 'act_range' + '/' + str(multiplier) + 'x' + '/' + str(opt_layer) +'.txt'
#defailt file
#init_file="img4.jpg" #"images/cat.jpg"

# Output dir
# output_dir="/datasets/sagarj/streetView/Transform_Boston150_Imagenet/"
output_dir="bostonDebug/"

#rm -rf ${output_dir}
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

    
    

    
if __name__ == "__main__":
    #print "wow"
    # imgList = pd.read_csv(imageList)
    with open(imageList, 'rb') as handle:
        imgList = pickle.load(handle)
    count = 0
    paths1 = []
    paths2 = []
    name1 = []
    name2 = []
    
    for row in imgList:
        #change this
        print imgList[row]
        if imgList[row][1]['label'] == 0:
            paths1.append(imgList[row][1]['path'])
            name1.append(imgList[row][0])
        else:
            paths2.append(imgList[row][1]['path'])
            name2.append(imgList[row][0])
        
    print "Processing %d beautyfication images and %d  uglification images images , total %d" , len(name1) , len(name2) , count
        # Running optimization across a sweep of hyperparams
    # for unit in units:
    for seed in range(1):
        for w in weights:
            for lr in rates:
                L2=1.05
                command = 'python ./act_max.py --act_layer %s --opt_layer %s --unit %s --xy %s \
                           --n_iters %d --start_lr %f --end_lr %f --L2 %f --seed %d --clip %d \
                           --debug %d --output_dir %s --net_weights %s --net_definition %s --bound %s \
                           '%(act_layer,opt_layer,'1',xy,iters,lr,end_lr,L2,seed,clip,debug,
                                                     output_dir,net_weights,net_definition,bound_file)
                for i in range(len(paths1)):
                    addendum = ' --appendImages ' + paths1[i] + ' --appendNames ' + name1[i]
                    command+=addendum
                #print command

                os.system(command)
    
#     for seed in range(1):
#         for w in weights:
#             for lr in rates:
#                 L2=1.05
#                 command = 'python ./act_max.py --act_layer %s --opt_layer %s --unit %s --xy %s \
#                            --n_iters %d --start_lr %f --end_lr %f --L2 %f --seed %d --clip %d \
#                            --debug %d --output_dir %s --net_weights %s --net_definition %s --bound %s \
#                            '%(act_layer,opt_layer,'0',xy,iters,lr,end_lr,L2,seed,clip,debug,
#                                                      output_dir,net_weights,net_definition,bound_file)
#                 for i in range(len(paths2)):
#                     addendum = ' --appendImages ' + paths2[i] + ' --appendNames ' + name2[i]
#                     command+=addendum
#                 #print command

#                 os.system(command)



