FROM continuumio/miniconda3

RUN conda install pytorch-nightly-cpu -c pytorch && pip install torchvision_nightly

COPY . /pretrained_resnet18

CMD cd /pretrained_resnet18 && python check_exported_model.py
