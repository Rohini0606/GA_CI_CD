FROM python:3.9-slim-buster
WORKDIR \Users\rohin\PycharmProjects\pythonProject1\Docker_test

COPY Requirements.txt .\

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r Requirements.txt

COPY . .

CMD ["python", "-m", "flask", "--app", "Loan_app", "run", "--host = 0.0.0.0"]
