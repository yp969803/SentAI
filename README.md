
# SentAI

A application to get analysis of the sentiments of your documents.




## Documentation

#### clone the repository
```
git clone https://github.com/yp969803/SentAI
```

#### Enter into the project directory
```
cd SentAI
```
#### Create virtual enviroment
```
python -m venv myenv
source /venv/bin/activate
```
#### Install dependencies
```
pip install -r requirements.txt
```

#### Run applicattion
```
python index.py
```

## API Reference

#### Upload file and get sentiment

```http
  POST /api/file/sentiment
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file`    | `file`   | **Required**. .txt file    |



## Tech Stack

**Server:** Flask
**Deeplearning Model:** TextBlob 


