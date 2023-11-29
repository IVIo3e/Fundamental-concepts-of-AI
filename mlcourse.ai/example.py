import json


def solution(mdp, gamma):
    # заполнили табличку нулями
    q_table = {
        state: {
            action: 0 for action in actions
        } for state, actions in mdp.items()
    }
    return q_table


def main():
    # Список словарей содержит данные о каждом МППР, который определяется
    # состояниями, действиями, вероятностями перехода и вознаграждениями.
    with open('mdps.json', "r") as f:
        mdps = json.load(f)

    Qs = []
    for mdp in mdps:
        Qs.append(solution(mdp, gamma=0.9))
    with open('submit.json', "w") as f:
        json.dump(Qs, f)


if __name__ == '__main__':
    main()

