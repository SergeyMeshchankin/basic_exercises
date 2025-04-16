"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import defaultdict

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def get_most_active_user(messages):
    user_counts = defaultdict(int)
    for msg in messages:
        user_counts[msg['sent_by']] += 1
    max_count = max(user_counts.values())
    most_active = [user for user, count in user_counts.items()
                   if count == max_count]
    return most_active[0] if most_active else None


def get_most_replied_user(messages):
    message_owners = {msg['id']: msg['sent_by'] for msg in messages}
    replies_count = defaultdict(int)
    for msg in messages:
        if msg['reply_for'] is not None:
            original_author = message_owners.get(msg['reply_for'])
            if original_author is not None:
                replies_count[original_author] += 1
    if not replies_count:
        return None
    max_count = max(replies_count.values())
    most_replied = [user for user,
                    count in replies_count.items() if count == max_count]
    return most_replied[0] if most_replied else None


def get_most_seen_users(messages):
    seen_by_per_user = defaultdict(set)
    for msg in messages:
        user = msg['sent_by']
        seen_by_per_user[user].update(msg['seen_by'])
    max_seen = max(len(v) for v in seen_by_per_user.values()
                   ) if seen_by_per_user else 0
    most_seen = [user for user, seen in seen_by_per_user.items()
                 if len(seen) == max_seen]
    return most_seen


def get_busiest_time(messages):
    time_counts = {'утро': 0, 'день': 0, 'вечер': 0}
    for msg in messages:
        hour = msg['sent_at'].hour
        if hour < 12:
            time_counts['утро'] += 1
        elif hour < 18:
            time_counts['день'] += 1
        else:
            time_counts['вечер'] += 1
    return max(time_counts, key=lambda k: time_counts[k])


def get_longest_threads(messages):
    children = defaultdict(list)
    for msg in messages:
        if msg['reply_for'] is not None:
            children[msg['reply_for']].append(msg['id'])

    thread_length = {}
    sorted_messages = sorted(
        messages, key=lambda x: x['sent_at'], reverse=True)

    for msg in sorted_messages:
        msg_id = msg['id']
        max_child = 0
        for child_id in children.get(msg_id, []):
            max_child = max(max_child, thread_length.get(child_id, 0))
        thread_length[msg_id] = 1 + max_child

    root_messages = [msg for msg in messages if msg['reply_for'] is None]
    if not root_messages:
        return []
    max_len = max(thread_length[msg['id']] for msg in root_messages)
    return [msg['id'] for msg in root_messages if thread_length[msg['id']] == max_len]


if __name__ == "__main__":
    messages = generate_chat_history()

print(
    f"1. Айди пользователя с наибольшим количеством сообщений: {get_most_active_user(messages)}")
print(
    f"2. Айди пользователя, на чьи сообщения больше всего отвечали: {get_most_replied_user(messages)}")
print(
    f"3. Айди пользователей с наибольшим охватом: {', '.join(map(str, get_most_seen_users(messages)))}")
print(f"4. Самое активное время: {get_busiest_time(messages)}")
print(
    f"5. Идентификаторы самых длинных тредов: {', '.join(map(str, get_longest_threads(messages)))}")
