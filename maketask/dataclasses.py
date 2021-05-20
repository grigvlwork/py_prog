from PyQt5 import QtGui
from PyQt5.Qt import QStandardItemModel, QStandardItem
from collections import deque


class Table:
    def __init__(self, table, fields, cursor):
        self.table = table
        self.fields = fields
        self.cursor = cursor

    def insert_sql(self, values):
        return "INSERT INTO " + self.table + " (" + ",".join(self.fields) + \
               ") VALUES (" + ",".join(values) + ")"

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
        self.cursor.execute(self.insert_sql(values))


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
            parent.appendRow([
                QtGui.QStandardItem(node[name_index]),
                QtGui.QStandardItem(str(db_id)),
            ])
            seen[db_id] = parent.child(parent.rowCount() - 1)
