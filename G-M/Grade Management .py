import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["id", "name", "score"]


def load_students():
    """从 CSV 加载学生数据，返回 {学号: {'name': ..., 'score': ...}}"""
    students = {}
    if not os.path.exists(CSV_FILE):
        return students

    try:
        with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sid = row.get("id", "").strip()
                if not sid:
                    continue
                score_str = row.get("score", "").strip()
                students[sid] = {
                    "name": row.get("name", "").strip(),
                    "score": float(score_str) if score_str else 0.0,
                }
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"⚠️ 读取 CSV 失败：{e}")
    return students


def save_students(students):
    """将学生数据写入 CSV"""
    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for sid, info in students.items():
            writer.writerow({
                "id": sid,
                "name": info["name"],
                "score": info["score"],
            })


def input_score(prompt="成绩 (0-100): "):
    """输入并验证成绩"""
    while True:
        val = input(prompt).strip()
        try:
            score = float(val)
            if 0 <= score <= 100:
                return score
            print("⚠️ 成绩必须在 0 到 100 之间。")
        except ValueError:
            print("⚠️ 请输入有效数字。")


def add_student(students):
    sid = input("学号: ").strip()
    if not sid:
        print("⚠️ 学号不能为空。")
        return
    if sid in students:
        print("⚠️ 该学号已存在。")
        return

    name = input("姓名: ").strip()
    if not name:
        print("⚠️ 姓名不能为空。")
        return

    score = input_score()
    students[sid] = {"name": name, "score": score}
    save_students(students)
    print(f"✅ 已添加：{sid} {name} {score}")


def delete_student(students):
    sid = input("要删除的学号: ").strip()
    if sid in students:
        info = students.pop(sid)
        save_students(students)
        print(f"✅ 已删除：{sid} {info['name']}")
    else:
        print("⚠️ 未找到该学号。")


def update_student(students):
    sid = input("要修改的学号: ").strip()
    if sid not in students:
        print("⚠️ 未找到该学号。")
        return

    info = students[sid]
    print(f"当前记录：姓名={info['name']}，成绩={info['score']}")

    name = input("新姓名（留空保持不变）: ").strip()
    if name:
        info["name"] = name

    score_input = input("新成绩（留空保持不变）: ").strip()
    if score_input:
        try:
            score = float(score_input)
            if 0 <= score <= 100:
                info["score"] = score
            else:
                print("⚠️ 成绩需在 0-100 之间，未修改。")
        except ValueError:
            print("⚠️ 无效成绩，未修改。")

    save_students(students)
    print("✅ 修改完成。")


def query_student(students):
    keyword = input("输入学号或姓名关键字: ").strip().lower()
    if not keyword:
        print("⚠️ 关键字不能为空。")
        return

    found = False
    for sid, info in students.items():
        if keyword in sid.lower() or keyword in info["name"].lower():
            print(f"{sid}\t{info['name']}\t{info['score']}")
            found = True
    if not found:
        print("没有匹配的记录。")


def list_students(students):
    if not students:
        print("暂无学生记录。")
        return

    print(f"{'学号':<10} {'姓名':<10} {'成绩':<6}")
    print("-" * 30)
    for sid, info in students.items():
        print(f"{sid:<10} {info['name']:<10} {info['score']:<6}")


def main():
    students = load_students()
    menu = """
===== 学生成绩管理 =====
1. 显示全部
2. 添加学生
3. 删除学生
4. 修改学生
5. 查询学生
6. 保存并退出
请选择 (1-6): """

    while True:
        choice = input(menu).strip()
        if choice == "1":
            list_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            query_student(students)
        elif choice == "6":
            save_students(students)
            print("已保存，再见！")
            break
        else:
            print("⚠️ 无效选项，请重新输入。")


if __name__ == "__main__":
    main()
