# Set this to the path to Caffe installation on your system
caffe_root = "/work/sagarj/Work/caffe-fr-chairs/python" 
gpu = True

# -------------------------------------
# These settings should work by default
# DNN being visualized
# These two settings are default, and can be overriden in the act_max.py
#net_weights = "nets/caffenet/caffenet.caffemodel"
#net_weights = "nets/Urban/caffe_model_beauty_city_augmented_iter_2000.caffemodel"
#net_weights = "nets/Urban/caffe_model_beauty_city_augmented_iter_2000.caffemodel"
net_weights = "nets/Urban/caffe_model_beauty_augmented_iter_10000.caffemodel"

#net_definition = "nets/caffenet/caffenet.prototxt"
net_definition = "nets/Urban/caffenet_deploy_1.prototxt"

# Generator DNN
generator_weights = "nets/upconv/fc6/generator_augmented.caffemodel"
#generator_weights = "nets/upconv/fc6/generator_38000_city.caffemodel"
generator_definition = "nets/upconv/fc6/generator.prototxt"

# Encoder DNN
encoder_weights = "nets/caffenet/caffenet.caffemodel"
encoder_definition = "nets/caffenet/caffenet.prototxt"
