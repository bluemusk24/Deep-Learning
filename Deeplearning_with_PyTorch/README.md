## Severless Deployment of Neural Network Image Classification Model with AWS Lambda_Function

```Google Colab``` notebook is used for this workshop(training neural network image classifcation model) because of GPU access.
[Pytorch_model notebook](Deeplearning_with_PyTorch/Deeplearning_with_PyTorch.ipynb)

```bash
pip install uv
uv init
uv sync
uv add jupyter onnx onnxruntime keras_image_helper numpy fastapi uvicorn

uv run jupyter notebook 
python predict.py           # runs predictions locally
python main.py              # Starts the FastAPI user interface
```

* Create the following:
[onnx_model_test notebook](Deeplearning_with_PyTorch/test.ipynb)
[test_script.py](Deeplearning_with_PyTorch/test.py)
[predict_script](Deeplearning_with_PyTorch/predict.py)
[main_script](Deeplearning_with_PyTorch/main.py)      * 

## Containerization
[dockerfile](Deeplearning_with_PyTorch/Dockerfile)

```bash
docker build --no-cache -t cloth_classifier .

docker run -it --rm -p 8080:8080 cloth_classifier

http://localhost:8080/docs          # access the FastAPI UI

# then POST to the API (in another terminal)
curl -s -X POST http://127.0.0.1:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"url":"http://bit.ly/mlbookcamp-pants"}' | jq
```