import os
import sys


opt_layer='fc6'
act_layer='fc8'
units=['0','1']
xy='0'

# Hyperparam settings for visualizing AlexNet
iters=200
weights=[0.01]
rates=[0.01]
end_lr=1e-4
net_weights='nets/Urban/caffe_model_beauty_augmented_iter_10000.caffemodel'
net_definition='nets/Urban/caffenet_deploy_1.prototxt'

debug = 1
# Clipping
clip=0
multiplier=1
bound_file= 'act_range' + '/' + str(multiplier) + 'x' + '/' + str(opt_layer) +'.txt'
#defailt file
init_file="3.jpeg" #"images/cat.jpg"

# Output dir
output_dir="pythonRunner"

#rm -rf ${output_dir}
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

    
    

    
if __name__ == "__main__":
    #print "wow"

    # Running optimization across a sweep of hyperparams
    for unit in units:
        for seed in range(1):
            for w in weights:
                for lr in rates:
                    L2=1.05
                    command = 'python ./act_max.py --act_layer %s --opt_layer %s --unit %s --xy %s \
                               --n_iters %d --start_lr %f --end_lr %f --L2 %f --seed %d --clip %d \
                               --debug %d --output_dir %s --net_weights %s --net_definition %s --bound %s \
                               --init_file %s'%(act_layer,opt_layer,unit,xy,iters,lr,end_lr,L2,seed,clip,debug,
                                                         output_dir,net_weights,net_definition,bound_file,init_file)
                    print command

                    os.system(command)



