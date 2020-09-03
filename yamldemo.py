import yaml, time


def main():
    # with open("./test.yaml", "r", encoding="utf-8") as f:
    #     date = yaml.load(f, Loader=yaml.FullLoader)
    #     print(date)
    date = {'name': 'zhangsha', 'people': [{'name1': 1}, {'name2': 2}, {'name3': 3}]}
    with open("./test.yaml", "w", encoding="utf-8") as f:
        yaml.dump(date, f, encoding="utf-8", allow_unicode=True)


if __name__ == '__main__':
    main()
