#/bin/bash

opt_layer=fc6
act_layer=fc8
units=1
xy=0

# Hyperparam settings for visualizing AlexNet
iters=50
weights=0.1
rates="0.05"
end_lr=1e-4
net_weights="nets/Urban/caffe_model_1_iter_24732.caffemodel"
net_definition="nets/Urban/caffenet_deploy_1.prototxt"

# Clipping
clip=0
multiplier=3
bound_file=act_range/${multiplier}x/${opt_layer}.txt
init_file="img5.jpg" #"images/cat.jpg"

# Debug
debug=1
if [ "${debug}" -eq "1" ]; then
  rm -rf debug
  mkdir debug
fi

# Output dir
output_dir="output"
#rm -rf ${output_dir}
mkdir -p ${output_dir}

# Running optimization across a sweep of hyperparams
for unit in ${units}; do

  for seed in {0..0}; do
  #for seed in {0..8}; do

    for n_iters in ${iters}; do
      for w in ${weights}; do
        for lr in ${rates}; do

          L2=1.05

          # Optimize images maximizing fc8 unit
          python ./act_max_orig.py \
              --act_layer ${act_layer} \
              --opt_layer ${opt_layer} \
              --unit ${unit} \
              --xy ${xy} \
              --n_iters ${n_iters} \
              --start_lr ${lr} \
              --end_lr ${end_lr} \
              --L2 ${L2} \
              --seed ${seed} \
              --clip ${clip} \
              --debug ${debug} \
              --output_dir ${output_dir} \
              --net_weights ${net_weights} \
              --net_definition ${net_definition} \
              --bound ${bound_file} \
              --init_file ${init_file}
        done
      done
    done
  
  done
done

if [ "${debug}" -eq "1" ]; then
  output_file=${output_dir}/example3.jpg
  montage debug/*.jpg -tile 10x20 -geometry +1+1 ${output_file}
  convert ${output_file} -trim ${output_file}

  echo "Intermediate results: ${output_file}"
fi
