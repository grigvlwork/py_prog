from PyQt5 import QtGui, Qt
from PyQt5.Qt import QStandardItemModel
from collections import deque


class Table:
    def __init__(self, table, fields, cursor):
        self.table = table
        self.fields = fields
        self.cursor = cursor

    def insert_sql(self, values):
        vals = list(map(str, values))
        sql = 'INSERT INTO ' + self.table + ' (' + ','.join(self.fields[1:]) + \
               ') VALUES (' + ','.join(vals) + ')'
        print(sql)
        return sql

    def update_sql(self, field, value, id_rec):
        return "UPDATE " + self.table + " SET " + field + ' = "' + value + \
               '" WHERE ID = ' + id_rec

    def delete_sql(self, id_rec):
        return "DELETE FROM " + self.table + " WHERE ID = " + id_rec

    def select1_sql(self, id_rec):
        return "SELECT * FROM " + self.table + " WHERE ID = " + id_rec

    def select_detail_sql(self, master_field, id_rec):
        return "SELECT * FROM " + self.table + " WHERE " + master_field + " = " + str(id_rec)

    def select_all_sql(self):
        return "SELECT * FROM " + self.table

    def select_all(self):
        self.cursor.execute(self.select_all_sql())
        return self.cursor.fetchall()

    def select_detail(self, master_field, id_rec):
        self.cursor.execute(self.select_detail_sql(master_field, id_rec))
        return self.cursor.fetchall()

    def insert(self, values):
        sql = self.insert_sql(values)
        self.cursor.execute(sql)


class Record:
    def __init__(self, table):
        self.table = table
        self.values = []

    def set_values(self, values):
        self.values = values

    def get_values(self):
        return self.values


class SectionRecord(Record):
    def __init__(self):
        super().__init__('section')

    def insert(self):
        self.table.insert_sql(self.values)

    def update(self):
        sql = 'UPDATE SECTION SET SUBJECT_ID = ' + self.values[1] + ', ' \
                                                                    'PARENT_SECTION_ID = ' + self.values[2] + ', ' \
                                                                                                              'NAME = "' + \
              self.values[3] + '" WHERE ID = ' + self.values[0]
        self.table.cursor.execute(sql)


class Subject(Table):
    def __init__(self, cur):
        super().__init__("subject", ['id', 'name'], cur)


class Section(Table):
    def __init__(self, cur):
        super().__init__("section", ["id", "subject_id", "parent_section_id", "name"], cur)

    def select_detail(self, id_rec):
        self.cursor.execute(self.select_detail_sql('subject_id', id_rec))
        return self.cursor.fetchall()


class Task(Table):
    def __init__(self, cur):
        super().__init__("task", ['id', 'section_id', 'name', 'condition'], cur)

    def select_detail(self, id_rec):
        self.cursor.execute(self.select_detail_sql('section_id', id_rec))
        return self.cursor.fetchall()


class TreeItem(QtGui.QStandardItem):
    def __init__(self, txt='', font_size=10, set_bold=False, color=QtGui.QColor(0, 0, 0), dbid=0):
        super().__init__()
        self.db_id = dbid
        fnt = QtGui.QFont('Arial', font_size)
        fnt.setBold(set_bold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

    def get_id(self):
        return self.db_id


class TaskListItem(QtGui.QStandardItem):
    def __init__(self, txt='', font_size=10, set_bold=False, color=QtGui.QColor(0, 0, 0), dbid=0):
        super().__init__()
        self.db_id = dbid
        fnt = QtGui.QFont('Arial', font_size)
        fnt.setBold(set_bold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

    def get_id(self):
        return self.db_id


class Tree:
    def __init__(self):
        self.model = QStandardItemModel()

    def import_data(self, node_list, id_index, parent_id_index, name_index):
        self.model.setRowCount(0)
        root_node = self.model.invisibleRootItem()
        nodes_deque = deque(node_list)
        seen = dict()
        while nodes_deque:
            node = nodes_deque.popleft()
            if node[parent_id_index] == -1:
                parent = root_node
            else:
                pid = node[parent_id_index]
                if pid not in seen:
                    nodes_deque.append(node)
                    continue
                parent = seen[pid]
            db_id = node[id_index]
            parent.appendRow(TreeItem(txt=node[name_index], dbid=db_id))
            seen[db_id] = parent.child(parent.rowCount() - 1)


class List:
    def __init__(self):
        self.model = QStandardItemModel()

    def import_data(self, data, id_index, name_index):
        self.model.setRowCount(0)
        for item in data:
            self.model.appendRow(TaskListItem(txt=item[name_index], dbid=item[id_index]))
